# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     # else:
#     return n*fact(n-1)
# print(fact(5))

'''Reverse list '''
# def reverse_list(lst):
#     return lst[::-1]
#
# # Example usage
# my_list = [1, 2, 3, 4, 5]
# print(reverse_list(my_list))  # Output: [5, 4, 3, 2, 1]

'''Find the Largest Element in a List'''
# def find_largest(lst):
#     return max(lst)
#
# # Example usage
# my_list = [3, 1, 4, 1, 5, 9]
# print(find_largest(my_list))  # Output: 9

'''convert list into tuple'''
# def list_to_tuple(lst):
#     return tuple(lst)
#
# # Example usage
# my_list = [1, 2, 3, 4, 5]
# print(list_to_tuple(my_list))  # Output: (1, 2, 3, 4, 5)

'''find the index of element in tuple'''
# def find_index(tpl, element):
#     return tpl.index(element)
#
# # Example usage
# my_tuple = (1, 2, 3, 4, 5)
# print(find_index(my_tuple, 3))  # Output: 2
#
# '''marge two dictionary'''
# def merge_dicts(dict1, dict2):
#     return {**dict1, **dict2}
#
# # Example usage
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# print(merge_dicts(dict1, dict2))  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
'''sort dictionary by values'''
# def sort_by_value(d):
#     return dict(sorted(d.items(), key=lambda item: item[1]))
#
# # Example usage
# my_dict = {'a': 3, 'b': 1, 'c': 2}
# print(sort_by_value(my_dict))  # Output: {'b': 1, 'c': 2, 'a': 3}
#
'''union of to sets'''
# def union_sets(set1, set2):
#     return set1.union(set2)
#
# # Example usage
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(union_sets(set1, set2))  # Output: {1, 2, 3, 4, 5}
#
# '''intersection'''
# def intersection_sets(set1, set2):
#     return set1.intersection(set2)
#
# # Example usage
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(intersection_sets(set1, set2))  # Output: {3}
#
# '''1.Reverse a List
# Write a function to reverse a list without using the built-in reverse method.'''
# def reverse_list(lst):
#     reversed_list = []
#     for i in range(len(lst)-1, -1, -1):
#         reversed_list.append(lst[i])
#     return reversed_list
#
# # Example usage
# my_list = [1, 2, 3, 4, 5]
# print(reverse_list(my_list))  # Output: [5, 4, 3, 2, 1]
#
#
'''2.Find the Second Largest Element in a List
Write a function to find the second largest element in a list of integers.'''
# def second_largest(lst):
#     unique_lst = list(set(lst))
#     unique_lst.sort()
#     return unique_lst[-2]
#
# # Example usage
# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(second_largest(my_list))  # Output: 6

'''check elements exist in tuple'''
# def element_exists(tpl, element):
#     return element in tpl
#
# # Example usage
# my_tuple = (1, 2, 3, 4, 5)
# print(element_exists(my_tuple, 3))  # Output: True

'''''Given a list of words, return a set of those words that are palindromes'''
# list=['elpple','nitin','nikita','vishu']
# s=li.split()
# print(s)
# for i in list:
#     if i== i[::-1]:
#         print("pelindrome",i)
#     else:
#         print("not palindrome",i)

'''Write a python program to find and display the product of three positive integer
values based on the rule mentioned below:
It should display the product of the three values except when one of the integer
value is 7. In that case, 7 should not be included in the product and the values to
its left also should not be included.
If there is only one value to be considered, display that value itself. If no values
can be included in the product, display -1.
Note: Assume that if 7 is one of the positive integer values, then it will occur
only once. Refer the sample I/O given below.
Sample Input Expected Output
1, 5, 3 =15
3, 7, 8 =8
7, 4, 3=12
1,5,7=-1'''
# def product(a,b,c):
#     if a==7:
#          print(b*c)
#     elif b==7:
#         print(c)
#     elif c==7:
#         print(-1)
#     else:
#         print(a*b*c)
#
# product(1,5,7)
# product(1,5,3)
# product(3,7,8)
# product(7,4,3)

