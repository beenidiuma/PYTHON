#problem 1
total_minutes = int(input("Enter no.of minutes:"))
hours = total_minutes // 60
remaining_minutes = total_minutes % 60
total_seconds = total_minutes * 60

print("Hours:", hours)
print("Remaining minutes:", remaining_minutes)
print("Total seconds:", total_seconds)

#problem 2 
#display personal details using variables
name = str(input("Enter name:"))
age = int(input("Enter age:"))
height = float(input("Enter height:"))
print(name)
print(age)
print(height)

#problem 3
#personalized greeting
name = input()
print(f"hello,{name}!")

#problem 4
#power calculation
base = int(input("enter base:"))
exponent = int(input("enter exponent"))
print(base**exponent)

#problem 5
#average of three numbers
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number"))
total = a+b+c
avg = total/3
print(avg)

#problem 6
#greater than comparision
a = int(input("enter first number"))
b = int(input("enter second number"))
print(a>b)

#problem 7
#equality check
a = int(input("enter first number"))
b = int(input("enter second number"))
print(a == b)

#problem 8
#add two numbers read as strings
a = input("enter first number")
b = input("enter second number")
a = int(a)
b = int(b)
total = a+b
print(total)

#problem 9
#float to integer conversion
n = float(input())
print(n)
new = int(n)
print(new)

#problem 10
#sum using arithmetic operator
a = int(input("enter first number"))
b = int(input("enter second number"))
print(a+b)

#problem 11
#area of a rectangle
length = float(input("enter first number"))
breadth = float(input("enter second number"))
area = length*breadth
print(area)

#problem 12
#quotient and remainder
a = int(input("enter first number"))
b = int(input("enter second number"))
q = a/b
r = a%b
print(q)
print(r)

#problem 13
#Both numbers positive check
n1 = int(input("enter first number"))
n2 = int(input("enter second number"))
print(n1%2 == 0)
print(n2%2 == 0)

#problem 14
#logical NOT on a condition
num = int(input())
print(not(num>0))

#problem 15
#augmented assignment operations
a = int(input())
#20
a = a+5 # a = 20+5 --> 25
a = a*2 # a = 25*2 --> 50
a = a-3 # a = 50-3 --> 47
print(a)

#problem 16
#exchange values of two variables
a = int(input())
b = int(input())

#logic 1 - using temp variable
temp = a
a = b
b = temp
print(a)
print(b)

#logic 2 - without using temp(3 variable)
a = a+b
b = a-b
print(a)
print(b)

#logic 3 - without using temp(3 variable)
a = a^b
b = a^b
a = a^b
print(a)
print(b)

#logic 4 - without using temp (3 variable)
a = a*b
b = a/b
a = a/b
print(a)
print(b)

#logic 5 - using python's special
a,b = b,a
print(a)
print(b)

#problem 17
#calculate simple interest
principle = float(input("enter first number"))
rate = float(input("enter second number"))
time = float(input("enter third number"))
si = (principle*rate*time)/100
print(si)

#problem 18
#temperature conversion (celsius to fahrenheit)
#formula:F = (c* 9/5)+32
c = float(input(56))
f = (c*9/5)+32
print(f)

#problem 19
#check divisibility by 3 and 5
n = int(input("enter first number"))
print(n%3)
print(n%5)

#problem 20
#sum of digits of a two-digit number
num = int(input("enter first number"))
tens = num//10
units = num%10
total = tens+units
print(total)

#problem 21
#atleast one even number
#evne number : if the number is divisible by 2 without any reaminder
n1 = int(input())
n2 = int(input())
print(n1%2==0 or n2%2==0) 
