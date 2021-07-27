#1)
def isnegative(n):
    if n < 0:
        return True
    else: 
        return False
isnegative(-6)

#1)
list1 = [1,2,3] 
def count_evens(list1):
    even_count = 0
    for num in list1:  
        if num % 2 == 0: 
            even_count += 1
print(even_count)

#1)
def increment_odds(n):
    nums = []
    for n in range(1, 2*n, 2):
        nums.append(n)
    return nums
increment_odds(3)

#1)
def average(l):
    for n in l:
        return round(len(l)/n, 2)
average([1,2,3])

#1)
name_to_dict = dict()
name_to_dict["frist_name"] = "Ada"
name_to_dict["last_name"] = "Lovelace"
name_to_dict 

#1)
def capitalize_names(name):
    for n in name[0]:
        return(f"{name}".capitalize())
capitalize_names("")

#1)
def count_vowels(value):
    value = value.lower()
    vowel = ['a','e','i','o','u']
    count = 0
    for a in value:
        if a in vowel:
            count += 1 
        
    return count
count_vowels('abcde')

#1)
def analyze_word(word):
    vowels = ['a','e','i','o','u']
    og_word = {}
    num_of_vowels = {}
    num_of_char = {}
    
    for c in word:
        if c in num_of_char:
            num_of_char[word] += 1
        else:
            num_of_char[word] = 1
    return len(word)
    for c in word:
        if c in vowels:
            num_of_char[word] += 1
        else:
            num_of_char[word] = 1
    return(c)
analyze_word('word')