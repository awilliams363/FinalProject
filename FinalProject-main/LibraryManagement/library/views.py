#This file defines webpage views and functions and connects them to the desired .html webpage
#Majority of the apps functionality is defined here 
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import auth
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.urls import reverse
from django.utils import timezone
from .models import IssuedBook

#Defines the returns for requests for the index, home, and logout pages 
def index_view(request):
    return render(request, 'library/index.html')

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'library/index.html')

def logout_view(request):
    if request.method=='POST':
        return render(request,'library/index.html')
    else:
        return render(request,'library/logout.html')


#If student account is signed in, then displays Student Afterlogin page 
#If not, then it displays signup/login webpage for students
def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'library/studentclick.html')

#If libarian(admin) account is signed in, then displays Librarian Afterlogin page 
#If not, then it displays signup/login webpage for Librarians
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'library/adminclick.html')

#If faculty account is signed in, then displays Faculty Afterlogin page 
#If not, then it displays signup/login webpage for Faculty
def facultyclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'library/facultyclick.html')


#Defines the return for requests to sign up for librarian(admin), student, and faculty accounts 
def adminssignup_view(request):
    adform1=forms.AdminUserForm()
    mydict={'adform1':adform1}
    if request.method=='POST':
        adform1=forms.AdminUserForm(request.POST)
        if adform1.is_valid():
            user=adform1.save()
            user.set_password(user.password)
            user.save()

            my_admin_group = Group.objects.get_or_create(name='LIBRARIAN')
            my_admin_group[0].user_set.add(user)
        return HttpResponseRedirect('adminlogin')
    return render(request,'library/adminsignup.html',context=mydict)

def studentsignup_view(request):
    form1=forms.StudentUserForm()
    form2=forms.StudentExtraForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.StudentUserForm(request.POST)
        form2=forms.StudentExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            user2=f2.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)

        return HttpResponseRedirect('studentlogin')
    return render(request,'library/studentsignup.html',context=mydict)

def facultysignup_view(request):
    fform1=forms.FacultyUserForm()
    fform2=forms.FacultyExtraForm()
    mydict={'fform1':fform1,'fform2':fform2}
    if request.method=='POST':
        fform1=forms.FacultyUserForm(request.POST)
        fform2=forms.FacultyExtraForm(request.POST)
        if fform1.is_valid() and fform2.is_valid():
            user=fform1.save()
            user.set_password(user.password)
            user.save()
            f2=fform2.save(commit=False)
            f2.user=user
            user2=f2.save()

            my_faculty_group = Group.objects.get_or_create(name='FACULTY')
            my_faculty_group[0].user_set.add(user)

        return HttpResponseRedirect('facultylogin')
    return render(request,'library/facultysignup.html',context=mydict)


#Roles are defined by grouping users into LIBRARIAN, STUDENT, OR FACULTY 
def is_admin(user):
    if user.is_superuser or user.is_staff:
        return True
    elif user.groups.filter(name='LIBRARIAN').exists():
        return True
    else:
        return False

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

def is_faculty(user):
    return user.groups.filter(name='FACULTY').exists()


#Routes the afterlogin view by user's role
def afterlogin_view(request):
    if is_admin(request.user):
        return render(request,'library/adminafterlogin.html')
    
    elif(is_student(request.user)):
        return render(request,'library/studentafterlogin.html')
    
    elif(is_faculty(request.user)):
        return render(request,'library/facultyafterlogin.html')
    
    else:
        return render(request,'library/studentafterlogin.html')

#Add Book to Library 
#Exclusive to Librarian
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def addbook_view(request):
    #empty book form for sending to html
    form=forms.BookForm()
    if request.method=='POST':
        #updating form to data entered by user from the webpage
        form=forms.BookForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request,'library/bookadded.html')
    return render(request,'library/addbook.html',{'form':form})


#View all Library Books
def viewbook_view(request):
    books=models.Book.objects.all()

    #This commented out portion of code was used to do a manual update to borrowed book6 (student2)
    #The issue date and expirydate are being changed to demonstrate the reminders function and late fee
    #Other books can be modified to test these features by updating id='5' to the desired IssuedBook id
    #To complete the modification visit the /viewbook page and the update will be reflected in the borrow record

    #testobj=models.IssuedBook.objects.filter(id='5')
    #testobj.update(issuedate='2025-04-01')
    #testobj.update(expirydate=timezone.now().date() + timedelta(days=7))

    return render(request,'library/viewbook.html',{'books':books})

#Return books 
def bookreturn_view(request):
    rform=forms.ReturnBookForm()
    if request.method=='POST':
        rform=forms.ReturnBookForm(request.POST)
        if rform.is_valid():    
            robj=models.Book.objects.filter(isbn=request.POST.get('isbn3'))
            robj.update(status= 'Available')
            robj2=models.IssuedBook.objects.filter(isbn=request.POST.get('isbn3'))
            robj2.update(status= 'Returned')                
            return render(request,'library/bookreturn.html')
    return render(request,'library/bookreturn.html',{'rform':rform})

