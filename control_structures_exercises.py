#1) Conditional Basics

#A)prompt the user for a day of the week, print out whether the day is Monday or not
day = input("day_of_the_week? ") # user interaction # day stores the input
if day.startswith("Mon"):
    print("Happy Monday")
else: 
    print("Today is not Monday")

#B)prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day = input("day_of_the_week? ")
if day.lower().startswith("s"):
    print(f"{day} is a Weekend")
else: 
    print(f"{day} is a Weekday")

#C)create variables and make up values for
#the number of hours worked in one week
#the hourly rate
#how much the week's paycheck will be

#write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
hr = input("Hours Worked? ")
hr = int(hr)
rate = input("hourly Rate? ")
rate = int(rate)
week_pay = hr * rate
if hr > 40:
    print((rate * 40)+(1.5 * rate * (hr - 40)))
else:
    print(week_pay)

#2) Loop Baiscs 

#A)While Loops

#Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
 i = 0
while i <= 100:
    print(f"i: {i}")
    i += 2

#Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i += -5

#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 2
while i < 1000000:
    print(f"i: {i}")
    i = i ** 2
##
i = 100
while i <= 100 and i >= 5:
    print(i)
    i += -5

#B)For Loops
    
#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
num = input("Number? ")
num = int(num)
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)

#Create a for loop that uses print to create the output shown below.
for i in range(1, 10):
    print(str(i)*i)

#C)Break and Continue

#Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement
while True:
    odd_input = input('please enter an odd number between 1 and 50. ')
    if odd_input.isdigit():
        odd_input = int(odd_input)
        if odd_input % 2 ==0:
            continue
        break
        
i = 1
while i <= 50:
    if i == odd_input:
        print(f"Yikes! Skipping number: {i}")
        i += 2
        continue
    print(f"Here is an odd number: {i}")
    i += 2

#D)
# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)
# Enter a positive number
while True: # infinite loop 
    positive_input = input('please enter a positive number. ')
    if positive_input.isdigit():
        positive_input = int(positive_input) # If digit then convert to int
        if positive_input < 0:  
            continue
        break

for i in range(0, positive_input +1):
    print(i)

#E) 
# Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
while True: # infinite loop 
    positive_input = input('please enter a positive number. ')
    if positive_input.isdigit():
        positive_input = int(positive_input) # If digit then convert to int
        if positive_input < 0:  
            continue
        break

for i in range(positive_input, 0, -1):
    print(i)

#3)Fizzbuzz

#One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

#Write a program that prints the numbers from 1 to 100.
#For multiples of three print "Fizz" instead of the number
#For the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print("Fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else: 
        print(i)

#4)Display a table of powers.

#Prompt the user to enter an integer.
#Display a table of squares and cubes from 1 to the value entered.
#Ask if the user wants to continue.
#Assume that the user will enter valid data.
#Only continue if the user agrees to.
#Bonus: (Research python's format string specifiers to align the table)

user_input = int(input("Please enter an interger "))

print("number | squared | cubed")
print("-------|---------|------")
for i in range(1, user_input + 1):
    print("%6d | %7d | %5d" % (i, i**2, i**3))

#5)Convert given number grades into letter grades.

#Prompt the user for a numerical grade from 0 to 100.
#Display the corresponding letter grade.
#Prompt the user to continue.
#Assume that the user will enter valid integers for the grades.
#The application should only continue if the user agrees to.

#Grade Ranges:
#A : 100 - 88
#B : 87 - 80
#C : 79 - 67
#D : 66 - 60
#F : 59 - 0

#Bonus: (Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+))
while True:      
    numeric_grade = int(input("Please enter a number grade: "))
    # convert to letter
    if numeric_grade >= 88:
        print("A")
    elif numeric_grade >= 80:
        print("B")
    elif numeric_grade >= 67:
        print("C")
    elif numeric_grade >= 60:
        print("D")
    else:
        print("F")
     wants_to_continue = input("Do you want to continue? ")
    if not wants_to_continue.lower().startswith("y"):
        break

#6)Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.

#Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# Create a list of dicts
books = [
        {"title": "Naked Statistics", "author": "Charles Wheelan", "genre": "Stats"},
        {"title": "Alex Rider", "author": "Anthony Horwitz", "genre": "Action-Fiction"}
]

selected_genre = input("Please enter a genre: ")
selected_books = [book for book in books if book["genre"]== selected_genre]

for book in books:
    print("---")
    print("title: {}".format(book["title"]))
    print("author: {}".format(book["author"]))
    print("genre: {}".format(book["genre"]))