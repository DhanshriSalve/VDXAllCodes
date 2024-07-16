'''1 Aditi has used a text editing software to type some text. After saving the article as
WORDS.TXT, she realized that she has wrongly typed alphabet J in place of alphabet I
everywhere in the article.

Write a function definition for JTOI() in Python that would display the corrected version of
entire content of the file WORDS.TXT with all the alphabets "J" to be displayed as an
alphabet "I" on screen.
Note: Assuming that WORD.TXT does not contain any J alphabet otherwise.
Example:
If Aditi has stored the following content in the file WORDS.TXT:
WELL, THJS JS A WORD BY JTSELF. YOU COULD STRETCH THJS TO BE A
SENTENCE
The function JTOI() should display the following content:
WELL, THIS IS A WORD BY ITSELF. YOU COULD STRETCH THIS TO BE A
SENTENCE'''


# def JTOI():
#     try:
#         f = open("WORDS.TXT", 'r')
#         line = f.read()
#         word=line.replace('J','I')
#         file = open("WORDS.TXT", 'w')
#         file.write("WELL, THJS JS A WORD BY JTSELF. YOU COULD STRETCH THJS TO BE A SENTENCE")
#         print(word)
#     except FileNotFoundError as e:
#             print("File does not exist :",e)
# JTOI()

#output:
# WELL, THIS IS A WORD BY ITSELF. YOU COULD STRETCH THIS TO BE A SENTENCE


'''Write a program that prompts the user to input a number and reverse its digits.
For example, the reverse of 12345 is 54321.'''
# def reverse_digits():
#     num = input("Enter a number: ")
#     reversed= num[::-1]
#     print("Reverse of", num, "is", reversed)
# reverse_digits()



#output
# Enter a number: 12345
# Reverse of 12345 is 54321


'''3.a.write a python program to count count unique values inside a list.'''
#
# l = [1, 2, 2, 3, 4, 4, 4, 5, 6]
# def count_unique(l):
#     l=len(l)
#     return (l(set(l)))
#
# print(count_unique(l))

# def count_unique(list):
#     unique_values = []
#
#     for item in input_list:
#         if item not in unique_values:
#             unique_values.append(item)
#
#     count = len(unique_values)
#     return count
# list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# unique= count_unique(list)
# print("Number of unique values:", unique)

'''3.b. write a python program to Extract elements with Frequency greater than K
Input - test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
Output : [4, 3]'''

# l=([4, 6, 4, 3, 3, 4, 3, 4, 3, 8])
# k=3
# def count_unique(l,k):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#         fre=[]
#     for i,n in d.items():
#         if n>k:
#             fre.append(i)
#     return fre
#
# print(count_unique(l,k))


str="hello"
# l=len(str)
print(str[:1])




