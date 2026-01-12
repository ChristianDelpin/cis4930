"""
CIS-4930 Introduction to Python, Spring 2026
Homework : 0
Student Name: Christian Delpin
Student ID: CAD23J
Section: 3
Submission Date: [MM-DD-YYYY]
"""

# Problem 1: Planetary Cargo Weight Checker

# TODO: Check if need to define every function for every problem then call via main(). For now, using.

def planetary_cargo_weight_checker():
    # TODO: Change below to not use dict
    planetary_weights = {
        "earth": 500,
        "moon": 300,
        "mars": 250
    }

    destination = input("What planet is this cargo headed to: ").lower() # TODO: See if input validation is necessary.
    qty = int(input("How many items are in your shipment: ")) # TODO: See if input validation is necessary.

    total_weight = 0

    # TODO: See if it should print out overweight even before reaching the end of # of items.
    for i in range(qty):
        total_weight += float(input(f"Item weight in kg: ")) # TODO: See if input validation is necessary.
        i += 1
    
    if total_weight <= planetary_weights[destination]:
        print("OK")
    else:
        print("OVER LIMIT")


# Problem 2: Astronaut Training Fatigue Tracker

def astronaut_training_fatigue_tracker():
    n = int(input("Enter number of hours tracked: ")) # TODO: See if input validation is necessary.

    fatigue_levels = []
    for i in range(n):
        fatigue = int(input(f"Hour {i + 1} fatigue level: "))
        if(fatigue < 1 or fatigue > 10):
            print("Invalid fatigue level. Please enter a value between 0 and 10.")
            # re-prompt for the same hour maybe with a continue statement?
        fatigue_levels.append(fatigue)
        i += 1

    print("End")






def main():    
    #planetary_cargo_weight_checker()
    astronaut_training_fatigue_tracker()

if __name__ == "__main__":
    main()