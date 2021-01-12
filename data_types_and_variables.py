
#1)
# You have rented some movies for your kids: 
# The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

rented_movie1 = {
        "name": "little Mermaid",
        "rent_day": 3
}
print(rented_movie1)

rented_movie2 = {
        "name": "Borther Bear",
        "rent_day": 5,
        "like": True
}
print(rented_movie2)

rented_movie3 = {
        "name": "Hercules",
        "rent_day": 1,
        "like": "?"
}
print(rented_movie3)

rented_movies = [rented_movie1, rented_movie2, rented_movie3]
print(rented_movies)

(rented_movie1["rent_day"]) * 3
(rented_movie2["rent_day"]) * 3
(rented_movie3["rent_day"]) * 3

#This is the final Answer
total_rent = ((rented_movie1["rent_day"]) * 3) + ((rented_movie2["rent_day"]) * 3) + ((rented_movie3["rent_day"]) * 3)
total_rent
# $27 to rent all the movies

#2) 
# Suppose you're working as a contractor for 3 companies: 
# Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, 
# Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 
# 6 hours for Google and 4 hours for Amazon.
h_pay = 350
hours = 10
facebook_pay = h_pay * hours
print(facebook_pay)

h_pay = 400
hours = 6
google_pay = h_pay * hours
print(google_pay)

h_pay = 380 
hours = 4
amazon_pay = h_pay * hours
print(amazon_pay)

total_pay = sum(facebook_pay, google_pay, amazon_pay)
print(total_pay)
# $7420


#3)
# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
class_not_full = True
class_overlap = False

can_enroll = class_not_full and not class_overlap

print(can_enroll)


#4)
# A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a specific amount of products.
premium_member = True
enough_items = True
past_expire_date = False

product_offer = enough_items or premium_member and not past_expire_date

print(product_offer)


#5)
# Create a variable that holds a boolean value for each of the following conditions:

    #the password must be at least 5 characters
    #the username must be no more than 20 characters
    #the password must not be the same as the username
    #(bonus) neither the username or password can start or end with whitespace


username = 'codeup'
password = 'notastrongpassword'

password_at_least_5 = len(username) <= 20
username_no_more_than_20 = len(password) >= 5
password_not_username = password != username
no_blanks_pass = password == password.strip()
no_blanks_user = username == username.strip()

is_valid_username_and_password = (password_at_least_5
                                and username_no_more_than_20
                                and password_not_username
                                and no_blanks_pass
                                and no_blanks_user)
is_valid_username_and_password


##Extra(List Comp)

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

#For Loop
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

up_fruits = []
for fruit in fruits:
    up_fruits.append(fruit.upper())
up_fruits

#List Comp
up_fruits1 = [fruit.upper() for fruit in fruits]
up_fruits1

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
cap_fruits = [fruit.capitalize() for fruit in fruits]
cap_fruits

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
def is_vowel(string):
    string = string.lower()
    return string in ["a","e","i","o","u"]

def count_vowels(string):
    count = 0
    for letter in string:
        if is_vowel(letter):
            count += 1
    return count

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if fruit.count("a")
+ fruit.count("e")
+ fruit.count("i")
+ fruit.count("o")
+ fruit.count("u") > 2]

fruits_with_more_than_two_vowels


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels = [fruit for fruit in fruits if fruit.count("a")
+ fruit.count("e")
+ fruit.count("i")
+ fruit.count("o")
+ fruit.count("u") == 2]
fruits_with_only_two_vowels


# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_with_more_than_5_characters = [fruit for fruit in fruits if len(fruit) > 5]
fruits_with_more_than_5_characters


# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_with_exactly_5_characters = [fruit for fruit in fruits if len(fruit) == 5]
fruits_with_exactly_5_characters


# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_with_less_than_5_characters = [fruit for fruit in fruits if len(fruit) < 5]
fruits_with_less_than_5_characters


# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
fruits_number_of_characters = [len(fruit) for fruit in fruits]
fruits_number_of_characters


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits if fruit.count("a")]
fruits_with_letter_a


# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

even_numbers = [number for number in numbers if (number % 2 == 0)]
even_numbers


# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [number for number in numbers if not (number % 2 == 0)]
odd_numbers


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [number for number in numbers if number > 0]
positive_numbers


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negitive_numbers = [number for number in numbers if number < 0]
negitive_numbers


# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
num_with_more_than_2_numerals = [number for number in numbers if number >= 10]
num_with_more_than_2_numerals



# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [number **2 for number in numbers]
numbers_squared


# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [number for number in numbers if not (number % 2 == 0) and number < 0]
odd_negative_numbers


# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [number + 5 for number in numbers]
numbers_plus_5



# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
prime_list = [number for number in numbers if all(number % numbers != 0 for numbers in range(2, number))]
prime_list