'''Python file program to get the file’s first
three and last three lines.'''
import re

# file= open("abc.txt","w")
#
# file .write('''File handling in Python is a powerful and versatile tool that can \nbe used to perform a wide range of operations.
# However, it is important to carefully \n consider the advantages and disadvantages of file handling
#  when writing Python programs, to ensure that \n the code is secure, reliable, and performs well.
# In\n this article we will explore Python File Handling, Advantages.
# Disadvantages and How open, \n write and append functions works in python file.''')
#
# with open("abc.txt","r")as file:
#
#     line=file.readlines()
#     first_l=line[:3]
#     last_l=line[-3:]
#
# for l in first_l:
#     print(l)
# for l in last_l:
#     print(l)
#
# file.close()

'''2). Python file program to get all the email ids from a text file.'''

# import re
#
# # file=open("niks.txt","w")
# with open("niks.txt","r" )as file:
#     x=file.readlines()
#     # print(x)
#     pat="[a-z0-9]+@[a-z]+\.com"
#     # pat='.'
#     for i in x:
#         res=re.search(pat ,i )
#         print(res.group())

    # line=file.readlines()
    # l=line[:]
    # for i in l:
    #    print(i)
#
# '''3). Python file program to get a specific line from the file.'''
# with open("C:\Users\dhans\PycharmProjects\pythonProject1\abc.txt", 'r') as file:
#             lines = file.readlines()
#             def get_specific_line(file_path, line_number):
#                     if 1 <= line_number <= len(lines):
#                         return lines[line_number - 1].strip()
#                     else:
#                         return f"Error: Line number {line_number} is out of range. The file has {len(lines)} lines."
#
# abc= 'example.txt'  # Replace with your file path
# line_number = int(input("Enter the line number you want to retrieve: "))
# result = get_specific_line(file_path, line_number)
# print(result)


'''6). Python file program to find the longest word in a file.
'''
# f=open("abc1.txt","w")
# f.write("This is python programing code")
# f.close()
# s=[]
# f2=open("abc1.txt","r")
# lines=f2.read()
# res=lines.split()
#
# print(res)
# temp=''
#
# for i in res:
#     if len(i)>len(temp):
#
#         temp=i
#
# print(temp)

'''7). Python file program to get the count of a specific word in a file.'''

#
# file=open("abc.txt","r")
# line=file.read()
# search_word = input("Enter the word to count in the file: ")
# count = 0
# words=line.split()
# for j in words:
#     if j==search_word:
#         count +=1
# print(count)

'''8.Python file program to read a random line from a file.'''
file=open("abc.txt","r")
line=file.readlines()
(print(line[:2]))
file.close()

# read_line= int(input("Enter which line you read : "))
# l=len(line)
# if 1 <=read_line <=l:
#     print(line[read_line -1 ])
# else:
#     print("Line number out of range.")
#



'''9). Python file program to copy the file’s contents to another file after converting it to lowercase.
# '''
# file=open("abc.txt","r")
# line=file.readlines()
# file.close()
# for

'''Write a function in Python to read lines from a text file "notes.txt". 
For example: If the content of the file is:
"India is the fastest-growing economy. India is looking for more investments around 
the globe. The whole world is looking at India as a great market. Most of the Indians 
can foresee the heights that India is capable of reaching."
A. Your function should find and display the occurrence of the word "the".
 The output should be: 5
b. Read the contents of file in reverse order.'''



# f1=open("abc2.txt",'w')
# f1.write("""India is the fastest-growing economy. India is looking for more investments around
# the globe. The whole world is looking at India as a great market. Most of the Indians
# can foresee the heights that India is capable of reaching.""")
# f1.close()
# def process_notes(filename):
#
#     try:
#         with open('abc2.txt', 'r') as file:
#             lines = file.readlines()
#
#             # Count the occurrences of the word "the"
#             text = ''.join(lines).lower()  # Convert to lowercase for case-insensitive matching
#             word_count = text.split().count("india")
#             print(f"The occurrence of the word 'the': {word_count}")
#
#             # Print the contents of the file in reverse order
#             print("\nContents of the file in reverse order:")
#             for line in reversed(lines):
#                 print(line.strip()[::-1])  # Reverse each line and remove trailing newlines
#
#     except FileNotFoundError:
#         print(f"The file {filename} does not exist.")
#
# process_notes('abc2.txt')
