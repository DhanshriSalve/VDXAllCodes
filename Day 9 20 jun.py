#oops concept
#class,object,inheritance,polymorphism,abstraction,encapsulation

# local:inside the the variable ascceesig only called local variable
# global:it created in main progeam it can access any were in the program
# using self called instance attribute
#self it holds the address of current object
# class

# class Employee:
#     name='Dhanshri'
#     age='21'
#     add='pune'

#     def display(self):
#         self.name
#         self.age
#         self.add
# e1=Employee('Dhanshri','21','pune')
#
# e2=Employee('Nikita',21,'nagar')
# print(e2.name)
# e2=Employee()

#by using constructor _init_
# class Employee:
#     name='Dhanshri'
#     age='21'
#     add='pune'
#
#     def _init_(self,name,age,add): #self.name=instance variable access any were in the program
#         self.name=name              #name it cannot access
#         self.age=age
#         self.add=add
#
#     def display(self):
#         self.name
#         self.age
#         self.add
# # e1=Employee('Dhanshri','21','pune')
# # e2=Employee()
# e2=Employee('Nikita',21,'nagar')
# print(e2.display())



#calculate area of circle using constructor

# class Area:
#     def __init__(self,rad):
#         self.radius=rad
#
#     def show(self):
#         res=3.14*self.radius*self.radius
#         print("Area of circle :",res)
# ob1=Area(5)
# ob2=Area(10)
# ob1.show()
# ob2.show()


#Assignment today 20 jun

"""1.	 Define a class DateFormat and define  a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

Examples
format_date("11/12/2019") ➞ "20191211"

format_date("12/31/2019") ➞ "20193112"

format_date("01/15/2019") ➞ "20191501"

"""
# class DateFormat:
#     @staticmethod
#     def format_date(date):
#         month, day, year = date.split('/')
#         return f"{year}{day}{month}"
# d=DateFormat()
# print(d.format_date('11/12/2019'))


'''2.	 You work for a manufacturer, and have been asked to calculate the total profit 
made on the sales of a product. You are given a dictionary containing the cost price per unit (in dollars),
sell price per unit (in dollars), and the starting inventory. Define class Profit and return the total profit made.
Examples
profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}) ➞ 14796

profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}) ➞ 32411
'''
# class profit:
#     def _init_(self,cost,sell,inven):
#         self.cs_p=cost
#         self.se_p=sell
#         self.inv=inven
#
#     def t_profit(self):
#         profits=((self.se_p -self.cs_p)*self.inv)
#         print("Profit of product :",int(profits))
#
# p1=profit(32.67,45.00,1200)
# p1.t_profit()


'''3.Create a class that takes the following four arguments for a particular football player:

name
age
height
weight
Also, create three functions for the class that returns the following strings:

get_age() returns "name is age age"
get_height() returns "name is heightcm"
get_weight() returns "name weighs weightkg"
Examples
 p1 = player("David Jones", 25, 175, 75)

 p1.get_age() ➞ "David Jones is age 25"
 p1.get_height() ➞ "David Jones is 175cm"
 p1.get_weight() ➞ "David Jones weighs 75kg"

'''
# class Football:
#     def _init_(self,name,age,height,weight):
#         self.name=name
#         self.age=age
#         self.height=height
#         self.weight=weight
#
#     def ages(self):
#         print(f"{self.name} is age {self.age}")
#
#     def heights(self):
#         print(f"{self.name} is {self.height} cm")
#     def weights(self):
#         print(f"{self.name} weight {self.weight} kg")
#
# p1=Football("dhanshri",'21',160,48)
#
# p1.ages()
# p1.heights()
# p1.weights()
#

"""4.Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:

Form the fullname by simply joining the first and last name together, separated by a space.
Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. 
Make sure the entire email is in lowercase.

Examples
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
emp_1.fullname ➞ "John Smith"

emp_2.email ➞ "mary.sue@company.com"

emp_3.firstname ➞ "Antony"
# """
# class Employee:
#     def __init__(self,first,last):
#         self.fst=first
#         self.lst=last
#     def show(self):
#         mail=(self.fst+ "." +self.lst+ "."+"@gmail.com")
#         print("Employee Email :",mail)
# p1=Employee("dhanshri","salve")
# p1.show()

# class Employee:
#     def __init__(self, first, last):
#         self.firstname = first
#         self.lastname = last
#         self.fullname = f"{self.firstname} {self.lastname}"
#         self.email = f"{self.firstname.lower()}.{self.lastname.lower()}@company.com"
#
#     def show(self):
#         print(f"Employee Fullname: {self.fullname}")
#         print(f"Employee Email: {self.email}")
#
# # Example
# p1 = Employee("Dhanshri", "Salve")
# p1.show()

