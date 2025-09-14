# exercise3.py
# Arithmetic Operations Lab
# Nawaf T Alrwaly
# 2025-08-31

# Test numbers
a = 17
b = 5
c = 2.5

print("Test Values:")
print(f"a = {a}, b = {b}, c = {c}")
print("-" * 30)

# Addition
add_result = a + b
print(f"{a} + {b} = {add_result}")

# Subtraction
sub_result = a - b
print(f"{a} - {b} = {sub_result}")

# Multiplication
mul_result = a * b
print(f"{a} * {b} = {mul_result}")

# Division-  always returns float.
div_result = a / b
print(f"{a} / {b} = {div_result} (Type: {type(div_result)})")

# Integer Division ( // ) - returns the whole-number portion of a division.
int_div_result = a // b
print(f"intdiv({a}, {b}) = {int_div_result} (Type: {type(int_div_result)})")

# Modulo (%) - remainder of division
mod_result = a % b
print(f"{a} % {b} = {mod_result}")

# Exponentiation (**)
exp_result = a ** c
print(f"{a}  {c} = {exp_result}")

print("-" * 30)

# Mixed type operations
print("Mixed Type Operations:")

# int + float
mixed1 = a + c
print(f"{a} + {c} = {mixed1} (Type: {type(mixed1)})")

# float  int
mixed2 = b * c
print(f"{b} * {c} = {mixed2} (Type: {type(mixed2)})")

# Negative integer division example
neg_div = -17 // 5
print(f"-17 // 5 = {neg_div} (rounds down)")

# Large number example
big = 10 ** 50
print(f"10^50 = {big}")
print(f"Type of big number : {type(big)}")