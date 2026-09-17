a = 10
print(type(a))
b = 3.14
print(type(b))
phone = True
print(phone)
print(type(phone))
z = 3+4j
print(z)
print(type(z))
s = '''python'''
print(s)
print(type(s))

#list in python
#list is an ordered and changeable collection that can store
marks = [80,90,75,85]
print(marks)


#accesing elements in list
marks = [80,90,75,85]
print(marks[0])
print(marks[1])
print(marks[2])

#change elements in a list
marks = [80,90,75]
marks[1] = 95
print(marks)

#add elements to a list
#add the elements at the end of the list
marks = [80,90,75]
marks.append(85)
print(marks)

#remove elements from the list
marks = [80,90,75]
marks.remove(90)
print(marks)

#insert elements in a list
numbers = [10,20,30]
numbers.insert(1,40)
print(numbers)

#extend a list
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

#remove all the elements
numbers = [10,20,30]
numbers.clear()
print(numbers)

#index method
numbers = [10,20,30,40]
print(numbers.index(30))

#count method
numbers = [10,20,30,40]
print(numbers.count(30))

#sort method
numbers =[40,10,30,20]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#reverse method
numbers = [10,20,30,40]
numbers.reverse()
print(numbers)

#copy method
a = [1,2,3]
b = a.copy()
print(b)

numbers = [10,20,30,40,50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])


#tuples in python
#tuple is a collection of multiple values that is ordered and cannot be changed after creation
student = ("Uma",18,"python")
print(student[0])

#acess values in a tuple
student = ("uma",21,85.5)
print(student[0])
print(student[1])
print(student[2])

#immutable nature of tuples
student = ("uma,21,85.5")
student[1] = 22


#tuples are immutable,meaning they cannot be changed after
numbers = (10,20,20,30,20)
print(numbers.count(20))

numbers = (10,20,30,40,50)
print(numbers.index)


numbers = (10,20,30,40)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#sets in python
#set is a collection of unique values that is unordered and mutable
numbers = {10,20,30,20,10}
print(numbers)


#why use set?
#suppose students have selected subjects
subjects = {"Python","Java","Python","SQL","Java"}
print(subjects)

#add values to a set
subjects = {"Python","SQL"}
subjects.add("SQL")
print(subjects)

#remove values in a set
subjects.remove("java")
print(subjects)


#sets do not allow duplicate values
numbers = {1,2,2,3,3,4}
print(numbers)












