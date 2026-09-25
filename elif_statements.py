#problem 1
a = 10
b = 20
if a>=17:
    print("a is greater than b")
elif a>=20:
    print("a is equal to b")  
else:
    print("a is less than b")   

#problem 2   
#we can use elif statement as many times we want
# #using 'and' operator
marks = int(input("enter marks:"))   
if marks>=90: 
    print("grade A")
elif marks<= 89 and marks>= 60:
    print("grade B" )
elif marks<= 59 and marks<= 35:
    print("grade C")    
else:
    print("grade D")    

#problem 3
day = int(input("enter day number:"))
if day == 1:
    print("monday")
elif day == 2:
    print("tuesday")
elif day == 3:
    print("wednesday")
elif day == 4:
    print("thursday")
elif day == 5:
    print("friday")
elif day == 6:
    print("saturday")
else:
    print("sunday")

#problem 4
