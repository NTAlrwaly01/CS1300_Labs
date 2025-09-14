# ================================
# Part 1: Case Conversion Methods
# ================================

# -------------------------------
# Exercise 1.1: Changing Case
# -------------------------------

# Original text
text = "Hello World"

# Convert to uppercase
uppercase = text.upper()
print("Uppercase:", uppercase)

# Task: Complete these conversions
lowercase = text.lower()
print("Lowercase:", lowercase)

title_case = text.title()
print("Title case:", title_case)

swapped = text.swapcase()
print("Swapped case:", swapped)

# Try with different text
name = "jOHn DoE"
print("\nOriginal name:", name)

# Fix the name to proper format
proper_name = name.title()
print("Proper name:", proper_name)

# Task: Convert to all caps
name_caps = name.upper()
print("All caps:", name_caps)

# Convert to all lowercase
name_lower = name.lower()
print("All lowercase:", name_lower)


# -------------------------------
# Exercise 1.2: Case Practice
# -------------------------------

# Practice with different strings
text1 = "PYTHON programming"
text2 = "hELLo WoRLd"
text3 = "data science 101"

# Task: Apply the right method

# Make text1 all lowercase
result1 = text1.lower()
print("text1 lowercase:", result1)

# Make text2 title case (Each Word Capitalized)
result2 = text2.title()
print("text2 title case:", result2)

# Make text3 all uppercase
result3 = text3.upper()
print("text3 uppercase:", result3)

# Capitalize only first letter of text3
result4 = text3.capitalize()
print("text3 capitalized:", result4)

# ================================
# Part 2: Testing String Content
# ================================

# -------------------------------
# Exercise 2.1: Checking String Properties
# -------------------------------

# Test different strings
string1 = "Hello"
string2 = "12345"
string3 = "Hello123"
string4 = " "
string5 = ""

# Check if all alphabetic
print("'Hello' all letters?", string1.isalpha())
print("'12345' all letters?", string2.isalpha())

# YOUR TURN: Complete these tests
print("'12345' all digits?", string2.isdigit())
print("'Hello123' all letters?", string3.isalpha())
print("'Hello123' letters or digits?", string3.isalnum())
print("' ' all spaces?", string4.isspace())

# Check case
text_upper = "HELLO"
text_lower = "hello"
text_mixed = "Hello"

print("\n'HELLO' is uppercase?", text_upper.isupper())
print("'hello' is lowercase?", text_lower.islower())
print("'Hello' is uppercase?", text_mixed.isupper())
print("'Hello' is lowercase?", text_mixed.islower())


# -------------------------------
# Exercise 2.2: Validation Practice
# -------------------------------

# Check user input
input1 = "abc123"
input2 = "123"
input3 = "Hello World"
input4 = "ALLCAPS"

# YOUR TURN: Test these inputs
# Is input1 only letters?
test1 = input1.isalpha()
print("'abc123' only letters?", test1)

# Is input2 only digits?
test2 = input2.isdigit()
print("'123' only digits?", test2)

# Is input3 alphanumeric? (Note: it has a space!)
test3 = input3.isalnum()
print("'Hello World' alphanumeric?", test3)

# Is input4 all uppercase?
test4 = input4.isupper()
print("'ALLCAPS' all uppercase?", test4)