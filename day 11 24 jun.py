# SQlite3 query


# import sqlite3 as sql
# con=sql.connect('test.db')
# print(con)

# con.execute("create table employee(id int not null,name char(20), address varchar(40) not null,salary int)")

# con.execute("insert into employee(id,name,address,salary) values(1,'dhanu','pune','2000')")
# con.execute("insert into employee(id,name,address,salary) values(2,'niks','pune','1900')")
# con.execute("insert into employee(id,name,address,salary) values(3,'yogita','pune','2200')")
# con.execute("insert into employee(id,name,address,salary) values(4,'piya','pune','1000')")
# con.execute("insert into employee(id,name,address,salary) values(5,'sneha','pune','32000')")

# con.rollback()
# con.commit()

# data=con.execute("Select * from employee where id=2")
# for i in data:
#     print(i)

# data=con.execute("Select * from employee ")
# for i in data:
#     print(i)

# con.execute("update employee set address='loni' where id=2")
# data=con.execute("select * from employee")
# for i in data:
#     print(i)

# con.execute("delete  from employee  where id=2")
# data=con.execute("select * from employee")
# for i in data:
#     print(i)


#Assignment todays

"""1.	Write a menu driven program to perform CRUD and Search operation on
 Product Collection(Name,Price,Manufacturer,Colour,Type).
Menus are:
1.	Show all records
2.	Insert record
3.	Update record
4.	Delete record
5.	Search record
6.	Exit

"""
# import sqlite3 as sql
# conn=sql.connect('data.db')
# print(conn)

# conn.execute("create table producta(name char(20), price int not null, manufacture char(40),clour char(20) not null,type text )")

# conn.execute("insert into producta(name,price,manufacture,clour,type) values('bmw',60000,'tata','black','car')")
# conn.execute("insert into producta(name,price,manufacture,clour,type) values('audi',60000,'hero','white','car')")
# conn.execute("insert into producta(name,price,manufacture,clour,type) values('baleno',60000,'honda','red','car')")
# conn.execute("insert into producta(name,price,manufacture,clour,type) values('swift',60000,'maruti','blue','car')")
# conn.execute("insert into producta(name,price,manufacture,clour,type) values('creta',60000,'hyndayi','pink','car')")

# d=conn.execute("select * from product")
# for i in d:
#      print(i)
#  def show():
#     data1=conn.execute("SELECT * FROM Products")
#     print("name price manufacture colour type")
#     for row in data1:
#         print(row[0]," ",row[1]," ",row[2]," ",row[3]," ",row[4]," ",row[5])


# def insert():
#     name1=input("Enter your name :")
#     price1=int(input("Enter your price :"))
#     manufacture1=input("Enter manufacture name:")
#     color1=input("Enter your color :")
#     typee1=input("Enter tpye of car :")
#
#     conn.execute(f"insert into producta (name,price, manufacture,clour,type) values('{name1}','{price1}',' {manufacture1}',' {color1}','{typee1}')")
#     conn.commit()
#

# def update():
#     name1=input("Enter you want to change :")
#     price1=input("Enter you:")
#     conn.execute(f"update producta SET price={price1}  where name={name1} ")
#     conn.commit()
#     print("Recored updated Successfully")
#


# d=conn.execute("select * from producta")
# for i in d:
#      print(i)

#
#
# def delete():
#     id=int(input("Enter id where you want to delete"))
#
#     conn.execute(f"delete from Products where ID={id}")
#     conn.commit()
#
#
# def search():
#     data = conn.execute(f"SELECT * FROM Products where ID={s}")
#     for i in data:
#         print(i)
#
# def main():
    # while True:       #to keep code running until a condition is acheived
    # #     print("1.Show ")
    # #     print("2.Insert")
    # #     print("3.Update")
    # #     print("4.Delete")
    # #     print("5.Search")
    # #     print("6. Exit")

    #
    #     s=input("Enter product Id for search")
    #     choice=input("Enter your choice:")
    #
    #     if choice=='1':
    #         show()
    #
    #     elif choice=='2':
    #         insert()
    #
    #     elif choice=='3':
    #         Update()
    #
    #     elif choice=='4':
    #         delete()
    #
    #     elif choice=='5':
    #         search()
    #
    #     else:
    #     exit()

# main()

"""2.	Write a program to perform CRUD and Search operation on Database Company. Create tables like

 Dept(dept_id,name,hod,staff) Employee(emp_id,name,salary,address), Attendance(emp_id,present-days,leaves). 

Perform following operations.
1	Show all records 
a.	Show records from employee where salary is greater than 50000.
b.	Show records from attendance  those are present for all 30 days.
c.	Show records from dept where staff>30

2	Insert record 
3	Update record 
a.	Update records of employee , salary=50000 where address=”Delhi”
b.	Update records of attendance where id>5

4	Delete record
a.	Delete record of attendance where leaves >10
b.	Delete record of dept where staff<5.

5	Search record
6	Exit
"""

# import sqlite3 as sql
# conn=sql.connect('text.db')
# print(conn)

# conn.execute("""create table Dept
#             (dept_id int primary key,
#             name char(20),
#             hod char(30) NOT NULL,
#             staff int);""")
# conn.execute("""create table Employee
#              (Emp_id int primary key,
#              name char(20) ,
#              salary int not null,
#              Address text);""")
#
# conn.execute("""create table Attendance
#              (Emp_id int primary key ,
#              pre_day int not null,
#             leave int,foregin key (Emp_id) references Employee(Emp_id))""")

# def show():
#     data1 = conn.execute("SELECT * FROM Dept ")
#     for row in data1:
#         print(row[0], " ", row[1], " ", row[2], " ", row[3])

# def show1():
#     print("Employees salary greater than 50000")
#     data2 = conn.execute("SELECT * FROM Employee where salary>=50000 ")
#     for row in data2:
#        print(row[0], " ", row[1], " ", row[2], " ", row[3])


# def show2():
#     print("Employees present for all 30 days")
#     data3 = conn.execute("SELECT * FROM Attendance where presentdays==30 ")
#     for row in data3:
#         print(row[0], " ", row[1], " ", row[2], " ", row[3])
#

# def insertDept(staff1=None):
#     dept_id1=int(input("Enter your dept ID :"))
#     name1=input("Enter Dept name :")
#     hod1=(input("Enter HOD name :"))
#     sta=(input("Enter staff :"))
#     # staff1=input("Enter staff")
#     conn.execute( f"insert into Dept(dept_id,name,hod,staff) values('{dept_id1}','{name1}',' {hod1}',' {staff1}')")
#     conn.commit()
#
# def insertEmployee():
#     Emp1=int(input("Enter Employee ID:"))
#     name2=input("Enter Employee Name:")
#     salary1=int(input("Enter Employee Salary:"))
#     Add1=input("Enter Employee Address:")
#     conn.execute(f"insert into Employee(Emp_id,name,salary,Address) values('{Emp1}','{name2}',' {salary1}',' {Add1}')")
#     conn.commit()
#
# def insertAttendance():
#     Emp1=int(input("Enter Employee ID:"))
#     pre_day1=int(input("Enter present Day:"))
#     leaves1=int(input("Enter leaves:"))
#     conn.execute(f"insert into Attendance(Emp_id,Pre_day,leave) values('{Emp1}','{pre_day1}','{leaves1}')")
#     conn.commit()
# def update():
#     conn.execute(f"UPDATE Employee SET salary =50000 where Address='Delhi'")
#     conn.commit()
#     print("Updated Salary")
#
#     conn.execute(f"UPDATE Attendance SET pre_day=20 where id>5")
#     conn.commit()
#     print("Updated present Days")
#
# def delete():
#     conn.execute(f"delete * form Attendance where leaves>10")
#     conn.commit()
#     print("Deleted Record")
#
#     conn.execute(f"delete * from Dept where staff<5")
#     conn.commit()
#     print("Deleted")
#
# def search():
#
#     Emp_id = input("Enter Employee Id for search")
#     data = conn.execute(f"SELECT * FROM Employee where emp_id={Emp_id}")
#     conn.commit()
#     for row in data:
#         print(row)
#
#     Dept_id= input("Enter Department ID for search")
#     data = conn.execute(f"SELECT * FROM Dept where dept_id={Dept_id}")
#     conn.commit()
#     for row in data:
#         print(row)

# def main():
#     while True:  # to keep code running until a condition is acheived
#         print("1.Show ")
#         print("2.Show1 ")
#         print("3.Show ")
#
#         print("4.Insert into Department")
#         print("5.Insert into Employee")
#         print("6.Insert into Attendance")
#         print("7.Update")
#         print("8.Delete")
#         print("9.Search")
#         print("10. Exit")
#
#         choice=input("Enter your choice:")
#
#         if choice=='1':
#             show()
#
#         elif choice=='2':
#             show1()
#
#         elif choice=='3':
#             show2()
#
#         elif choice=='4':
#             insertDept()
#
#         elif choice=='5':
#             insertEmployee()
#
#         elif choice=='6':
#             insertAttendance()
#
#         elif choice=='7':
#             update()
#
#         elif choice=='8':
#             delete()
#
#         elif choice=='9':
#             search()
#
#         else:
#             conn.close()
# # main()

# class Dept:
#     def insertDept(staff1=None):
#         dept_id1 = int(input("Enter your dept ID :"))
#         name1 = input("Enter Dept name :")
#         hod1 = (input("Enter HOD name :"))
#         # sta = (input("Enter staff :"))
#         staff1=input("Enter staff")
#         conn.execute(f"insert into Dept(dept_id,name,hod,staff) values('{dept_id1}','{name1}',' {hod1}',' {staff1}')")
#         conn.commit()
#
#
# class Employees:
#     def insertEmployee():
#         Emp1 = int(input("Enter Employee ID:"))
#         name2 = input("Enter Employee Name:")
#         salary1 = int(input("Enter Employee Salary:"))
#         Add1 = input("Enter Employee Address:")
#         conn.execute(
#             f"insert into Employee(Emp_id,name,salary,Address) values('{Emp1}','{name2}',' {salary1}',' {Add1}')")
#         conn.commit()
#
#     def showEithSalaryGreaterThen50000():
#         print("Employees salary greater than 50000")
#         data2 = conn.execute("SELECT * FROM Employee where salary>=50000 ")
#         for row in data2:
#             print(row[0], " ", row[1], " ", row[2], " ", row[3])
#
#     def update():
#         conn.execute(f"UPDATE Employee SET salary =50000 where Address='Delhi'")
#         conn.commit()
#         print("Updated Salary")
#
#
# emp = Employees
#
# emp.showEithSalaryGreaterThen50000()