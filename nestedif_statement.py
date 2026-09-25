#problem 1
username = input("enter username:")
password = input("enter password:")
if username == "admin":
    if password == "1234":
        print("login successful")
    else:
        print("incorrect password")  

#problem 2
a = float(input("enter first number")) 
b = float(input("enter second number"))   
operator = input("enter operator(+,-,*,/):")
if operator == "+":
    print("result:", a+b)
elif operator == "-" :
   print("result:", a-b)
elif operator =="*":
    print("result:", a*b)   
elif operator == "/":
    if b != 0:
     print("result:", a/b)
    else:   
      print("cannot divide by zero")
else:
    print("invalid operator")


#problem 3
balance = float(input("enter balance:"))
amount = float(input("enter withdrawal amount:"))
if amount > 0:
   if amount <= balance:
      balance = balance- amount
      print("withdrawal successful")
      print("remaining balance:", balance) 
   else:
      print("insufficient balance")
else:
   print("invalid amount")

#problem 4
age = int(input("enter age:"))  
test = input("did you pass the test? (yes/no):") 
if age >= 18:
   if test == "yes":
      print("license can be issued")
   else:
      print("pass the driving test first")
else:
   print("not eligible due to age")
   
   





