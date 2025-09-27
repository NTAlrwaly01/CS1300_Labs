"""
CS1300 - Homework #5: Advanced Control Structures
Name: Nawaf T Alrwaly
Date: 2025-10-06
Description: Advanced conditional logic and validation (Problems 1-5 + Debugging)
"""

# ===============================
# Homework 5 - Advanced Control Structures
# ===============================

from typing import Tuple

# -------------------------------
# Problem 1: Smart Thermostat Controller
# -------------------------------
def problem1_smart_thermostat():
    print("\n=== PROBLEM 1: SMART THERMOSTAT SYSTEM ===")
    # Get inputs with basic validation
    try:
        current_temp = float(input("Current temperature (F): ").strip())
        desired_temp = float(input("Desired temperature (F): ").strip())
        hour = int(input("Current hour (0-23): ").strip())
        if not (0 <= hour <= 23):
            print("Hour out of range (0-23). Aborting.")
            return
        season = input("Season (summer/winter/spring/fall): ").strip().lower()
    except ValueError:
        print("Invalid numeric input. Please enter numbers correctly.")
        return

    # 1. Check comfortable range using chained comparison
    comfortable = 68 <= current_temp <= 76

    # 2. Night time check: active if hour >= 22 or hour <= 6
    night_mode = (hour >= 22) or (hour <= 6)

    # 3. Apply seasonal restrictions:
    # - Summer: never below 72°F
    # - Winter: never above 70°F
    seasonal_limit_applied = False
    final_target = desired_temp

    if night_mode:
        # reduce desired by 3 degrees for energy saving
        final_target -= 3
        print("- Night mode: ACTIVE (reducing target by 3°F)")

    # Apply seasonal caps
    if season == "summer":
        # never below 72: ensure final_target >= 72
        if final_target < 72:
            final_target = 72
            seasonal_limit_applied = True
            print("- Season: Summer (min target 72°F applied)")
    elif season == "winter":
        # never above 70: ensure final_target <= 70
        if final_target > 70:
            final_target = 70
            seasonal_limit_applied = True
            print("- Season: Winter (max target 70°F applied)")
    else:
        # spring/fall - no extra restriction
        pass

    # 4. Calculate adjustment needed and estimate time to reach target
    adjustment = final_target - current_temp  # positive: need heating, negative: cooling
    hours_needed = abs(adjustment) / 2.0  # 2 degrees per hour

    # 5. Energy efficiency rating (simple heuristic)
    abs_adj = abs(adjustment)
    if abs_adj <= 2:
        efficiency = "EXCELLENT"
    elif abs_adj <= 5:
        efficiency = "GOOD"
    elif abs_adj <= 10:
        efficiency = "FAIR"
    else:
        efficiency = "POOR"

    # Display status
    print("\nCurrent Status:")
    print(f"- Current temp: {current_temp}°F ({'Comfortable' if comfortable else 'Too cold' if current_temp < 68 else 'Too hot'})")
    print(f"- Desired: {desired_temp}°F")
    if night_mode:
        print(f"- Night adjustment applied: target reduced by 3°F -> {desired_temp - 3:.1f}°F")
    if seasonal_limit_applied:
        print(f"- Seasonal limit applied -> Final target: {final_target:.1f}°F")
    else:
        print(f"- Final target: {final_target:.1f}°F")

    print(f"\nHeating/Cooling required: {adjustment:.1f}°F")
    print(f"Estimated time: {hours_needed:.1f} hours")
    print(f"Energy efficiency: {efficiency}")