'''exception on balance'''
# class InsufficientBalanceError(Exception):
#     def __init__(self, balance, amount):
#         self.balance = balance
#         self.amount = amount
#
#     def __str__(self):
#         return f"Insufficient balance ({self.balance}) to withdraw {self.amount}."
# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self.balance = balance
#     def deposit(self, amount):
#         """Deposit money into the account."""
#         try:
#             if amount <= 0:
#                 raise ValueError("Deposit amount must be positive.")
#             self.balance += amount
#             print(f"Deposit of {amount} successful. New balance: {self.balance}")
#         except ValueError as ve:
#             print(f"Error: {ve}")
#         except Exception as e:
#             print(f"Unexpected error during deposit: {e}")
#
#     def withdraw(self, amount):
#         """Withdraw money from the account."""
#         try:
#             if amount <= 0:
#                 raise ValueError("Withdrawal amount must be positive.")
#             if amount > self.balance:
#                 raise InsufficientBalanceError(self.balance, amount)
#             self.balance -= amount
#             print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
#         except ValueError as ve:
#             print(f"Error: {ve}")
#         except InsufficientBalanceError as ibe:
#             print(ibe)
#         except Exception as e:
#             print(f"Unexpected error during withdrawal: {e}")
#
#     def display_balance(self):
#         """Display the current balance of the account."""
#         print(f"Account Number: {self.account_number}, Current Balance: {self.balance}")
#
#
# # Function to handle user interactions
# def main():
#     account_number = "1234567890"  # Example account number
#     account1 = BankAccount(account_number, 1000)  # Initial balance of 1000
#
#     while True:
#         print("\nChoose an option:")
#         print("1. Deposit")
#         print("2. Withdraw")
#         print("3. Display Balance")
#         print("4. Exit")
#
#         choice = input("Enter your choice (1/2/3/4): ")
#
#         if choice == '1':
#             amount = float(input("Enter amount to deposit: "))
#             account1.deposit(amount)
#
#         elif choice == '2':
#             amount = float(input("Enter amount to withdraw: "))
#             account1.withdraw(amount)
#
#         elif choice == '3':
#             account1.display_balance()
#
#         elif choice == '4':
#             print("Exiting the program.")
#             break
#
#         else:
#             print("Invalid choice. Please enter 1, 2, 3, or 4.")
#
#
# if __name__ == "__main__":
#     main()

'''Given an array of in its, return True if the sequence of numbers 1, 2, 3 appears in 
the array somewhere.
array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
'''
# a=array([1,1,2,3,1])
# def char(a):
#     for i in range(len(a)-1):
#         if a[i]==1 and a[i+1]==2 and a[i+2]==3:
#             return True
#     return False
# print(char([1,1,2,1,3,1]))

'''You work for a manufacturer, and have been asked to calculate the total profit 
made on the sales of a product. You are given a dictionary containing the cost price 
per unit (in dollars), sell price per unit (in dollars), and the starting inventory. Define 
class Profit and return the total profit made.
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
}) ➞ 32411 '''

# class profit:
#     def __init__(self,cost,cell,inventory):
#         self.cost=cost
#         self.cell=cell
#         self.inv=inventory
#
#     def profits(self):
#         profit_per_unit = self.cell - self.cost
#         total_profit = profit_per_unit * self.inv
#         print(int(total_profit))
#
# p1=profit(32.67,45.00,1200)
# p1.profits()

'''Write python statement to create a one–dimensional array using arange() function 
.Elements will be in the range 10 to 30 with a step of 4 (including both 10 and 30). 
Reshape this one- dimensional array to two dimensional array of shape(2,3). Then 
display only those elements of this two –dimensional array which are divisible by 5'''

#
# import numpy as np
# array=np.arange(10,31,4)
# print(array)
#
# T_D_array=array.reshape(2,3)
# print(T_D_array)
#
# array2 =T_D_array[T_D_array %5==0]
# print(array2)

'''A book shop maintain the inventory of books that are being sold at the shop. The 
list includes details such as author, title, price, publisher and stock position. Whenever 
a customer wants a book, the sales person inputs the title and author and the system 
searches the list and display it is available or not. If it is not, an appropriate message 
is displayed. If it is the system displays the book details and requests for the number 
of copies required. If the requested copies are available, the total cost of the requested 
copies is displayed; otherwise, the message “required copies not in stock” is displayed. 
Design a system using a class called Books with suitable member functions and 
constructors.'''
# class inventory:
#     def __init__(self,author,title,price,publisher,stock)
#         self.author=author
#         self.title=title
#         self.price=price
#         self.publisher=publisher
#         self.stock=stock
#     def insert(self):
#         self.author=input("Enter Author :")
#         self.title=input("Enter Title :")
#         self.price=int(input("Enter price :"))
#         self.publisher=input("Enter Publisher :")
#         self.stock=int(input("Enter Stock:"))
#     def display(self):

'''function to calculate the power (a,b)'''
# def power(a,b):
#     if b==1:
#         return 1
#     else:
#         return a*power(a,b-1)
# print(power(1,1))

'''WAP to define a class Area and define methods in it for calculating Area
a. Calculate and display area of circle
b. Calculate and display area of triangle
c. Calculate and display area of square
d. Calculate and display area of rectangle'''

