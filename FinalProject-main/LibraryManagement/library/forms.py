#Defines the user entry fields for all forms within the app
#All forms reference a model from the models.py folder
from django import forms
from django.contrib.auth.models import User
from . import models

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class AdminUserForm(forms.ModelForm): 
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

#Will add a department field to this 
class FacultyUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['major','classification']

class FacultyExtraForm(forms.ModelForm):
    class Meta:
        model=models.FacultyExtra
        fields=['department']

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['name','isbn','author','subject','publisher','publishDate']

#to_field_name value will be stored when form is submitted
# __str__ method of book model will be shown there in html pages as the name of the entry field for the form 
class IssuedBookForm(forms.Form):
    isbn2=forms.ModelChoiceField(queryset=models.Book.objects.all(),empty_label="Book name and ISBN", to_field_name="isbn",label='Name and Isbn')
    enrollment2=forms.ModelChoiceField(queryset=models.StudentExtra.objects.all(),empty_label="Name and Major or Department",to_field_name='major',label='Name and enrollment')
    
class ReturnBookForm(forms.Form):    
    isbn3=forms.ModelChoiceField(queryset=models.Book.objects.all(),empty_label="Book name and ISBN", to_field_name="isbn",label='Name and Isbn')
    enrollment3=forms.ModelChoiceField(queryset=models.StudentExtra.objects.all(),empty_label="Name and enrollment",to_field_name='major',label='Name and enrollment')

class ReserveBookForm(forms.Form):    
    isbn4=forms.ModelChoiceField(queryset=models.Book.objects.all(),empty_label="Book name and ISBN", to_field_name="isbn",label='Name and Isbn')
    enrollment4=forms.ModelChoiceField(queryset=models.StudentExtra.objects.all(),empty_label="Name and enrollment",to_field_name='major',label='Name and enrollment')