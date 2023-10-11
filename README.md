# The ALX Africa AirBnB Clone Project
![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

## Project Description
## Welcome to the AirBnB clone project!
This is the first step towards building our first full web application: 
<b>the AirBnB clone</b> This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration… 

Data (python objects) generated are stored in a json file and can be accessed with the help of the json module in python

## Description of the command interpreter:

This command line interpreter  serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

  =>  create - Create a new object (ex: a new User or a new Place)
  =>  show -   Retrieve an object from a file, a database etc…
  =>  update - Update attributes of an object
  =>  destroy - Destroy an object
  => others -   count, compute stats, etc…

## How to start it

To run/start on on your local machine (ubuntu 22.04) clone it from github, this is only for development and testing purposes.

## Installing

clone the repository of the project from Github @addiserp. This will contain the simple shell program and all of its dependencies.

```
git clone https://github.com/addiserp/AirBnB_clone.git
```
After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to work.

> /console.py : The main command interpreter.
>
> models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON file to instances
> 
> models/__ init __.py:  A unique `FileStorage` instance fot program
> 
> models/base_model.py: Class that defines all common attributes/methods for other classes.
> 
> models/user.py: User class that inherits from BaseModel
>
>models/city.py: City class that inherits from BaseModel
> 
>models/state.py: State class that inherits from BaseModel
>
>models/place.py: Place class that inherits from BaseMode
>
>models/review.py: Review class that inherits from BaseModel
>
>models/amenity.py: Amenity class that inherits from BaseModel
>

## How to use it
You can choose in two different modes:


**Non-interactive** or **Interactive** 

In **Non-interactive mode**, the shell will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. In this mode no prompt will appear, and no further input will be expected from the user.


```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
In **Interactive mode**, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

## Format of Command Input

In order to give commands to the console, these will need to be piped through an echo in case of  **Non-interactive mode**.

In  **Interactive Mode**  
In this mode, the console can be exited using the **CTRL + D** combination,  **CTRL + C**, or the command **quit** or **EOF**.

## Arguments

Most commands have several options or arguments that can be used when executing the program. In order for the Shell to recognize those parameters, you must separate everything with spaces.

Example:

```

user@ubuntu:~/AirBnB$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
user@ubuntu:~/AirBnB$ ./console.py

```

or

```
user@ubuntu:~/AirBnB$ ./console.py $ echo "create BaseModel" | ./console.py
(hbnb)
e37ebcd3-f8e1-4c1f-8095-7a019070b1fa
(hbnb)
user@ubuntu:~/AirBnB$ ./console.py
```

## Available commands and what they do

The recognizable commands by the interpreter are the following:

|Command| Description |
|--|--|
| **-----** | **-----** |
| **help** | Provides a text describing how to use a command.  |
| **Usage** | By itself --or-- **help <command\>** |
| **-----** | **-----** |
| **create** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`.  Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| **Usage** | **create <class name\>**|
| **-----** | **-----** |
| **show** | Prints the string representation of an instance based on the class name and `id`  |
| **Usage** | **show <class name\> <id\>** --or-- **<class name\>.show(<id\>)**|
| **-----** | **-----** |
| **all** | Prints all string representation of all instances based or not on the class name.  |
| **Usage** | By itself or **all <class name\>** --or-- **<class name\>.all()** |
| **-----** | **-----** |
| **update** | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file).  |
| **Usage** | **update <class name\> <id\> <attribute name\> "<attribute value\>"** ---or--- **<class name\>.update(<id\>, <attribute name\>, <attribute value\>)** --or-- **<class name\>.update(<id\>, <dictionary representation\>)**|
| **-----** | **-----** |
| **count** | Retrieve the number of instances of a class.  |
| **Usage** | **<class name\>.count()** |
| **-----** | **-----** |
| **destroy** | Deletes an instance based on the class name and `id` (saves the change into a JSON file).  |
| **Usage** | **destroy <class name\> <id\>** --or-- **<class name>.destroy(<id>)** |
| **-----** | **-----** |
| **quit or EOF** | Exits the program |
| **Usage** | By itself |

## Authors

Mikias Gedlu | Email: [addiserp](mailto:addiserp@gmail.com) 

BRYAN ASEGA | Github: [brayanasega](mailto:brayanasega@gmail.com)