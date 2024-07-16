
'''1.	Extract all odd numbers  and even number separately from array.'''


# import numpy as np
#
# A=[2,4,6,9,7,5,3,1,3,20]
# even=[]
# odd=[]
# for i in A:
#     if i%2==0:
#         #print("Even Number :",i)
#         even.append(i)
#     else:
#         #print("odd Number :",i)
#       odd.append(i)
# print("even :",even)
# print("odd:",odd)
'''2.	Create a 3×3 numpy array of all True’s'''

# import numpy as np
# a=np.array([[True]*3]*3)
# print(a)

'''3.	Generate a sequence of numbers in the form of a numpy 
array from 0 to 100 with gaps of 2 numbers.'''

# import numpy as np
# n=np.arange(0,100,2)#0-start 100-last 2-step
# print(n)




'''4.	Getting the positions (indexes) where elements of 2 numpy arrays match.'''

# import numpy as np
# n1=np.array([1,2,3,4,5])
# n2=np.array([5,4,3,2,1])
#
# l=[]
# for i in range (len(n1)):
#     if n1[i]==n2[i]:
#         l.append(i)
# print("position of matching array :",l)

'''5.	Array Generation of random integers within a specified range Output a 5-by-5 array 
of random integers between 0 (inclusive) and 10 (exclusive)'''

# import numpy as np
# n=np.random.randint(0,10,size=(5,5))
# print(n)

'''6.	Given an array- [[1,2,3],[3,4,5],5,6,7]]
Display rows separately and columns separately.
'''
# import numpy as np
# a=np.array( [[1, 2, 3],
#              [4, 5, 6],
#              [7, 8, 9]])
# print(a)
# print('Rows :')
# print(a[0,:],a[1,:],a[2,:])
#
# print('Columns :')
# print(a[:,0],a[:,1],a[:,2])


'''7.	Write a program to cancat 2 matrix i) row wise ii)Colum wise'''

# import numpy as np
#
# a=np.array([[0 ,1, 2],
# [3, 4, 5],
# [6 ,7, 8]])
# print(a)
# b=np.array([[10, 11, 12],
# [13, 14, 15],
# [16, 17, 18]])
# print(b)
#
# print("Rowwise concatination")
# print(np.concatenate([a,b],axis=1))
#
# print("column wise concatination")
# print(np.concatenate([a,b],axis=0))

'''8.	Write a program to create 4 by 4 matrix and values should be between 0,15.'''

# import numpy as np
# n=np.random.randint(0,15,size=(4,4))
# print(n)

'''9.	Consider the following ndarrays:
A=[10,20,30,40,50,60,70,80,90]
B=[[0,1,2,3],
[4,5,6,7],	
[8,9,10,11],
[12,13,14,15]]
What will be the array slices as per the following?
i)	B[0:2,1:3]
ii)	A[2:6:3]
iii)A[-1:-3]
iv)	B[::-1]
v)	B[:3,2:]
'''

# import numpy as np
# A=np.array([10,20,30,40,50,60,70,80,90])
# B=np.array([[0,1,2,3],
# [4,5,6,7],
# [8,9,10,11],
# [12,13,14,15]])
#
# y=B[0:2,1:3]
# print(y)
# print("\n")
#
# x=A[2:6:3]
# print(x)
# print("\n")
#
# x=A[-1:-3]
# print(x)
# print("\n")
#
#
# y=B[::-1]
# print(y)
# print("\n")
#
# y=B[:3,2:]
# print(y)

'''10.	Write commands to perform following operations on two 4×4 ndarrays namely P and Q:
adding 10 to P	
Multplication of two arrays P and Q
Divide all elements of Q by 7
Calculate the remainder of all elements of P when divided by 7
Calculate the square root of all elements of Q Ans:
'''

# import numpy as np
#
# P=np.array([
#  [0,1,2,3],
#  [4,5,6,7],
#  [8,9,10,11],
#  [12,13,14,15]])
#
# Q=np.array([
#     [6,7,4,2],
#     [1,3,5,4],
#     [10,50,32,16],
#     [55,12,6,9]])
#
# y=(P+10)
# print(y)
# print("\n")

# z=(P*Q)
# print(z)
# print("\n")

# x=(Q%7)
# print(x)
# print("\n")

# x=(P//7)
# print(x)
# print("\n")

# import math
# print(np.sqrt(Q))

#Assignment no 2