# class Area:
#     def __init__(self,radius,length,breadth,heigth,side):
#         self.r=radius
#         self.l=length
#         self.b=breadth
#         self.h=heigth
#         self.s=side
#
#     def circle(self):
#         a=3.14*self.r *self.r
#         return a
#
#     def triangle(self):
#         t=0.5*self.h*self.b
#         return t
#
#     def square(self):
#         sq=self.s*self.s
#         return sq
#
#     def rectangle(self):
#         rec=self.l*self.b
#         return rec
# a1=Area(2,4,6,8,9,)
# print(a1.circle())
# print(a1.triangle())
# print(a1.square())
# print(a1.rectangle())

'''fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
Use a list comprehension to create a new list to show 
fruits_with_more_than_two_vowels.'''

# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
# l=[]
# for i in fruits:
#     count=0
#     for x in i:
#         if x in 'aeiou':
#             count +=1
#     if count > 2:
#             l.append(i)
# print(l)

''' Write a program to perform CRUD and Search operation on Database 
Company. Create tables like
Dept(dept_id,name,hod,staff) 
Employee(emp_id,name,salary,address),
Attendance(emp_id,present-days,leaves). 
Perform following operations.
1. Show all records 
a. Show records from employee where salary is greater than 50000.
b. Show records from attendance those are present for all 30 days.
c. Show records from dept where staff>30
2. Insert record 
3. Update record 
a. Update records of employee , salary=50000 where address=”Delhi”
b. Update records of attendance where id>5
4. Delete record
a. Delete record of attendance where leaves >10
b. Delete record of dept where staff<5.
5. Search record'''

# import sqlite3 as sq
# conn=sq.connect("company".db)
# print("Connect Sucessfully")
#
# conn.execute('''create table Dept(
#                 dept_id int NOT NULL,
#                 name char(20),
#                 hod char(20),
#                 staff int NOT NULL);''')

