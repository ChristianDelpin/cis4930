"""
CIS-4930 Introduction to Python, Spring 2026
Homework : 1
Student Name: Christian Delpin
Student ID: CAD23J
Section: 3
Submission Date: [MM-DD-YYYY]
"""

# Problem 1: Campus WiFi Access Log Analyzer
wifi_logs = [
# bldg  dvc hr
("LIB", 45, 9), 
("LIB", 92, 11),
("CSC", 67, 14),
("LIB", 78, 13),
("ENG", 120, 10),
("CSC", 55, 15),
("ENG", 89, 16)
]

# Using set to find all bldgs with >50 devices connected

high_traffic_bldgs = set()
for log in wifi_logs:
    bldg, device_count, time_of_day = log
    if device_count > 50:
        high_traffic_bldgs.add(bldg)

# Using list comprehension to find all hours with >80 devices connected
high_traffic_hours = [(bldg, time_of_day) for bldg, device_count, time_of_day in wifi_logs if device_count > 80]

# Using slicing to iterate and count num devices for LIB bldg only
lib_device_counts = 0
for log in wifi_logs[:]:
    bldg, device_count, time_of_day = log
    if bldg == "LIB":
        lib_device_counts+=device_count

# Identify busiest bldg by avg devices
bldg_device_totals = {}
for log in wifi_logs:
    bldg, device_count, time_of_day = log
    if bldg not in bldg_device_totals:
        bldg_device_totals[bldg] = [0, 0]  # total devices, count
    bldg_device_totals[bldg][0] += device_count
    bldg_device_totals[bldg][1] += 1

bldg_avg_devices = {}
for bldg, totals in bldg_device_totals.items():   
    bldg_avg_devices[bldg] = totals[0] // totals[1]

max_blg_avg = 0
busiest_bldg = ""
for bldg, avg in bldg_avg_devices.items():
    if avg > max_blg_avg:
        max_blg_avg = avg
        busiest_bldg = bldg

# Results

print(f"Set of high traffic buildings: {high_traffic_bldgs}")
print(f"High traffic hours: {high_traffic_hours}")
print(f"Number of devices in LIB: {lib_device_counts}")
print(f"Busiest building by average number of devices: {busiest_bldg} with an average of {max_blg_avg} devices.")

# Problem 2: University Course Planner

#dict of courses
#each course has: code, title, num_credits, prereq_list

courses = {
    "CIS4930": {
        "title": "Special Topics in Computer Science",
        "crenum_creditsdits": 3,
        "prereq_list": ["COP3330"]
    },
    "CEN4020": {
        "title": "Software Engineering 1",
        "num_credits": 3,
        "prereq_list": ["COP4530"]
    },
    "CDA3100": {
        "title": "Computer Organization 1",
        "num_credits": 3,
        "prereq_list": ["COP3330"]
    },
    "CNT4504":{
        "title": "Introduction to Computer Networks",
        "num_credits": 3,
        "prereq_list": ["COP4530"]
    },
    "COP3330":{
        "title": "Data Structures, Algorithms and Generic Programming 1",
        "num_credits": 3,
        "prereq_list": ["COP3014", "COP3353"]
    },
    "COP3014":{
        "title": "Programming 1",
        "num_credits": 3,
        "prereq_list": []
    }
}


user_input = input("Enter a course code: ").upper()


if user_input in courses:
    course = courses.get(user_input)
    print(f"{user_input} - {course["title"]}")

    prereqs = course.get("prereq_list", [])
    if prereqs: # checking if list is empty
        print(f"Pre-requisite(s): {prereqs}")
    else:
        print("Pre-requisite(s): None")

    total_credits = course["num_credits"]
    for i in course["prereq_list"]:
        if i in courses:
            total_credits+=courses[i].get("num_credits")
        else:
            continue
    print(f"Total credits with prereqs: {total_credits}")
else:
    print("Course not found.")

# Problem 3: Cafeteria Menu and Order Validator