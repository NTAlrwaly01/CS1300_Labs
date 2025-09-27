"""
CS 1300 - Homework #6
Name: Nawaf T Alrwaly
Date: 09/27/2025
Description: Introduction to Lists - Creation, Indexing, Slicing, Methods
"""

# ============================
# Part 1: List Creation Basics
# ============================
print("="*50)
print("PART 1: LIST CREATION")
print("="*50)

# Problem 1.1: Your First Lists
print("\n--- Problem 1.1: Your First Lists ---")
my_classes = ["English", "Math", "History", "Biology"]
my_grades = [85, 92, 78, 95, 88]
my_notes = []
print("Classes:", my_classes)
print("Grades:", my_grades)
print("Notes:", my_notes)

# Problem 1.2: Different Types in Lists
print("\n--- Problem 1.2: Different Types in Lists ---")
about_me = ["Nawaf", 21, 5.9, True]
mixed_bag = [42, "Hello", 3.14, [1, 2, 3]]
print("About me:", about_me)
print("Mixed bag:", mixed_bag)

# Problem 1.3: Creating Lists Different Ways
print("\n--- Problem 1.3: Creating Lists Different Ways ---")
zeros = [0] * 10
letters = list("HELLO")
pattern = [1, 2] * 3
print("Zeros:", zeros)
print("Letters:", letters)
print("Pattern:", pattern)

# ===============================
# Part 2: Accessing List Elements
# ===============================
print("\n" + "="*50)
print("PART 2: ACCESSING ELEMENTS")
print("="*50)

# Problem 2.1: Reading from Lists
print("\n--- Problem 2.1: Reading from Lists ---")
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
print("Months list:", months)
print("Length:", len(months))
print("First month:", months[0])
print("Sixth month:", months[5])
print("Last month (positive index):", months[len(months)-1])
print("Last month (negative index):", months[-1])
print("December by positive index:", months[11])
print("January by negative index:", months[-12])
print("Month at index 7:", months[7])

# Problem 2.2: Modifying List Elements
print("\n--- Problem 2.2: Modifying Elements ---")
temperatures = [72, 75, 71, 73, 74, 76, 70]
print("Original:", temperatures)
temperatures[1] = 77      # Monday
temperatures[4] = 78      # Friday
temperatures[0] = 74      # Sunday
temperatures[-1] = 72     # Saturday
temperatures[2] = 75      # Wednesday
print("Corrected:", temperatures)
print("Number of days:", len(temperatures))
print("Index of last day:", len(temperatures)-1)

# Problem 2.3: Index Errors and Safety
print("\n--- Problem 2.3: Index Errors and Safety ---")
colors = ["red", "blue", "green"]
if 1 < len(colors):
    print("Index 1:", colors[1])
if 5 < len(colors):
    print("Index 5:", colors[5])
else:
    print("Index 5 does not exist")
if len(colors) > 0:
    print("First element:", colors[0])
if len(colors) >= 1:
    print("Last element:", colors[-1])
if -4 >= -len(colors):
    print("Index -4:", colors[-4])
else:
    print("Index -4 is invalid")
print("Smallest valid negative index:", -len(colors))

# ========================
# Part 3: List Slicing
# ========================
print("\n" + "="*50)
print("PART 3: LIST SLICING")
print("="*50)

# Problem 3.1: Basic Slicing
print("\n--- Problem 3.1: Basic Slicing ---")
numbers = [10,20,30,40,50,60,70,80,90,100]
print("First 4:", numbers[0:4])
print("Last 3:", numbers[-3:])
print("Index 2 to 6:", numbers[2:7])
print("From 5 to end:", numbers[5:])
print("Start to 4:", numbers[:5])
print("Complete copy:", numbers[:])
print("Empty slice:", numbers[3:3])

# Problem 3.2: Slicing with Steps
print("\n--- Problem 3.2: Step Slicing ---")
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
print("Every 3rd:", alphabet[::3])
print("Every other from b:", alphabet[1::2])
print("Reversed:", alphabet[::-1])
mid = len(alphabet)//2
print("First half:", alphabet[:mid])
print("Second half:", alphabet[mid:])
print("Indices 2-8 every other:", alphabet[2:9:2])
print("Reverse first 5:", alphabet[0:5][::-1])

# Problem 3.3: Practical Slicing
print("\n--- Problem 3.3: Practical Slicing ---")
hourly_temps = [55,54,53,52,52,54,58,62,66,70,73,75,76,77,77,76,74,71,68,65,62,59,57,55]
print("Morning (0-5):", hourly_temps[:6])
print("Afternoon (12-17):", hourly_temps[12:18])
print("Evening (18-23):", hourly_temps[-6:])
print("Every other hour:", hourly_temps[::2])
print("Middle 4 hours (10-13):", hourly_temps[10:14])
print("6-9am:", hourly_temps[6:10])

# ==============================
# Part 4: List Methods - Adding
# ==============================
print("\n" + "="*50)
print("PART 4: ADDING ITEMS")
print("="*50)

# Problem 4.1: append()
print("\n--- Problem 4.1: append() ---")
shopping_list = []
shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("eggs")
shopping_list.append("cheese")
shopping_list.append("apples")
print("Shopping list:", shopping_list)
favorites = []
favorites.append("Pizza")
favorites.append("Pasta")
favorites.append("Ice cream")
print("Favorites:", favorites)