# conn.execute('''create table Employee(
#     emp_id int  primary key NOT NULL,
# name char(20),salary int,add varchar);''')
#
# conn.execute('''CREATE TABLE IF NOT EXISTS Attendance(
#     attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     emp_id INTEGER NOT NULL,
#     present INTEGER NOT NULL,
#     leaves INTEGER NOT NULL,
#     FOREIGN KEY (emp_id) REFERENCES Employee(emp_id)
# );''')
#
# conn.commit()
#
# def show1():
#     print("All records from Dept")
#     d = conn.execute("SELECT * FROM Dept")
#     for row in d:
#         print(row)
#
# def show2():
#     print("All records from Employee")
#     d = conn.execute("SELECT * FROM Employee")
#     for row in d:
#         print(row)
#
# def show3():
#     print("All records from Attendance")
#     d = conn.execute("SELECT * FROM Attendance")
#     for row in d:
#         print(row)
#
# def showEmpsal():
#     print("Employees with salary greater than 50000")
#     d1 = conn.execute("SELECT * FROM Employee WHERE salary > 50000")
#     for row in d1:
#         print(row)
#
# def showEmppresent30days():
#     print("Attendance records where present days are 30")
#     d1 = conn.execute("SELECT * FROM Attendance WHERE present = 30")
#     for row in d1:
#         print(row)
#
# def showwherestaff30():
#     print("Departments where staff is greater than 30")
#     d1 = conn.execute("SELECT * FROM Dept WHERE staff > 30")
#     for row in d1:
#         print(row)
#
# def insertintoDept():
#     DEPT_ID = int(input("Enter Department ID: "))
#     NAME = input("Enter Department Name: ")
#     HOD = input("Enter HOD: ")
#     STAFF = int(input("Enter number of staff: "))
#
#     conn.execute("INSERT INTO Dept (dept_id, name, hod, staff) VALUES (?, ?, ?, ?)", (DEPT_ID, NAME, HOD, STAFF))
#     conn.commit()
#     print("Record inserted into Dept")
#
# def insertintoEmployee():
#     EMP_ID = int(input("Enter Employee ID: "))
#     NAME = input("Enter Employee Name: ")
#     SALARY = float(input("Enter salary: "))
#     ADDRESS = input("Enter Employee Address: ")
#
#     conn.execute("INSERT INTO Employee (emp_id, name, salary, address) VALUES (?, ?, ?, ?)", (EMP_ID, NAME, SALARY, ADDRESS))
#     conn.commit()
#     print("Record inserted into Employee")
#
# def insertintoAttendance():
#     EMP_ID = int(input("Enter Employee ID: "))
#     PRESENT = int(input("Enter present days: "))
#     LEAVES = int(input("Enter leave days: "))
#
#     conn.execute("INSERT INTO Attendance (emp_id, present, leaves) VALUES (?, ?, ?)", (EMP_ID, PRESENT, LEAVES))
#     conn.commit()
#     print("Record inserted into Attendance")
#
# def updateaddrsalaryis50000():
#     print("Updating salary to 50000 where address is 'Delhi'")
#     conn.execute("UPDATE Employee SET salary = 50000 WHERE address = 'Delhi'")
#     conn.commit()
#     print("Salary updated")
#
# def UpdateAttendepresentdays():
#     print("Updating Attendance for employees with ID > 5")
#     conn.execute("UPDATE Attendance SET present = 25 WHERE emp_id > 5")
#     conn.commit()
#     print("Attendance updated")
#
# def deleteleavesgreaterthan10():
#     conn.execute("DELETE FROM Attendance WHERE leaves > 10")
#     conn.commit()
#     print("Deleted records from Attendance where leaves > 10")
#
# def deletefromdeptwherestaffidifsmallthan5():
#     conn.execute("DELETE FROM Dept WHERE staff < 5")
#     conn.commit()
#     print("Deleted records from Dept where staff < 5")
#
# def search():
#     eid = int(input("Enter Employee ID for search: "))
#     data = conn.execute("SELECT * FROM Employee WHERE emp_id = ?", (eid,))
#     for row in data:
#         print(row)
#
# while True:
#     print("1. Show all records from Dept")
#     print("2. Show all records from Employee")
#     print("3. Show all records from Attendance")
#     print("4. Show Employees with salary > 50000")
#     print("5. Show Attendance where present days are 30")
#     print("6. Show Departments where staff > 30")
#     print("7. Insert into Dept")
#     print("8. Insert into Employee")
#     print("9. Insert into Attendance")
#     print("10. Update Employee salary to 50000 where address is 'Delhi'")
#     print("11. Update Attendance where emp_id > 5")
#     print("12. Delete from Attendance where leaves > 10")
#     print("13. Delete from Dept where staff < 5")
#     print("14. Search Employee by ID")
#     print("15. Exit")
#
#     choice = input("Enter your choice: ")
#
#     if choice == '1':
#         show1()
#     elif choice == '2':
#         show2()
#     elif choice == '3':
#         show3()
#     elif choice == '4':
#         showEmpsal()
#     elif choice == '5':
#         showEmppresent30days()
#     elif choice == '6':
#         showwherestaff30()
#     elif choice == '7':
#         insertintoDept()
#     elif choice == '8':
#         insertintoEmployee()
#     elif choice == '9':
#         insertintoAttendance()
#     elif choice == '10':
#         updateaddrsalaryis50000()
#     elif choice == '11':
#         UpdateAttendepresentdays()
#     elif choice == '12':
#         deleteleavesgreaterthan10()
#     elif choice == '13':
#         deletefromdeptwherestaffidifsmallthan5()
#     elif choice == '14':
#         search()
#     elif choice == '15':
#         break
#     else:
#         print("Invalid choice. Please try again.")
#
# conn.close()







'''Write a program to find the largest and smallest numbers in a list.
'''
# l=[2,4,6,8,9,10,50]
# large=l[0]
# small=l[0]
#
# for i in l:
#     if i > large:
#         large=i
#     if i< small:
#         small=i
# print(small)
# print(large)
#

'''Write a program to convert a list of tuples into a dictionary.
'''
# l=[(1,1),(2,4),(3,9),(4,16)]
# t={}
# for k,v in l:
#     t[k]=v
# print(t)
'''Write a program to convert a list  into a dictionary.
'''
# l=[1,2,3,4,5]
# dict={i: l[i] for i in range(len(l))}
# # for k,v in l:
# #     dict[k]=v
# print(dict)
'''Write a program to read a text file and count the number of lines.
'''
# f1=open("abc1.txt","r")
# lines=f1.readlines()
# l=len(lines)
# print(l)
# f1.close()

'''Write a program to append text to an existing file.
'''
# f1=open("abc1.txt","r")
# lines=f1.readlines()
# content="This is new content to append .\n"
# f2=open("abc.txt","a")
# f2.write(content)
# print(lines+[content])
# f1.close()
# f2.close()

'''Write a program that handles division by zero exception.
'''
# n1=int(input("Enter 1st number :"))
# n2=int(input("Enter 2nd number :"))
# try:
#     result=n1%n2
#     print(result)
#
# except ZeroDivisionError:
#     print("error:zero division error occured.")

