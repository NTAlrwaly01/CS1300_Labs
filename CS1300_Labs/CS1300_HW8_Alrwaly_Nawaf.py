# CS1300_HW8_Alrwaly_Nawaf.py
# Author: Nawaf T. Alrwaly
# Date: November 7, 2025


# Problem 1: Multiplication Table Generator

# input table size with validation
while True:
    try:
        size = int(input("Enter table size (1-12): "))
        if 1 <= size <= 12:
            break
        else:
            print("Invalid! Please enter a number between 1 and 12.")
    except ValueError:
        print("Please enter a valid integer between 1 and 12.")

print(f"\nMULTIPLICATION TABLE ({size}x{size})")
print("=" * (size * 4))

# Header row
print("    ", end="")
for i in range(1, size + 1):
    print(f"{i:4}", end="")
print("\n" + "-" * (size * 4 + 4))

#loops for rows and columns
for i in range(1, size + 1):
    print(f"{i:2} |", end="")
    for j in range(1, size + 1):
        print(f"{i * j:4}", end="")
    print() 


# Problem 2: Pattern Detective

# Analyze and apply multiple iteration patterns

numbers = [23, 8, 45, 12, 78, 34, 67, 91, 15, 52, 41, 3]
print("\n=== PATTERN ANALYSIS ===")
print("Original numbers:", numbers)

# SEARCH PATTERN: Find first number > 75
for index, num in enumerate(numbers):
    if num > 75:
        print(f"\n1. SEARCH PATTERN\nFirst number > 75: {num} (at position {index + 1})")
        break

# FILTER PATTERN: Get all even numbers
even_numbers = [n for n in numbers if n % 2 == 0]
print("\n2. FILTER PATTERN\nEven numbers:", even_numbers)

# COUNTER PATTERN: Count numbers in different ranges
ranges = {"0-25": 0, "26-50": 0, "51-75": 0, "76-100": 0}
for num in numbers:
    if 0 <= num <= 25:
        ranges["0-25"] += 1
    elif 26 <= num <= 50:
        ranges["26-50"] += 1
    elif 51 <= num <= 75:
        ranges["51-75"] += 1
    elif 76 <= num <= 100:
        ranges["76-100"] += 1

print("\n3. COUNTER PATTERN")
for k, v in ranges.items():
    print(f"Range {k}: {v} numbers")

# ACCUMULATOR PATTERN: Sum numbers divisible by 3
div_by_3 = []
sum_div_3 = 0
for n in numbers:
    if n % 3 == 0:
        div_by_3.append(n)
        sum_div_3 += n
print("\n4. ACCUMULATOR PATTERN")
print(f"Numbers divisible by 3: {div_by_3}")
print(f"Sum of these numbers: {sum_div_3}")

# SENTINEL PATTERN: Add numbers until user enters -1
print("\n5. SENTINEL PATTERN")
print("Add more numbers (enter -1 to stop):")
while True:
    try:
        new_number = int(input("Enter number: "))
        if new_number == -1:
            break
        numbers.append(new_number)
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("Updated list:", numbers)
print(f"New count: {len(numbers)} numbers")


# Problem 3: Grade Report Generator

# Using nested loops and iteration patterns for grade analysis

students = ["Alice", "Bob", "Carol", "David", "Emma"]
assignments = ["HW1", "HW2", "Quiz1", "Exam1", "Quiz2"]
grades = [
    [92, 88, 95, 87, 90],
    [78, 82, 73, 85, 80],
    [95, 91, 98, 92, 94],
    [65, 70, 68, 72, 75],
    [88, 85, 82, 90, 87]
]

print("\n=== GRADE REPORT SYSTEM ===")
print("Grade Table:\nHW1  HW2  Quiz1 Exam1 Quiz2   AVG   Grade")
print("-" * 55)

student_averages = []
for i in range(len(students)):
    total = 0
    for j in range(len(assignments)):
        total += grades[i][j]
        print(f"{grades[i][j]:5}", end="")
    avg = total / len(assignments)
    student_averages.append(avg)
    if avg >= 90:
        letter = "A"
    elif avg >= 80:
        letter = "B"
    elif avg >= 70:
        letter = "C"
    elif avg >= 60:
        letter = "D"
    else:
        letter = "F"
    print(f"{avg:8.1f} {letter:>3}")

# Assignment Statistics
print("\nAssignment Statistics:")
for j in range(len(assignments)):
    col = [grades[i][j] for i in range(len(students))]
    avg = sum(col) / len(col)
    high = max(col)
    low = min(col)
    high_student = students[col.index(high)]
    low_student = students[col.index(low)]
    print(f"{assignments[j]}: Avg: {avg:.1f} | High: {high} ({high_student}) | Low: {low} ({low_student})")

# Honor Roll and Warnings
honor = [students[i] for i in range(len(students)) if student_averages[i] >= 90]
warning = [students[i] for i in range(len(students)) if student_averages[i] < 70]
print("\nHonor Roll:", ", ".join(honor) if honor else "None")
print("Academic Warning:", ", ".join(warning) if warning else "None")

# Class Summary
overall_avg = sum(student_averages) / len(student_averages)
top_student = students[student_averages.index(max(student_averages))]
low_student = students[student_averages.index(min(student_averages))]
print(f"\nClass Average: {overall_avg:.1f}%")
print(f"Highest Overall: {top_student} ({max(student_averages):.1f}%)")
print(f"Lowest Overall: {low_student} ({min(student_averages):.1f}%)")



# --------------------------------
# BONUS CHALLENGE: Pattern Printer
# --------------------------------

def print_diamond(rows=5):
    """Prints a diamond pattern using nested loops"""
    print("\nPattern 1: Diamond\n")
    # Upper half
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)
    # Lower half
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "* " * i)


def print_hollow_square(size=5):
    """Prints a hollow square pattern"""
    print("\nPattern 2: Hollow Square\n")
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()


def print_number_pyramid(rows=5):
    """Prints a number pyramid pattern"""
    print("\nPattern 3: Number Pyramid\n")
    for i in range(1, rows + 1):
        print((str(i) + " ") * i)


# User Menu 
print("\n=== BONUS CHALLENGE: ADVANCED PATTERN PRINTER ===")
print("Choose a pattern to display:")
print("1. Diamond")
print("2. Hollow Square")
print("3. Number Pyramid")
print("4. Display All")
print("5. Exit")

while True:
    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        print_diamond()
    elif choice == "2":
        print_hollow_square()
    elif choice == "3":
        print_number_pyramid()
    elif choice == "4":
        print_diamond()
        print_hollow_square()
        print_number_pyramid()
    elif choice == "5":
        print("\nExiting Pattern Printer. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")