# Overview

The program that I wrote connects with the MySQL database and displays information about a companies employees such as salary and name. The program uses a menu to select from a list of actions and then based on the choice will execute the statement. 

I designed this program so that information about the employees in a company could easily be accessed by someone without having to know SQL. 

[Software Demo Video](https://youtu.be/gu7Ltar-Z2U)

# Relational Database

I am using MySQL database. 

I created two tables one that stores the workers information such as their worker id, name, address, and salary. The other table stores the number of hours worked for each employee. Each employee can have multiple sets of hours worked in the table but is related to each employee. 

# Development Environment

Visual Studio Code

Python 3.9.5 64 bit
mysql.connector 
CSV library

# Useful Websites

* [W3 Schools](https://www.w3schools.com/sql/)

# Future Work

* Improve database layout and make output from databse more readable
* Use a web app to display information instead of console
* Add adition functionality such as updating addresses to improve user experince. 