<p align="center">
  <img src="https://github.com/Ethan1709/holbertonschool-AirBnB_clone/blob/main/logo.png" alt="HolbertonBnB logo">
</p>

<h1 align="center">HolbertonBnB</h1>
<p align="center">An AirBnB clone.</p>
---

# AirBnB clone - The console

## Description of the project

It is the first step towards building a full web application. This project is entierly in Python. Here are the main implementations in this project:

- Creation of the parent class called BaseModel that creates the flow between serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- Creation of child classes that inherits from the main class BaseModel: such as User, State, City, Place, review, state, amenity...
- Creation of the class FileStorage which is a storage engine
- Creation of the console
- And making test files to handle errors we may encounter



## Requirements

Python Scripts:

 - All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)


 Python Unit Tests

 - Test files should be inside a folder tests
 - The unittest module have to be used
 - Test files should be python files (extension: .py)
 - Test files and folders should start by test_
 - File organization in the tests folder should be the same as in the project
 - All tests should be executed by using this command: ```python3 -m unittest discover tests```
 - tests should also pass in non-interactive mode: ```$ echo "python3 -m unittest discover tests" | bash```

## Description of the command interpreter

The command interpreter can be run in interactive mode and in non-interactive mode like in the examples below.


How to start it:

Interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

How to use it:

```
$ ./console.py 
(hbnb) create BaseModel
4027b8d1-7465-4758-9a4e-322055c1e4f6
(hbnb) show BaseModel 4027b8d1-7465-4758-9a4e-322055c1e4f6
[BaseModel] (4027b8d1-7465-4758-9a4e-322055c1e4f6) {'id': '4027b8d1-7465-4758-9a4e-322055c1e4f6', 'created_at': datetime.datetime(2023, 2, 23, 17, 59, 30, 12952), 'updated_at': datetime.datetime(2023, 2, 23, 17, 59, 30, 12978)}
(hbnb)
```
To quit the console, we can use the quit command or the EOF command:
```
$ ./console.py
(hbnb) quit
$
```
```
$ ./console.py
(hbnb) EOF
$
```

What are all the commands that are implemented and how to use them ?


Create a User and Show all instances created
```
./create User
e63c2296-af78-403d-812f-fe95ce1ced80
(hbnb) all
(hbnb) ["[BaseModel] (11563025-add0-4ed6-8265-0861dc8428b7) {'id': '11563025-add0-4ed6-8265-0861dc8428b7', 'created_at': datetime.datetime(2023, 2, 21, 17, 22, 37, 770256), 'updated_at': datetime.datetime(2023, 2, 21, 17, 22, 37, 770273)}", "[City] (b894b822-5192-4377-b990-626565826ea0) {'id': 'b894b822-5192-4377-b990-626565826ea0', 'created_at': datetime.datetime(2023, 2, 23, 18, 10, 38, 513340), 'updated_at': datetime.datetime(2023, 2, 23, 18, 10, 38, 513360)}", "[User] (e63c2296-af78-403d-812f-fe95ce1ced80) {'id': 'e63c2296-af78-403d-812f-fe95ce1ced80', 'created_at': datetime.datetime(2023, 2, 23, 18, 13, 44, 426827), 'updated_at': datetime.datetime(2023, 2, 23, 18, 13, 44, 426837)}"]
```

Update an Instance
```
(hbnb) create User
ff4efc6d-7971-4026-aed2-06be925c80ad
(hbnb) update User ff4efc6d-7971-4026-aed2-06be925c80ad email 42@cnul.com
(hbnb) show User ff4efc6d-7971-4026-aed2-06be925c80ad
[User] (ff4efc6d-7971-4026-aed2-06be925c80ad) {'id': 'ff4efc6d-7971-4026-aed2-06be925c80ad', 'created_at': datetime.datetime(2023, 2, 23, 18, 26, 39, 535110), 'updated_at': datetime.datetime(2023, 2, 23, 18, 26, 39, 535131), 'email': '42@cnul.com'}
```

Destroy an Instance
```
(hbnb) show User ff4efc6d-7971-4026-aed2-06be925c80ad
[User] (ff4efc6d-7971-4026-aed2-06be925c80ad) {'id': 'ff4efc6d-7971-4026-aed2-06be925c80ad', 'created_at': datetime.datetime(2023, 2, 23, 18, 26, 39, 535110), 'updated_at': datetime.datetime(2023, 2, 23, 18, 26, 39, 535131), 'email': '42@cnul.com'}
(hbnb) destroy User ff4efc6d-7971-4026-aed2-06be925c80ad
** no instance found **
(hbnb)
```

## AUTHORS

- Ethan B benyayerethan@gmail.com
- simonrichard-dev simon.insa@gmail.com
