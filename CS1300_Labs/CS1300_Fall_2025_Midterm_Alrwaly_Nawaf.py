# PROBLEM 1: String Manipulation 


print("=" * 60)
print("PROBLEM 1: STRING MANIPULATION")
print("=" * 60)

# Given information (DO NOT MODIFY)
full_name = "John Michael Smith"
email = "john.smith@university.edu"
phone = "555-123-4567"

# Task 1.1 (3 points): Extract and print the first name only
first_name = full_name.split()[0]
print(f"Task 1.1 - First name: {first_name}")

# Task 1.2 (3 points): Extract and print the last name only
last_name = full_name.split()[-1]
print(f"Task 1.2 - Last name: {last_name}")

# Task 1.3 (3 points): Create and print initials (J.M.S.)
name_parts = full_name.split()
initials = ".".join([part[0] for part in name_parts]) + "."
print(f"Task 1.3 - Initials: {initials}")

# Task 1.4 (3 points): Check if the email contains "university" (case-insensitive)
contains_university = "university" in email.lower()
print(f"Task 1.4 - Email contains 'university': {contains_university}")

# Task 1.5 (3 points): Replace all dashes in phone with spaces and print
phone_with_spaces = phone.replace("-", " ")
print(f"Task 1.5 - Phone with spaces: {phone_with_spaces}")

print()


# PROBLEM 2: Arithmetic and Conditionals


print("=" * 60)
print("PROBLEM 2: RESTAURANT RATING CALCULATOR")
print("=" * 60)

# Task 2.1 (3 points): Get these ratings
atmosphere = 4.5
food = 3.4
service = 2.5
cleanliness = 3.0

print(f"Task 2.1 - Ratings collected:")
print(f"  Atmosphere: {atmosphere}")
print(f"  Food: {food}")
print(f"  Service: {service}")
print(f"  Cleanliness: {cleanliness}")

# Task 2.2 (4 points): Calculate weighted average
# Weights: atmosphere=10%, food=45%, service=20%, cleanliness=25%
average = (atmosphere * 0.10 + food * 0.45 + service * 0.20 + cleanliness * 0.25)
print(f"Task 2.2 - Weighted average: {average:.2f}")

# Task 2.3 (8 points): Determine restaurant rating
# ****: 4.0 and above
# ***: 3.0-4.0
# **: 2.0-3.0
# *: 1.0-2.0
# *: below 1.0

if average >= 4.0:
    star_rating = "****"
elif average >= 3.0:
    star_rating = "***"
elif average >= 2.0:
    star_rating = "**"
elif average >= 1.0:
    star_rating = "*"
else:
    star_rating = "*"

print(f"Task 2.3 - Star rating: {star_rating}")
print(f"Restaurant rating: {average:.2f} ({star_rating})")

print()


# PROBLEM 3: List Operations


print("=" * 60)
print("PROBLEM 3: MOVIE REVIEW NUMBER MANAGEMENT")
print("=" * 60)

# Task 3.1 (2 points): Create a list with these movie review numbers
numbers = [3, 5, 4, 3, 2, 1, 3]
print(f"Task 3.1 - Initial list: {numbers}")

# Task 3.2 (3 points): Add a new review number of 4 to the end
numbers.append(4)
print(f"Task 3.2 - After adding 4: {numbers}")

# Task 3.3 (3 points): The third review number (4) was entered wrong. Change it to 3
numbers[2] = 3
print(f"Task 3.3 - After changing index 2 to 3: {numbers}")

# Task 3.4 (3 points): Remove the review number 1 from the list
numbers.remove(1)
print(f"Task 3.4 - After removing 1: {numbers}")

# Task 3.5 (3 points): Insert a review number of 3 at position 2
numbers.insert(2, 3)
print(f"Task 3.5 - After inserting 3 at position 2: {numbers}")

# Task 3.6 (3 points): Create and print a sublist of the first 3 numbers
first_three = numbers[0:3]
print(f"Task 3.6 - First 3 numbers: {first_three}")

# Task 3.7 (3 points): Print:
# - How many movie review numbers
# - The first review number
# - The last review number
print(f"Task 3.7:")
print(f"  Number of movie review numbers: {len(numbers)}")
print(f"  First review number: {numbers[0]}")
print(f"  Last review number: {numbers[-1]}")

print()


# PROBLEM 4: Shopping Cart System


print("=" * 60)
print("PROBLEM 4: SHOPPING CART SYSTEM")
print("=" * 60)

# Initial setup (DO NOT MODIFY)
items = ["bread", "milk", "eggs", "cheese", "apples"]
prices = [2.50, 3.99, 2.99, 5.49, 4.99]
cart = []
cart_total = 0.0

print("Available items:", items)
print("Prices:", prices)
print()

# Task 4.1 (4 points): Add "milk" to cart
item_to_add = "milk"
if item_to_add in items:
    item_index = items.index(item_to_add)
    cart.append(item_to_add)
    cart_total = cart_total + prices[item_index]
    print(f"Task 4.1 - Added '{item_to_add}' to cart")
    print(f"  Cart: {cart}")
    print(f"  Cart total: ${cart_total:.2f}")
else:
    print(f"Task 4.1 - '{item_to_add}' not available")

# Task 4.2 (4 points): Add "eggs" to cart
item_to_add = "eggs"
if item_to_add in items:
    item_index = items.index(item_to_add)
    cart.append(item_to_add)
    cart_total = cart_total + prices[item_index]
    print(f"Task 4.2 - Added '{item_to_add}' to cart")
    print(f"  Cart: {cart}")
    print(f"  Cart total: ${cart_total:.2f}")
else:
    print(f"Task 4.2 - '{item_to_add}' not available")

# Task 4.3 (4 points): Try to add "cookies" to cart
item_to_add = "cookies"
if item_to_add in items:
    item_index = items.index(item_to_add)
    cart.append(item_to_add)
    cart_total = cart_total + prices[item_index]
    print(f"Task 4.3 - Added '{item_to_add}' to cart")
else:
    print(f"Task 4.3 - '{item_to_add}' is not available")

print(f"  Cart: {cart}")
print(f"  Cart total: ${cart_total:.2f}")

# Task 4.4 (4 points): Apply discount
original_total = cart_total
if cart_total > 6.00:
    cart_total = cart_total * 0.90
    print(f"Task 4.4 - Discount applied!")
    print(f"  Original total: ${original_total:.2f}")
    print(f"  Discounted total: ${cart_total:.2f}")
else:
    print(f"Task 4.4 - No discount applied (total not > $6.00)")

# Task 4.5 (4 points): Final report
print(f"\nTask 4.5 - Final Report:")
print(f"  Items in cart: {cart}")
print(f"  Number of items: {len(cart)}")
if cart_total < original_total:
    print(f"  Final total (with discount): ${cart_total:.2f}")
else:
    print(f"  Final total: ${cart_total:.2f}")

print()
print("=" * 60)
print("ALL PROBLEMS COMPLETED")
print("=" * 60)
