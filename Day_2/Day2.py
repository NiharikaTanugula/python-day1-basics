x= int(input("enter x value:"))
y= int(input("enter y value:"))
print(f"Sum= {x+y}")
print(f"Difference={x-y}")
print(f"Product={x*y}")

age= int(input("enter your age:"))
if age>=18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")


num=int(input("enter a number:"))
if num==0:
    print("Entered number is zero")
elif num>0:
    print("Entered number is Positive")
else:
    print("Entered number is Negative")


marks=float(input("enter your marks:"))
if marks<0 and marks>100:
    print("Invalid entry")
elif marks>=40:
    print("Pass")
else:
    print("Fail")



number= int(input("Enter another number"))
if number%2 == 0:
    print("Even")
else:
    print("Odd")



#Toady i learnedhow to take input from user, perform type casting, use arithmetic, comparision, logical and conditional statements.