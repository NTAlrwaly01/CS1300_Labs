"""
CS 1300 - Final Examination 
Name: Nawaf T. Alrwaly
Date: December 11, 2025
Description: Final Examination for CS 1300"""

print("="*60)
print("PART 2: PROGRAMMING EXAMINATION")
print("="*60)
# Problem 1: Count Negative Numbers (25 points)
def count_negative(numbers):
   
    count = 0
    for num in numbers:
        if num < 0:
            count += 1
    return count


# Test  function:
print(count_negative([5, -2, 0, -3, 1, -8]))  
print(count_negative([-1, -2, -3]))            
print(count_negative([-10, -20, -30]))         
print(count_negative([]))                      


# Problem 2: Grade Classifier 
def get_letter_grade(score):
   
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


def count_letter_grades(scores):
   
    grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    for score in scores:
        letter = get_letter_grade(score)
        grades[letter] += 1
    
    return grades


# Test functions:
print(get_letter_grade(95))    
print(get_letter_grade(82))     
print(get_letter_grade(78))     
print(get_letter_grade(65))     
print(get_letter_grade(55))     

scores_list = [95, 82, 75, 65, 55, 92, 88, 45]
print(count_letter_grades(scores_list))  


# Problem 3: String Reverser 
def reverse_string(text):
    
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text


# Test function:
print(reverse_string("hello"))     
print(reverse_string("Python"))     
print(reverse_string("12345"))      
print(reverse_string("a"))        
print(reverse_string(""))          


# Problem 4: Star Pattern
def create_star_pattern(n):
  
    pattern = []
    for i in range(1, n + 1):
        pattern.append("*" * i)
    return pattern


def print_star_pattern(n):
    """
    Print the star pattern.
    """
    rows = create_star_pattern(n)
    for row in rows:
        print(row)


# Test function:
print_star_pattern(3)

print()  

print_star_pattern(5)

# Return value test:
result = create_star_pattern(4)
print(result) 


# Problem 5: Find Maximum 
def find_maximum(numbers):
   
    if len(numbers) == 0:
        return None
    
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


# Test  function:
print(find_maximum([5, 2, 8, 1, 9]))     
print(find_maximum([10, 20, 30]))        
print(find_maximum([-1, -2, -8]))        
print(find_maximum([42]))                 
print(find_maximum([]))                   