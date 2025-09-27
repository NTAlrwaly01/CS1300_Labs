"""
CS1300 - Homework 4: Decision Structures I
Name: Nawaf T Alrwaly
Date: 2025-09-15
Description: Programs using conditional statements for decision-making
"""

# ----------------------------------------
# Helpful imports
# ----------------------------------------
from typing import Optional

# ----------------------------------------
# Problem 1
# Temperature Converter & Weather Advisor
# ----------------------------------------
def problem1_temperature_converter():
    print("\n=== PROBLEM 1: Temperature Converter & Weather Advisor ===")
    try:
        temp = float(input("Enter temperature: ").strip())
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    scale = input("Is this Celsius or Fahrenheit? (C/F): ").strip().upper()
    if not scale:
        print("No scale entered. Please enter 'C' or 'F'.")
        return

    if scale == 'C':
        # C -> F
        f = (temp * 9/5) + 32
        c = temp
        print(f"{c:.1f}°C = {f:.1f}°F")
    elif scale == 'F':
        # F -> C
        c = (temp - 32) * 5/9
        f = temp
        print(f"{f:.1f}°F = {c:.1f}°C")
    else:
        print("Scale not recognized. Please enter 'C' or 'F'.")
        return

    # Weather advice based on Fahrenheit
    # Ranges: below 32, 32-50, 50-70, 70-85, above 85
    if f < 32:
        advice = "Freezing! Bundle up warmly!"
    elif 32 <= f <= 50:
        advice = "Cold - wear a warm jacket"
    elif 50 < f <= 70:
        advice = "Cool - a light jacket would be nice"
    elif 70 < f <= 85:
        advice = "Pleasant - enjoy the weather!"
    else:
        advice = "Hot - stay hydrated!"

    print(advice)


# ----------------------------------------
# Problem 2
# Movie Ticket Pricing System
# ----------------------------------------
def problem2_movie_tickets():
    print("\n=== PROBLEM 2: Movie Theater Ticket System ===")
    try:
        age = int(input("Enter customer age: ").strip())
    except ValueError:
        print("Invalid age. Please enter an integer.")
        return

    day = input("Enter day of week: ").strip().lower()

    # Tuesday special check (highest priority)
    if day == "tuesday":
        price = 7.00
        print(f"Your ticket price: ${price:.2f} (Tuesday Special!)")
        return

    # Not Tuesday: ask for show time
    try:
        show_time = int(input("Enter show time (0-23): ").strip())
        if show_time < 0 or show_time > 23:
            print("Show time out of range (0-23). Assuming no matinee discount.")
            show_time = None
    except ValueError:
        print("Invalid show time input. Assuming no matinee discount.")
        show_time = None

    # Base price by age
    if age <= 12:
        base = 8.0
        age_tag = "Child"
    elif age >= 65:
        base = 10.0
        age_tag = "Senior"
    else:
        base = 15.0
        age_tag = "Regular"

    # Matinee discount before 17:00
    matinee = (show_time is not None and show_time < 17)
    price = base
    if matinee:
        price -= 3.0

    # Build descriptive tag
    tag_parts = []
    if matinee:
        tag_parts.append("Matinee")
    tag_parts.insert(0, age_tag)  # e.g. "Senior Matinee" or "Regular"
    tag = " ".join(tag_parts)

    print(f"Your ticket price: ${price:.2f} ({tag})")


# ----------------------------------------
# Problem 3
# Grade Calculator with Letter Grade
# ----------------------------------------
def problem3_grade_calculator():
    print("\n=== PROBLEM 3: Grade Calculator ===")
    try:
        test1 = float(input("Enter Test 1 score (0-100): ").strip())
        test2 = float(input("Enter Test 2 score (0-100): ").strip())
        test3 = float(input("Enter Test 3 score (0-100): ").strip())
    except ValueError:
        print("Invalid input. Please enter numeric test scores.")
        return

    # Validate
    for i, s in enumerate((test1, test2, test3), start=1):
        if s < 0 or s > 100:
            print(f"Error: Test {i} score {s} is out of range (0-100).")
            return

    avg = (test1 + test2 + test3) / 3.0
    # Determine letter grade
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

    # Passing criteria: letter D or better AND at least one test >= 60
    has_one_ge_60 = max(test1, test2, test3) >= 60
    passes_letter = letter != "F"
    passing = passes_letter and has_one_ge_60

    print(f"Average: {avg:.2f}")
    print(f"Letter Grade: {letter}")
    print("Status:", "PASSING" if passing else "FAILING")