# -------------------------------
# Problem 2: Password Security Analyzer
# -------------------------------
def problem2_password_analyzer():
    print("\n=== PROBLEM 2: PASSWORD SECURITY ANALYZER ===")
    password = input("Enter password to analyze: ").strip()

    # Score breakdown variables (points allocated per spec)
    # Length: 8+ (10), 12+ (20), 16+ (30)
    length_points = 30 if len(password) >= 16 else 20 if len(password) >= 12 else 10 if len(password) >= 8 else 0

    # Uppercase letters (15 points)
    has_upper = True if any(c.isupper() for c in password) else False
    upper_points = 15 if has_upper else 0

    # Lowercase letters (15 points)
    has_lower = True if any(c.islower() for c in password) else False
    lower_points = 15 if has_lower else 0

    # Numbers (15 points)
    has_digit = True if any(c.isdigit() for c in password) else False
    digit_points = 15 if has_digit else 0

    # Special characters (15 points)
    has_special = True if any(not c.isalnum() for c in password) else False
    special_points = 15 if has_special else 0

    # No common patterns like "123", "abc", "qwerty" (10 points)
    common_patterns = ["123", "abc", "qwerty", "password", "111"]
    has_pattern = any(pat in password.lower() for pat in common_patterns)
    pattern_points = 0 if has_pattern else 10

    # Total score
    score = length_points + upper_points + lower_points + digit_points + special_points + pattern_points
    if score > 100:
        score = 100

    # Strength level using conditional expressions (ternary-like)
    if score >= 85:
        strength = "STRONG"
    elif score >= 70:
        strength = "GOOD"
    elif score >= 50:
        strength = "FAIR"
    else:
        strength = "WEAK"

    # Provide recommendations
    recommendations = []
    if length_points < 30:
        recommendations.append("- Consider using 16+ characters for maximum points")
    if not has_upper:
        recommendations.append("- Add uppercase letters")
    if not has_lower:
        recommendations.append("- Add lowercase letters")
    if not has_digit:
        recommendations.append("- Add numeric characters")
    if not has_special:
        recommendations.append("- Add special characters (e.g., @, #, !)")
    if has_pattern:
        recommendations.append("- Avoid common patterns like '123', 'abc', 'qwerty'")

    # Display detailed analysis
    print("\nSecurity Analysis:")
    print(f"✓ Length: {len(password)} characters ({length_points}/30 points)")
    print(f"✓ Uppercase letters: {'Yes' if has_upper else 'No'} ({upper_points}/15 points)")
    print(f"✓ Lowercase letters: {'Yes' if has_lower else 'No'} ({lower_points}/15 points)")
    print(f"✓ Numbers: {'Yes' if has_digit else 'No'} ({digit_points}/15 points)")
    print(f"✓ Special characters: {'Yes' if has_special else 'No'} ({special_points}/15 points)")
    print(f"{'✗ Common pattern detected' if has_pattern else '✓ No common patterns'} ({pattern_points}/10 points)")

    print(f"\nTotal Score: {score}/100")
    print(f"Strength Level: {strength}")

    if recommendations:
        print("\nRecommendations:")
        for rec in recommendations:
            print(rec)
    else:
        print("\nNo recommendations — great password!")


