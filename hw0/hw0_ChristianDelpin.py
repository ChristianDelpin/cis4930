"""
CIS-4930 Introduction to Python, Spring 2026
Homework : 0
Student Name: Christian Delpin
Student ID: CAD23J
Section: 3
Submission Date: [MM-DD-YYYY]
"""

# Problem 1: Planetary Cargo Weight Checker

destination = input("What planet is this cargo headed to: ").lower() # TODO: See if input validation is necessary.
qty = int(input("How many items are in your shipment: ")) # TODO: See if input validation is necessary.

total_weight = 0

# TODO: See if it should print out overweight even before reaching the end of # of items.
for i in range(qty):
    total_weight += float(input("Item weight in kg: ")) # TODO: See if input validation is necessary.
    i += 1

msg = "OVER LIMIT"
if destination == "earth":
    if total_weight <= 500:
        msg = "OK"
elif destination == "moon":
    if total_weight <= 300:
        msg = "OK"
elif destination == "mars": 
    if total_weight <= 250:
        msg = "OK"
print(f"Weight: {total_weight:.2f} kg")
print(msg)

# Problem 2: Astronaut Training Fatigue Tracker

n = int(input("Enter number of hours tracked: ")) # TODO: See if input validation is necessary.

fatigue_levels = []
fatigue_increase = 0
fatigue_min = 11
fatigue_max = -1
fatigue_previous = 0
fatigue_danger = 8
fatigue_danger_count = 0
fatigue_danger_flag = False
for i in range(n):
    fatigue = int(input(f"Hour {i + 1} fatigue level: "))
    if(fatigue < 1 or fatigue > 10):
        print("Invalid fatigue level. Please enter a value between 0 and 10.")
        # re-prompt for the same hour maybe with a continue statement?
    fatigue_levels.append(fatigue)
    
    # Track min fatigue
    if fatigue < fatigue_min:
        fatigue_min = fatigue
    
    # Track max fatigue
    if fatigue > fatigue_max:
        fatigue_max = fatigue
    
    # Track fatigue increases
    if i == 0:
        fatigue_previous = fatigue
    else:
        if fatigue > fatigue_previous:
            fatigue_increase += 1
        fatigue_previous = fatigue
    
    # Track if fatigue is in danger zone
    if fatigue >= fatigue_danger: # Short circuiting to avoid unnecessary checks
        fatigue_danger_flag = True
        fatigue_danger_count += 1

    i += 1

# Risk Check
if fatigue_danger_flag:
    print("HIGH RISK - Medical review required")
elif fatigue_increase > 3:
    print("MODERATE RISK - Extra rest recommended")
else:
    print("NORMAL - Proceed")

# Mission Log
print(f"Hours Tracked: {n}, Max fatigue: {fatigue_max}, Dangerous hours: {fatigue_danger_count}, Increases: {fatigue_increase}")
    
# Problem 3: Interactive "Dungeon Door" Code Puzzle

energy = 0
io = ""
quit_flag = False
while energy < 50 and io != "quit":
    io = input("Enter an integer (or 'quit' to give up):")
    if io == "quit":
        quit_flag = True
        break
    energy += int(io)
    if energy <= 0:
        energy = 0
        print("Door resets!")
if quit_flag:
    print(f"You gave up with energy {energy}")
else:
    print(f"Door opens with energy {energy}")

# Problem 4: Librarian's Overdue Book Fine Calculator

book_type = input("Enter book type: ")
days_overdue = int(input("Enter number of days overdue: "))
borrower_age = int(input("Enter borrower's age: "))

fine = 0.0
standard_rate = 0.25
base_fine = 0.0
youth_fee_waive = 0.0
overdue_fee_applied = False

# I'm sorry about the icky creation below. I was required to have all of the applications to the fee within a nested if. I must repent for my sins now.
if book_type == "novel":
    fine = standard_rate * days_overdue
    base_fine = fine
    if borrower_age < 12:
        youth_fee_waive = fine * 0.5
        fine -= youth_fee_waive
    if days_overdue > 30:
        fine += 5
        overdue_fee_applied = True
elif book_type == "textbook":
    fine = standard_rate * 2 * days_overdue
    base_fine = fine
    if borrower_age < 12:
        youth_fee_waive = fine * 0.5
        fine -= youth_fee_waive
    if days_overdue > 30:
        fine += 5
        overdue_fee_applied = True
elif book_type == "childrens":
    fine = standard_rate * 0.5 * days_overdue
    base_fine = fine
    if borrower_age < 12:
        youth_fee_waive = fine * 0.5
        fine -= youth_fee_waive
    if days_overdue > 30:
        fine += 5
        overdue_fee_applied = True
else:
    print("Unknown type; using novel rate")
    fine = standard_rate * days_overdue
    base_fine = fine
    if borrower_age < 12:
        youth_fee_waive = fine * 0.5
        fine -= youth_fee_waive
    if days_overdue > 30:
        fine += 5
        overdue_fee_applied = True

print(f"\nBook: {book_type}, Days overdue: {days_overdue}, Borrower age: {borrower_age}")
print(f"Base fine: ${base_fine:.2f}")
if youth_fee_waive > 0:
    print(f"Youth discount applied: -${youth_fee_waive:.2f}")
if overdue_fee_applied:
    print("Long overdue fee: $5.00")
else:
    print("Long overdue fee: $0.00")

print(f"Total due: ${fine:.2f}")

# Problem - 5. “Guess the Number” with Adaptive Hints 

num = 36
guess_count = 0
guess = 0
while guess != num:
    guess = int(input(f"Enter a guess: "))
    guess_count += 1
    if guess == num:
        print(f"Correct! You found it in {guess_count} guesses.")
    elif num >= guess - 5 and num <= guess + 5:
        print("Very close!")
    elif num >= guess - 15 and num <= guess + 15:
        print("Warm")
    elif guess > num:
        print("Too high")
    else:
        print("Too low")
        
print(f"Secret number: {num}, your final guess: {guess}, total guesses: {guess_count}")