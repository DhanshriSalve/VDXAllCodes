# '''1.	Write a menu driven program to perform CRUD and Search operation on Product
# Collection(Name,Price,Manufacturer,Colour,Type).
# Menus are:
# 1.	Show all records
# 2.	Insert record
# 3.	Update record
# 4.	Delete record
# 5.	Search record
# 6.	Exit
# '''
# # import sqlite3 as sql
# # conn =sql.connect('testS.db')
# #
# # print(conn)
# # # conn.execute("create table PRODUCTS (name varchar(30) not null, price int not null,manufacturer text not null, colour text not null ,type text not null)")
# # conn.execute ("insert into PRODUCTS (name,price,manufacturer,colour,type)values('car',20,'audi','black','suv')")
# # conn.execute ("insert into PRODUCTS(name,price,manufacturer,colour,type)values('bike',30,'hero','black','suv')")
# # conn.execute ("insert into PRODUCTS(name,price,manufacturer,colour,type)values('truck',40,'tata','blue','suv')")
# # conn.execute ("insert into PRODUCTS(name,price,manufacturer,colour,type)values('bus',50,'mercedes','red','suv')")
# # conn.execute ("insert into PRODUCTS(name,price,manufacturer,colour,type)values('cart',60,'auto','green','suv')")
# # conn.execute ("insert into PRODUCTS(name,price,manufacturer,colour,type)values('plane',700,'AI','white','suv')")
# # conn.execute ("insert into PRODUCTS(name,price,manufacturer,colour,type)values('jcb',90,'xplane','yellow','suv')")
# # conn.execute ("insert into PRODUCTS(name,price,manufacturer,colour,type)values('tractor',45,'JD','orange','suv')")
# #
# #
# # def insert():
# #     name =(input("enter your name: "))
# #     price =(int(input("enter th price: ")))
# #     manufacturer =(input("enter the manufacturer name:"))
# #     colour =(input("enter the colour of your product:"))
# #     typee =input("enter the type: ")
# #     conn.execute (f"insert into PRODUCTS (name,price,manufacturer,colour,type)"
# #                   f"values('{name}','{price}','{manufacturer}','{colour}','{typee}')")
# #
# #     print("inserted successfully")
# #
# #
# #
# # def update():
# #     name = (input("enter your name to be updated: "))
# #     price = (int(input("enter the price to be updated: ")))
# #     manufacturer = (input("enter the manufacturer name to be updated:"))
# #     colour = (input("enter the colour of your product to be updated:"))
# #     typee = input("enter the type to be updated: ")
# #     conn.execute((f"update PRODUCTS set price='{price}', manufacturer='{manufacturer}', "
# #                  f"colour ='{colour}',type='{typee}'where name='{name}'"))
# #     conn.commit()
# #     print("updated successfully")
# #
# # def delete():
# #     name = (input("enter your name to be deleted: "))
# #     conn.execute(f"delete from PRODUCTS where name='{name}'")
# #     conn.commit()
# #     print("deleted successfully")
# #
# #
# # def search():
# #     name = (input("enter your name to be searched: "))
# #     x = conn.execute(f" select * from PRODUCTS where name='{name}'")
# #     #     rows=cursor.fetchall()
# #     #     conn.commit()
# #     print(x)
# #     for i in x:
# #         print("searched successfully:", (i))
# #
# # def show():
# #     data = conn.execute("select* from PRODUCTS")
# #     for i in data:
# #         print(i)
# #
# # while True:
# #         print("\nChoose an operation:")
# #         print("1. Insert a record")
# #         print("2. Update a record")
# #         print("3. Delete a record")
# #         print("4. Search for a record")
# #         print("5. Show all records")
# #         print("6.exit")
# #
# #         choice = input("Enter your choice (1-6): ")
# #
# #         if choice == '1':
# #             insert()
# #         elif choice == '2':
# #             update()
# #         elif choice == '3':
# #             delete()
# #         elif choice == '4':
# #             search()
# #         elif choice == '5':
# #             show()
# #         elif choice == '6':
# #             print("Connection closed.")
# #             break
# #         else:
# #             print("Invalid choice. Please try again.")
# #
#
#
# '''2.	Write a program to perform CRUD and Search operation on Database Company. Create tables like
#
#  Dept(dept_id,name,hod,staff) Employee(emp_id,name,salary,address), Attendance(emp_id,present-days,leaves).
#
# Perform following operations.
# 1	Show all records
# a.	Show records from employee where salary is greater than 50000.
# b.	Show records from attendance  those are present for all 30 days.
# c.	Show records from dept where staff>30
#
# 2	Insert record
# 3	Update record
# a.	Update records of employee , salary=50000 where address=”Delhi”
# b.	Update records of attendance where id>5
#
# 4	Delete record
# a.	Delete record of attendance where leaves >10
# b.	Delete record of dept where staff<5.
# 5	Search record
# 6	Exit
#
# '''
#
# # import sqlite3 as sql
# # conn =sql.connect('testS.db')
# # conn.execute("pragma foreign_keys=off")
# # print(conn)
# # # conn.execute("create table DEPT(dept_id int not null, name varchar(30) not null ,hod varchar(30) not null ,staff int not null)")
# # def insert_dept():
# #     dept_id =(input("enter your dept_id: "))
# #     name =(input("enter the name: "))
# #     hod =(input("enter the  hod name:"))
# #     staff =int(input("enter the count of the staff:"))
# #     conn.execute (f"insert into DEPT(dept_id,name,hod,staff)values('{dept_id}','{name}','{hod}','{staff}')")
# #     print("inserted successfully")
# #     conn.commit()
# # def delete_dept():
# #     conn.execute("delete from DEPT where staff < 5")
# #     conn.commit()
# #     print("deleted successfully")
# # def show_dept():
# #     x=conn.execute("select * from DEPT where staff > 30")
# #
# #     for i in x:
# #         print("searched successfully ", i)
# # #insert_dept()
# # #delete_dept()
# # #show_dept()
# # # conn.execute("create table Emp(emp_id int primary key not null, name varchar(30) not null ,address varchar(30) not null ,salary int not null)")
# # def insert_employee():
# #     emp_id =(input("enter your emp_id: "))
# #     name =(input("enter the name: "))
# #     address=(input("enter the  address:"))
# #     salary =int(input("enter your salary:"))
# #     conn.execute (f"insert into Emp(emp_id,name,address,salary)values('{emp_id}','{name}','{address}','{salary}'")
# #     print("inserted successfully")
# #     conn.commit()
# #
# # def show_employee():
# #     data=conn.execute("select * from Emp salary<50000")
# #     for i in data:
# #         print(i)
# #
# # def update_employee():
# #     emp_id = (input("enter your emp_id to br updated : "))
# #     name = (input("enter the name: "))
# #     address = (input("enter the  address:"))
# #     salary = int(input("enter your salary:"))
# #     conn.execute("UPDATE Emp SET name = ?, address = ?, salary = ? WHERE emp_id = ?"
# #                  ,(name, address, salary, emp_id))
# #     conn.commit()
# #     print("updated successfully")
# #
# # def update_salary():
# #     #mp_id = (input("enter your emp_id to br updated : "))
# #
# #     conn.execute("UPDATE Emp SET salary = 50000  where  address = 'delhi' ")
# #     conn.commit()
# #     print("updated successfully")
# #
# # #conn.execute("create table Attendance(emp_id int primary key not null, presentdays  int not null ,leaves int not null ,foreign key (emp_id) references Emp (emp_id))")
# # def insert_attendance():
# #     emp_id =(input("enter your emp_id: "))
# #     presentdays =int(input("enter no of days: "))
# #     leaves = int(input("enter no of leaves: "))
# #     conn.execute (f"insert into Attendance(emp_id,presentdays,leaves)values('{emp_id}','{presentdays}','{leaves}') ")
# #     print("inserted successfully")
# #     conn.commit()
# #
# # def show_emp_present():
# #     data=conn.execute("select * from Attendance where presentdays>=30")
# #     for i in data:
# #         print(i)
# #
# # #conn.execute("drop table Attendance ")
# # def delete_leaves_10 ():
# #     conn.execute("delete from Attendance where leaves > 10")
# #     conn.commit()
# #     print("deleted successfully")
#
#
# # #---------------------------------------------------------------------------------------
# # insert_dept()
# # delete_dept()
# #show_dept()
# # insert_employee()
# # show_employee()
# # update_employee()
# # update_salary()
# # insert_attendance()
# # show_emp_present()
# # delete_leaves_10()
#
#
# '''3.	A Student Database Management System automates and streamlines various tasks and processes
#  related to student information, making it easier for educators and administrators to access and analyze data.
#
# Dataset: For this project, build a sample dataset contains the following variables:
#
# Studen_ID: A unique code for each student
#
# Student Name: Full name of the student
#
# Age: Age of student in numbers
#
# Gender: Variable specifying the gender of the student
#
# Grade-level: Grade in which the student is
#
# Attendance: Total number of days the student attended the classes
#
# GPA: Score of the student
# '''
# # import sqlite3 as sql
# # conn=sql.connect('testS.db')
# # print(conn)
# # # conn.execute ('''create table SDM(student_id int
# # # primary key  not null,name text not null,gender text not null,age int not null,grade char(5) not null,attendance int not null,GPA real )''')
# # def insert():
# #     student_id = (input("enter your student_id: "))
# #     name = (input("enter the name: "))
# #     age = (input("enter the  age:"))
# #     gender =(input("enter your gender:"))
# #     grade = (input("enter your grade:"))
# #     attendance = int(input("enter your attendance:"))
# #     GPA = float(input("enter your GPA:"))
# #
# #
# #     conn.execute(f"insert into SDM(student_id,name,age,gender,grade,attendance,GPA)values('{student_id}','{name}','{age}','{gender}','{grade}','{attendance}','{GPA}')")
# #     print("inserted successfully")
# #     conn.commit()
# # #insert()
# # def count_of_student():
# #     x=conn.execute("select count (name) from SDM")
# #     for i in x:
# #         print(i[0])
# #
# # def count_of_student():
# #     y=conn.execute("select * from SDM where attendance > 30")
# #     for i in y:
# #         print(i)
# #
# # def avg_GPA():
# #     z=conn.execute("select avg (GPA) from SDM")
# #     for i in z:
# #         print(i)
#
# # insert()
# # avg_GPA()
# # count_of_student()
#
#
# '''4.	Traveling is fun! But planning a trip, booking tickets, making reservations, dealing with last-minute cancellations, etc., can be stressful! A railway management system allows users to book tickets, cancel reservations, check tariffs, etc.
# Dataset: The dataset contains only one file which has the train details,
# o	Train No,
# •	Station Code,
# •	Station Name,
# •	Arrival time,
# •	Departure Time,
# •	Distance,
# •	Source Station,
# •	Source Station Name,
# •	Destination Station,
# •	Destination Station Name
# SQL Project Idea: This project uses MySQL as the backend database to let users perform the following tasks-
# 1.	Book a ticket or cancel a booked ticket.
# 2.	Check fares before booking, and also check their bookings.
# 3.	Check the available trains. '''
# import sqlite3 as sql
# conn= sql.connect ('testS.db')
# print(conn)
# conn.execute("create table INDRAIL(train_no int primary key ,st_code int ,st_name int ,arr_time int ,dept_time int,dis int,sr_st char(30),dst_st char(30))")
# import sqlite3 as sq
#
# conn = sq.connect("RailwayReservation.db")
# print("Database connection established:", conn)
#
# conn.execute('''
# CREATE TABLE IF NOT EXISTS Trains (
#     train_no INTEGER PRIMARY KEY NOT NULL,
#     station_code INTEGER,
#     station_name TEXT,
#     arrival_time TEXT,
#     departure_time TEXT,
#     distance INTEGER,
#     source_station TEXT,
#     destination_station TEXT
# );
# ''')
#
# conn.execute('''
# CREATE TABLE IF NOT EXISTS Ticket (
#     ticket_id INTEGER PRIMARY KEY NOT NULL,
#     train_no INTEGER,
#     FOREIGN KEY(train_no) REFERENCES Trains(train_no)
# );
# ''')
#
#
# def insertTrains():
#     train_no = int(input("Enter Train Number"))
#     station_code = int(input("Enter Station code"))
#     station_name = input("Enter Station Name")
#     arrival_time = input("Enter Arrival Time")
#     departure_time = input("Enter Departure Time ")
#     distance = int(input("Enter Distance"))
#     source = input("Enter source")
#     destination = input("Enter Destination")
#
#     conn.execute("Insert into Trains values(?,?,?,?,?,?,?,?)",
#                  (train_no, station_code, station_name, arrival_time, departure_time, distance, source, destination))
#
#     print("Record Inserted")
#
#
# def book_ticket():
#     ticket_id = int(input("Enter Ticket ID: "))
#     train_no = int(input("Enter Train Number: "))
#     conn.execute("INSERT INTO Ticket (ticket_id, train_no) VALUES (?, ?)", (ticket_id, train_no))
#     conn.commit()
#     print("Train Booked Successfully")
#
#
# def cancel_ticket():
#     ticket_id = int(input("Enter Ticket ID: "))
#     conn.execute(f"DELETE FROM Ticket WHERE ticket_id = {ticket_id}")
#     conn.commit()
#     print("Ticket Canceled Successfully")
#
#
# def show_fares():
#     train_no = int(input("Enter Train Number: "))
#     data = conn.execute("SELECT * FROM Trains WHERE train_no = ?", (train_no,))
#     # row = data.fetchone()
#     for row in data:
#         print(row)
#     if row:
#         print("Train No:", row[0])
#         print("Station Code:", row[1])
#         print("Station Name:", row[2])
#         print("Arrival Time:", row[3])
#         print("Departure Time:", row[4])
#         print("Distance:", row[5])
#         print("Source Station:", row[6])
#         print("Destination Station:", row[7])
#     else:
#         print("No train found with the given number")
#
# #
# def check_available_trains():
#     data = conn.execute("SELECT * FROM Trains")
#     for row in data:
#         print("Train No:", row[0])
#         print("Station Code:", row[1])
#         print("Station Name:", row[2])
#         print("Arrival Time:", row[3])
#         print("Departure Time:", row[4])
#         print("Distance:", row[5])
#         print("Source Station:", row[6])
#         print("Destination Station:", row[7])
#         # print("-" * 20)
#
#
# while True:
#     print("1.Insert into Trains")
#     print("2. Book Ticket")
#     print("3. Cancel Ticket")
#     print("4. Check Fares")
#     print("5. Check Available Trains")
#     print("6. Exit")
#
#     choice = int(input("Enter your choice: "))
#
#     if choice == 1:
#         insertTrains()
#
#
#     elif choice == 2:
#         book_ticket()
#     elif choice == 3:
#         cancel_ticket()
#     elif choice == 4:
#         show_fares()
#     elif choice == 5:
#         check_available_trains()
#     elif choice == 6:
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Please try again.")
#
# conn.close()

print("Good Morning !!!")