# -------------------------------
# Problem 3: Student Grade Validator
# -------------------------------
def problem3_grade_validator():
    print("\n=== PROBLEM 3: GRADE VALIDATION SYSTEM ===")
    try:
        test1 = float(input("Test 1 score: ").strip())
        test2 = float(input("Test 2 score: ").strip())
        test3 = float(input("Test 3 score: ").strip())
        test4 = float(input("Test 4 score: ").strip())
    except ValueError:
        print("Invalid input; please enter numeric scores.")
        return

    # 1. Validate each score is 0-100 using chained comparisons
    all_valid_range = (0 <= test1 <= 100) and (0 <= test2 <= 100) and (0 <= test3 <= 100) and (0 <= test4 <= 100)
    if not all_valid_range:
        print("Error: One or more scores are out of range (0-100).")
        return

    # 2. Check suspicious patterns
    # All identical
    all_identical = (test1 == test2 == test3 == test4)

    # Huge jumps (>40 points) between consecutive tests
    huge_jump = (abs(test2 - test1) > 40) or (abs(test3 - test2) > 40) or (abs(test4 - test3) > 40)

    # Perfect scores on all tests
    all_perfect = (test1 == 100 and test2 == 100 and test3 == 100 and test4 == 100)

    # 3. Use truth table logic for validation combinations
    not_suspicious = not (all_identical or huge_jump or all_perfect)
    valid_and_trustworthy = all_valid_range and not_suspicious

    # Print validation results
    print("\nValidation Results:")
    print(f"✓ All scores in valid range? {'Yes' if all_valid_range else 'No'}")
    print(f"✓ All identical? {'Yes' if all_identical else 'No'}")
    print(f"✓ Huge jumps between consecutive tests? {'Yes' if huge_jump else 'No'}")
    print(f"✓ All perfect scores? {'Yes' if all_perfect else 'No'}")

    if not valid_and_trustworthy:
        print("\nWarning: Scores flagged as suspicious.")
        # provide tailored feedback
        if all_identical:
            print("- All scores identical: possible cheating or data entry error.")
        if huge_jump:
            print("- Large jumps detected (>40 points) between consecutive tests.")
        if all_perfect:
            print("- All perfect scores: verify grading/authenticity.")
        # still compute basic stats unless invalid ranges (we already validated ranges)
    else:
        print("\n✓ Scores show normal variation")

    # 4. If valid, calculate average, highest, lowest, improvement/trend
    average = (test1 + test2 + test3 + test4) / 4.0
    highest = max(test1, test2, test3, test4)
    lowest = min(test1, test2, test3, test4)
    improvement = test4 - test1  # overall change from first to last

    if improvement > 0:
        trend = "IMPROVING"
    elif improvement < 0:
        trend = "DECLINING"
    else:
        trend = "STABLE"

    # 5. Determine letter grade using average
    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"

    # PASS/FAIL logic: (not explicitly requested here but keep sensible)
    passing = (letter != "F")

    print("\nStatistics:")
    print(f"- Average: {average:.2f}")
    print(f"- Highest: {highest}")
    print(f"- Lowest: {lowest}")
    print(f"- Trend: {trend}")
    print(f"Grade: {letter}")
    print(f"Status: {'PASSING' if passing else 'FAILING'}")


# -------------------------------
# Problem 4: Event Scheduling Conflict Detector
# -------------------------------
def problem4_event_scheduler():
    print("\n=== PROBLEM 4: EVENT SCHEDULING SYSTEM ===")
    valid_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

    print("\nEVENT 1 DETAILS:")
    event1_name = input("Event name: ").strip()
    event1_day = input("Day (Mon-Sun): ").strip().lower()[:3]
    try:
        event1_start = float(input("Start time (0-24): ").strip())
        event1_end = float(input("End time (0-24): ").strip())
    except ValueError:
        print("Invalid time input.")
        return

    print("\nEVENT 2 DETAILS:")
    event2_name = input("Event name: ").strip()
    event2_day = input("Day (Mon-Sun): ").strip().lower()[:3]
    try:
        event2_start = float(input("Start time (0-24): ").strip())
        event2_end = float(input("End time (0-24): ").strip())
    except ValueError:
        print("Invalid time input.")
        return

    # 1. Validate times are in range 0-24 and end > start
    event1_valid = (event1_day in valid_days) and (0 <= event1_start < 24) and (0 < event1_end <= 24) and (event1_end > event1_start)
    event2_valid = (event2_day in valid_days) and (0 <= event2_start < 24) and (0 < event2_end <= 24) and (event2_end > event2_start)

    if not event1_valid or not event2_valid:
        print("\nError: One or both events have invalid day/time entries.")
        print(f"Event1 valid? {event1_valid}, Event2 valid? {event2_valid}")
        return

    # 2. Check the overlap condition
    same_day = event1_day == event2_day
    overlap = same_day and (event1_start < event2_end) and (event2_start < event1_end)

    # 3. Gap between events (if same day)
    gap = None
    if same_day:
        # gap = start of later - end of earlier
        if event1_end <= event2_start:
            gap = event2_start - event1_end
        elif event2_end <= event1_start:
            gap = event1_start - event2_end
        else:
            gap = -1  # indicates overlap

    # 4. Back-to-back: less than 0.5 hours (30 minutes)
    back_to_back = (gap is not None and gap >= 0 and gap < 0.5)

    # 5. Too early or too late
    event1_early_or_late = (event1_start < 6) or (event1_end > 23)
    event2_early_or_late = (event2_start < 6) or (event2_end > 23)

    # 6. Calculate durations and total commitment
    dur1 = event1_end - event1_start
    dur2 = event2_end - event2_start
    total_commitment = dur1 + dur2

    # Present analysis
    print("\nSchedule Analysis:")
    print(f"✓ Event 1 valid times: {event1_start} - {event1_end}")
    print(f"✓ Event 2 valid times: {event2_start} - {event2_end}")
    if same_day:
        if overlap:
            print("⚠ Events CONFLICT: times overlap on the same day.")
        elif back_to_back:
            print(f"⚠ Events are back-to-back (gap = {gap:.2f} hours).")
        else:
            print(f"✓ No direct conflict (gap = {gap:.2f} hours)." if gap is not None else "✓ No conflict info")
    else:
        print("✓ Events are on different days - no overlap.")

    if event1_early_or_late or event2_early_or_late:
        print("⚠ One or more events scheduled very early (<6) or very late (>23).")

    print(f"\nEvent 1: {event1_name}")
    print(f"- {event1_day.title()} {format_time(event1_start)} - {format_time(event1_end)} ({dur1:.2f} hours)")
    print(f"Event 2: {event2_name}")
    print(f"- {event2_day.title()} {format_time(event2_start)} - {format_time(event2_end)} ({dur2:.2f} hours)")

    print(f"\nTotal time commitment: {total_commitment:.2f} hours")
    if overlap:
        print("Recommendation: Reschedule or shorten one event to avoid overlap.")
    elif back_to_back:
        print("Recommendation: Add buffer time between events (>= 0.5 hours).")
    else:
        print("Recommendation: Schedule looks fine.")


