# calculator.py
# Simple Calculator with Type Handling
# Nawaf T Alrwaly
# 2025-08-31

print("=" * 40)
print(" ARITHMETIC CALCULATOR")
print("=" * 40)

# Step 1: Define two numbers
first_number = 10  
second_number = 3

# Display numbers and their types
print(f"First number: {first_number} (Type: {type(first_number).__name__})")
print(f"Second number: {second_number} (Type: {type(second_number).__name__})")
print("-" * 40)

# Step 2: Perform arithmetic operations
print("CALCULATIONS:")

# Addition
sum_result = first_number + second_number
print(f"Addition: {first_number} + {second_number} = {sum_result}")

# Subtraction
diff_result = first_number - second_number
print(f" Subtraction: {first_number} - {second_number} = {diff_result}")

# Multiplication
product_result = first_number * second_number
print(f"Mutiplication: {first_number} * {second_number} = {product_result}")

# Division(regular),
div_result = first_number / second_number
print(f"Divison: {first_number} / {second_number} = {div_result}")

# IntegerDivision
int_div_result = first_number // second_number
print(f"IntegerDivision: {first_number} // {second_number} = {int_div_result}")
# Modulo
mod_result = first_number % second_number
print(f"Modulo: {first_number} % {second_number} = {mod_result}")

# Exponentiation
exp_result = first_number ** second_number
print(f"Exponentiation: {first_number} ** {second_number} = {exp_result}")
print("-" * 40)

# Step 3: Type Analysis
print("TYPE ANALYSIS:")
print(f"Addition results type: {type(sum_result).__name__}")
print(f"Subtraction results type: {type(diff_result).__name__}")
print(f"Multiplication results type: {type(product_result).__name__}")
print(f"Division results type: {type(div_result).__name__} (always a float)")
print(f"IntegerDivision type: {type(int_div_result).__name__}")
print(f"Modulo results type: {type(mod_result).__name__}")
print(f"Exponentiation results type: {type(exp_result).__name__}")
print("-" * 40)

# Step 4: FunCalculations
print("Fun calculations:")

# Area of a circle
pi = 3.14159
area = pi * first_number ** 2
print(f"The area of a circle with radius {first_number}: {area:.2f}")

# Compound interest
principal = first_number * 100
rate = second_number / 100
time = 5
amount = principal * (1 + rate) ** time
print(f"${principal} at {second_number}% for {time} years = ${amount:.2f}")

# Pizza slices example
total_slices_needed = first_number * second_number
slices_per_pizza = 8
whole_pizza = total_slices_needed // slices_per_pizza
extra_slices = total_slices_needed % slices_per_pizza
print(f"{first_number} people × {second_number} slices each =")
print(f" Need {whole_pizza} pizza with {extra_slices} left over")
print("=" * 40)
