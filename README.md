# University Library Management System:
The University Library Management System (ULMS) is designed to handle the process of managing books, borrowing, and user interactions in a university library. The system will cater to students, faculty, and librarians by providing an intuitive web-based interface for managing books, borrowing, inventory, and accounts. 


## User Roles and Access

### Librarian
- Can Create Librarian accounts and Login
- Can Add, Borrow, Return, Reserve, and Search Books
- Can Issue a Book to a registered Student
- Can View Borrow Record of All Students
- Can View all Students that are registered into system.

### Student
- Can Create Student accounts and Login
- Can Borrow, Return, Reserve, and Search Books
- Can View their personal Borrow Record


### Faculty
- Can Create Faculty accounts and Login
- Can Borrow, Return, Reserve, and Search Books
- Can View their personal Borrow Record

---

## Functions: 

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

## Search Books
- Search for library books by their title 
- Notifies user of whether book exists in the system 
- Notifies user of whether books in the system are available 

## View Books 
- View all Books in the Library System including their Availability Status 

## View Borrow Record
- View as Record of Books that have been Borrowed and track their Status 
- Students can view their personal borrow record 
- Librarians can view the borrow records of all students 

## View All Students 
- View all Students in the Library System
- Exclusive to Librarians 

--- 

## HOW TO RUN THIS PROJECT
- Install Python (3.13.2 or most recent version)
- Open Terminal and Execute Following Commands :
```
git clone https://github.com/awilliams363/FinalProject.git
python3 pip install Django 
If you are not already in the LibraryManagement Folder enter: 
cd FinalProject-main
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