# CS 1300 - Homework 2
# Name: Nawaf T Alrwaly
# Date: 09/12/2025
# Description: Variables, Input/Output, and Type Conversions

print("=" * 50)
print("CS 1300 - HOMEWORK 2")
print("=" * 50)

# ============ Problem 1: Personal Finance Calculator ============
print("\n" + "=" * 40)
print("Problem 1: Personal Finance Calculator")
print("=" * 40)

print("=" * 40)
print("PERSONAL FINANCE CALCULATOR")
print("=" * 40)

# Get user input and convert to float
monthly_income = float(input("Enter your monthly income: "))
housing_cost = float(input("Enter housing/rent cost: "))
food_expenses = float(input("Enter food expenses: "))
transportation_cost = float(input("Enter transportation cost: "))
other_expenses = float(input("Enter other expenses: "))

# Perform calculations using compound operators where appropriate
total_expenses = 0.0
total_expenses += housing_cost
total_expenses += food_expenses
total_expenses += transportation_cost
total_expenses += other_expenses

remaining_balance = monthly_income - total_expenses
savings_rate = remaining_balance / monthly_income

# Display formatted budget report
print("=" * 40)
print("MONTHLY BUDGET REPORT")
print("=" * 40)
print(f"Income: $ {monthly_income:.2f}")
print("-" * 40)
print("Expenses:")
print(f"Housing: $ {housing_cost:.2f}")
print(f"Food: $ {food_expenses:.2f}")
print(f"Transportation: $ {transportation_cost:.2f}")
print(f"Other: $ {other_expenses:.2f}")
print("-" * 40)
print(f"Total Expenses: $ {total_expenses:.2f}")
print(f"Remaining Balance: $ {remaining_balance:.2f}")
print(f"Savings Rate: {savings_rate:.1%}")
print("=" * 40)

# ============ Problem 2: Grade Statistics Calculator ============
print("\n" + "=" * 40)
print("Problem 2: Grade Statistics Calculator")
print("=" * 40)

print("*" * 40)
print("GRADE STATISTICS CALCULATOR")
print("*" * 40)

# Collect test scores using descriptive variable names
score1 = float(input("Enter score for Test 1 (out of 100): "))
score2 = float(input("Enter score for Test 2 (out of 100): "))
score3 = float(input("Enter score for Test 3 (out of 100): "))
score4 = float(input("Enter score for Test 4 (out of 100): "))
score5 = float(input("Enter score for Test 5 (out of 100): "))

# Calculate statistics step by step
total_points = 0.0
total_points += score1
total_points += score2
total_points += score3
total_points += score4
total_points += score5

average_score = total_points / 5
highest_possible = 500
overall_percentage = (total_points / highest_possible) * 100

# Calculate points needed for 90%
target_percentage = 0.90
points_needed_90 = (highest_possible * target_percentage) - total_points

print("*" * 40)
print("GRADE REPORT")
print("*" * 40)
print("Test Scores Entered:")
print(f"Test 1: {score1:.1f}/100")
print(f"Test 2: {score2:.1f}/100")
print(f"Test 3: {score3:.1f}/100")
print(f"Test 4: {score4:.1f}/100")
print(f"Test 5: {score5:.1f}/100")
print("*" * 40)
print("Statistics:")
print(f"Total Points: {total_points:.1f}/{highest_possible}")
print(f"Average Score: {average_score:.1f}")
print(f"Overall Grade: {overall_percentage:.1f}%")
print(f"Points needed for 90%: {points_needed_90:.1f}")
print("*" * 40)

# ============ Problem 3: Time Zone Converter ============
print("\n" + "=" * 40)
print("Problem 3: Time Zone Converter")
print("=" * 40)

print("+" + "-" * 38 + "+")
print("|" + " TIME ZONE CONVERTER ".center(38) + "|")
print("+" + "-" * 38 + "+")

# Get current time input
current_hour = int(input("Enter current hour (EST, 0-23): "))
current_minute = int(input("Enter current minute (0-59): "))

# Calculate time zones using modulo for wraparound
est_hour = current_hour
cst_hour = (current_hour - 1) % 24
mst_hour = (current_hour - 2) % 24  
pst_hour = (current_hour - 3) % 24

# Convert each time zone to 12-hour format
# EST conversion
if est_hour == 0:
    est_display_hour = 12
    est_ampm = "AM"
elif est_hour < 12:
    est_display_hour = est_hour
    est_ampm = "AM"
elif est_hour == 12:
    est_display_hour = 12
    est_ampm = "PM"
else:
    est_display_hour = est_hour - 12
    est_ampm = "PM"

# CST conversion
if cst_hour == 0:
    cst_display_hour = 12
    cst_ampm = "AM"
elif cst_hour < 12:
    cst_display_hour = cst_hour
    cst_ampm = "AM"
elif cst_hour == 12:
    cst_display_hour = 12
    cst_ampm = "PM"
