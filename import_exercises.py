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
def Product(arr1, arr2):
    return list(product(arr1, arr2))
print(Product(arr1, arr2))

#B) How many different ways can you combine two of the letters from "abcd"?
from itertools import combinations
print (list(combinations("abcd", 2)))

#3)Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
import json
with open('profiles.json') as f:
    data = json.load(f)
print(data[0])

# Total number of Users
users = []
for user in range(len(data)):
    if data[user]:
        users.append(data[user]['name'])
print(users)
len(users)
#19

# Total active users
active_user = []
for user in range(len(data)):
    if data[user]['isActive'] == True:
        active_user.append(data[user]['name'])
print(active_user)
len(active_user)
#9

# Total inactive users
inactive_user = []
for user in range(len(data)):
    if data[user]['isActive'] == False:
        inactive_user.append(data[user]['name'])
print(inactive_user)
len(inactive_user)
#10

# Grand total of balances for all users

grand_total = []
for balance in range(len(data)):
    if data[user]['isActive'] == False:
        inactive_user.append(data[user]['name'])
print(inactive_user)
len(inactive_user)
