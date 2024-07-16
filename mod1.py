
#factorial
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#sum
sum=0
def add(num):
    if num==0 or num==1:
        return 1
    else:
        rem=num%10
        num=num//10
        return rem+add(num)