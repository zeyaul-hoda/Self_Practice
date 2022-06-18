#Set
# A set contains an unordered collection of unique objects. The set data type is, as the name implies, 
# a mathematical set. Set does not allow duplicates. 
# Set does not maintain order.(even though some times it looks like ordered.)

#Python has a built-in function hash() which returns an unique identifier for each value we pass.
#This hash code is unique for every value in the lifetime of a program.

#Example
from tkinter import PIESLICE


s = {2, 3, 1, 2, 1, 3}
print(s)

# Here in above it did not print any duplicate values or in order.

#Creating empty set

s = set()
print(s)

# Most people use curly braces instead of open braces in sets but that creates dictionary.

s = {}
print(type(s))

# here in above example it shows the type of s which is showing dictionary.

# Set Best Example to Understand

l = [2, 6, 3, 2, 6, 3, 2, 4, 1, 3]
print(set(l))

s1 = {2, 6, 3, 2 ,6, 3, 2, 4, 1, 3}
print(s1)

s2 = {2.3, 4.5, 3.2, 2.3, 5.3}
print(s2)

s3 = {"Apple", "Orange", "Banana", "Orange", "Apple", "Banana"}
print(s3)

# here in above example so many elements are given 2 time 3 times but set are not printing duplicate elements

#add() function is used to add the element in set
s = {2, 5}
s.add(3)
print(s)

#remove() function is used to remove the element in set
s = {3, 4, 5}
x = 4
s.remove(x) # if element is not present it will throw an error (if we use discard() function it won't throw error if not present)
print(s)

#update() Update function is used to update the all function from another sets
s1 = {4, 5, 2, 1}
s2 = {7, 8, 5, 6}
s1.update(s2)
print(s1)

#Set Unpacking

s = {'Apple', 'Ball', 'Cat'}
print (s)
x, y, z = s
print(x, y, z)
