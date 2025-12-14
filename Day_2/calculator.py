x = input("Enter x:") # input function alwaysnreturns the value in string data type, even if you enter any number or any value
y = input("Enter y:")

z = x + y #returns the concatenation of x and y
print(z)

#To over come the above situation, we need to TYPE CAST - Convert one data type to another,using functions like int(),float()
#one way:

print(int(x)+int(y))

#second way:
x1= int(input("x1 value?"))
y1=int(input("y1 value?"))

print(x1+y1)

#FLOAT
x2= float(input("x2 value?"))
y2=float(input("y2 value?"))

print(x2+y2)
# round(number[,ndigits]) -> [] square brackets in documentations indicates OPTIONAL
print(round(x2+y2))
z= x2+y2
print(round(123456,-2))#negative integer, the rounding occurs to the left of the decimal point