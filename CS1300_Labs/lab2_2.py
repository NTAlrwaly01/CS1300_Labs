# lab2_2.py
# Week 2 Session 2 Lab - Input/Output Practice
# Nawaf T Alrwaly
# 2025-09-01


print("=" * 50)
print(" Week 2 Session 2 Lab - Input/Output Practice ")
print("=" * 50)


# ==================Part 1: Type Conversion =======================
print("\n----- Problem 1: Age Calculator -----")
year_of_birth = int(input("Enter year of birth: "))
age = 2024 - year_of_birth
print(f"you are {age} years old!")

print("\n------- Problem 2: Temperature Converter -----")
celsius = float(input(" Enter Temperature in Celsius: "))
farhrenheit = celsius * 9/5 + 32
print(f"{celsius: .1f}°C = {farhrenheit: .1f}°F")

print("\n------ Problem 3: Rectangle Measurement ------")
length = float(input(" Enter the lenght :"))
width = float(input("Enter the width : "))
area_of_rectangle = length * width
perimeter_of_retangle = 2 * (length + width)
print(f"The area of rectangle = {area_of_rectangle: .2f}, The perimeter of rectangle = {perimeter_of_retangle: .2f}")

print("\n------ Problem 4: Bill Calculator ------")
cost_of_meal = float(input("Enter your total cost of the meal : $"))
preferred_tip_percentage = float(input("Enter your preferred tip percentage : "))
tip_amount = cost_of_meal * (preferred_tip_percentage / 100)
total_bill = cost_of_meal + tip_amount
print(f"Meal: ${cost_of_meal: .2f}, Tip: ${tip_amount: .2f}, Total: ${total_bill: .2f}")


# ==================== Part 2: Print Function ====================
print("\n------ Problem 5: Student Info Display -------")
student_name = input("please enter name : ")
student_age = int(input("Please enter age :"))
student_major = input("Please enter major : ")
print(student_name, student_age, student_major) # default spacing
print(student_name, student_age, student_major, sep=", ") # comma separation
print(student_name, student_age, student_major, sep=" | ") # pipe separation


print("\n----- Problem 6: Progress Indicator -----")
print("Processing", end ="")
for _ in range(5):
    print(".", end ="")
print(" Complete! ")

print("\n----- Problem 7: Data Table Header ------")
print("=" * 40)
print("Name", "Score", "Grade" , sep="\t")
print("=" * 40)

name_of_student = input("Enter student name: ")
score = int(input("Enter score: "))
grade = input("Enter grade: ")
print(name_of_student, score, grade, sep="\t")


print("\n--- Problem 8: Message Box ---")
message = input("Enter a short message: ")
print("+" + "-" * 30 + "+")
print(f"| {message:<28} |")  # left-aligned inside box
print("+" + "-" * 30 + "+")

# ================ PART 3: F-STRING FORMATTING ====================
print("\n--- Problem 9: Price Display ---")
item = input("Enter item name: ")
price = float(input("Enter price: "))
print(f"{item:<10} ${price:>6.2f}")

print("\n--- Problem 10: Percentage Calculator ---")
earned = float(input("Enter earned points: "))
total_points = float(input("Enter total points: "))
percentage = (earned / total_points) * 100
print(f"Score: {earned:.0f}/{total_points:.0f} = {percentage:.1f}%")

print("\n--- Problem 11: Receipt Line Item ---")
product = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))
total_price = quantity * unit_price
print(f"{product:<20}{quantity:^10}{'$'+format(total_price, '.2f'):>10}")

print("\n--- Problem 12: ID Formatter ---")
number = int(input("Enter a number: "))
print(f"4-digit: {number:04d}")
print(f"6-digit: {number:06d}")
print(f"8-digit: {number:08d}")

print("\n" + "=" * 50)
print("LAB COMPLETED!")
print("=" * 50)