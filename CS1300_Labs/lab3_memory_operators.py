print("=== Memory Investigation ===")
# Create variables with small integers
a = 100
b = 100
print(f"a = {a}, memory address = {id(a)}")
print(f"b = {b}, memory address = {id(b)}")
print(f"a and b same object? {id(a) == id(b)}")
print()
# Create variables with large integers
c = 1000
d = 1000
print(f"c = {c}, memory address = {id(c)}")
print(f"d = {d}, memory address = {id(d)}")
print(f"c and d same object? {id(c) == id(d)}")
print()
# Create variables with strings
e = "Python"
f = "Python"
print(f"e = '{e}', memory address = {id(e)}")
print(f"f = '{f}', memory address = {id(f)}")
print(f"e and f same object? {id(e) == id(f)}")


# Q1: Why do a and b share the same memory address?
# answer:Small integers (typically between -5 and 256) are cached in Python. In Python creating a = 100 and b = 100 allows the object to be reused in memory rather than to be made a new one. This is why their values of id are exactly the same.

# Q2: Why might c and d have different memory addresses?
# answer: Bigger integers (such as 1000) are not automatically Cached. Every time you make a variable a large integer Python can assign a new object in memory. Thus, c and d may refer to other memory addresses although their values are identical.

# Q3: What happens with string variables e and f?
# answer:Python data Pythons make strings immutable, particularly simple names such as Python. This is to say that it keeps only one copy in memory and reuses it to be efficient. This means that e and f are the same object of a string which has the same memory address.


# === variable reference String Example ===
print("\n=== String Reference Example ===")
# Create a variable type string
sample = "hello"
print(f"sample = '{sample}', id = {id(sample)}")

# Create a reference to the variable
sample_ref = sample
print("sample_ref = sample")
print(f"sample_ref = '{sample_ref}', id = {id(sample_ref)}")
print(f"The same object? {id(sample) == id(sample_ref)}")
print()

# Modify the original string variable using concatenation
sample = sample + " World"
print("After: sample = samle + ' World'")
print(f"sample = '{sample}', id = {id(sample)}")
print(f"sample_ref = '{sample_ref}', id = {id(sample_ref)}")
print(f"Still same object? {id(sample) == id(sample_ref)}")



print("\n=== Memory Changes with Operations ===")

# Initial value
x = 200
original_id = id(x)
print(f"Initial: x = {x}, id = {original_id}")

# Test 1: x = x * 2
x = 200  # reset
x = x * 2
print(f"Test 1 - x * 2: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")

# Test 2: x = x - 100
x = 200  # reset
x = x - 100
print(f"Test 2 - x - 100: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")

# Test 3: x = x / 2
x = 200  # reset
x = x / 2
print(f"Test 3 - x / 2: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")

# Test 4: x = x // 3
x = 200  # reset
x = x // 3
print(f"Test 4 - x // 3: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")

# Test 5: x = x % 7
x = 200  # reset
x = x % 7
print(f"Test 5 - x % 7: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")

# Final observation
print("\nObservation: Every action produces a new integer object, thus the address of the memory is changed..")
print("This is due to immutable nature of integers in python and any operation would leave behind a new object.")



print("\nUse compound operators:")
c = 100
print(f"Start: c = {c}")

# Add 25 to c using compound operator
c += 25
print(f"After adding 25: c = {c}")

# Divide c by 5 using compound operator
c /= 5
print(f"After dividing by 5: c = {c}")

# Get remainder when c is divided by 7 using compound operator
c %= 7
print(f"After modulo 7: c = {c}")


print("\n=== Building a Total ===")
# Calculate a restaurant bill
bill = 0.0
print(f"Starting bill: ${bill:.2f}")

# Add items using compound operators
appetizer = 12.99
bill += appetizer
print(f"Added appetizer (${appetizer}): ${bill:.2f}")

entree = 24.50
bill += entree
print(f"Added entree (${entree}): ${bill:.2f}")

dessert = 8.99
bill += dessert
print(f"Added dessert (${dessert}): ${bill:.2f}")

#  bill calculation

# Calculate 20% tip (multiply bill by 0.20)
tip = bill * 0.20
print(f"Tip (20%): ${tip:.2f}")

# Add tip to bill using compound operator
bill += tip
print(f"Total with tip: ${bill:.2f}")

# Calculate 8.5% tax on the original bill (before tip)
original_bill = appetizer + entree + dessert
tax = original_bill * 0.085
print(f"Tax (8.5%): ${tax:.2f}")

# Add tax to bill using compound operator
bill += tax
print(f"Final total: ${bill:.2f}")



print("\n=== String Building ===")
# Build a message using compound operators
message = "Shopping list"
print(f"1. message = '{message}'")

message += ":"
print(f"2. After += ':' -> '{message}'")

message += " apples"
print(f"3. After += ' apples' -> '{message}'")

# Build shopping list Continuation

# Add ", bananas" to message
message += ", bananas"
print(f"4. After adding bananas -> '{message}'")

# Add ", milk" to message
message += ", milk"
print(f"5. After adding milk -> '{message}'")

