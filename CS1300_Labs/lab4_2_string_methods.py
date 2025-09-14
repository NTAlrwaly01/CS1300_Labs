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


# ================================
# Part 3: Finding and Counting
# ================================

# -------------------------------
# Exercise 3.1: Finding Substrings
# -------------------------------

text = "Python is awesome. Python is fun."

# Find first occurrence of "Python"
first_python = text.find("Python")
print("First 'Python' at position:", first_python)

# Find "is"
first_is = text.find("is")
print("First 'is' at position:", first_is)

# YOUR TURN: Find these
# Find "awesome"
pos_awesome = text.find("awesome")
print("'awesome' at position:", pos_awesome)

# Find "fun"
pos_fun = text.find("fun")
print("'fun' at position:", pos_fun)

# Find something that doesn't exist
pos_java = text.find("Java")
print("'Java' at position:", pos_java)  # Should be -1

# Count occurrences
count_python = text.count("Python")
print("\n'Python' appears:", count_python, "times")

# YOUR TURN: Count these
count_is = text.count("is")
print("'is' appears:", count_is, "times")

count_spaces = text.count(" ")
print("Spaces appear:", count_spaces, "times")


# -------------------------------
# Exercise 3.2: Checking Start and End
# -------------------------------

filename = "document.pdf"
website = "https://www.example.com"
email = "student@university.edu"

# Check file extension
is_pdf = filename.endswith(".pdf")
print("\nIs PDF?", is_pdf)

is_txt = filename.endswith(".txt")
print("Is TXT?", is_txt)

# YOUR TURN: Complete these checks
# Check if website starts with "https"
is_secure = website.startswith("https")
print("Is secure website?", is_secure)

# Check if website ends with ".com"
is_com = website.endswith(".com")
print("Is .com website?", is_com)

# Check if email ends with ".edu"
is_edu_email = email.endswith(".edu")
print("Is educational email?", is_edu_email)

# Check if email starts with "student"
is_student = email.startswith("student")
print("Is student email?", is_student)


# ================================
# Part 4: Modifying Strings
# ================================

# -------------------------------
# Exercise 4.1: Removing Whitespace
# -------------------------------

# Text with extra spaces
messy_text = " Hello World "
print("Original:", repr(messy_text))  # repr shows spaces clearly

# Remove spaces from both ends
cleaned = messy_text.strip()
print("Cleaned:", repr(cleaned))

# Remove from left only
left_cleaned = messy_text.lstrip()
print("Left cleaned:", repr(left_cleaned))

# Remove from right only
right_cleaned = messy_text.rstrip()
print("Right cleaned:", repr(right_cleaned))

# YOUR TURN: Clean these strings
text1 = " Python "
text2 = "\nHello\n"
text3 = "\t\tData\t\t"  # \n is newline, \t is tab

clean1 = text1.strip()
print("\nCleaned text1:", repr(clean1))

clean2 = text2.strip()
print("Cleaned text2:", repr(clean2))

clean3 = text3.strip()
print("Cleaned text3:", repr(clean3))


# -------------------------------
# Exercise 4.2: Replacing Text
# -------------------------------

sentence = "I like apples. Apples are healthy."

# Replace "apples" with "oranges"
new_sentence = sentence.replace("apples", "oranges")
print("\nModified:", new_sentence)

# Note: "Apples" wasn't replaced (case sensitive!)
# Replace both
fixed = sentence.replace("apples", "oranges").replace("Apples", "Oranges")
print("Fully fixed:", fixed)

# YOUR TURN: Make these replacements
text = "Hello World. World is beautiful."

# Replace "World" with "Python"
result1 = text.replace("World", "Python")
print("\nResult 1:", result1)

# Remove all spaces (replace with empty string)
result2 = text.replace(" ", "")
print("Result 2:", result2)

# Replace periods with exclamation marks
result3 = text.replace(".", "!")
print("Result 3:", result3)


# ================================
# Part 5: Splitting and Joining
# ================================

# -------------------------------
# Exercise 5.1: Splitting Strings
# -------------------------------

# Split sentence into words
sentence = "Python is a great language"
words = sentence.split()
print("Words:", words)
print("Number of words:", len(words))
print("First word:", words[0])
print("Last word:", words[-1])

# Split with specific separator
data = "apple,banana,orange"
fruits = data.split(",")
print("\nFruits:", fruits)

# YOUR TURN: Split these strings
email = "john.doe@example.com"
# Split at the @ symbol
email_parts = email.split("@")
print("\nEmail parts:", email_parts)

date = "2025-09-11"
# Split at the dash
date_parts = date.split("-")
print("Date parts:", date_parts)

path = "folder/subfolder/file.txt"
# Split at the forward slash
path_parts = path.split("/")
print("Path parts:", path_parts)


# -------------------------------
# Exercise 5.2: Joining Strings
# -------------------------------

# Join list of words into string
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print("\nSentence:", sentence)

# Join with different separators
items = ["apple", "banana", "orange"]
comma_list = ", ".join(items)
print("Comma list:", comma_list)

# YOUR TURN: Create these joined strings
names = ["John", "Jane", "Bob"]

# Join with " and "
result1 = " and ".join(names)
print("\nResult 1:", result1)

# Join with " - "
result2 = " - ".join(names)
print("Result 2:", result2)

# Join with no separator
result3 = "".join(names)
print("Result 3:", result3)

# Create a path from parts
folders = ["home", "user", "documents"]
path = "/".join(folders)
print("Path:", path)


# ================================
# Part 6: Putting It All Together
# ================================

# -------------------------------
# Exercise 6.1: Clean and Format Text
# -------------------------------

# Messy input
user_input = " hELLo WoRLd "

# Step 1: Remove extra spaces
step1 = user_input.strip()
print("Step 1 (stripped):", step1)

# Step 2: Convert to lowercase
step2 = step1.lower()
print("Step 2 (lowercase):", step2)

# Step 3: Capitalize first letter
step3 = step2.capitalize()
print("Step 3 (capitalized):", step3)

# All in one line
cleaned = user_input.strip().lower().capitalize()
print("All at once:", cleaned)

# YOUR TURN: Clean this text
messy = " pYTHon PROgramming "

# Step 1: Strip spaces
clean1 = messy.strip()

# Step 2: Convert to title case
clean2 = clean1.title()
print("\nCleaned:", clean2)

# Do it in one line
one_line = messy.strip().title()
print("One line:", one_line)


# -------------------------------
# Exercise 6.2: Process User Data
# -------------------------------

# Process a name
raw_name = " JOHN DOE "

# Clean and format
name = raw_name.strip().title()
print("\nFormatted name:", name)

# Create username (lowercase, no spaces)
username = name.lower().replace(" ", "")
print("Username:", username)

# Create email
email = username + "@company.com"
print("Email:", email)

# YOUR TURN: Process this data
raw_data = " jaNE SMITH "

# Format the name properly
formatted_name = raw_data.strip().title()
print("\nFormatted:", formatted_name)

# Create username (lowercase, replace space with dot)
user = formatted_name.lower().replace(" ", ".")
print("Username:", user)

# Check if it contains "smith"
has_smith = "smith" in user.lower()
print("Contains 'smith'?", has_smith)