def format_time(hour_float: float) -> str:
    # Convert decimal hour to H:MM format for display
    h = int(hour_float)
    m = int(round((hour_float - h) * 60))
    return f"{h:02d}:{m:02d}"


# -------------------------------
# Problem 5 (Bonus): Retail Discount Calculator
# -------------------------------
def problem5_retail_discount():
    print("\n=== PROBLEM 5: RETAIL DISCOUNT CALCULATOR (BONUS) ===")
    try:
        price = float(input("Item price: $").strip())
        quantity = int(input("Quantity: ").strip())
    except ValueError:
        print("Invalid price or quantity.")
        return

    customer_type = input("Customer type (regular/member/vip/employee): ").strip().lower()
    day = input("Day of week: ").strip().lower()
    coupon = input("Coupon code (or 'none'): ").strip().upper()

    subtotal = price * quantity
    running = subtotal
    print(f"\nOrder Summary:\nItems: {quantity} × ${price:.2f} = ${subtotal:.2f}")

    # 1. Bulk discount (10+ -> 10%, 20+ -> 15%, 50+ -> 20%)
    bulk_rate = 0.20 if quantity >= 50 else 0.15 if quantity >= 20 else 0.10 if quantity >= 10 else 0.0
    bulk_discount = running * bulk_rate
    running -= bulk_discount
    print(f"1. Bulk discount ({int(bulk_rate*100)}%): -${bulk_discount:.2f}")
    print(f"   Subtotal: ${running:.2f}")

    # 2. Customer type discount
    cust_rate = 0.15 if customer_type == "employee" else 0.10 if customer_type == "vip" else 0.05 if customer_type == "member" else 0.0
    cust_discount = running * cust_rate
    running -= cust_discount
    print(f"2. Customer discount ({int(cust_rate*100)}%): -${cust_discount:.2f}")
    print(f"   Subtotal: ${running:.2f}")

    # 3. Day discount: Tuesday 5%, weekend (sat/sun) 10%
    day_rate = 0.10 if day in ("sat", "sun", "saturday", "sunday") else 0.05 if day.startswith("tue") or day == "tuesday" else 0.0
    day_discount = running * day_rate
    running -= day_discount
    print(f"3. Day discount ({int(day_rate*100)}%): -${day_discount:.2f}")
    print(f"   Subtotal: ${running:.2f}")

    # 4. Coupon codes
    coupon_map = {"SAVE10": 0.10, "SAVE20": 0.20, "STUDENT": 0.15}
    coupon_rate = coupon_map.get(coupon, 0.0)
    coupon_discount = running * coupon_rate
    running -= coupon_discount
    print(f"4. Coupon {coupon if coupon_rate>0 else 'NONE'} ({int(coupon_rate*100)}%): -${coupon_discount:.2f}")
    print(f"   Subtotal: ${running:.2f}")

    # Effective total discount percentage (multiplicative approach)
    effective_discount = 1 - (running / subtotal) if subtotal > 0 else 0

    # 5. Apply maximum total discount cap of 40%
    cap = 0.40
    if effective_discount > cap:
        # reduce to cap by setting running to subtotal*(1-cap)
        capped_price = subtotal * (1 - cap)
        saved_amount = subtotal - capped_price
        print(f"\nTotal Discount capped at {int(cap*100)}% to protect business policy.")
        print(f"Total Discount: ${subtotal - capped_price:.2f} ({(1 - capped_price/subtotal)*100:.1f}%)")
        print(f"Final Price: ${capped_price:.2f}")
    else:
        print(f"\nTotal Discount: ${subtotal - running:.2f} ({effective_discount*100:.1f}%)")
        print(f"Final Price: ${running:.2f}")

    print("You saved: ${:.2f}!".format(subtotal - running if effective_discount <= cap else subtotal - subtotal*(1-cap)))


