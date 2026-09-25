#problem 1
#print numbers from 1 to 10
for i in range (1,11):
    print(i)

#print numbers from 10 to 1
    for i in range (10,0,-1):
        print(i)

# even numbers from 1 to 50
for i in range (1,51):
    print(i)

#odd numbers from 1 to 50
for i in range (1,51):
    print(i)    

#print even numbers from 2 to 50
for i in range (2,51,2) :
    print(i)

#print multiples of 5 from 5 to 50
for i in range (5,51,5):
    print(i)    

#multipication table
number = int(input("enter nuber:")) 
for i in range (1,11):
    print(number,"x",i,"=",number *i)  

#sum of numbers from 1 to n
n = int(input("enter n:"))
total = 0
for i in range(1,n+1):
    total = total+i
    print("sum:",total)

#factorial of a numbers
n = int(input("enter n:"))
factorial = 1
for i in range(1,n+1):
    factorial = factorial * i
print("factorial:",factorial)

#sum of even numbers from 2 to n
n = int(input("enter n:"))
total = 0
for i in range(2,n+1,2):
    total = total+i
    print("sum of even numbers:",total)

#count of multiples of 3
n = int(input("enter n:")) 
count = 0
for i in range (1,n+1):
    if i% 3 ==0:
        count = count + 1
        print("count:",count)

#sum pf multiple of 5
n = int(input("enter n:"))    
total = 0
for i in range (1,n+1):
    if i% 5 ==0:
        total = total +i
        print("sum",total)

#while loop
#print all even numbers 2 to 50
i = 2
while i <= 50:
    print(i)
    i = i+2


#print all odd numbers 1 to 50
i = 1
while i<= 50:
    print(i) 
    i = i+2

#print total of numbers entered by user until 0 is entered 
total = 0
number = int(input("enter number:"))
while number != 0:
    total = total + number
    number = int(input("enter number:"))
    print("total:", total)

#password check
password = ""
while password != "python123":
    password = input("enter password:")
print("login successful")

#count the number of digits in anumber
number = int(input("enter number:"))
count = 0
while number > 0:
    number = number//10
    count = count+1
    print("number of digits:",count)

#sum of digits in a number
number = int(input('enter number:'))
total = 0
while number > 0:
    digit = number % 10
    number = number// 10
    total = total + digit
    print("sum of digits:",total)

#reverse a number
number = int(input("enter number:"))    
reverse = 0
while number > 0:
    digit = number % 10
    number = number //10
    reverse = reverse * 10 +digit
    print("reverse:",reverse)

#check if a number is palindrome 
number = int(input("enter number:")) 
original = number
reverse = 0
while number>0:
    digit = number %10
    reverse = reverse*10 + digit
    number = number//10

    if original == reverse:
        print("palindrome")
    else:
        print("not palindrome")

    #for loop
    #check if a number is a prime
    number = int(input("enter number:"))  
    count = 0
    for i in range(1,number+1):
        if number % 1 == 0:
            count = count+1

            if count == 2:
                print("prime number") 
            else:
                print("not a prime number")

    #print all prime numbers between 2 and 100
    for number in range(2,101):
        count = 0
        for i in range(1,number+1):
            if number % 1 ==0:
             count = count +1

            if count == 2:
                print(number)            


#calculate the sum of positive numbers entered by the user 
total = 0
while True:
    number = int(input("enter number:"))
    if number < 0:
        continue
    if number == 0:
        break
    total = total+ number
    print("total:",total)

#find the first number between 1 and 100 that is divisible 
for i in range(1,101):
    if i%3 == 0 and i% 5 ==0:
        print("first number:",i)
        break

    total = 0
    for i in range(10):
        number = int(input("enter number:"))
        if number > 0:
            total = total + number

    correct_password = "python123"
    for attempt in range(1,4):
        password = input("enter password:") 
        if password == correct_password:
            print("login successful")
            break
        print("wrong password")
    else:
        print("account locked")

#find the largest number among 5 numbers entered by the user
largest = None
for i in range(5):
    number = int(input("enter number:"))
    if largest is None or number > largest:
        largest = number
        print("largest:",largest)


    #find the smallest number among 5 numbers entered by the user
    smallest = None
    for 1 in range (5):
        number = int(input("enter number:"))
        if smallest is None or number < smallest:
            smallest = number
            print("smallest:",smallest)

                

    















           
    
    