'''Write a program to catch and handle a specific exception (e.g.value error)'''
# n=int(input("Enter number:"))
# try:
#     result=n**2
#     print(result)
#
# except ValueError:
#     print("Error : please enter valid integer")

'''"""7. Write a function called transform_and_combine that takes in two parameters, list_one, which
must have at least one element, and list_two. Remove the last element from list_one, then reverse 
the list. Sort list_two, then extend list_two with list_one, and return list_two. Hint: Use list methods
(e.g., pop, sort, append, reverse, and extend). 
For example, transform_and_combine([5, 20, 3, 15, 200, 0, 17], ['Hello', 'Bye', 'How are you?'])
would return ['Bye', 'Hello', 'How are you?', 0, 200, 15, 3, 20, 5].
"""'''
# x=[5, 20, 3, 15, 200, 0, 17]
# y=['Hello', 'Bye', 'How are you?']
# def combine(x,y):
#     x.pop()
#     x.reverse()
#
#     y.sort()
#     y.extend(x)
#     print(y)
# z=combine(x,y)
# print(z)

'''"""6.WAP to without using built in functions
1. search a number from list
2. find min number from list
3. find max number
4. sorting Ascending and descending '''

# l=[20,50,54,23,21,90]
#
#
# for i in l:
#     n = int(input("Enter number:"))
#     if n==i:
#          print(i)
#     else:
#          print("number not in list")
#     break
# max=l[0]
# min=l[0]
# for i in l:
#     if i > max:
#         max=i
#
#     if i < min:
#         min=i
#
# print(max)
# print(min)
#
# l.sort()
# z=l[::-1]
# print(l)
# print(z)

'''2.Implement Password Generator process. Generate a password with 
1. min len=8 
2. at least 1 capital char, 1 small alphabet, 1 int, 1 special symbol
'''
'''most contain 1,2,3 any where'''
# l=[1,2,4,3,6,8,9]
# count1=0
# count2=0
# count3=0
# def co(l):
#     for i in l:
#         count1+=1
#         if i==1:
#             count1+=1
#         elif i==2 :
#             count1+=1
#         elif i==3:
#             count3+=1
#         else:
#              return False
#         if count1==1 and count2==1 and count3==1:
#             return True
# print(co(l))


# def contains_1_2_3(l):
#     found_1 = False
#     found_2 = False
#     found_3 = False
#
#     for i in l:
#         if i == 1:
#             found_1 = True
#         elif i == 2:
#             found_2 = True
#         elif i == 3:
#             found_3 = True
#
#     return found_1 and found_2 and found_3

# Example usage
# l = [1, 2, 4, 6, 3, 8, 9]
# print(contains_1_2_3(l))  # Output: True




'''find most common prefix'''
# s=['flow','flower','fly']
#
# print(l)


'''make smallest number,greatest number,find differance'''
# n=[538]
# str_num=str(num)
# digit=[]
# for i in str_num:
#     if
#         digit.append(i)
# print(digit)
# x=min(digit)
# y=max(digit)
# asc=(sorted)
# des=(sorted=True)
# print(asc)
# print(dec)
# def smallest(n):
#     digit=list(str(n))
#     small=int("".join(sorted(digit)))
#     return small
# print(smallest(n))

'''Write a program to calculate the factorial of a number using recursion.
'''
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

'''Write a program to find the second largest number in a list.
'''


# def find_second_largest(numbers):
#     if len(numbers) < 2:
#         return "List must contain at least two elements."
# #
#     first, second = float('-inf'), float('-inf')
#
#     for number in numbers:
#         if number > first:
#             second = first
#             first = number
#         elif first > number > second:
#             second = number
#
#     return second
#
#
# # Example usage
# numbers = [10, 20, 4, 45, 99]
# second_largest = find_second_largest(numbers)
# print("The second largest number is:", second_largest)

"""Write a program to rotate an array by a given number of steps.
"""
# def rotate_array(arr, steps):
#     if not arr:
#         return arr
#     steps = steps % len(arr)
#     return arr[-steps:] + arr[:-steps]
#
# # Example usage
# arr = [1, 2, 3, 4, 5, 6, 7]
# steps = 3
# rotated_array = rotate_array(arr, steps)
# print("The rotated array is:", rotated_array)

'''Write a program to merge two sorted arrays into a single sorted array'''

'''Write a program to read a CSV file and display its contents.'''

