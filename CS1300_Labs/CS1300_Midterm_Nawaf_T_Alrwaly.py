"""
CS 1300 - Midterm Examination (Mock)
Name: Nawaf T. Alrwaly
Date: October 6, 2025
Description: Midterm programming problems — String & List Operations
"""

print("="*60)
print("PART 2: PROGRAMMING EXAMINATION")
print("="*60)

# --------------------------------------------------------
# Problem 1: Student ID Processing
# --------------------------------------------------------

print("\n=== Problem 1: Student ID Processing ===")

# Given information
student_id = "2025-CS-0342"
student_email = "SMITH.JANE@SCHOOL.EDU"
course_code = "CS1300-001"

# Task 1.1: Extract the year (indices 0–4)
year = student_id[0:4]
print("Year:", year)

# Task 1.2: Extract student number (last 4 digits)
student_number = student_id[-4:]
print("Student Number:", student_number)

# Task 1.3: Convert email to lowercase and extract username before "@"
email_lower = student_email.lower()
username = email_lower.split("@")[0]
print("Username:", username)

# Task 1.4: Check if course_code starts with "CS"
is_cs_course = course_code.startswith("CS")
print("Is CS course?:", is_cs_course)

# Task 1.5: Create new ID format "year_number"
new_id = year + "_" + student_number
print("New ID format:", new_id)

# --------------------------------------------------------
# Problem 2: Restaurant Bill Calculator
# --------------------------------------------------------

print("\n=== Problem 2: Restaurant Bill Calculator ===")

food_total = 45.50
drinks_total = 18.75
dessert_total = 12.25

# Subtotal and tax
subtotal = food_total + drinks_total + dessert_total
tax = subtotal * 0.08
total_with_tax = subtotal + tax

# Tip calculation
if total_with_tax >= 50:
    tip = total_with_tax * 0.20
elif total_with_tax >= 30:
    tip = total_with_tax * 0.18
elif total_with_tax >= 15:
    tip = total_with_tax * 0.15
else:
    tip = total_with_tax * 0.10

final_total = total_with_tax + tip

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Final Total: ${final_total:.2f}")

# --------------------------------------------------------
# Problem 3: Product Inventory
# --------------------------------------------------------

print("\n=== Problem 3: Product Inventory ===")

products = ["laptop", "mouse", "keyboard", "monitor", "cable"]

# Add "headphones" to end
products.append("headphones")

# Insert "webcam" at position 3
products.insert(3, "webcam")

# Remove "cable"
products.remove("cable")

# Replace "mouse" with "wireless mouse"
mouse_index = products.index("mouse")
products[mouse_index] = "wireless mouse"

# Last three items
last_three = products[-3:]

# Display results
print("Updated Inventory:", products)
print("Last 3 Items:", last_three)
print("Total Products:", len(products))
print("First Alphabetically:", sorted(products)[0])
print("Even Index Products:", products[::2])

# --------------------------------------------------------
# Problem 4: Gym Membership Calculator
# --------------------------------------------------------

print("\n=== Problem 4: Gym Membership Calculator ===")

membership_types = ["basic", "standard", "premium", "vip"]
monthly_prices = [29.99, 49.99, 79.99, 99.99]

selected_plan = []
total_cost = 0

# Select "standard" plan
if "standard" in membership_types:
    index = membership_types.index("standard")
    selected_plan.append("standard")
    total_cost = monthly_prices[index] * 3
print("Standard 3-month cost:", total_cost)

# Try adding yoga class
if "yoga" in membership_types:
    print("Yoga added.")
else:
    print("Yoga not available.")

# Upgrade to "premium"
selected_plan.clear()
selected_plan.append("premium")
index = membership_types.index("premium")
total_cost = monthly_prices[index] * 3
print("Premium 3-month cost:", total_cost)

# Apply discounts
if total_cost >= 200:
    discount = total_cost * 0.15
elif total_cost >= 150:
    discount = total_cost * 0.10
else:
    discount = 0

final_cost = total_cost - discount
print(f"Original cost: ${total_cost:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Final cost after discount: ${final_cost:.2f}")

# Summary
print("\nMembership Summary:")
print(f"Selected Plan: {selected_plan[0]}")
print("Months: 3")
print(f"Final Total: ${final_cost:.2f}")

# --------------------------------------------------------
# BONUS: Library Book System
# --------------------------------------------------------

print("\n=== BONUS: Library Book System ===")

all_books = ["Python", "Java", "HTML", "CSS", "JavaScript", "SQL", "Ruby"]
borrowed = ["Java", "CSS", "Ruby"]

# Available books
available = ["Python", "HTML", "JavaScript", "SQL"]

# Patron returns "Java" and borrows "Python"
borrowed.remove("Java")
borrowed.append("Python")
available = ["HTML", "JavaScript", "SQL", "Java"]

# Status Report
print("\nStatus Report:")
print("Python: Borrowed")
print("Java: Available")
print("HTML: Available")
print("CSS: Borrowed")
print("JavaScript: Available")
print("SQL: Available")
print("Ruby: Borrowed")