else:
    cst_display_hour = cst_hour - 12
    cst_ampm = "PM"

# MST conversion
if mst_hour == 0:
    mst_display_hour = 12
    mst_ampm = "AM"
elif mst_hour < 12:
    mst_display_hour = mst_hour
    mst_ampm = "AM"
elif mst_hour == 12:
    mst_display_hour = 12
    mst_ampm = "PM"
else:
    mst_display_hour = mst_hour - 12
    mst_ampm = "PM"

# PST conversion
if pst_hour == 0:
    pst_display_hour = 12
    pst_ampm = "AM"
elif pst_hour < 12:
    pst_display_hour = pst_hour
    pst_ampm = "AM"
elif pst_hour == 12:
    pst_display_hour = 12
    pst_ampm = "PM"
else:
    pst_display_hour = pst_hour - 12
    pst_ampm = "PM"

# Display formatted time table
print("+" + "-" * 38 + "+")
print("|" + " CURRENT TIMES ".center(38) + "|")
print("+" + "-" * 38 + "+")
print("| Time Zone | Time     | 12-hr Format|")
print("|-----------|----------|-------------|")
print(f"| EST       | {est_hour:2d}:{current_minute:02d}     | {est_display_hour:2d}:{current_minute:02d} {est_ampm}  |")
print(f"| CST       | {cst_hour:2d}:{current_minute:02d}     | {cst_display_hour:2d}:{current_minute:02d} {cst_ampm}  |")
print(f"| MST       | {mst_hour:2d}:{current_minute:02d}     | {mst_display_hour:2d}:{current_minute:02d} {mst_ampm}  |")
print(f"| PST       | {pst_hour:2d}:{current_minute:02d}     | {pst_display_hour:2d}:{current_minute:02d} {pst_ampm}  |")
print("+" + "-" * 38 + "+")

# ============ Problem 4: Recipe Scaler ============
print("\n" + "=" * 40)
print("Problem 4: Recipe Scaler")
print("=" * 40)

print("#" * 48)
print("RECIPE SCALER")
print("#" * 48)

# Get serving size information
original_servings = int(input("Enter original serving size: "))
desired_servings = int(input("Enter desired serving size: "))

print("Enter 5 ingredients:")

# Collect ingredient information
ingredient1_name = input("Ingredient 1 name: ")
ingredient1_amount = float(input("Amount: "))
ingredient1_unit = input("Unit: ")

ingredient2_name = input("Ingredient 2 name: ")
ingredient2_amount = float(input("Amount: "))
ingredient2_unit = input("Unit: ")

ingredient3_name = input("Ingredient 3 name: ")
ingredient3_amount = float(input("Amount: "))
ingredient3_unit = input("Unit: ")

ingredient4_name = input("Ingredient 4 name: ")
ingredient4_amount = float(input("Amount: "))
ingredient4_unit = input("Unit: ")

ingredient5_name = input("Ingredient 5 name: ")
ingredient5_amount = float(input("Amount: "))
ingredient5_unit = input("Unit: ")

# Calculate scaling factor
scaling_factor = desired_servings / original_servings

# Scale each ingredient amount
scaled1_amount = ingredient1_amount * scaling_factor
scaled2_amount = ingredient2_amount * scaling_factor
scaled3_amount = ingredient3_amount * scaling_factor
scaled4_amount = ingredient4_amount * scaling_factor
scaled5_amount = ingredient5_amount * scaling_factor

# Display results in formatted table
print("#" * 48)
print("RECIPE SCALING RESULTS")
print("#" * 48)
print(f"Scaling factor: {scaling_factor:.2f}x ({original_servings} → {desired_servings} servings)")
print("-" * 48)
print(f"Original Recipe ({original_servings} servings) | Scaled Recipe ({desired_servings} servings)")
print("-" * 29 + "|" + "-" * 18)
print(f"{ingredient1_name}: {ingredient1_amount:.2f} {ingredient1_unit:<10} | {ingredient1_name}: {scaled1_amount:.2f} {ingredient1_unit}")
print(f"{ingredient2_name}: {ingredient2_amount:.2f} {ingredient2_unit:<10} | {ingredient2_name}: {scaled2_amount:.2f} {ingredient2_unit}")
print(f"{ingredient3_name}: {ingredient3_amount:.2f} {ingredient3_unit:<10} | {ingredient3_name}: {scaled3_amount:.2f} {ingredient3_unit}")
print(f"{ingredient4_name}: {ingredient4_amount:.2f} {ingredient4_unit:<10} | {ingredient4_name}: {scaled4_amount:.2f} {ingredient4_unit}")
print(f"{ingredient5_name}: {ingredient5_amount:.2f} {ingredient5_unit:<10} | {ingredient5_name}: {scaled5_amount:.2f} {ingredient5_unit}")
print("#" * 48)

print("\n" + "=" * 50)
print("END OF HOMEWORK 2")
print("=" * 50)