# exercise2.py
# Type Detective
# Nawaf T Alrwaly
# 2025-08-31

# Mystery variables - know what they are!
mystery1 = 42
mystery2 = "42"
mystery3 = 42.0
mystery4 = "42.0"
mystery5 = True
mystery6 = "True"

# Print out all the mystery variables and their type
print("mystery1 is", mystery1, "type is", type(mystery1))
print("Mystery 2:", mystery2, "type is:", type(mystery2))
print("Mystery 3 is", mystery3, "type is", type(mystery3))
print("mystery4 is type", type(mystery4), ": mystery4 is", mystery4)
print("mystery5 is", mystery5, "of type", type(mystery5))
print("Mystery 6 is", mystery6, "of type", type(mystery6))

# --- Predictions before running ---
# Prediction 1: What is mystery1 + mystery3?
# int + float => result is float (42 + 42.0 = 84.0)
result1 = mystery1 + mystery3
print("\nPrediction 1: It should be shown that the type of int + float is float.")
print("mystery1 + mystery3 =", result1, "Type:", type(result1))

# Predictive statement 2: What is mystery2 + mystery4?
# As if they were both strings, and concatenated together: "42" + "42.0" = "4242.0".
result2 = mystery2 + mystery4
print("\nPrediction 2: concatenating str+str")
print("mystery2 + mystery4 =", result2, "Type:", type(result2))

# mystery2 contains the string ("42") to be cast to integer and concatenated to mystery1.
converted = int(mystery2)
sum_result = converted + mystery1
print("Result (sum(int(mystery2) + mystery1)):", sum_result)

# Convert boolean (True) to integer mystery5
bool_as_int = int(mystery5)
print(f"True as integer = {bool_as_int}")

# Convert mystery6 (string "True") to boolean
# Note: any non-empty string evaluates to True
converted_bool = bool(mystery6)
print(f"mystery6 ('True') converted with bool() = {converted_bool}")