# -------------------------------
# Debugging Challenge: Fix the broken grade calculator
# -------------------------------
def debugging_challenge_fixed():
    print("\n=== DEBUGGING CHALLENGE: FIXED GRADE CALCULATOR ===")
    # Original broken code had multiple issues. Below is the corrected implementation.
    try:
        hw = float(input("Homework average: ").strip())
        midterm = float(input("Midterm score: ").strip())
        final = float(input("Final score: ").strip())
    except ValueError:
        print("Invalid input - please enter numeric scores.")
        return

    # Correct calculation of weighted average
    average = (hw * 0.3) + (midterm * 0.3) + (final * 0.4)

    # Correct comparisons and logic
    if 90 <= average <= 100:
        grade = "A"
    elif average >= 80:   # >= 80 and < 90
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    # Print result
    print(f"Final numeric average: {average:.2f}")
    print(f"Letter grade: {grade}")

    # Additional fixes: using == for comparisons and checking correct case
    if grade == "A":
        print("Excellent!")
    if grade == "F":
        print("Needs improvement")

    # Final fixed variable name
    final_grade = grade
    print(f"Final grade: {final_grade}")

    # List each bug and fix (brief)
    print("\nBug list and fixes:")
    print("1. Missing type conversion for input -> fixed by converting to float.")
    print("2. Wrong logical operator in range check -> use 'and' via chained comparison: 90 <= avg <=100.")
    print("3. Incorrect comparison operators (use >= appropriately).")
    print("4. Missing colon on elif -> corrected.")
    print("5. Assignment instead of comparison (if grade = 'A') -> use '=='.")
    print("6. Case sensitivity issue (grade 'F' vs 'f') -> standardized 'F'.")
    print("7. Impossible logic (average >=60 and grade == 'F') -> removed / corrected.")
    print("8. Undefined variable final_grade -> use the 'grade' variable and print it.")


# -------------------------------
# Main menu to run problems individually
# -------------------------------
def main_menu():
    print("\nCS1300 - Homework #5 Helper (Advanced Control Structures)")
    options = {
        "1": problem1_smart_thermostat,
        "2": problem2_password_analyzer,
        "3": problem3_grade_validator,
        "4": problem4_event_scheduler,
        "5": problem5_retail_discount,
        "debug": debugging_challenge_fixed,
        "quit": None
    }

    while True:
        print("\nSelect a problem to run:")
        print("1) Problem 1 - Smart Thermostat (15 pts)")
        print("2) Problem 2 - Password Security Analyzer (25 pts)")
        print("3) Problem 3 - Grade Validator (25 pts)")
        print("4) Problem 4 - Event Scheduler (35 pts)")
        print("5) Problem 5 - Retail Discount (Bonus 20 pts)")
        print("debug) Debugging challenge (Bonus)")
        print("quit) Exit")
        choice = input("Enter choice: ").strip().lower()
        if choice == "quit":
            print("Exiting. Good luck on submission!")
            break
        func = options.get(choice)
        if func:
            func()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()