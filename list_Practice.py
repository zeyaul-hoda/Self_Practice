# List is a collection of items (Python objects) which is ordered and mutable.
# The purpose of the list is, to group up the things, which fall under the same category.
#Creating a list in python is putting different comma-separated-values, between square brackets
#Example
#Homogenious Data Type

# List is mutable.
# List uses indexing to access values.
#Lists are not hashable.
#Type of list is 'list'.

from audioop import reverse
from functools import total_ordering
from inspect import stack


l1 = [30,40,45,50,2]
#Non-Homogenious Type
l2 = [123, 'Zeya', 23.0]
#List with Single Value
l3 = [99]
# Create empty List
l4 = []
# Create empty list using list
l5 = list()
# Create list using list
l6 = list([4, 5, 5, 8])

#Accesing List by index
fruits = ['Apple', 'Banana', 'Mango']
print(fruits[0], fruits[2], fruits[-2])

# l = [1, 3, 4, 8, 25, 9, 18, 0, 6]
# print(1[:5]) # first five
# print(1[5:]) # return list after 5
# print(1[-5:]) # return list last 5

#Above example is called list Slicing

#Membership Operator (in, not in) Ex -
l = [5, 8, 12, 25, 18, 90, 15, 29, 30]
print(12 in l)
print(4 in l)
print(18 in l)

# Modify value at specific index
i = 2
s = [10, 20, 30, 35, 90]
s[i] = 25
print(s)

#append() -- append function used to add element at the end
a = [5, 8, 1, 50]
s = [55, 66, 77]
a.extend(s)
a.append(100)
print(a)
print(s)

# extend() method is used to append individual element. Ex
l = [3, 5, 7]
a = [55, 66, 77]
l.extend(a)
print(l)

# insert() is used to insert new element at specific index.
l = [1, 5, 10, 15, 20]
l.insert(3, 55)
print(l)

# pop() function to remove the element from the end by default and returns the deleted element.
l = [1,5,6,8,10,20]
#l.pop() # It will delete aautomatic from the end
l.pop(3) # It will delete index 3
print(l)

# remove() function is used to simply remove the first occurrence of the value. 
# It doesn't return a value.Throws ValueError, if element not found.
l = [10, 12, 15, 18, 100] # l = [10, 12, 15, 18, 100]
l.remove(18)
print(l)

# Concatenate lists (Add)
# One of the simplest ways to join two lists in Python is to use the "+" operator. 
# The "+" operator also allows you to concatenate more than two lists as well.
# "*" ways to join two lists in Python is to use the "+" operator

l1 = [1,2,3]
l2 = [4,5,6]
#l3 = [l1 + l2]
l3 = [*l1, *l2]
print(l3)

fruits_1 = ["apple", "banana"]
fruits_2 = ["grapes", "mango"]
fruits_3 = ["orange", "pickle", "pine"]
total_fruits = [*fruits_1, *fruits_2, *fruits_3]
print(total_fruits)

# max() function is used to find largest element in the list
l = [1, 5, 55, 74,32]
print(max(l))

# min() function is used to find the smallest element in a list.
l = [1, 5, 55, 74,32]
print(min(l))

# sum() function is used to calculate the sum of all the elements in a list.
l = [1, 5, 55, 74,32]
print(sum(l))

# reverse() function is used to changes(reverse) the list in-place.-------
l = [1, 5, 55, 74,32]
l.reverse()
print(l)

# List Unpacking-----------------------------------------------------------
l = [1, 5, 8]
x, y, z = l
print("x: {} : y : {} : z : {}".format(x,y,z))

# Iterate elements in a list using "for" loop------------------------------
l = [4, 8, 11, 5, 55]
for x in l:
    print(x)

# Python in-built function "enumerate()"" adds a sequence number starts from zero to each item in the list
#-----------------------------------------------------

# stack()-The stack is a data structure in which, insertion and deletion operations follow the pattern,
# We can achieve this using append() and pop() functions.

stack = [5, 8, 9]
print(stack)
stack.append(5)
print(stack)
stack.pop()
print(stack)

#reverse() function is used to reverse the element
l = [4, 8, 11, 5, 55]
l.reverse()
print(l)

# sort() method to arrange items in a list in ascending or descending order.
l = [4, 8, 11, 5, 55]
l.sort()
print(l)
l.sort(reverse=True)
print(l)

# sorted() which has the same implementation as sort() function, 
# actually designed for immutable containers like strings, tuple etc
s = 'NewYork'
print(sorted(s))
print(sorted(s, reverse=True))

# is() operator compares ''id'' of both values being compared, with same i'd they have dif location(address)

