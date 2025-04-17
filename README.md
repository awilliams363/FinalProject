# FinalProject
 Here's the source code: 
 SourceCode: https://github.com/sumitkumar1503/librarymanagement.git

NOTES: 

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
*Ill add in the faculty pages and functionsa as well, theyre mainly the same as the student functions 



*This below is from the original readme file:
## Functions
### Admin
- Create Admin account and Login.
- Can Add, View, Book
- Can Issue Book (added by Admin) to registered student.
- Can view Issued book with issued date and expiry date.
- Can view Fine (10 rupees for each day after expiry date).
- Can View Students that are registered into system.

### Student
- Create account and Login.
- Can view their issued book only with expiry date and fine(if there any otherwise 0)
---

## HOW TO RUN THIS PROJECT
- Install Python(3.7.6 (that was the version used in the sourcecode. I have the most recent version installed and had no issues)) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :
```
python -m pip install -r requirements. txt
```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```
