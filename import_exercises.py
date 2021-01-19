#1) Import and test 3 of the functions from your functions exercise file.

# import the module and refer to the function with the . syntax
Import each function in a different way:
import function_exercises
function_exercises.is_two(2)

# use from to import the function directly
from function_exercises import is_two
is_two(2)

# use from and give the function a different name
from function_exercises import is_two as  i_s
is_two(2)

#2) For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.

#A) How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
from itertools import product
arr1 = "abc"
arr2 = "123"
def Prod(arr1, arr2):
    return list(product(arr1, arr2))
print(Prod(arr1, arr2))
len((Prod(arr1, arr2)))

#B) How many different ways can you combine two of the letters from "abcd"?
from itertools import combinations
print (list(combinations("abcd", 2)))
len (list(combinations("abcd", 2)))

#3)Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
import json
with open('profiles.json') as f:
    data = json.load(f)
print(data[0])

#4) Total number of Users
users = []
for user in range(len(data)):
    if data[user]:
        users.append(data[user]['name'])
print(users)
len(users)
#19

#5) Total active users
active_user = []
for user in range(len(data)):
    if data[user]['isActive'] == True:
        active_user.append(data[user]['name'])
print(active_user)
len(active_user)
#9

#6) Total inactive users
inactive_user = []
for user in range(len(data)):
    if data[user]['isActive'] == False:
        inactive_user.append(data[user]['name'])
print(inactive_user)
len(inactive_user)
#10

#7) Grand total of balances for all users
def handle_commas1(num_string):
    return float(num_string.replace(",","").replace("$",""))

balance_list = [handle_commas1(d['balance']) for d in data]
sum(balance_list)

#8) Average balance per user
avg_bal = sum(balance_list)/float(len(balance_list))
round(avg_bal, 2)

#9) User with the lowest balance
min_bal = min(balance_list)
min_bal

#10) User with the highest balance
max_bal = max(balance_list)
max_bal

#11) Most common favorite fruit
from collections import Counter
favoriteFruit_list = [d['favoriteFruit'] for d in data]
Counter(favoriteFruit_list)
print(max(favoriteFruit_list))

#12) Least common favorite fruit
print(min(favoriteFruit_list))

#13) Total number of unread messages for all users
def normalize_greeting(string): # creat a funtion that normalizes the greeting to just show numbers.
    string = string.lower()
    string = string.strip()  
    if not string:
        return string
    elif string[0] not in '1234567890':
        return normalize_greeting(string[1:])
    return string[0] + normalize_greeting(string[1:])
print(normalize_greeting('s2dk4fj3kjd0'))

greetings = [int(normalize_greeting(d['greeting'])) # use this to sum the normal greetings and their repective numbers.
             for d in data]
total_unread = sum(greetings)
total_unread