# Problem 4.2: insert()
print("\n--- Problem 4.2: insert() ---")
line = ["Alice", "Bob", "Charlie"]
line.insert(0, "David")
line.insert(2, "Eve")
line.insert(len(line), "Frank")
print("Final line:", line)
schedule = ["Math", "History", "Science"]
schedule.insert(2, "Lunch")
schedule.insert(0, "Homeroom")
print("Updated schedule:", schedule)

# Problem 4.3: extend()
print("\n--- Problem 4.3: extend() ---")
primary_colors = ["red","blue","yellow"]
secondary_colors = ["green","orange","purple"]
primary_colors.extend(secondary_colors)
print("All colors:", primary_colors)
list1 = [1,2,3]
list1.append([4,5])
print("Append:", list1)
list2 = [1,2,3]
list2.extend([4,5])
print("Extend:", list2)
my_list = ["a","b"]
my_list.append(["c","d"])
print("Append with ['c','d']:", my_list)
my_list = ["a","b"]
my_list.extend(["c","d"])
print("Extend with ['c','d']:", my_list)

# ==============================
# Part 5: List Methods - Removing
# ==============================
print("\n" + "="*50)
print("PART 5: REMOVING ITEMS")
print("="*50)

# Problem 5.1: remove()
print("\n--- Problem 5.1: remove() ---")
pets = ["dog","cat","bird","cat","fish","cat"]
pets.remove("bird")
pets.remove("cat")
print("After removals:", pets)
if "hamster" in pets:
    pets.remove("hamster")
numbers = [5,3,8,3,9,3,2]
while 3 in numbers:
    numbers.remove(3)
print("Removed all 3s:", numbers)

# Problem 5.2: pop()
print("\n--- Problem 5.2: pop() ---")
stack = [10,20,30,40,50]
last_item = stack.pop()
print("Popped:", last_item, "Stack now:", stack)
first_item = stack.pop(0)
middle_item = stack.pop(1)
print("After more pops:", stack)
queue = ["Person1","Person2","Person3","Person4"]
served = queue.pop(0)
queue.pop(-1)
print("Served:", served)
print("Queue now:", queue)

# Problem 5.3: del and clear()
print("\n--- Problem 5.3: del and clear() ---")
data = [100,200,300,400,500,600,700]
del data[0]
del data[2]
del data[1:3]
print("After deletions:", data)
readings = [0,5,-999,10,15,-999,20]
while -999 in readings:
    readings.remove(-999)
print("Clean readings:", readings)

# ============================================
# Part 6: Membership and Length Operations
# ============================================
print("\n" + "="*50)
print("PART 6: MEMBERSHIP AND LENGTH")
print("="*50)

# Problem 6.1: in and not in
print("\n--- Problem 6.1: Membership ---")
valid_grades = ['A','B','C','D','F']
print("Is 'B' valid?", 'B' in valid_grades)
print("Is 'E' not valid?", 'E' not in valid_grades)
user_grade = 'C'
print("User grade valid?", user_grade in valid_grades)
menu_options = [1,2,3,4,5]
print("Option 3 available?", 3 in menu_options)
print("Option 9 available?", 9 in menu_options)
enrolled = ["Alice","Bob","Charlie","Diana"]
print("Is Eve enrolled?", "Eve" in enrolled)
if "Frank" not in enrolled:
    enrolled.append("Frank")
to_check = ["Alice","Eve","Bob","George"]
print("Alice enrolled?", "Alice" in enrolled)
print("Eve enrolled?", "Eve" in enrolled)
print("Bob enrolled?", "Bob" in enrolled)
print("George enrolled?", "George" in enrolled)

# Problem 6.2: len()
print("\n--- Problem 6.2: len() ---")
tasks = ["homework","dishes","laundry","shopping","exercise"]
print("Number of tasks:", len(tasks))
print("Index of last task:", len(tasks)-1)
print("More than 3 tasks?", len(tasks) > 3)
middle_index = len(tasks)//2
print("Middle task:", tasks[middle_index])
inbox = []
if len(inbox) == 0:
    print("Inbox is empty (len)")
if not inbox:
    print("Inbox is empty (falsy)")
waiting = ["P1","P2"]
max_capacity = 4
spaces = max_capacity - len(waiting)
print("Spaces available:", spaces)
if len(waiting)<max_capacity: waiting.append("P3")
if len(waiting)<max_capacity: waiting.append("P4")
print("Updated waiting:", waiting)

# ==========================
# Bonus: Inventory System
# ==========================
print("\n" + "="*50)
print("BONUS: INVENTORY SYSTEM")
print("="*50)
inventory = ["apples","bananas","milk","bread","eggs"]
quantities = [10,15,5,8,24]
print("Current Inventory:")
print(inventory[0], quantities[0])
print(inventory[1], quantities[1])
print(inventory[2], quantities[2])
print(inventory[3], quantities[3])
print(inventory[4], quantities[4])
quantities[0] -= 3
quantities[2] += 10
inventory.append("cheese")
quantities.append(12)
for i in range(len(quantities)):
    if quantities[i] <= 0:
        del inventory[i]
        del quantities[i]
        break
print("Final Inventory:", inventory)
print("Quantities:", quantities)
print("Number of items:", len(inventory))
if quantities[0] < 5: print("Restock", inventory[0])
if quantities[1] < 5: print("Restock", inventory[1])
if quantities[2] < 5: print("Restock", inventory[2])
if quantities[3] < 5: print("Restock", inventory[3])