'''Write a program to copy the contents of one file to another.'''
# def copy_file_contents(source_file, destination_file):
#     with open(source_file, 'r') as src:
#         with open(destination_file, 'w') as dst:
#             for line in src:
#                 dst.write(line)
#
# # Example usage
# source_file = 'source.txt'
# destination_file = 'destination.txt'
# copy_file_contents(source_file, destination_file)
#
#
# '''Write a program to handle multiple exceptions (e.g., IOError, ValueError).'''
# def handle_multiple_exceptions():
#     try:
#         # Some code that might raise exceptions
#         result = 10 / 0
#         num = int("abc")
#     except ZeroDivisionError:
#         print("Caught ZeroDivisionError: division by zero.")
#     except ValueError:
#         print("Caught ValueError: invalid literal for int().")
#     except Exception as e:
#         print(f"Caught unexpected exception: {e}")
#
# # Example usage
# handle_multiple_exceptions()
#
# '''Write a program to raise and handle a custom exception.'''
# def handle_multiple_exceptions():
#     try:
#         # Some code that might raise exceptions
#         result = 10 / 0
#         num = int("abc")
#     except ZeroDivisionError:
#         print("Caught ZeroDivisionError: division by zero.")
#     except ValueError:
#         print("Caught ValueError: invalid literal for int().")
#     except Exception as e:
#         print(f"Caught unexpected exception: {e}")
#
# # Example usage
# handle_multiple_exceptions()
#
#
#
# '''Write a program to create a numpy array and perform basic arithmetic operations.'''
# import numpy as np
#
# def numpy_arithmetic_operations():
#     arr = np.array([1, 2, 3, 4, 5])
#     print("Original array:", arr)
#     print("Array + 2:", arr + 2)
#     print("Array * 2:", arr * 2)
#     print("Array squared:", arr ** 2)
#
# # Example usage
# numpy_arithmetic_operations()
#
# '''Write a program to calculate the dot product of two numpy arrays.'''
# import numpy as np
#
# def calculate_dot_product():
#     arr1 = np.array([1, 2, 3])
#     arr2 = np.array([4, 5, 6])
#     dot_product = np.dot(arr1, arr2)
#     print("Dot product:", dot_product)
#
# # Example usage
# calculate_dot_product()
#
#
#
# '''Write a program to create a DataFrame from a dictionary of lists.'''
# import pandas as pd
#
# def create_dataframe():
#     data = {
#         'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 35],
#         'City': ['New York', 'Los Angeles', 'Chicago']
#     }
#     df = pd.DataFrame(data)
#     print("DataFrame:\n", df)
#
# # Example usage
# create_dataframe()
#
# '''Write a program to read a CSV file into a DataFrame and display basic statistics.'''
# import pandas as pd
#
# def read_csv_and_display_statistics(file_path):
#     df = pd.read_csv(file_path)
#     print("DataFrame:\n", df)
#     print("Basic Statistics:\n", df.describe())
#
# # Example usage
# file_path = 'example.csv'
# read_csv_and_display_statistics(file_path)
#
# # Advanced
# # Arrays and Numpy:
#
# '''Write a program to implement matrix multiplication using numpy.'''
# import numpy as np
#
# def matrix_multiplication():
#     matrix1 = np.array([[1, 2], [3, 4]])
#     matrix2 = np.array([[5, 6], [7, 8]])
#     result = np.dot(matrix1, matrix2)
#     print("Matrix multiplication result:\n", result)
#
# # Example usage
# matrix_multiplication()
#
# '''Write a program to perform element-wise operations on two numpy arrays.'''
# import numpy as np
#
# def element_wise_operations():
#     arr1 = np.array([1, 2, 3])
#     arr2 = np.array([4, 5, 6])
#     print("Element-wise addition:", arr1 + arr2)
#     print("Element-wise multiplication:", arr1 * arr2)
#
# # Example usage
# element_wise_operations()
#
# # Pandas:
#
# '''Write a program to clean and preprocess data in a DataFrame.'''
# import pandas as pd
#
# def clean_and_preprocess_data():
#     data = {
#         'Name': ['Alice', 'Bob', None, 'Charlie'],
#         'Age': [25, None, 30, 35],
#         'City': ['New York', 'Los Angeles', 'Chicago', None]
#     }
#     df = pd.DataFrame(data)
#     print("Original DataFrame:\n", df)
#
#     # Fill missing values
#     df['Age'].fillna(df['Age'].mean(), inplace=True)
#     df['City'].fillna('Unknown', inplace=True)
#
#     # Drop rows with missing values
#     df.dropna(subset=['Name'], inplace=True)
#
#     print("Cleaned DataFrame:\n", df)
#
# # Example usage
# clean_and_preprocess_data()
#
# '''Write a program to perform groupby operations and aggregate functions on a DataFrame.'''
# import pandas as pd
#
# def groupby_and_aggregate():
#     data = {
#         'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
#         'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles'],
#         'Sales': [100, 200, 150, 300, 400]
#     }
#     df = pd.DataFrame(data)
#     print("Original DataFrame:\n", df)
#
#     grouped = df.groupby('City').agg({'Sales': 'sum'})
#     print("Grouped and aggregated DataFrame:\n", grouped)
#
# # Example usage
# groupby_and_aggregate()
#
# # Openpyxl:
#
# '''Write a program to read data from an Excel file and print it.'''
# from openpyxl import load_workbook
#
# def read_excel_file(file_path):
#     workbook = load_workbook(filename=file_path)
#     sheet = workbook.active
#     for row in sheet.iter_rows(values_only=True):
#         print(row)
#
# # Example usage
# file_path = 'example.xlsx'
# read_excel_file(file_path)
#
# '''Write a program to create and write data to an Excel file using openpyxl.'''
# from openpyxl import Workbook
#
# def write_to_excel_file(file_path):
#     workbook = Workbook()
#     sheet = workbook.active
#     data = [
#         ['Name', 'Age', 'City'],
#         ['Alice', 25, 'New York'],
#         ['Bob', 30, 'Los Angeles'],
#         ['Charlie', 35, 'Chicago']
#     ]
#     for row in data:
#         sheet.append(row)
#     workbook.save(filename=file_path)
#
# # Example usage
# file_path = 'output.xlsx'
# write_to_excel_file(file_path)
#
# # SQLite3:
#
# '''Write a program to create a SQLite database and a table.'''
# import sqlite3
#
# def create_database_and_table(db_name):
#     conn = sqlite3.connect(db_name)
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY,
#             name TEXT NOT NULL,
#             age INTEGER NOT NULL,
#             city TEXT NOT NULL
#         )
#     ''')
#     conn.commit()
#     conn.close()
#
# # Example usage
# db_name = 'example.db'
# create_database_and_table(db_name)
#
# '''Write a program to insert, update, delete, and query data from a SQLite database.'''
# import sqlite3
#
#
# def database_operations(db_name):
#     conn = sqlite3.connect(db_name)
#     cursor = conn.cursor()
#
#     # Insert data
#     cursor.execute("INSERT INTO users (name, age, city) VALUES ('Alice', 25, 'New York')")
#     cursor.execute("INSERT INTO users (name, age, city) VALUES ('Bob', 30, 'Los Angeles')")
#
#     # Update data
#     cursor.execute("UPDATE users SET age = 28 WHERE name = 'Alice'")
#
#     # Delete data
#     cursor.execute("DELETE FROM users WHERE name = 'Bob'")
#
#     # Query data
#     cursor.execute("SELECT * FROM users")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#
#     conn.commit()
#     conn.close()
#
#
# # Example usage
# db_name = 'example.db'
# database_operations(db_name)
#
# # File Handling and Exception Handling:
#
# '''Write a program to read a large file in chunks and handle potential exceptions.'''
# def read_large_file_in_chunks(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             while True:
#                 chunk = file.read(1024)
#                 if not chunk:
#                     break
#                 print(chunk)
#     except IOError as e:
#         print(f"Error reading file: {e}")
#
# # Example usage
# file_path = 'large_file.txt'
# read_large_file_in_chunks(file_path)
#
# '''Write a program to process multiple files in a directory and handle exceptions for
#     files that cannot be opened.'''
# import os
#
# def process_files_in_directory(directory_path):
#     for filename in os.listdir(directory_path):
#         file_path = os.path.join(directory_path, filename)
#         try:
#             with open(file_path, 'r') as file:
#                 print(f"Processing file: {filename}")
#                 # Process file content
#                 print(file.read())
#         except (IOError, FileNotFoundError) as e:
#             print(f"Error opening file {filename}: {e}")
#
# # Example usage
# directory_path = 'example_directory'
# process_files_in_directory(directory_path)
#
# #
# # import pandas as pd
# # # Creating the dataframe
# # df = pd.DataFrame({"A":[6, 5, 2, 1],
# # "B":[11, 2, 5, 8],
# # "C":[1, 8, 66, 4]})
# # # Print the dataframe df
# # # applying idxmax() function.
# # x=df.idxmax(axis = 0)
# # print(x)
#
# # import pandas as pd
# # name=pd.Series(['Sanjeev','Keshav','Rahul'])
# # age=pd.Series([37,42,38])
# # designation=pd.Series(['Manager','Clerk','Accountant'])
# # d1={'Name':name,'Age':age,'Designation':designation}
# # df=pd.DataFrame(d1)
# # # print(df)
# # # ascending order
# # df1=df.sort_values(by='Age')
# # # print(df1)
# # #desending order by name
# # df2=df.sort_values(by='Name',ascending=1)
# # print(df2)
#
# #first two and last 3 rows
# # import pandas as pd
# d={'Player':['Hardik Pandya','K L Rahul','AndreRussel','Jasprit Bumrah','Virat Kohli','Rohit Sharma'],
# 'Team':['Mumbai Indians','Kings Eleven','Kolkata Knight Riders','Mumbai Indians','RCB','Mumbai Indians'],
# 'Category':['Batsman','Batsman','Batsman','Bowler','Batsman','Batsman'] ,
# 'Bidprice':[13,12,7,10,17,15], 'Runs':[1000,2400,900,200,3600,3700]}
# df=pd.DataFrame(d)
# print(df)
# print(df.iloc[:2,:])
# print(df.iloc[-3:,:])
# print(df.iloc[:,:])
# print(d[d['BidPrice'] == d['BidPrice'].max()])
# print(df.groupby('Team').Player.count())

