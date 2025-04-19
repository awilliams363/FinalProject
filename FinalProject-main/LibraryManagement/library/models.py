#Defines class objects and the datatypes of their attributes
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta, date


#Django's user class has a preset list of attributes that cannot be editted (see attributes in db file under auth_user)
#StudentExtra defines other student attribute columns and has its own table in the db (library_StudentExtra)
#FacultyExtra defines other faculty attribute columns and has its own table in the db (library_FacultyExtra)
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    major=models.CharField(max_length=40)
    classification=models.CharField(max_length=40) #i.e freshmen, sophmore, junior, senior
    #used in issue, return, and reserve book webpages and function to select a students name and major 
    #to display a combination of the two fields in the form
    def __str__(self):
        return self.user.first_name+'['+str(self.major)+']'
    @property
    def get_name(self):
        return self.user.first_name
    @property
    def getuserid(self):
        return self.user.id


class FacultyExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    department=models.CharField(max_length=40)
    def __str__(self):
        return self.user.first_name+'['+str(self.department)+']'
    @property
    def get_name(self):
        return self.user.first_name
    @property
    def getuserid(self):
        return self.user.id

#Defines a Book and its atributes 
class Book(models.Model):
    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biology', 'Biology'),
        ('history', 'History'),
        ('fiction', 'Fiction'),
        ('nonfiction', 'Nonfiction'),
        ]
    name=models.CharField(max_length=30)
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    publisher=models.CharField(max_length=40, default='NoPublisher')
    publishDate=models.DateField(default=date.today)
    subject=models.CharField(max_length=30,choices=catchoice,default='education')
    availabilityStatus=models.BooleanField(default= True)
    statuschoice= [
        ('Borrowed', 'Borrowed'),
        ('Returned', 'Returned'),
        ('Available','Available'),
        ('Reserved', 'Reserved')
        ]
    status=models.CharField(max_length=40,choices=statuschoice,default="Available")
    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'


#used for issuing fines, used in views.py
def get_expiry():
    return datetime.today() + timedelta(days=15)

#Defines elements of the Borrow Record
class IssuedBook(models.Model):
    major=models.CharField(max_length=30)
    isbn=models.CharField(max_length=30)
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)
    statuschoice= [
        ('Borrowed', 'Borrowed'),
        ('Returned', 'Returned'),
        ('Returned&Reserved', 'Returned&Reserved'),
        ('Available','Available'),
        ('Reserved', 'Reserved')
        ]
    status=models.CharField(max_length=20,choices=statuschoice,default="Available")
    def __str__(self):
        return self.major
