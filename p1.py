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
    total_weight += float(input(f"Item weight in kg: ")) # TODO: See if input validation is necessary.
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

print(msg)