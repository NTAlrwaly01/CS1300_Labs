"""
CS 1300 – Homework #10
Built-in Functions & Design
Student: Nawaf T Alrwaly
"""

# PROBLEM 1: STATISTICS CALCULATOR


def get_numbers():
    """
    Get numbers from user until they enter 'done'.
    Must enter at least 1 number.
    Returns a list of floats.
    """
    numbers = []

    while True:
        value = input("Enter a number (or 'done'): ").strip().lower()

        if value == "done":
            if len(numbers) == 0:
                print("You must enter at least one number.")
                continue
            break

        try:
            num = float(value)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return numbers


def calculate_stats(numbers):
    """
    Calculate min, max, average, and range.
    Returns all four values.
    """
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    range_val = maximum - minimum
    return minimum, maximum, average, range_val


def format_stats(minimum, maximum, average, range_val):
    """
    Format statistics for display.
    Returns a formatted multi-line string.
    """
    return (
        f"Minimum: {round(minimum, 2):.2f}\n"
        f"Maximum: {round(maximum, 2):.2f}\n"
        f"Average: {round(average, 2):.2f}\n"
        f"Range: {round(range_val, 2):.2f}"
    )


def main_statistics():
    """Main program for Problem 1."""
    print("=== Statistics Calculator ===")
    nums = get_numbers()
    mn, mx, avg, rng = calculate_stats(nums)
    output = format_stats(mn, mx, avg, rng)
    print(output)



# PROBLEM 2: GRADE PROCESSING SYSTEM


def validate_score(score_str):
    """
    Validate that string is a valid score 0-100.
    Returns True or False.
    """
    if not score_str.isdigit():
        return False
    num = int(score_str)
    return 0 <= num <= 100


def get_valid_score(prompt):
    """
    Ask user for a valid score.
    Uses validate_score helper.
    """
    while True:
        score_str = input(prompt)
        if validate_score(score_str):
            return int(score_str)
        print("Invalid score. Enter a number between 0 and 100.")


def calculate_letter(score):
    """
    Convert numeric score to letter grade.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def process_student():
    """
    Process one student's grades.
    Get 3 test scores, calculate average and letter.
    Returns name, list of scores, average, and letter.
    """
    name = input("Student name: ")
    scores = []
    for i in range(1, 4):
        score = get_valid_score(f"Score {i}: ")
        scores.append(score)

    average = sum(scores) / len(scores)
    letter = calculate_letter(average)

    return name, scores, average, letter


def display_report(name, scores, average, letter):
    """
    Display formatted student report.
    """
    print("\n--- Student Report ---")
    print(f"Name: {name}")
    print(f"Scores: {scores}")
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {letter}")


def main_grade_system():
    """
    Main grade processing program.
    Handles multiple students.
    """
    print("=== Grade Processing System ===")
    count_str = input("How many students? ")

    while not count_str.isdigit() or int(count_str) <= 0:
        print("Enter a valid positive number.")
        count_str = input("How many students? ")

    count = int(count_str)

    class_total = 0

    for _ in range(count):
        name, scores, avg, letter = process_student()
        display_report(name, scores, avg, letter)
        class_total += avg

    class_avg = class_total / count
    print(f"\nClass Average: {class_avg:.2f}")



# PROBLEM 3: SHOPPING LIST MANAGER


def validate_price(value):
    """
    Validate that price is a positive float.
    """
    try:
        price = float(value)
        return price >= 0
    except ValueError:
        return False


def get_item():
    """
    Get a single item and price.
    Returns (item, price) tuple.
    """
    item = input("Item (or 'done'): ").strip()
    if item.lower() == "done":
        return None, None

    price_str = input("Price: ")
    while not validate_price(price_str):
        print("Invalid price. Enter a positive number.")
        price_str = input("Price: ")

    return item, float(price_str)


def calculate_total(prices):
    """
    Calculate sum of all prices.
    """
    return sum(prices)


def apply_discount(total):
    """
    Apply 10% discount if total > 50.
    Returns (final_total, discount_amount)
    """
    if total > 50:
        discount = total * 0.10
        return total - discount, discount
    return total, 0


def display_shopping_list(items, prices, total, discount):
    """
    Display formatted shopping list and totals.
    """
    print("\n=== Shopping List ===")
    for item, price in zip(items, prices):
        print(f"{item}: ${price:.2f}")

    print(f"\nSubtotal: ${total:.2f}")
    if discount > 0:
        print(f"10% discount: -${discount:.2f}")
    print(f"Final Total: ${total - discount:.2f}")


def main_shopping():
    """
    Main program for the shopping list manager.
    """
    print("=== Shopping List Manager ===")

    items = []
    prices = []

    while True:
        item, price = get_item()
        if item is None:
            break
        items.append(item)
        prices.append(price)

    total = calculate_total(prices)
    final_total, discount = apply_discount(total)
    display_shopping_list(items, prices, final_total, discount)



# MAIN SWITCH (FOR TESTING)


if __name__ == "__main__":
    print("Choose a program:")
    print("1. Statistics Calculator")
    print("2. Grade Processing System")
    print("3. Shopping List Manager")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        main_statistics()
    elif choice == "2":
        main_grade_system()
    elif choice == "3":
        main_shopping()
    else:
        print("Invalid choice.")