# def oldest(people):
#     if not people:
#         return 0
#
#     oldest_person =0
#     max_age = -1
#
#     for name, age in people.items():
#         if age > max_age:
#             max_age = age
#             oldest_person = name
#
#     return oldest_person
#
# # Example usage
# print(oldest({"Emma": 71, "Jack": 45, "Amy": 15, "Ben": 29}))  # Output: "Emma"
# print(oldest({"Max": 9, "Josh": 13, "Sam": 48, "Anne": 33}))  # Output: "Sam"

'''Write a program to open a file named example.txt and print its contents.
'''
# f=open("example.txt",'w')
# f.write("Hi I am Dhanshri Salve")
#
# f=open('example.txt','r')
# lines=f.readlines()
# print(lines)
# f.close()

''' Create a program that writes the string "Hello, World!" to a file named output.txt.
'''
# f=open("example.txt",'w')
# f.write("hello world!")
#
# f=open('example.txt','r')
# lines=f.readlines()
# print(lines)
# f.close()

''' Write a program to read the first line of a file named data.txt.
'''

# f=open("example.txt",'w')

# f.write("hello world!")
#
# f=open('example.txt','r')
# lines=f.readline()
# # x=lines.index[:1]

# print(lines)
# f.close()

'''  Write a program to append the text "Python is fun!" to a file named notes.txt
'''
# file= open('example.txt','a')
# file.write("Python is fun!")
#
#
# f=open('example.txt','r')
# lines=f.readlines()
#
# print(lines)

