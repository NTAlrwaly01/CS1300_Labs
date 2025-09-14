# exercise1.py
# varible type demonstration
# Nawaf T Alrwaly
# 2025-08-31

# Create variables of each type 

# Integer variable for your age
age = 20  

# Float variable for your GPA (make one up if needed)
gpa = 3.75  

# String variable for your name
name = "Nawaf T Alrwaly"  

# Boolean variable for whether you like Python
likes_python = True

# None variable for something not yet defined
future_job = None

#  Print each variable and its type 
print("Age:", age, "- Type: ", type(age))
print("GPA:", gpa, "- Type: ", type(gpa))
print("Name:", name, "- Type: ", type(name))
print("likes Python:", likes_python, "- Type: ", type(likes_python))
print("Future job:", future_job, "- Type: ", type(future_job))

# --- TODO ---

# 1) Add 1 to age and print result
next_year = age + 1
print("Next year I'll be:", next_year)

# 2) Add 0.1 to GPA and print result
improved_gpa = gpa + 0.1
print("If I improve:", improved_gpa)

# 3) Multiply your name by 3 and print result
name_repeated = name * 3
print("Name repeated : ", name_repeated)

# 4) What happens if you try: age + name?
# This raises a TypeError because int and str can't be added.
# Try/catch so the file keeps running and shows you the error:
try:
    bad_mix = age + name  # This will raise TypeError for incompatible types
    print("age + name =", bad_mix)
except TypeError as e:
    print("age + name caused TypeError:", e)

