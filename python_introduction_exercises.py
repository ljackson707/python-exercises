print('Hello, World')

greeting = "Hello Liam"
print(greeting)

favorite_number = 42
n = favorite_number + 7
print(n)

x = 1
print(x)
x = x + 1 
print(x)
x = x * 3 + x
print(x)

#formating

name = 'World'

'Hello %s!' % name
print (name)

f'Hello, {name}!'
print(name)

'Hello, {}!'.format(name)
print (name)

s = ' Hello, Codeup! '
print(s.lower())

s = ' Hello, Codeup! '
print (s.upper())

s = ' Hello, Codeup! '
print (s.strip())

s = ' Hello, Codeup! '
print (s.isdigit())

'123'.isdigit()

s = ' Hello, Codeup! '
print(s.strip().split(', '))

print(', '.join(['one', 'two', 'three']))

#lists 
x = [1,2,3]
print(x)

x = ['one', 'two', 'three']
print(x)

x = [[1,2,3], [4,5,6], [7,8,9]]
print(x)

#List Comprehensions
print([n for n in range(10)])

print([n * 2 for n in range(10)])

print([n * 2 for n in range(10) if n%2==0])

#List Operations

#To Add 
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

#To Remove
numbers = [1, 2, 3, 4]
numbers.pop()
print(numbers)

print('Here is a single quote --> \' <-- ')
print("Here is a single quote --> ' <-- ")
print()
print("Here is a double quote --> \" <--")
print('Here is a double quote --> " <--')
print()
print('Newlines are indicated by the character "n" preceded by a backslash, like so')
print()
print('This string\ncontains a newline')