''' Create a program that reads all lines from a file named input.txt and prints them in reverse order.
# '''
# f=open('example.txt','r')
# lines=f.readlines()
# # x=lines.index[:1]
# for i in reversed(lines):
#     print(i[::-1],end=' ')
# f.close()

''' Write a program to copy the contents of source.txt to destination.txt.
'''
# f=open("example.txt",'r')
# lines=f.read()
#
# f1=open('abc.txt','w')
# l=f1.write(lines)
# print(l)
# f1.close()
# f.close()

# Open the source file in read mode
# with open('example.txt', 'r') as source_file:
#     # Read the contents of the source file
#     contents = source_file.read()
#
# # Open the destination file in write mode
# with open('abc.txt', 'w') as destination_file:
#     # Write the contents to the destination file
#     destination_file.write(contents)

# def pattern(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#              print('*',end='')
#         print("\n")
# n=int(input("Enter number:"))
# pattern(n)

# def pat(n):
#      for i in range(1,n+1):
#          x=i
#          for j in range(1,i+1):
#              print(x,end=" ")
#          print("\n")
# n=int(input("enter number"))
# pat(n)

# def pat(n):
#     for i in range(1,n+1):
#         x=i
#         for j in range(1,i+1):
#             print(x, end="")
#             x=x-1
#
#         print("\n")
# n=int(input("Enter number :"))
# pat(n)

# def full_pyramid(n):
#     for i in range(1, n + 1):
#         for j in range(n - i):
#             print(" ", end="")
#
#         for k in range(1, 2 * i):
#             print("*", end="")
#         print()
#
# full_pyramid(5)


# for i in range(1, 6):
#     print('*' * i)



# class add:
#     def _init_(self,n1,n2,n3):
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

def longest_common_prefix(strs):
    if not strs:
        return ""

    shortest_str = min(strs, key=len)

    for i, char in enumerate(shortest_str):
        print(i, char)
        for other_str in strs:
            if other_str[i] != char:
                return shortest_str[:i]

    return shortest_str


a = ['flower', 'flowwww', 'fly']
result = longest_common_prefix(a)
print(result)