#Book Reservation
def bookreservation_view(request):
    brform=forms.ReserveBookForm()
    if request.method=='POST':
        brform=forms.ReserveBookForm(request.POST)
        if brform.is_valid():
            brobj=models.Book.objects.filter(isbn=request.POST.get('isbn4'))
            brobj.update(status= 'Reserved')
            brobj2=models.IssuedBook.objects.filter(isbn=request.POST.get('isbn4'))
            brobj2.update(status= 'Reserved')
            return render(request, 'library/bookreservation.html')
    return render(request,'library/bookreservation.html',{'brform':brform})

#Borrow Book 
def issuebook_view(request):
    form=forms.IssuedBookForm()
    if request.method=='POST':
        form=forms.IssuedBookForm(request.POST)
        if form.is_valid():
            obj=models.IssuedBook()
            obj.major=request.POST.get('enrollment2')
            obj.isbn=request.POST.get('isbn2')
            obj.status= 'Borrowed'
            obj.save()
            obj2=models.Book.objects.filter(isbn=request.POST.get('isbn2'))
            obj2.update(status= 'Borrowed')
            return render(request,'library/bookissued.html')
    return render(request,'library/issuebook.html',{'form':form})

#View Full Borrow Record of All Students 
#Excluse to Libraraians 
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def viewissuedbook_view(request):
    issuedbooks=models.IssuedBook.objects.all()
    li=[]
    
    for ib in issuedbooks:
        issdate=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
        expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
        #fine calculation
        days=(date.today()-ib.issuedate)
        print(date.today())
        d=days.days
        fine=0
        if d>15:
            day=d-15
            fine=day*10.00


        books=list(models.Book.objects.filter(isbn=ib.isbn))
        students=list(models.StudentExtra.objects.filter(major=ib.major))
        i=0
        for l in range(len(books)):
            if i in range(len(students)):
                t=(students[i].get_name,students[i].major,books[i].name,books[i].author,issdate,expdate,fine,ib.status)
                i=i+1
                li.append(t)
    return render(request,'library/viewissuedbook.html',{'li':li})


#View all student registered students 
#Exclusive to Librarians
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def viewstudent_view(request):
    students=models.StudentExtra.objects.all()
    return render(request,'library/viewstudent.html',{'students':students})


#View Personal Borrow Record 
#Exclusive to Students 
def viewissuedbookbystudent(request):
    student=models.StudentExtra.objects.filter(user_id=request.user.id)
    issuedbook=models.IssuedBook.objects.filter(major=student[0].major)

    li1=[]

    li2=[]
    for ib in issuedbook:
        books=models.Book.objects.filter(isbn=ib.isbn)
        for book in books:
            t=(request.user,student[0].major,student[0].classification,book.name,book.author)
            li1.append(t)
        issdate=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
        expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
        #fine calculation
        days=(date.today()-ib.issuedate)
        print(date.today())
        d=days.days
        fine=0
        if d>15:
            day=d-15
            fine=day*10
        t=(issdate,expdate,fine,ib.status,ib.id)
        li2.append(t)

    return render(request,'library/viewissuedbookbystudent.html',{'li1':li1,'li2':li2})


#About Us Page 
def aboutus_view(request):
    return render(request,'library/aboutus.html')


#Search Books
def searchbook_view(request):
    message = None
    if request.method == 'POST':
        query = request.POST.get('search_query')
        book = models.Book.objects.filter(name__icontains=query).first()
        if not book:
            message = "❌ Book not found."
        elif book.status == 'Available':
            message = "✅ Book is available."
        else:
            message = "⚠️ Book is currently not available."
    return render(request, 'library/searchbook.html', {'message': message})


#Advanced Function
#Automated Book Return Reminders 
@login_required
def reminder_view(request):
    today = timezone.now().date()
    upcoming_dates = [today + timedelta(days=7), today + timedelta(days=2)]

    reminders = []

    try:
        if request.user.groups.filter(name='STUDENT').exists():
            student = models.StudentExtra.objects.get(user=request.user)
            reminders = IssuedBook.objects.filter(
                major=student.major,
                expirydate__in=upcoming_dates,
                status='Borrowed'
            )
        elif request.user.groups.filter(name='FACULTY').exists():
            faculty = models.FacultyExtra.objects.get(user=request.user)
            reminders = IssuedBook.objects.filter(
                major=faculty.department,
                expirydate__in=upcoming_dates,
                status='Borrowed'
            )
    except (models.StudentExtra.DoesNotExist, models.FacultyExtra.DoesNotExist):
        reminders = []

    reminder_data = []
    for r in reminders:
        days_left = (r.expirydate - today).days
        reminder_data.append({
            'isbn': r.isbn,
            'due_date': r.expirydate,
            'days_left': days_left
        })

    context = {'reminders': reminder_data}
    return render(request, 'library/reminder.html', context)
