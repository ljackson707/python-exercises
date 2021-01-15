#1) Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(n):  
    if n == 2 or n == "2":
        return True
    else:
        return False
is_two(2)

#2) Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(letter):
    vowels = ["a","e","i","o","u"]
    return letter.lower() in vowels

is_vowel("u")

#3) Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
vowels = ["a","e","i","o","u"]
def is_consonant(letter):
    return letter.isalpha() and not is_vowel(letter)
is_consonant("M")

#4) Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def cap_word(word):
    for n in word[0]:
        if is_consonant(n):
            return (f"{word}".capitalize())
        else:
            return word
cap_word("li")

#5) Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(percent, bill):
    tip_amount = percent*bill
    return tip_amount
calculate_tip(.25, 100)

#or 

def calculate_tip(percent, bill):
    if percent > 1:
        percent /= 100 # Allows user to put in whole number as percentage.
    tip_amount = percent*bill
    return round(tip_amount, 2)
calculate_tip(.25, 100)

#6) Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(price, discount):
    return price-(price*discount)
apply_discount(100, .05)

#7) Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(string):
    return float(string.replace(',',''))
handle_commas("1,000,2")

#8) Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade in range(80, 90):
        return "B"
    elif grade in range(70, 80):
        return "C"
    else:
        return "F"
get_letter_grade(110)

#9) Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(string):
    for c in string:
        if c in vowels:
            word = string.replace(c,'')
    return word
remove_vowels("liam")

#10) Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
def normalize_name(word):
    word = "".join(c for c in word if c.isalnum() or c == " ") 
    for c in word:
            return word.lower().replace(" ", "_")
normalize_name("%Lord lo%")

#11) Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
def cumulative_sum(numbers):
    total = 0
    for n in numbers:
        total += n
        yield total
list(cumulative_sum([1,2,3,4]))

#or 
def cumulative_sum(list_of_numbers):
    sums = [list_of_numbers[0]]
    print(f"sums: {sums}")
    for n in list_of_numbers[1:]:
        previous_total = sums[-1]
        sums.append(previous_total + n)
        print(f"End of for loop sums: {sums}")
cumulative_sum([1,1,1])

# Bonus

#1) Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour 
def twelveto24(string):
    if string[-2:] == "AM" and string[:2] == "12": 
        return "00" + string[3:5]
    elif string[-2:] == "AM": 
        return string[:-2] 
    elif string[-2:] == "PM" and string[:2] == "12": 
        return string[:-2]
    else:
        return str(int(string[:2]) + 12) + string[2:5] 
print(twelveto24("09:45 AM"))

#2) Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
def col_index(c_name):
    if c_name == ('A'):
        print(1)
    elif c_name == ('B'):
        print(2)
    elif c_name == ('AA'):
        print(27)
col_index("AA")