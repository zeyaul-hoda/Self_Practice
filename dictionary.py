# Find the temperature

# l = [34, 32.5, 33, 35, 32, 35.1, 33.6]
'''d = {'Sunday' : 34, 'Monday' : 32.5, 'Tuesday' : 33, 
'Wednesday' : 35, 'Thursday' : 32, 'Friday' : 35.1, 'Saturday' : 33.6}'''

d = {
     'Sunday':34,
     'Monday':32.5,
     'Tuesday':33,
     'Wednesday':35,
     'Thursday':32,
     'Friday':35.1,
     'Saturday':33.6
    }
print(d['Thursday'])

#Create an Empty Dictionary
d1 = {} # Empty dictionary
d2 = dict() # Empty dictionary
print(d1)
print(d2)

#Adding key-value pair to a dictionary
# Syntax = 
#d[Key] = Value

d = {'Mango': 30, 'Banana': 15, 'Peach': 20}
d['Orange'] = 40
print(d)

#Example
d = {'Orange': 40, 'Mango': 30, 'Banana': 15}

print(d.get('Orange')) # returns 40
print(d.get('Peach')) # returns None if 'Peach' doesn't exist
print(d.get('Peach', 10)) # returns 10 if 'Peach' doesn't exist
print(d) # d doesn't change

print(d.setdefault('Orange')) # returns 40
print(d.setdefault('Peach')) # returns None if 'Peach' doesn't exist
print(d) # d changes as 'Peach' is added as key and None as value

print(d.setdefault('Gauva', 60)) # returns 10 if 'Peach' doesn't exist
print(d) # d changes as 'Gauva' is added as key and 60 as value


#Check the Key existence in a dictionary  Using 'in' operator

d = {'Apple': 20, 'Orange': 15, 'Peach': 10}
key = 'Peach'
print(key in d)


#Iterate through a dictionary

d = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}

for x in d:
    print (x)


# Another

d = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}

for x in d:
    print(x, d[x])

#Counting Problems
#Program:Find the occurrence of each word in the given list.
# words = ["Apple", "Orange", "Apple", "Banana", "Peach", "Banana", "Apple", "Peach", "Apple", "Banana"]

#Without dictionary with list
words = ["Apple", "Orange", "Apple", "Banana", "Peach",
          "Banana", "Apple", "Peach", "Apple", "Banana"]
for word in words:
    print(word, '->', words.count(word))

#with Dictionary

words = ["Apple", "Orange", "Apple", "Banana", "Peach",
          "Banana", "Apple", "Peach", "Apple", "Banana"]

count = {}
for word in words:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1
print(count)
print(count.items())

#Program: Finding the word with maximum frequency in the given list.
# words = ["Apple", "Orange", "Apple", "Banana", "Peach", "Banana", "Apple", "Peach", "Apple", "Banana"]

words = ["Apple", "Orange", "Apple", "Banana", "Peach", "Banana", "Apple", "Peach", "Apple", "Banana"]
count ={}
for word in words:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1
max_count = max(count.items(), key=lambda x:x[1])
print(max_count)

# sorting a dictionary into accending and descending order
words = ["Apple", "Orange", "Apple", "Banana", "Peach", "Banana", "Apple", "Peach", "Apple", "Banana"]
count = {}
for word in words:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1
print(sorted(count.items()))  #sort based on word
print(sorted(count.items(), key=lambda x:x[1]))

# Finding MAX and MIN

words = ["Apple", "Orange", "Apple", "Banana", "Peach",
          "Banana", "Apple", "Peach", "Apple", "Banana"]

count = {}
for word in words:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1
print(max(count.items(), key=lambda x:x[1]))
print(min(count.items(), key=lambda x:x[1]))


#Program 1: Below are the customer ids and deposits done by customers in a typical day of a bank. Find the Customer Id and list of deposits done by each customer.
trans = [(1237, 87522),
(1234, 1000),
(1236, 6754),
(1234, 200),
(1236, 1700),
(1234, 400),
(1234, 600),
(1236, 788),
(1234, 500),
(1237, 126653)
]


trans = [(1237, 87522),
 (1234, 1000),
 (1236, 6754),
 (1234, 200),
 (1236, 1700),
 (1234, 400),
 (1234, 600),
 (1236, 788),
 (1234, 500),
 (1237, 126653),
 (1999, 1000)]

deposites = {}

for cust_id, amount in trans:
    if cust_id not in deposites:
        deposites[cust_id] = [amount]
    else:
        deposites[cust_id].append(amount)
print(deposites)
print(deposites.items())
print(max(deposites.items()))
print(max(deposites.items(), key=lambda x:len(x[1])))
print(max(deposites.items(), key=lambda x:sum(x[1])))
print(max(deposites.items(), key=lambda x:max(x[1])))
print(len(deposites))

#Defaultdict()
#program
#Find the count of each word in the given list.
fruits = ["Apple", "Orange", "Banana", "Orange", "Apple", "Banana", "Apple", "Peach", "Apple", "Banana"]

from collections import defaultdict

d = defaultdict(int)
fruits = ["Apple", "Orange", "Banana", "Orange", "Apple", "Banana", "Apple",
         "Peach", "Apple", "Banana"]
for fruit in fruits:
    d[fruit] += 1
print (d)