'''1.	Write a program to create a 4×4 ndarray having values ranging 0 to 15(both inclusive) '''

# import numpy as np
# n=np.random.randint(0,15,size=(4,4))
# print(n)

'''2.	Write a Numpy program to replace all even numbers in an array with -3 
and copy the contents to a new array. The original array shouldn’t be modified.'''
#
# import numpy as np
# A=np.array([[2,6,4]
#             ,[8,7,5],
#             [3,1,9],
#             [11,26,15]])
# #print(A)
# A=np.copy(B)
# B=([A%2==0]-3)
# print(A)
# print(B)


'''3.	Write a NumPy program to create a 3x3 identity matrix, i.e. 
diagonal elements are 1, the rest are 0. Replace all 0 to random number from 10 to 20'''

#import numpy as np
#import random
# # n=np.array([[1,2,3],
# #            [4,5,6]
# #            [7,8,9,]])
# # n=np.random.randint(10,20,size=(3,3))
# # print(n)
# # l=[]
# #
#
# n=np.identity(3,dtype=int)
# print(n)
# for i in range(len(n)):
#     for j in range(len(n[i])):
#         if i!=j:
#             n[i][j]=random.randrange(10,21)
# print(n)


"""4.	write a Numpy program to convert a 1D array into a 2D array with 3 rows."""


"""5.	Consider the ndarrays Arr1 and Arr2 . 
Arr1= array([[0,1,2],
          [3,4,5],
          [6,7,8]])
Arr2=  array([[10,20,30],
     [40,50,60],
                     [70,80,90]])
What	will	be	the resultant array,	if the following statement	is	executed? np.hstack((Arr2,Arr1))
np.vstack((Arr2,Arr1))
"""

# import numpy as np
# Arr1=np.array([[0,1,2],
#           [3,4,5],
#           [6,7,8]])
# Arr2=np.array([[10,20,30],
#              [40,50,60],
#             [70,80,90]])
#
# print(np.hstack((Arr2,Arr1)))
# print("\n")
#
# print(np.vstack((Arr2,Arr1)))

"""6.	Write python statement to create a one –dimensional array using arange() function 
.Elements will be in the range 10 to 30 with a step of 4 (including both 10 and 30).
 Reshape this one- dimensional array to two dimensional array of shape(2,3).
  Then display only those elements of this two –dimensional array which are divisible by 5."""


"""7.	Find the output:
import numpy as np a=np.array([[0,2,4,6],[8,10,12,14],[16,18,20,22],[24,26,28,30]])
print(a)
print(a[:3,3:])
print(a[1::2,:3])
print(a[-3:-1,-4::2])
print(a[::-1,::-1])
"""

# import numpy as np
# a=np.array([
#     [0,2,4,6],
#     [8,10,12,14],
#     [16,18,20,22],
#     [24,26,28,30]])
#
# print(a)
# print("\n")
#
# print(a[:3,3:])
# print("\n")
#
# print(a[1::2,:3])
# print("\n")
#
# print(a[-3:-1,-4::2])
# print("\n")
#
# print(a[::-1,::-1])

'''8.Find the output:
import numpy as np
a=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(a)
print(np.hsplit(a,2))
print(np.hsplit(a,4))
print(np.vsplit(a,3))
a1,a2=np.hsplit(a,2)
print(a1)
print(a2)

'''

# import numpy as np
# a=np.array([
#     [1,2,3,4],
#     [1,2,3,4],
#     [1,2,3,4]])
# print(a)
# print("\n")
#
# print(np.hsplit(a,2))
# print("\n")
#
# print(np.hsplit(a,4))
# print("\n")
#
# print(np.vsplit(a,3))
# print("\n")
# a1,a2=np.hsplit(a,2)
# print("\n")
# print(a1)
# print(a2)

'''9.	Write a program to create the two one dimensional random array of size 10
 between the range of 1 to 10. Display the elements which are equal.'''


# import numpy as np
# n1=np.random.randint(1,10,size=(10))
# n2=np.random.randint(1,10,size=(10))
# print(n1)
# print(n2)
# l=[]
# for i in n1:
#     if i in n2:
#         l.append(i)
#     l=list(set(l))
# print(l)


"""10.	Write a python program to create a 3 X 3 numpy array having 5’s.
 Replace all the boundary elements with 0."""


#Assignment 3 28/jun

