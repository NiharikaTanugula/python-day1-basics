#Even odd
num= int(input("enter a number:"))
if num%2==0:
    print("Even")
else:
    print("odd")


#Find Largest of two numbers
x=int(input("enter x:"))
y=int(input("enter y:"))
if x>y:
    print(f'{x} is greater than {y}')
elif y>x:
    print(f'{y} is greater than {x}')
else:
    print(f'{x} is equal to {y}')


#Check Positive, Negative or Zero
n= int(input("enter a number:"))
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")

#Print numbers from 1 to N
a= int(input("enter a:"))
for i in range(1,a+1):
    print(i)

"""
i=1
while i<=a:
    print(i)
    i +=1
"""


#Print Even Numbers between 1 and 20
for i in range(1,21):
    if i%2==0:
        print(i)
#better version:
for i in range(2, 21, 2):
    print(i)

#Sum of First N Natural Numbers - Interview tip: Also mention formula → n*(n+1)//2
n1= int(input("enter n1:"))
i = 1
sum=0
while (i<=n1):
    sum=sum + i
    i +=1

print(sum)

#Check Prime Number
n2= int(input("enter n2"))
count=0
for i in range(1,n2+1):
    if n2%i==0:
        count +=1

if count==2:
    print("prime")
else:
    print("Not prime")


#Reverse a number
x1=int(input("enter x1 number:"))
x2=0
while x1>0:
    r= x1%10
    x2 = x2*10+r
    x1= x1//10 #// integer division
print(x2)

#Factorial of a Number
x3=int(input("enter x3:"))
res=1
for i in range(1,x3+1):
    res= res * i

print(res)



