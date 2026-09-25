#problem 1
number = int(input("enter number"))
if number % 2== 0:
    print("even")
else:
    print("odd")   

#problem 2
#temperature check
temperature : float(input("enter temperature"))
if:  temperature > 40:
    print("high temperature")
else:
    print("low temperature")    


#problem 3
a = int(input("enter a first number:"))
b = int(input("enter a second number:"))
c = int(input("enter a third number:"))
if a>b and a>c:
    print("greatest:", a)
elif b>a and b>c:
    print("greatest:", b)
else:
    print("greatest:", c)
