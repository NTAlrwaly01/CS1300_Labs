
# CS 1300 – Homework #9 (Functions)
# Student: Nawaf T Alrwaly
# Date: November 16, 2025



# Problem 1: Temperature Converter

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = C * 9/5 + 32
    """
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) * 5/9
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def temperature_report(temp, scale="C"):
    """
    Print temperature in both scales.

    Parameters:
    temp: numerical value
    scale: "C" for Celsius or "F" for Fahrenheit (default is "C")

    Behavior:
    - If scale is "C", convert Celsius → Fahrenheit
    - If scale is "F", convert Fahrenheit → Celsius
    """
    if scale.upper() == "C":
        converted = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {converted:.1f}°F")
    else:
        converted = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {converted:.1f}°C")



# Problem 2: Grade Calculator with Multiple Parameters

def calculate_weighted_grade(homework, midterm, final, 
                             hw_weight=0.3, mid_weight=0.3, final_weight=0.4):
    """
    Calculate weighted grade using provided weights.

    Parameters:
        homework: homework average (0-100)
        midterm: midterm exam score
        final: final exam score
        hw_weight, mid_weight, final_weight: weighting factors

    Returns:
        Weighted grade (float)
    """
    weighted = (homework * hw_weight +
                midterm * mid_weight +
                final * final_weight)
    return weighted


def get_letter_grade(score):
    """
    Convert numeric score to letter grade.
    A: >= 90
    B: >= 80
    C: >= 70
    D: >= 60
    F: < 60
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def print_grade_report(name, hw, mid, final):
    """
    Print a complete grade report for the student.

    Displays:
    - Name
    - Raw scores
    - Weighted average
    - Letter grade
    """
    weighted = calculate_weighted_grade(hw, mid, final)
    letter = get_letter_grade(weighted)

    print("\n=== GRADE REPORT ===")
    print(f"Student: {name}")
    print(f"Homework: {hw}")
    print(f"Midterm: {mid}")
    print(f"Final: {final}")
    print(f"Weighted Average: {weighted:.1f}")
    print(f"Letter Grade: {letter}")
    print("====================\n")



# Problem 3: Scope Challenge

# Global score variables
total_points = 0
bonus_multiplier = 1.1


def add_score(points):
    """
    Add points to total score.
    Needs global keyword because we modify total_points.
    """
    global total_points   
    total_points = total_points + points
    return total_points


def apply_bonus():
    """
    Apply bonus multiplier to total score.
    Uses the global keyword because we are modifying total_points.
    """
    global total_points   # Modify the global veriable
    total_points = total_points * bonus_multiplier


def get_final_score():
    """
    Return the final score.
    Only reads the global.
    """
    return total_points


def reset_game():
    """
    Reset total score to zero.
    Uses global keyword.
    """
    global total_points
    total_points = 0
    print("Game has been reset.")




# TEST CASES 


print("\n--- Temperature Converter Tests ---")
print(celsius_to_fahrenheit(0))     
print(celsius_to_fahrenheit(100))   

print(fahrenheit_to_celsius(32))    
print(fahrenheit_to_celsius(68)) 

temperature_report(25)             
temperature_report(77, "F")         


print("\n--- Grade Calculator Tests ---")
grade1 = calculate_weighted_grade(85, 78, 92)
print(f"Grade 1: {grade1}")     

grade2 = calculate_weighted_grade(90, 85, 80, 
                                  hw_weight=0.4, 
                                  mid_weight=0.2, 
                                  final_weight=0.4)
print(f"Grade 2: {grade2}")       

print_grade_report("Alice Smith", 88, 91, 85)


print("\n--- Scope Challenge Tests ---")
reset_game()            # Reset to 0
add_score(100)          
add_score(50)           
apply_bonus()          
print(f"Final score: {get_final_score()}")  