# Add ", bread" to message
message += ", bread"
print(f"6. Final list -> '{message}'")

# Check memory - does += create a new string?
original_message = "Test"
original_id = id(original_message)
original_message += " String"
new_id = id(original_message)

print(f"\nString memory test:")
print(f"Original id: {original_id}")
print(f"After += id: {new_id}")
print(f"Same object? {original_id == new_id}")

print("\n=== Operator Precedence - Predict First! ===")

# Example
# Prediction: 14
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")
print("Explanation: Multiplication happens before addition\n")

# YOUR TURN - Predict before running:

# Prediction: 4
result1 = 10 - 2 * 3
print(f"10 - 2 * 3 = {result1}")
print("Explanation: Multiplication occurs first (2*3=6), then subtraction 10-6=4\n")

# Prediction: 24
result2 = (10 - 2) * 3
print(f"(10 - 2) * 3 = {result2}")
print("Explanation: Parentheses override precedence: 10-2=8, then multiplied by 3 → 24\n")

# Prediction: 32
result3 = 2 ** 3 * 4
print(f"2 ** 3 * 4 = {result3}")
print("Explanation: Exponentiation happens first (2**3=8), then multiplied by 4 → 32\n")

# Prediction: 4096
result4 = 2 ** (3 * 4)
print(f"2 ** (3 * 4) = {result4}")
print("Explanation: Parentheses evaluated first: 3*4=12, then 2**12=4096\n")

# Prediction: 50.0
result5 = 100 / 10 * 5
print(f"100 / 10 * 5 = {result5}")
print("Explanation: Division and multiplication have same precedence, evaluated left to right: 100/10=10, then 10*5=50\n")

# Prediction: 2.0
result6 = 100 / (10 * 5)
print(f"100 / (10 * 5) = {result6}")
print("Explanation: Parentheses first: 10*5=50, then 100/50=2\n")


print("\n=== Fix the Expression with Parentheses ===")

# Each calculation is wrong. Add parentheses to fix it.

# Goal: Calculate the average of 10 and 20
wrong_avg = 10 + 20 / 2
print(f"Wrong average: {wrong_avg}")
#  FIX:
fixed_avg = (10 + 20) / 2
print(f"Fixed average: {fixed_avg}")

# Goal: Calculate 5% of 200
wrong_percent = 5 / 100 * 200
print(f"Wrong calculation: {wrong_percent}")
# FIX:
fixed_percent = (5 * 200) / 100
print(f"Fixed calculation: {fixed_percent}")

# Goal: Convert 75 minutes to hours (divide by 60)
wrong_hours = 75 / 60 * 60
print(f"Wrong hours: {wrong_hours}")
# FIX:
fixed_hours = 75 / 60
print(f"Fixed hours: {fixed_hours}")


print("\n=== Understanding Division Operations ===")

# Regular division (/)
print("Regular division (/):")
print(f"17 / 5 = {17 / 5}")
print(f"20 / 4 = {20 / 4}")
print(f"Type of 20 / 4: {type(20 / 4)}")
print()

# Floor division (//)
print("Floor division (//):")
print(f"17 // 5 = {17 // 5}")
print(f"20 // 4 = {20 // 4}")
print(f"Type of 20 // 4: {type(20 // 4)}")
print()

# Modulo (%)
print("Modulo (%):")
print(f"17 % 5 = {17 % 5}")
print(f"20 % 4 = {20 % 4}")
print()

# Task
numerator = 23
denominator = 7

# Regular division
regular_div = numerator / denominator

# Floor division
floor_div = numerator // denominator

# Remainder
remainder = numerator % denominator

print(f"{numerator} / {denominator} = {regular_div}")
print(f"{numerator} // {denominator} = {floor_div}")
print(f"{numerator} % {denominator} = {remainder}")

# Verify: numerator should equal (floor_div * denominator) + remainder
verification = (floor_div * denominator) + remainder
print(f"Verification: {floor_div} * {denominator} + {remainder} = {verification}")


print("\n=== Time Conversion ===")

# Convert total seconds to hours, minutes, seconds
total_seconds = 7325
print(f"Converting {total_seconds} seconds:")

# Calculate hours
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
print(f"Hours: {hours}")
print(f"Remaining seconds: {remaining_seconds}")

# Calculate minutes from remaining seconds
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")
print(f"Result: {hours} hours, {minutes} minutes, {seconds} seconds")

# Task: Convert 9876 seconds
total_seconds_2 = 9876
print(f"\nConverting {total_seconds_2} seconds:")

# Calculate hours
hours_2 = total_seconds_2 // 3600
remaining_2 = total_seconds_2 % 3600

# Calculate minutes
minutes_2 = remaining_2 // 60
seconds_2 = remaining_2 % 60

print(f"Result: {hours_2} hours, {minutes_2} minutes, {seconds_2} seconds")


print("\n=== Making Change ===")

# Calculate coins needed for given cents
cents = 287
print(f"Making change for {cents} cents:")

