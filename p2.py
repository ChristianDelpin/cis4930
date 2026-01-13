"""
CIS-4930 Introduction to Python, Spring 2026
Homework : 0
Student Name: Christian Delpin
Student ID: CAD23J
Section: 3
Submission Date: [MM-DD-YYYY]
"""
# Problem 2: Astronaut Training Fatigue Tracker

n = int(input("Enter number of hours tracked: ")) # TODO: See if input validation is necessary.
fatigue_levels = []
for i in range(n):
    fatigue = int(input(f"Hour {i + 1} fatigue level: "))
    if(fatigue < 1 or fatigue > 10):
        print("Invalid fatigue level. Please enter a value between 0 and 10.")
        # re-prompt for the same hour maybe with a continue statement?
    fatigue_levels.append(fatigue)
    i += 1