# FinalProject

## NOTES: 
***PASSWORD FOR ALL ACCOUNTS ON FILE: 1a2b3c4d ***
    Check db.sqlite3 file for usernames and other attributes 
*Make sure to download Django first in the terminal you may also want to create a virtual environment 

*To make and add functions: 
    -create function within the views.py file 
        -def functionname_view(request):
    -build a webpage file (.html) in the templates folder 
    -reference the desired webpage in the end of the function inside the views.py file
        -return render(request,'pathname/webpage.html')
    -Then add a path to the webpage in the urls.py file following the same format as the other entries

*Forms can be added to the forms.py file and referenced in the webpage .html files or the views.py files 

*In the models.py file you can define classes, objects, define elements in a form, or define the elements of an object/database table 
    -the models can then be used in the webpages or views. 

*Ill likely be getting rid of the Contact Us section, but some of features in it may be useful for building the notification function 

*Other Notes: 
    -the sourcecode used issuebooks and viewbook for the borrow and borrow record functions. I've change the front end names to borrow and borrow record but Ill keep the names the same as the source code on the backend 
    -the to view the databse you'll need sqlite viewer 
    -many of the databse tables a columns came with the source code. Ill be updating the column names and dataypes to match the project 
    -If you update anything to do with the database you may have to run makemigrations in the terminal to see the changes 
    -Django tutorials, django documentation pages, and stack overflow were very helpful towards making these edits

***PASSWORD FOR ALL ACCOUNTS ON FILE: 1a2b3c4d
    


*Ill update this readme file to include and describe all the correct functions, users, etc once I clean up everything
*Ill also cleanup the webpage layout and change the colorscheme to look more professional 

*This below is from the original readme file:
## Users
### Librarian
- Create Librarian account and Login.
- Can Add, Borrow, Return, and Reserve Books
- Can Issue a Book to a registered Student.
- Can View Borrow Record of All Students.
- Can view Fine (10 dollars for each day after expiry date).
- Can View all Students that are registered into system.

### Student
- Create Student account and Login.
- Can Borrow, Return, and Reserve Books
- Can View their own Borrow Record.


### Faculty
- Create Faculty account and Login.
- Can Borrow, Return, and Reserve Books
- Can View their own Borrow Record.
---
## Functions 

## Add Books
- Add books to the Library System 
- Exclusive to Librarians 

## Borrow Books 
- Borrow Books from the Library System 
- Books can only be Borrowed by Students 
- Books can also be Issued to Students by Librarians

## Return Books
- Borrowed Books can be Returned to the Library
- The Availability status of the Book will update to "Available" 
- The Status of the Book in the Borrow Record will update to "Returned" 

## Reserve Books
- Currently Borrowed or Available Books can be Reserved 
- The Availability status of the Book will update to "Reserved" 
- The Status of the Book in the Borrow Record will update to "Reserved" 

## View Books 
- View all Books in the Library System including their Availability Status 

## View Borrow Record
- View as Record of Books that have been Borrowed and track their Status 

## View All Students 
- View all Students in the Library System
- Exclusive to Librarians 

## HOW TO RUN THIS PROJECT
- Install Python (3.13.2 or most recent version)
- Open Terminal and Execute Following Commands :
```
git clone https://github.com/awilliams363/FinalProject.git
python3 pip install Django 
If you are not already in the LibraryManagement Folder enter: 
cd LibraryManagement 
To check to see if youre in the correct folder enter: 
ls 
and you should see the the file manage.py 
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
- Now enter following URL in Your Browser
```
http://127.0.0.1:8000/
```

## Source Code 
 Here's the source code if needed: 
 SourceCode: https://github.com/sumitkumar1503/librarymanagement.git
