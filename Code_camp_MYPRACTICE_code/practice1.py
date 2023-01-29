# importing math
from math import *

print("Hello World")

# variable name
character_name = "cat"
character_age = "5"
is_cat = True
print("There is a cat named " + character_name + " who is " + character_age + " years old.")

# playing with strings
print("Code\ncamp")
print("Code\"camp")
print("Code camp")

phrase = "Code Camp"
print(phrase)
print(phrase.lower())  # makes lower case
print(phrase.upper())  # makes upper case

print(phrase.islower())  # checks lower case
print(phrase.isupper())  # checks upper case

# index in python starts from 0 (moving forward)
# index in python starts from -1 (moving backward)
print(phrase[1])
print(phrase[-1])

print(phrase.index("C"))
print(phrase.replace("Camp", "Tent"))

# playing with numbers
print(0.5)
print(2+1)
print(2*3)
print(2**3)  # exponent
print(10/3)
print(8 % 3)  # mod

number = -5
print(str(number) + " is my favourite number")
print(number.__abs__())
print(number.__pow__(2))
print(min(1, 2, 3))
print(max(1, 2, 3))

# importing functions
print(floor(3.7))
print(ceil(3.7))
print(sqrt(3.7))

# getting some input
name = input("Enter your name: ")
print("Hi there " + name + ".")

# simple calculator
n1 = input()
n2 = input()
answer = float(n1) + float(n2)
print("Answer = " + str(answer))
