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