'''1.	Create a 5x5 array of random integers between 1 and 50.
 Find the sum, minimum, and maximum of the elements along both axes.'''

# import numpy as np
# n=np.random.randint(1,50,size=(5,5))
# print(n)
# minvalue=np.min(n)
# print("minvalue:",minvalue)
# mmaxvalue=np.max(n)
# print("maxvalue:",mmaxvalue)
# sum=np.sum(n)
# print("sum :",sum)

'''2.	Create a 1D array of 10 random integers and extract the elements at positions 2, 4, and 6.'''
# import numpy as np
# n=np.random.randint(1,10,size=(10))
# print(n)
#
# print(n[2])
# print(n[4])
# print(n[6])

'''3.	Create a 2D array of shape (4, 4) and extract the elements at positions (0,0), (1,1), and (2,2).'''

# import numpy as np
# n=np.array([ [2,4,6,8],
#              [5,6,7,8],
#              [7,2,1,5],
#              [9,3,6,4]])
#
# print(n)
# print("position of (0,0) :",n[0,0])
# print("position of (1,1) :",n[1,1])
# print("position of (2,2) :",n[2,2])
# print("position of (3,3) :",n[3,3])

'''4. Drop rows and columns with missing values from a 2D array.'''
# import numpy as np
# n=np.array([ [2,4,6,8],
#              [5,6,None ,8],
#              [7,2,1,5],
#              [9,3,6,4]])
# row=np.any(np.isnan(n), axis=1)
# print(row)
#
# col=np.any(np.isnan(n), axis=0)
# print(col)

'''5. Delete the second column from a given array and insert the following new column in its place.
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
newColumn = numpy.array([[10,10,10]])
'''

# import numpy as np
# n=np.array([[34,43,73],
#             [82,22,12],
#             [53,94,66]])
# print("original array \n",n)
#
# # print(n[:,1])
# n[:,1]=[10,10,10]
# print("new created array \n",n)

'6.	How to swap two columns in a 2d numpy array?'''
# import numpy as np
# n = np.array([[1, 2, 3, 4],
#                   [5, 6, 7, 8],
#                   [9, 10, 11, 12]])
# print("Original array:")
# print(n)
# def swap_columns(col1, col2):
#     n[:, [col1, col2]] = n[:, [col2, col1]]
#     return n
# swapped_array = swap_columns( 1, 3)
# print("\nArray after swapping columns:")
# print(swapped_array)

'''7. How to swap two rows in a 2d numpy array?'''

# import numpy as np
# n = np.array([[1, 2, 3, 4],
#                   [5, 6, 7, 8],
#                   [9, 10, 11, 12]])
# print("Original array:")
# print(n)
# def swap_columns(row1, row2):
#     n[[row1, row2],:] = n[[row2, row1],:]
#     return n
# swapped_array = swap_columns( 0, 2)
# print("\nArray after swapping rows:")
# print(swapped_array)


#

'''8.	 How to reverse the rows of a 2D array?'''
# import numpy as np
# n=np.array([[1,6,9],[5,9,2]])
# print(n)
#
# reversed=n[::-1]
# print(reversed)

'''9.	How to find the most frequent value in a numpy array?'''



'''10.	Find the index of the maximum value in a 2D array.'''

# import numpy as np
# n1=np.array([[20,30,90,40],[20,40,120,50]])
#
# print(n1)
#
# a1 = np.where(n1 == np.max(n1))
# print(a1)

# import numpy as np
#
# # Create a 3x3 array filled with 5's
# array = np.full((3, 3), 5)
# print("Original Array:")
# print(array)
#
# # Replace the boundary elements with 0
# array[0, :] = 0   # Top row
# array[-1, :] = 0  # Bottom row
# array[:, 0] = 0   # Left column
# array[:, -1] = 0  # Right column
#
# print("Array with Boundary Elements Replaced by 0:")
# print(array)

# import numpy as np
# a = 10
# b = 12
# print("binary representation of a:",bin(a))
# print("binary representation of b:",bin(b))
# print("Bitwise-and of a and b: ",np.bitwise_and(a,b))
# print("Bitwise-or of a and b: ",np.bitwise_or(a,b))
# print("left shift of 20 by 3 bits",np.left_shift(20, 3))
# print("Binary representation of 20 in 8 bits",np.binary_repr(20, 8))
# print("Binary representation of 160 in 8 bits",np.binary_repr(160,8))