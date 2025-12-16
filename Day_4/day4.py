"""
Day 4: Functions & Modular Programming
🎯 Goal of Day 4

Understand why functions are used - A function is a block of reusable code that performs a specific task

Write reusable, clean code

Use return properly

Get interview-ready examples
"""


#Even or odd using Function

def EvenOdd(num):
    if num%2==0:
        return "Even"
    else:
        return "odd"
    
def even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"


num= int(input("enter a number:"))
print(EvenOdd(num))


#Find Largest of two numbers
def maximum(x,y):
    if x>y:
        return (f'{x} is greater than {y}')
    elif y>x:
        return (f'{y} is greater than {x}')
    else:
        return (f'{x} is equal to {y}')
    
def maximum(x, y):
    return x if x >= y else y


x=int(input("enter x:"))
y=int(input("enter y:"))
print(maximum(x,y))

#Sum of First N Natural Numbers - Interview tip: Also mention formula → n*(n+1)//2
def SumOfN(n1):
    return n1*(n1+1)//2

n1= int(input("enter n1:"))
print(SumOfN(n1))


#Factorial using Function
def Fact(n2):
    res=1
    if(n2==0):
        res=1
    else:
        for i in range(1, n2+1):
            res= res*i

    return res
n2= int(input("enter n2:"))
print(Fact(n2))


#Check Prime using Function
def Prime(n2):
    if n2 <= 1:
        print("Not prime")
    else:
        for i in range(2, int(n2 ** 0.5) + 1):
            if n2 % i == 0:
                print("Not prime")
                break
        else:
            print("Prime")

Prime(n2)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Prime" if is_prime(n2) else "Not prime")


#Reverse a number
def rev(x1):
    x2=0
    while x1>0:
        r= x1%10
        x2 = x2*10+r
        x1= x1//10 #// integer division
    return (x2)

num1=int(input("enter num1 number:"))
print(rev(num1))


#Calculator using Functions
def add(a,b):
    return (a+b)
def subtract(a,b):
    return (a-b)
def multiply(a,b):
    return (a*b)
def divide(a,b):
    if b==0:
        return "Cannot divided by Zero"
    return (a/b)

a=int(input("enter a:"))
b=int(input("enter b:"))
print(add(a,b))
print(subtract(a,b))
print(multiply(a,b))
print(divide(a,b))