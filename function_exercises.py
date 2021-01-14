#1) Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(n):  
    if n == 2 or n == "2":
        return True
    else:
        return False
is_two(2)

#2) Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
vowels = ["a","e","i","o","u"]

def is_vowel(letter):
    if letter in vowels:
        return True
    else:
        return False
is_vowel("a")

#3) Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
vowels = ["a","e","i","o","u"]

def is_consonant(letter):
    if letter not in vowels:
        return True
    elif letter in vowels:
        return False
is_consonant("i")

#4) Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def cap_word(word):
    for n in word[0]:
        if is_consonant(n):
            print(f"{word}".capitalize())
        else:
            print(False)
cap_word("li")

#5) Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(x, bill):
    return bill*x
calculate_tip(.25, 100)

#6) Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(price, discount):
    return price-(price*discount)
apply_discount(100, .05)

#7) Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(string):
    return string.replace(',','')
handle_commas("1,000,2")

#8) Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(grade):
    if grade >= 90:
        print("A")
    elif grade in range(80, 90):
        print("B")
    elif grade in range(70, 80):
        print("C")
    else:
        print("F")
get_letter_grade(110)

#9) Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(string):
    for n in string:
        if n in vowels:
            word = string.replace(n,'')
    return word
remove_vowels("liam")

#10) Define a function named normalize_name. It should accept a string and return a valid python identifier, that is: