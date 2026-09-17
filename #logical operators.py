#logical operators
age = 25
citizen = True 
print(age >=18 and citizen == True)

age = 16
citizen = True 
print(age >=18 and citizen == True)

has_card = False
has_cash = True 
print(has_card or has_cash)

is_logged_in = True 
print(not is_logged_in)

#atm eligibility checker
balance = 10000
withdraw = 5000 
print(withdraw >0 and withdraw <=balance)

#student scholarship eligibity checker
marks = float(input("enter marks:"))
attendance = float(input("enter attendance:"))
eligible = marks>= 85 and attendance >=75
print("scholarship eligible:",eligible)

#identity operators
a = None
print(a is None)
print(a is not None)

#bitwise operators
a = 5
b = 3
print(a & b)
print(a | b)
print(a ^ b)
print(a << b)
print(a >> b)


#electric bill calculator
units = int(input("enter electricity units:"))
rate = 6
bill = units * rate
print("electricity bill:", bill)

#travel expense calculator
travel = float(input("travel expense:"))
food = float(input("food expenses:"))
hotel = float(input("hotel expenses:"))
total = travel+food+hotel
print("total expense:",total)

 