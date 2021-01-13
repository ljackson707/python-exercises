#1) Conditional Basics

#A)prompt the user for a day of the week, print out whether the day is Monday or not
       day = input("day_of_the_week?")
        if day == "Monday":
            print("Happy Monday")
        else: 
            print("Today is not Monday")

#B)prompt the user for a day of the week, print out whether the day is a weekday or a weekend
weekend = ["Saturday", "Sunday"]

day = input("day_of_the_week?")

if day not in weekend:
    print("Today is a Weekday")
else: 
    print("Today is The Weekend")

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
    print(i)
    i += 2

#Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i += -5

#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 2
while i < 1000000:
    print(i)
    i = i ** 2

#B)For Loops
    
#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
num = input("Number? ")
num = int(num)
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)

#Create a for loop that uses print to create the output shown below.

#C)Break and Continue

    #Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement
    other_odd_input = input('please enter an odd number between 1 and 50. ')
for n in range(0, 51):
    if n != other_odd_input and n % 2 == 0:
        continue
    print('Here is an odd number: {}'.format(n))
    if n == odd:
        print('Skip: {}'.format(n))
#D)
    # The input function can be used to prompt for input and use that input in your python code. 
    # Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
    # (Hints: first make sure that the value the user entered is a valid number, 
    # also note that the input function returns a string, so you'll need to convert this to a numeric type.)

#E) 
    # Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.