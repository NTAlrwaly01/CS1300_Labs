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