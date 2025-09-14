# lab4_1_strings.py
# Week 4 Session 1 Lab
# Nawaf T Alrwaly
# 2025-09-08

print("=" * 50)
print("WEEK 4 SESSION 1 LAB - STRING MANIPULATION")
print("=" * 50)

# ----------------- Exercise 1.1: Creating Strings -----------------
# Different ways to create strings
string1 = 'Hello'
string2 = "World"
string3 = '''This is
a multiline
string'''

print("String 1:", string1)
print("String 2:", string2)
print("String 3:", string3)

# Task: Create these strings
# String with apostrophe
my_string1 = "It's a nice day"
print("My string 1:", my_string1)

# String with quotes
my_string2 = 'He said "Hello"'
print("My string 2:", my_string2)

# My name
my_name = "Nawaf T Alrwaly"
print("My name:", my_name)


# ----------------- Exercise 1.2: String Length -----------------
# Finding the length of strings
text1 = "Python"
length1 = len(text1)
print("Length of 'Python':", length1)

text2 = "Hello World"
length2 = len(text2)
print("Length of 'Hello World':", length2)

# Task: Find lengths
text3 = "Programming"
length3 = len(text3)
print("Length of 'Programming':", length3)

# Empty string
empty = ""
empty_length = len(empty)
print("Length of empty string:", empty_length)

# Single space
space = " "
space_length = len(space)
print("Length of single space:", space_length)

# Your name
name_length = len(my_name)
print("Length of your name:", name_length)


# ----------------- Exercise 2.1: Accessing Characters -----------------

word = "Computer"
# Positions: C=0, o=1, m=2, p=3, u=4, t=5, e=6, r=7

# Get first character
first = word[0]
print("First character:", first)

# Get last character (two ways)
last_v1 = word[7]
last_v2 = word[-1]
print("Last character (method 1):", last_v1)
print("Last character (method 2):", last_v2)

# Task:
second_char = word[1]  # Should be 'o'
print("Second character:", second_char)

middle_char = word[4]  # Should be 'u'
print("Middle character:", middle_char)

third_from_end = word[-3]  # Should be 't'
print("Third from end:", third_from_end)


# ----------------- Exercise 2.2: Working with Indices -----------------

phrase = "Hello World"
# Remember: space is also a character!

# Find specific characters
h_char = phrase[0]
space_char = phrase[5]
w_char = phrase[6]

print("H is at index 0:", h_char)
print("Space is at index 5:", space_char)
print("W is at index 6:", w_char)

# Task: Find these characters
o_in_hello = phrase[4]  # First 'o' in Hello
print("First 'o':", o_in_hello)

o_in_world = phrase[7]  # 'o' in World
print("Second 'o':", o_in_world)

exclamation = "Python!"
last_char = exclamation[-1]  # Get the '!'
print("Exclamation:", last_char)

# Calculate middle index
text = "Programming"
text_length = len(text)
middle_index = text_length // 2  # Integer division
middle = text[middle_index]
print("Middle of 'Programming':", middle)



# ----------------- Exercise 3.1: Basic Slicing -----------------

message = "Python Programming"

# Get "Python" (indices 0-5)
first_word = message[0:6]
print("First word:", first_word)


# Get "Programming" (indices 7-end)
second_word = message[7:18]
print("Second word:", second_word)


# Task: Extract these substrings

# Get "Prog" from message
prog = message[7:11]
print("Prog:", prog)


# Get "gram" from message
gram = message[10:14]
print("gram:", gram)


# Get "Python Prog" (first 11 characters)
first_part = message[0:11]
print("First part:", first_part)


# Get "ming" (last 4 characters)
last_part = message[14:18]
print("Last part:", last_part)



# ----------------- Exercise 3.2: Slicing Shortcuts -----------------

text = "Hello World"

# Shortcuts for common slices
from_start = text[:5]
print("First 5:", from_start)  # First 5 characters


to_end = text[6:]
print("From index 6:", to_end)  # From index 6 to end


copy_all = text[:]
print("Full copy:", copy_all)  # Copy entire string


# Task: Use shortcuts

# Get first 3 characters of text
first_three = text[:3]
print("First three:", first_three)


# Get last 5 characters of text
last_five = text[-5:]
print("Last five:", last_five)


# Skip first and last character
middle = text[1:-1]
print("Middle part:", middle)


# Get everything except last 3 characters
except_last = text[:-3]
print("Except last 3:", except_last)




# ----------------- Exercise 3.3: Slicing with Steps -----------------

numbers = "0123456789"

# Every second character
every_second = numbers[::2]
print("Every second:", every_second)


# Every third character
every_third = numbers[::3]
print("Every third:", every_third)


# Reverse the string
reversed_nums = numbers[::-1]
print("Reversed:", reversed_nums)


# Task: Create these slices
alphabet = "abcdefghijklmnop"

# Get every second letter starting from 'a'
pattern1 = alphabet[::2]
print("Pattern 1:", pattern1)  # Should be "acegikmo"


# Get every second letter starting from 'b'
pattern2 = alphabet[1::2]
print("Pattern 2:", pattern2)  # Should be "bdfhjlnp"


# Get last 5 characters reversed
last_reversed = alphabet[-1:-6:-1]
print("Last 5 reversed:", last_reversed)  # Should be "ponml"


# Reverse your name
my_name = "Nawaf T Alrwaly"
name_reversed = my_name[::-1]
print("Name reversed:", name_reversed)



# ----------------- Exercise 4.1: Joining Strings -----------------

