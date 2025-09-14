# exercise4.py
# Order of Operations Practice
# Nawaf T Alrwaly
# 2025-08-31

# Test numbers
a = 17
b = 5
c = 2.5

# Expression 1
# Prediction: 2 + (3 * 4) = 14
result1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {result1}")

# Expression 2
# Prediction: (2 + 3) * 4 = 20
result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result2}")

# Expression 3
# Prediction: (10 / 2) * 3 = 15.0
result3 = 10 / 2 * 3
print(f"10 / 2 * 3 = {result3}")

# Expression 4
# Prediction: 10 / (2 * 3) = 1.6666...
result4 = 10 / (2 * 3)
print(f"10 / (2 * 3) = {result4}")

# Expression 5
# Prediction: 2 ** (3 ** 2) = 512
result5 = (2 ** 3 ** 2)
print(f"2 ** 3 ** 2 = {result5} (Exponentiation is right-to-left!)")

# Expression 6
# Prediction: same as previous = 512
result6 = 2 ** (3 ** 2)
print(f"2 ** (3 ** 2) = {result6}")

# My own complex expression (uses at least 4 operations)
# Prediction: 5 + 3 * 2 ** 2 / 4 - 1 = 7
my_expression = 5 + 3 * 2 ** 2 / 4 - 1
print(f"My expression: {my_expression}")


# Step-by-step evaluation of a complex expression
complex_expr = 10 + 20 * 30 / 10 - 5 ** 2
print("\nStep-by-step evaluation of: 10 + 20 * 30 / 10 - 5 ** 2")

# Step 1: Exponentiation first
step1 = 5 ** 2
print(f"Step 1: 5 ** 2 = {step1}")

# Step 2: Multiplication next
step2 = 20 * 30
print(f"Step 2: 20 * 30 = {step2}")

# Step 3: Division
step3 = step2 / 10
print(f"Step 3: 600 / 10 = {step3}")

# Step 4: Addition
step4 = 10 + step3
print(f"Step 4: 10 + 60.0 = {step4}")

# Step 5: Subtraction
step5 = step4 - step1
print(f"Step 5: 70.0 - 25 = {step5}")

# Final result
print(f"Final result: {complex_expr}")