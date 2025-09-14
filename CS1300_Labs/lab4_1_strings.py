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
print("\n--- Exercise 1.2: String Length ---")

# Built-in len() function
word1 = "Python"
word2 = "Data Science"
word3 = "   Spaces   "

print(f"Length of '{word1}':", len(word1))
print(f"Length of '{word2}':", len(word2))
print(f"Length of '{word3}':", len(word3))  # counts spaces too

# Task: Try with your own name
my_name = "Nawaf T Alrwaly"
print(f"Length of my name ('{my_name}'):", len(my_name))

