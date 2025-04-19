# University Library Management System:
The University Library Management System (ULMS) is designed to handle the process of managing books, borrowing, and user interactions in a university library. The system will cater to students, faculty, and librarians by providing an intuitive web-based interface for these functions. 

---

## User Roles and Access

### Librarian
- Can Create Librarian accounts and Login
- Can Add, Borrow, Return, Reserve, View, and Search Books
- Can Issue a Book to a registered Student
- Can View Borrow Record of All Students
- Can View all Students that are registered into system

### Student
- Can Create Student accounts and Login
- Can Borrow, Return, Reserve, View, and Search Books
- Can View their personal Borrow Record


### Faculty
- Can Create Faculty accounts and Login
- Can View and Search Books
- Can Issue and Return Books to and from registered Students

---

## Basic Functions

### Add Books
- Add books to the Library 
- Exclusive to Librarians 

### Borrow Books 
- Borrow Books from the Library 
- Books can only be Borrowed by Students 
- Books can be Issued to Students by Librarians or Faculty

### Return Books
- Borrowed Books can be Returned to the Library 
- Books registered to Students can be Returned by Librarian and Faculty Users or the Registered Student
- The Availability Status of the Book will update to "Available" 
- The Status of the Book in the User's Borrow Record will update to "Returned" 

### Reserve Books
- Currently Borrowed or Available Books can be Reserved 
- Books can be Reserved to a Registered Student by the Student or all Librarians 
- The Availability status of the Book will update to "Reserved" 
- The Status of the Book in the Borrow Record will update to "Reserved" 

### Search Books
- Search for library books by their title 
- Any Registered User can Search a Book 
- Notifies user of whether the Book exists in the Library 
- Notifies user of whether the Book is currently available 

### View Books 
- View all Books in the Library System including their Availability Status 
- Any Registered User can View the Books

### View Borrow Record
- View as Record of Books that have been Borrowed and track their Status 
- Students can view their Personal Borrow Record 
- Librarians can view the Borrow Records of all Students 

### View All Students 
- View all Students in the Library System
- Exclusive to Librarians 

--- 

## Advanced Function 

### Automated Book Return Reminders 
- Issues a Reminder when the Due Date for a Borrowed Book is in the next 7 days and 2 days 
- Reminder Notifications can be issued to and viewed by Students and Faculty 

---

## How to run the project
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

- You can create your own accounts for testing 
- You can use sample accounts: student1, student2, librarian1, and faculty1 
- Using password: 1a2b3c4d