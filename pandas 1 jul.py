
import pandas as pd
import numpy as np

# data=np.array([10,20,30])
# d=pd.Series(data)
# print(d)

# '''using index'''
# data=np.array([10,20,30])
# d=pd.Series(data,index=[5,6,7])
# print(d)

'''using dictionary'''
# data={'a':1,'b':2,'c':3}
# d=pd.Series(data)
# print(d)

# d={'one':pd.Series([1,2,3],index=['a','b','c']),
#    'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
# d1=pd.DataFrame(d)
# print(d1)
# print((d1.isna().sum()))
#
# t=d1.head()
# print(t)
# y=d1.tail()
# print(y)
# y=d1.describe()
# print(y)
#
# y=d1.min()
# print(y)
# y=d1.max()
# print(y)
#
# y=d1.mean()
# print(y)
# y=d1.median()
# print(y)
# y=d1.std()
# print(y)
#
# # y=d1.sample([])
# # print(y)
# x=d1['one'].dtype
# print(x)
# x=d1.dtypes
# print(x)
#
# t1=d1.shape
# print(t1[0])


'''data frame'''

# data=[1,2,3,4,5]
# d=pd.DataFrame({"name":['abc','xtz','pqr','lmn'],'age':[28.60,53,46]})
# d2=pd.DataFrame(data,index=[10,20,30,40])
# print(d)
# print(d2)

# data=[['abc',19],['pqr',57],['bob',43],['xyz',32]]
# d=pd.DataFrame(data,columns=['name','age'])


#assignment

'''1.	Write a program in python to find maximum value over index in Data frame.'''
d = {
    'age': [20, 21, 22, 23],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'marks': [85, 90, 95, 80]
}
d1=pd.DataFrame(d)
print(d1)
d2=d1.max()
print(d2)