# ----------------------------------------
# Problem 4
# Password Strength Checker
# ----------------------------------------
def problem4_password_strength():
    print("\n=== PROBLEM 4: Password Strength Checker ===")
    password = input("Enter a password to check: ")

    # Criteria checks
    criteria_met = 0
    feedback = []

    # Criterion 1: length at least 8
    if len(password) >= 8:
        criteria_met += 1
    else:
        feedback.append(f"- Password should be at least 8 characters (currently {len(password)})")

    # Criterion 2: at least one uppercase
    has_upper = any(ch.isupper() for ch in password)
    if has_upper:
        criteria_met += 1
    else:
        feedback.append("- Add at least one uppercase letter")

    # Criterion 3: at least one lowercase
    has_lower = any(ch.islower() for ch in password)
    if has_lower:
        criteria_met += 1
    else:
        feedback.append("- Add at least one lowercase letter")

    # Criterion 4: at least one digit
    has_digit = any(ch.isdigit() for ch in password)
    if has_digit:
        criteria_met += 1
    else:
        feedback.append("- Add at least one digit")

    # Criterion 5: not a common password
    common_passwords = {"password", "12345678", "qwerty", "123456", "letmein"}
    if password.lower() not in common_passwords:
        criteria_met += 1
    else:
        feedback.append("- Password is a common insecure password; choose something else")

    # Strength level
    if criteria_met <= 2:
        strength = "WEAK"
    elif criteria_met == 3:
        strength = "FAIR"
    elif criteria_met == 4:
        strength = "GOOD"
    else:  # 5
        strength = "STRONG"

    print(f"Password Strength: {strength}")
    print(f"Criteria met: {criteria_met} out of 5")
    if feedback:
        print("Issues to improve:")
        for item in feedback:
            print(item)
    else:
        print("No issues found. Nice password!")


# ----------------------------------------
# Problem 5 (Bonus)
# Restaurant Bill Calculator
# ----------------------------------------
def problem5_restaurant_bill():
    print("\n=== PROBLEM 5: Restaurant Bill Calculator (Bonus) ===")
    try:
        food_total = float(input("Enter food total: $").strip())
    except ValueError:
        print("Invalid food total.")
        return

    is_holiday = input("Is today a holiday? (yes/no): ").strip().lower()
    try:
        party_size = int(input("How many people in your party? ").strip())
    except ValueError:
        print("Invalid party size.")
        return

    # Membership question
    member = input("Are you a member? (yes/no): ").strip().lower()

    # Ask day of week
    day = input("What day is it? ").strip().lower()

    # Senior question only relevant for Wednesday
    has_seniors = "no"
    if day == "wednesday":
        has_seniors = input("Are there seniors in the party? (yes/no): ").strip().lower()

    # Calculation order:
    # 1. Apply holiday surcharge +15% (if applicable)
    holiday_surcharge = 0.0
    if is_holiday == "yes":
        holiday_surcharge = food_total * 0.15

    after_holiday = food_total + holiday_surcharge

    # 2. Membership discount (10% of current subtotal)
    member_discount = 0.0
    if member == "yes":
        member_discount = after_holiday * 0.10

    after_member = after_holiday - member_discount

    # 3. Senior discount (10% on Wednesdays if seniors present)
    senior_discount = 0.0
    if day == "wednesday" and has_seniors == "yes":
        senior_discount = after_member * 0.10

    subtotal_pre_tax = after_member - senior_discount

    # 4. Add tax to discounted amount (8.5%)
    tax_amount = subtotal_pre_tax * 0.085

    # 5. Automatic gratuity for parties of 6 or more (18%) on pre-tax amount
    gratuity = 0.0
    if party_size >= 6:
        gratuity = subtotal_pre_tax * 0.18

    total = subtotal_pre_tax + tax_amount + gratuity

    # Print itemized bill
    print("\n--- Bill Breakdown ---")
    print(f"Food Total: ${food_total:.2f}")
    if holiday_surcharge > 0:
        print(f"Holiday Surcharge (15%): +${holiday_surcharge:.2f}")
    if member_discount > 0:
        print(f"Member Discount (10%): -${member_discount:.2f}")
    if senior_discount > 0:
        print(f"Senior Discount (10%): -${senior_discount:.2f}")
    print(f"Subtotal: ${subtotal_pre_tax:.2f}")
    print(f"Tax (8.5%): ${tax_amount:.2f}")
    if gratuity > 0:
        print(f"Automatic Gratuity (18%): ${gratuity:.2f}")
    print(f"Total: ${total:.2f}")
    print("Thank you for dining with us!")


# ----------------------------------------
# Simple menu so you can run each problem separately
# ----------------------------------------
def main_menu():
    print("\nCS1300 - Homework 4 Helper")
    print("Run individual problem or 'all'. Type 'quit' to exit.")
    options = {
        "1": problem1_temperature_converter,
        "2": problem2_movie_tickets,
        "3": problem3_grade_calculator,
        "4": problem4_password_strength,
        "5": problem5_restaurant_bill,
        "all": None
    }

    while True:
        print("\nChoose which problem to run:")
        print("1) Temperature Converter (15 pts)")
        print("2) Movie Tickets (25 pts)")
        print("3) Grade Calculator (30 pts)")
        print("4) Password Strength Checker (30 pts)")
        print("5) Restaurant Bill (Bonus)")
        print("all) Run all problems (one after another)")
        print("quit) Exit")
        choice = input("Enter choice: ").strip().lower()

        if choice == "quit":
            print("Exiting. Good luck!")
            break
        if choice == "all":
            # Run @ problem in order; user will be asked for inputs for each
            problem1_temperature_converter()
            problem2_movie_tickets()
            problem3_grade_calculator()
            problem4_password_strength()
            # The running bonus
            run_bonus = input("\nRun bonus problem 5? (yes/no): ").strip().lower()
            if run_bonus == "yes":
                problem5_restaurant_bill()
            continue

        func = options.get(choice)
        if func:
            func()
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
   
    main_menu()