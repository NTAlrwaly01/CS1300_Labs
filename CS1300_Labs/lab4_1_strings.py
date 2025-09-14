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

# Using + to join strings
first = "Python"
second = "Programming"
combined = first + " " + second
print("Combined:", combined)


# Building strings piece by piece
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print("Message:", message)


# Task: Create these strings
word1 = "Data"
word2 = "Science"

# Create "Data Science"
phrase1 = word1 + " " + word2
print("Phrase 1:", phrase1)


# Create "DataScience" (no space)
phrase2 = word1 + word2
print("Phrase 2:", phrase2)


# Create a sentence
subject = "I"
verb = "love"
object = "Python"
sentence = subject + " " + verb + " " + object + "!"
print("Sentence:", sentence)


# Create an email address
username = "student"
domain = "university.edu"
email = username + "@" + domain
print("Email:", email)


# ----------------- Exercise 4.2: String Repetition -----------------

# Using * to repeat strings
star = "*"
line = star * 20
print("Line of stars:", line)

dash = "-"
separator = dash * 30
print("Separator:", separator)


# Task: Create these patterns

# Create 10 equals signs
equals = "=" * 10
print("Equals:", equals)

# Create "HoHoHo"
ho = "Ho" * 3
print("Ho pattern:", ho)

# Create a border: "+--------+"
plus = "+"
minus = "-" * 8
border = plus + minus + plus
print("Border:", border)

# Create "ABABAB"
ab = "AB"
pattern = ab * 3
print("AB pattern:", pattern)

# Create 5 copies of your initials
my_name = "Nawaf"  
first_initial = my_name[0]
space = " "
initials_repeated = (first_initial + space) * 5
print("Initials:", initials_repeated)


# ----------------- 5.1: Checking Membership -----------------

sentence = "Python is a powerful programming language"

# Check if words/letters are in the sentence
has_python = "Python" in sentence
has_java = "Java" in sentence
has_space = " " in sentence
print("Contains 'Python'?", has_python)
print("Contains 'Java'?", has_java)
print("Contains spaces?", has_space)

# Check if something is NOT in string
no_numbers = "0" not in sentence
print("No zeros?", no_numbers)


# Task: Check these
has_powerful = "powerful" in sentence
print("Contains 'powerful'?", has_powerful)

has_Program = "Program" in sentence  # Note capital P
print("Contains 'Program'?", has_Program)

has_gram = "gram" in sentence
print("Contains 'gram'?", has_gram)

no_exclamation = "!" not in sentence
print("No exclamation?", no_exclamation)

# Check in your name
my_name = "Nawaf"  
has_a = "a" in my_name.lower()
print("Your name has 'a'?", has_a)


# -----------------  5.2: String Comparison -----------------

# Strings are compared alphabetically
str1 = "apple"
str2 = "banana"
comparison1 = str1 < str2
print("'apple' < 'banana'?", comparison1)

# Case matters in comparison!
str3 = "Apple"
str4 = "apple"
comparison2 = str3 < str4
print("'Apple' < 'apple'?", comparison2)


# Task: Predict these comparisons
result1 = "cat" > "dog"
print("'cat' > 'dog'?", result1)

result2 = "10" < "2"  # Comparing as strings, not numbers!
print("'10' < '2'?", result2)

result3 = "Hello" == "hello"
print("'Hello' == 'hello'?", result3)

result4 = "abc" < "abcd"
print("'abc' < 'abcd'?", result4)

result5 = "" < "a"
print("Empty string < 'a'?", result5)


# -----------------  6.1: Extract Information -----------------

# Extract parts from formatted data

# Phone number
phone = "123-456-7890"
area_code = phone[0:3]
prefix = phone[4:7]
line_number = phone[8:12]

print("Phone:", phone)
print("Area code:", area_code)
print("Prefix:", prefix)
print("Line number:", line_number)


# Task: Extract from email
email_address = "john.doe@example.com"

# Get username (before @) - hint: @ is at index 8
username = email_address[:8]
print("Username:", username)

# Get domain (after @)
domain = email_address[9:]
print("Domain:", domain)

# Get just "example" (indices 9-16)
company = email_address[9:16]
print("Company:", company)


# Date extraction
date = "2025/09/08"
year = date[0:4]
month = date[5:7]
day = date[8:10]
print("Date parts:", year, month, day)


# ----------------- 6.2: Build Formatted Strings -----------------

# Create formatted output

# Create a title with decoration
title = "WELCOME"
decoration = "*" * len(title)
formatted_title = decoration + "\n" + title + "\n" + decoration
print(formatted_title)


# Task: Create formatted strings

# Create underlined text
heading = "Important Notice"
underline = "-" * len(heading)
formatted_heading = heading + "\n" + underline
print("\n" + formatted_heading)


# Create a box around text
text = "Hello"
text_length = len(text)
top_border = "+" + "-" * (text_length + 2) + "+"
middle = "| " + text + " |"
bottom_border = top_border  # Same as top
box = top_border + "\n" + middle + "\n" + bottom_border
print("\n" + box)


# Create centered text (simple version)
content = "Python"
total_width = 20
content_length = len(content)
spaces_needed = total_width - content_length
left_spaces = spaces_needed // 2
right_spaces = spaces_needed - left_spaces
centered = " " * left_spaces + content + " " * right_spaces
print("\nCentered: |" + centered + "|")