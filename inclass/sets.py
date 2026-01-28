students = [("Alice", "CS"), ("Bob", "Math"), ("Charlie", "CS"), ("David", "Physics")] # Is type list containing type tuples
present = ["Alice", "David"]

s_present = set(present) # Converted to set because sets will hash the data for faster lookup
for name, major in students:
    print(f"{name} - {major}")

print("\nAttendance Report:")
for name, major in students:
    status = "present" if name in s_present else "absent" # Converted to set because sets will hash the data for faster lookup
    print(f"{name} - {major} - {status}")

students_cs_present = [name for name, major in students if major == "CS" and name in s_present] # List comprehension to filter CS students who are present