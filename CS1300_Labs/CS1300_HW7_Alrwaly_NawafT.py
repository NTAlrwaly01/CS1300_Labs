# CS1300 Homework #7
# Author: Nawaf T Alrwaly
# Course: CS1300 - Introduction to Programming
# Topic: Loops Part 1 (for, while, break, continue)
# Date: November 3, 2025


# Problem 1: Temperature Analyzer

temperatures = [72, 68, 75, 71, 69, 77, 74, 70, 73, 76]

print("Temperature Analysis Report")
print("===========================")

# init tracking variables
total = 0
highest = temperatures[0]
lowest = temperatures[0]
above_72 = 0

# Iterate through temperatures
for i, temp in enumerate(temperatures):
    total += temp
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp
    if temp > 72:
        above_72 += 1

    celsius = (temp - 32) * 5 / 9
    print(f"Day {i + 1}: {temp}°F ({round(celsius, 1)}°C)")

# average temperature
average = total / len(temperatures)

# Print statistical summary
print("\nStatistics:")
print(f"Average Temperature: {round(average, 1)}°F")
print(f"Highest Temperature: {highest}°F")
print(f"Lowest Temperature: {lowest}°F")
print(f"Days Above 72°F: {above_72} days\n")


# Problem 2: Number Guessing Game

import random

print("=== NUMBER GUESSING GAME ===")
print("I'm thinking of a number between 1 and 20.")
print("You have 5 guesses!")

secret = random.randint(1, 20)
guesses = []

# Player: 5 attempts
for attempt in range(1, 6):
    guess = int(input(f"Guess {attempt}: "))
    guesses.append(guess)

    if guess == secret:
        print(f"Correct! You got it in {attempt} guesses!")

        # Feedback based on number of attempts
        if attempt == 1:
            print("Amazing! You're a mind reader!")
        elif attempt <= 3:
            print("Great job!")
        else:
            print("Good work!")
        break

    elif guess < secret:
        print("Too low! Try higher.")
    else:
        print("Too high! Try lower.")


else:
    print("Sorry! You've run out of guesses.")
    print(f"The number was {secret}.")
    print("Better luck next time!")

# Show player guesses
print(f"Your guesses were: {guesses}\n")


# Problem 3: Grade Processor

grades = [85, -10, 92, 150, 78, 0, 95, 88, -5, 100, 73, 200]

print("Processing Grades...")
print("===================")

# Initialize counters
valid_grades = []
invalid_count = 0
a_count = b_count = c_count = d_count = f_count = 0

# Iterate through all grades
for grade in grades:
    # Validate grade 
    if grade < 0 or grade > 100:
        print(f"Skipping invalid grade: {grade}")
        invalid_count += 1
        continue

    valid_grades.append(grade)

    # Assign grades
    if grade >= 90:
        letter = "A"
        a_count += 1
    elif grade >= 80:
        letter = "B"
        b_count += 1
    elif grade >= 70:
        letter = "C"
        c_count += 1
    elif grade >= 60:
        letter = "D"
        d_count += 1
    else:
        letter = "F"
        f_count += 1

    print(f"Grade {len(valid_grades)}: {grade} ({letter})")

# Compute average 
if len(valid_grades) > 0:
    avg = sum(valid_grades) / len(valid_grades)
else:
    avg = 0

# Display summary report
print("\nSummary Report")
print("==============")
print(f"Total grades processed: {len(valid_grades)}")
print(f"Invalid grades skipped: {invalid_count}")
print("\nGrade Distribution:")
print(f"A: {a_count} students")
print(f"B: {b_count} students")
print(f"C: {c_count} students")
print(f"D: {d_count} students")
print(f"F: {f_count} students")
print(f"Class Average: {round(avg, 1)}")