# Calculate quarters (25 cents)
quarters = cents // 25
remaining = cents % 25
print(f"Quarters: {quarters}, Remaining: {remaining} cents")

# Calculate dimes (10 cents)
dimes = remaining // 10
remaining = remaining % 10
print(f"Dimes: {dimes}, Remaining: {remaining} cents")

# Calculate nickels (5 cents)
nickels = remaining // 5
pennies = remaining % 5
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")

# Task: Calculate change for 193 cents
cents_2 = 193
print(f"\nMaking change for {cents_2} cents:")

# Calculate quarters
quarters_2 = cents_2 // 25
remaining_2 = cents_2 % 25

# Calculate dimes
dimes_2 = remaining_2 // 10
remaining_2 = remaining_2 % 10

# Calculate nickels and pennies
nickels_2 = remaining_2 // 5
pennies_2 = remaining_2 % 5

print(f"Quarters: {quarters_2}")
print(f"Dimes: {dimes_2}")
print(f"Nickels: {nickels_2}")
print(f"Pennies: {pennies_2}")

# Verify your answer
total_check = (quarters_2 * 25) + (dimes_2 * 10) + (nickels_2 * 5) + pennies_2
print(f"Verification: {total_check} cents")



print("\n=== Unit Conversion Calculator ===")

# Convert miles to various units
miles = 5.5
print(f"Starting with: {miles} miles")

# Convert to feet (1 mile = 5280 feet)
feet = miles * 5280
print(f"In feet: {feet:.1f} feet")

# Convert to yards (1 mile = 1760 yards)
yards = miles * 1760
print(f"In yards: {yards:.1f} yards")

# Convert to kilometers (1 mile = 1.60934 km)
kilometers = miles * 1.60934
print(f"In kilometers: {kilometers:.2f} km")

# Convert to meters (using the km value)
meters = kilometers
meters *= 1000
print(f"In meters: {meters:.2f} meters")

# YOUR TURN: Convert temperature
# Convert 75°F to Celsius and Kelvin
fahrenheit = 75
print(f"\n=== Temperature Conversion ===")
print(f"Starting with: {fahrenheit}°F")

# Convert to Celsius: C = (F - 32) * 5/9
celsius = (fahrenheit - 32) * 5 / 9
print(f"In Celsius: {celsius:.1f}°C")

# Convert to Kelvin: K = C + 273.15
kelvin = celsius
kelvin += 273.15
print(f"In Kelvin: {kelvin:.1f} K")

# YOUR TURN: Data Storage Units
# Convert 2.5 GB to other units
gigabytes = 2.5
print(f"\n=== Data Storage Conversion ===")
print(f"Starting with: {gigabytes} GB")

# Convert to MB (1 GB = 1024 MB)
megabytes = gigabytes * 1024
print(f"In Megabytes: {megabytes:.0f} MB")

# Convert to KB (use MB value, 1 MB = 1024 KB)
kilobytes = megabytes
kilobytes *= 1024
print(f"In Kilobytes: {kilobytes:.0f} KB")

# Convert to bytes (use KB value, 1 KB = 1024 bytes)
bytes_total = kilobytes
bytes_total *= 1024
print(f"In Bytes: {bytes_total:.0f} bytes")

# Convert to bits (1 byte = 8 bits)
bits = bytes_total
bits *= 8
print(f"In Bits: {bits:.0f} bits")


print("\n=== BONUS: Compound Interest with Memory Tracking ===")

# Annual compound interest
principal = 1000.00
rate = 0.05  # 5% annual
years = 3
print(f"Initial investment: ${principal:.2f}")
print(f"Annual rate: {rate*100}%")
print(f"Investment period: {years} years\n")

# Track the principal's memory address
print(f"Principal memory address: {id(principal)}")

# Yearly calculation
amount = principal
print(f"Year 0: ${amount:.2f}")
for year in range(1, years + 1):
    amount *= (1 + rate)
    print(f"Year {year}: ${amount:.2f} (memory: {id(amount)})")

# Total interest earned
interest = amount - principal
print(f"\nTotal interest earned: ${interest:.2f}")
print(f"Return on investment: {(interest / principal) * 100:.1f}%")

# Memory analysis
print(f"\nOriginal principal still: ${principal:.2f}")
print(f"Principal unchanged at memory: {id(principal)}")
print(f"Final amount at different memory: {id(amount)}")

# Task: Calculate monthly compound interest
monthly_principal = 500.00
monthly_rate = 0.06 / 12  # 0.5% per month
months = 6
print(f"\n=== Your Monthly Calculation ===")
print(f"Initial: ${monthly_principal:.2f}")
print(f"Monthly rate: {monthly_rate*100:.1f}%")

monthly_amount = monthly_principal
for month in range(1, months + 1):
    monthly_amount *= (1 + monthly_rate)
    print(f"Month {month}: ${monthly_amount:.2f} (memory: {id(monthly_amount)})")

# Total interest earned monthly
monthly_interest = monthly_amount - monthly_principal
print(f"\nTotal interest earned over {months} months: ${monthly_interest:.2f}")