"""5.	Define a class and  create a function that takes three integer as input and returns the amount of integers which are of equal value.

Examples
equal(3, 4, 3) ➞ 2

equal(1, 1, 1) ➞ 3

equal(3, 4, 1) ➞ 0
Notes
Your function must return 0, 2 or 3.
"""

# class add:
#     def __init__(self,n1,n2,n3):
#         self.num1=n1
#         self.num2=n2
#         self.num3=n3
#
#     def show(self):
#         if self.num1==self.num2 and self.num2==self.num3:
#             return(3)
#         if self.num1==self.num2 or self.num2==self.num3 or self.num3==self.num1:
#             return(2)
#         if self.num1!=self.num2 and self.num2!=self.num3:
#             return(0)
#
# p1=add(3,3,3)
# print(p1.show())

"""6.	Write a Python class to implement pow(x, n)."""
# class power:
#     def _init_(self,num1,num2):
#         self.n1=num1
#         self.n2=num2
#
#     def show(self):
#         powers=(self.n1 ** self.n2)
#         print("Power of number:",powers)
#
# p1=power(3,2)
# p1.show()

"""7.	Write a Python class to reverse a string word by word.
Input string : 'hello .py'
Expected Output : '.py hello'
"""
# class reverse:
#     def __init__(self,word):
#         self.wrd=word
#
#     def show(self):
#         words=self.wrd.split()
#         print(words)
#         r_wrd=words[::-1]
#         revs=''
#
#         for i in r_wrd:
#             revs+=i +' '
#
#         print(revs)
#
# p1=reverse("hello .py")
# p1.show()

'''8.	Given a class Item with an attributes of name and price

create an Order class that has an attribute item_list that is intitialized to the empty list in the constructor. 
Then add an add_item method that takes an item and appends it to the item_list attribute. 
Then create a get_total method that returns the total price for all the items in item_list attribute.

'''
# class item:
#     item_list=[]
#     def __init__(self):
#         self.item_list =item
#
# class order:
#     def add_item(self,items):
#         self.item_list.append(items)
#
#     def get_total(self):
#         count_total=0
#         for item in self.item_list:
#             count_total +=item
#             print(count_total)
#
# p1=item()
# p2.order()
# p2.add_item(5)
# p2.add_item(67)
# p2.get_total()

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.item_list = []

    def add_item(self, item):
        self.item_list.append(item)

    def get_total(self):
        total_price = sum(item.price for item in self.item_list)
        return total_price

# Example usage:
item1 = Item("Book", 15.99)
item2 = Item("Pen", 1.99)
item3 = Item("Notebook", 5.49)

order = Order()
order.add_item(item1)
order.add_item(item2)
order.add_item(item3)

print("Total price:", order.get_total())



"""9.	Problem Statement: Write a program to build a simple Student Management System using 
Python which can perform the following operations:
•	Accept
•	Display
•	Search
•	Delete
•	Update

"""
# class SMS:
#     def __init__(self):
#         self.name=[]
#         self.roll=[]
#
#     def Accept(self):
#         name=input("Enter name:")
#         roll=int(input("Enter roll no : "))
#         if roll not in self.roll:
#             self.name.append(name)
#             self.roll.append(roll)
#         else:
#             print("repeated roll no ",roll)
#
#     def show(self):
#         for i in range(0,len(self.name)):
#             print("name :",self.name[i])
#             print("roll :",self.roll[i])
#
#     def search(self):
#         x=int(input("Enter roll to search :"))
#         for i in range(0,len(self.roll)):
#             if x==i:
#                 print("name:",self.name[i],"rollno :",self.roll[i])
#                 break
#         else:
#                 print("not found")
#
#     def update(self):
#         x = int(input("Enter roll to search :"))
#         for i in range(0, len(self.roll)):
#             if x == self.roll[i]:
#                 nm=input("Enter name to update :")
#                 self.name[i]=nm
#                 break
#             else:
#                 print("not found")
#
#
# def menu():
#     system = SMS()
#     while True:
#         print("\nStudent Management System")
#         print("1. Accept")
#         print("2. Display")
#         print("3. Search")
#         print("4. Delete")
#         print("5. Update")
#         print("6. Exit")
#         choice = input("Enter your choice: ")
#
#         if choice == '1':
#             system.Accept()
#         elif choice == '2':
#             system.show()
#         elif choice == '3':
#             system.search()
#         elif choice == '4':
#             system.delete()
#         elif choice == '5':
#             system.update()
#         elif choice == '6':
#             print("Exiting the system. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 6.")
#
# menu()



'''10.	Write a Python program to create a class representing a bank. 
Include methods for managing customer accounts and transactions.'''