#inheritance
#if the both class method name is same then it called 1st priority method
#mro

#simple inheritance
#1 base 1 child

# multiple
# 1 base 2 child
#
# multilevel
# 1 base
#
# heirachical
#
# class A:
#     x=10
#     def display(self):
#         print("class of A")
#
# class B(A):
#     y=20
#     def show(self):
#         print("method of class b")
#
# class C(A):
#     z=30
#     def sum(self):
#         n=(self.x+self.y+self.z)
#         print("Addition :",n)
# class D(B,C):
#     def avg(self):
#         m=((self.x+self.y+self.z)/3)
#         print("average",m)
#
# obj=D()
# obj.display()
# obj.show()
# obj.sum()
# obj.avg()

#encapsulation
#__private
#_protected

#polymorphism
#oevrriding
# #same function but it can be run by the priority base
# class A():
#     x,y,z

#abstaction
#@-decorator- built in data type
#
# from abc import ABC, abstractmethod
#
# class Student(ABC):
#     @abstractmethod
#
#     def area(self):
#         pass
#
# class circle(Student):
#     def __init__(self,r):
#         self.r=r
#
#     def area(self):
#         area=3.14*self.r*self.r
#         print(area)
#
# obj=circle(5)
# obj.area()



# from abc import ABC, abstractmethod
#
# class Car(ABC):
#     @abstractmethod
#     def mileage(self):
#         pass
# class Tesla(Car):
#     def mileage(self):
#         print("The mileage is 30kmph")
# class Suzuki(Car):
#     def mileage(self):
#         print("The mileage is 25kmph ")
# class Duster(Car):
#     def mileage(self):
#         print("The mileage is 24kmph ")
# class Renault(Car):
#     def mileage(self):
#         print("The mileage is 27kmph ")
#
# t = Tesla()
# t.mileage()
#
# r = Renault()
# r.mileage()
#
# s = Suzuki()
# s.mileage()

# d = Duster()
# d.mileage()

#Assignment today 21 jun

'''1.	Rectangle class in Python language, allowing you to build a rectanglewith length and width attributes.2
a.	Create a Perimeter() method to calculate the perimeter of the rectangle and a Area()method
 to calculate the area of the rectangle.
b.	Create a method display() that display the length, width, perimeter and area of an object 
created using an instantiation on rectangle class
c.	.Create a Parallelepipe child class inheriting from the Rectangle class and with a height 
attribute and another Volume() method to calculate the volume

'''
# class Rectangle():
#     def __init__(self,len,bre):
#         self.length=len
#         self.breadth=bre
#
#     def perimeter(self):
#         self.perimeter=(2*(self.length + self.breadth))
#         return self.perimeter
#
#     def area(self):
#         self.area= (self.length * self.breadth)
#         return self.area
#
#     def dis(self):
#         print("Length :",self.length)
#         print("Breadth :",self.breadth)
#         print("Perimeter of Rectangle :",self.perimeter())
#         print("Area of Rectangle :",self.area())
#
# class Parallel(Rectangle):
#     def volume(self,h):
#         self.height=h
#         par=(self.length * self.breadth * self.breadth)
#         print("volume of parallel pipe :",par)
#
# obj=Parallel(2,3)
# obj.dis()
# obj.volume(5)

"""Exercice 2: Person class and child Student class ||Solution1.Create a Python class Person
with attributes:name and age of type string.
a.	Create a display()method that displays the name and age of an object created via thePerson class.
b.	Create a child class Student which inherits from the Person class and which also has a section attribute.
c.	Create a method displayStudent() that displays the name, age and section of an object created via 
the Student class.
d.	Create a student object via an instantiation on the Student class and then test the displayStudent method.
"""
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def display(self):
#         print("Person name:",self.name)
#         print("Person age:",self.age)
#
#
# class student(person):
#
#      def displayStudent(self):
#           self.section=section
#           print("Person name:", self.name)
#           print("Person age:", self.age)
#           print("Person Section:",self.section)
#
# p1=student("Dhanshri",55)
# p1.displayStudent("English")

'''Exercise 3. Bank Account class:
1.Create a Python class called BankAccount which represents a bank account, having 
as attributes:accountNumber (numeric type),name (name of the account owner as string type), balance.
2. Create a constructor with parameters:accountNumber, name, balance.
3.Create a Deposit() method which manages the deposit actions.
4 Create a Withdrawal() method which manages withdrawals actions.
5.Create an bankFees()method to apply the bank fees with a percentage of 5% of the balance account.
6.	Create  a display()method to display account details.
7.	Give the complete code for the BankAccount class
'''

# class BankAccount:
#     def __init__(self, acno, name, bal=0.0):
#         self.accountNumber = acno
#         self.name = name
#         self.balance = bal
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited {amount} into account {self.accountNumber}.")
#         else:
#             print("Deposit amount should be greater than zero.")
#
#     def withdrawal(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew {amount} from account {self.accountNumber}.")
#         else:
#             print("Insufficient Amount can't Withdraw.")
#
#     def bankFees(self):
#         fees = self.balance * 0.05
#         self.balance -= fees
#         print("Applied bank fees", self.balance)
#
#     def display(self):
#         print("Account Number: ",self.accountNumber)
#         print("Account Holder Name:",self.name)
#         print("Balance:",self.balance)
#
# account1 = BankAccount(12345, "John Doe")
#
# account1.deposit(1000)
# account1.withdrawal(500)
# account1.bankFees()
# account1.display()

'''4.Given a range of first 10 numbers, Iterate from start number to the end number and 
print the sum of the current number and previous number
Expected Output:
Printing current and previous number sum in a given range(10)
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7
Current Number 5 Previous Number  4  Sum:  9
Current Number 6 Previous Number  5  Sum:  11
Current Number 7 Previous Number  6  Sum:  13
Current Number 8 Previous Number  7  Sum:  15
Current Number 9 Previous Number  8  Sum:  17
'''
class number:
    def __init__(self,no):
        self.no=no

    def show(self):
        self.preno=0
        self.currno=0
        self.nextno=0
        print(f"Current Number: {self.currno} Previous Number: {self.preno} sum :{self.nextno}")
        for i in range(self.no):

            self.currno=i
            self.preno = i - 1

            self.nextno=self.preno +self.currno
            print(f"Current Number: {self.currno} Previous Number: {self.preno} sum :{self.nextno}")

p1=number(10)
p1.show()

"""Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
Expected output:
10 400
20 300
30 200
40 100

"""

