# A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. 
# The differences between tuples and lists are, the tuples cannot be changed, unlike lists. 
#Tuples use parentheses, whereas lists use square brackets.

#Tuple is immutable.
#Tuple values can be of multiple types.
#Tuple uses indexing to access value like a list.
#The Search operation is always O(n).
#Tuples are hashable.
#Type of tuple is 'tuple'

# Tuple Examples:
from ast import Lambda
from pyclbr import Function
from socketserver import BaseRequestHandler
from unicodedata import name


tup1 = (1234, 'John wesley', 240000.0, True)
tup2 = (1, 2, 3, 4, 5)
tup3 = 1, 3, 2, 4
tup4 = () # create empty tuple
tup5 = (3,) # tuple with one value, must always ends with a comma

l = [1, 3, 5 ]
print(type(l))
t = (1, 5, 5)
print(type(t))
t1 = 1, 5, 5
print(type(t1))

l = [3, 5, 4, 2, 1]  # initialising list
l[3] = 99 # updating value at 3rd index
print(l)
t = (3, 5, 4, 2, 1)  # initialising tuple
#t[3] = 99 # updating value at 3rd index
print(t) # through error because it's immutable

# tuple with single element     
x = (9)
print(type(x))
y = (9,)
print(type(y))

# indexing of tuple
t = (1,2,3,4,5)
print(t[3])

# Elements of tuple cannot be modified after initialisation.

# Iteration through tuple using "for" loop

t = (3, 5, 4, 2, 1)
print('tuple iteration: ')
for x in t:
    print(x)

# Swapping two values in python
x = 20
y = 30
x, y = y, x #  swapping in python
print ("x : {}, y : {}".format(x, y))

# count() function is used to count the element
t = (4, 3, 2 ,1 ,4, 3, 4)
print(t.count(4))

#  len() function is used to find the length of tuple
t = (7, 8, 9, 3, 2)
print(len(t))

# sortin the list of tuples
employees = [
            (1239, 'John', 23000, 25),
            (1235, 'Samantha', 13000, 21),
            (1238, 'Amanda', 45000, 30),
            (1237, 'Alex', 57000, 31),
            (1236, 'Vicky', 40000, 24)
            ]

sorted_records = sorted(employees)
print(sorted_records)

#Find out whether the salary of employ2 is greater than employ1 by considering the following information.
#emp1 = (1235, 'Samantha', 53000, 21)
#emp2 = (1236, 'Vicky', 40000, 24)

#Using Lambda Function
key = lambda x: x[2]
# if we give x:x[0] is will be considered for index 0

emp1 = (1235, 'Samantha', 53000, 21)
emp2 = (1236, 'Vicky', 40000, 24)

print(key(emp1) < key(emp2))

# Program: Print the details of employee with maximum salary.  
'''employees = [
(1239, 'John', 23000, 25),
(1235, 'Samantha', 13000, 21),
(1238, 'Amanda', 45000, 30),
(1237, 'Alex', 57000, 31),
(1236, 'Vicky', 40000, 24)
]'''

employees = [
            (1239, 'John', 23000, 25),
            (1235, 'Samantha', 13000, 21),
            (1238, 'Amanda', 45000, 30),
            (1237, 'Alex', 57000, 31),
            (1236, 'Vicky', 40000, 24)
            ]

print(max(employees, key=lambda x:x[2]))

# Program: Print the details of youngest employee among the employees.
'''employees = [
(1239, 'John', 23000, 25),
(1235, 'Samantha', 13000, 21),
(1238, 'Amanda', 45000, 30),
(1237, 'Alex', 57000, 31),
(1236, 'Vicky', 40000, 24)
]'''

employees = [
    (1239, 'John', 23000, 25),
    (1235, 'Samantha', 13000, 21),
    (1238, 'Amanda', 45000, 30),
    (1237, 'Alex', 57000, 31),
    (1236, 'Vicky', 40000, 24)
            ]
print("Min age:", min(employees, key=lambda x:x[3]))

#Print all friends and their emails who's last name is 'barner'.
'''contacts = [
('John', 'john.deer@gmail.com'),
('Alex', 'alex.barner@yahoo.com'),
('Brad', 'brad.cooper@hotmail.com'),
('Cindy', 'cindy.barner@hotmail.com'),
('Matt', 'matt.damon@gmail.com'),
('George', 'george.cloony@yahoo.com'),
('Mec', 'mc.barner@hotmail.com')
]'''

contacts = [
('John', 'john.deer@gmail.com'),
('Alex', 'alex.barner@yahoo.com'),
('Brad', 'brad.cooper@hotmail.com'),
('Cindy', 'cindy.barner@hotmail.com'),
('Matt', 'matt.damon@gmail.com'),
('George', 'george.cloony@yahoo.com'),
('Mec', 'mc.barner@hotmail.com')
]
contacts_2 = []
for name , email in contacts:
    if 'Barner' in email:
        contacts_2.append(email, name)
contacts_2.sort()
