"""
CIS-4930 Introduction to Python, Spring 2026
Homework : 1
Student Name: Christian Delpin
Student ID: CAD23J
Section: 3
Submission Date: [02-19-2026]
"""

import json
import csv
import datetime




class ErrorLogger:
    def __init__(self, file_path="grade_errors.log"):
        self.log_file = open(file_path, 'a')  # Keep file open

    def log(self, message, log_type="ERROR"):
        self.log_file.write(f"[{datetime.datetime.now().isoformat(timespec='seconds')}] {log_type}: {message}\n")
        self.log_file.flush()

error_logger = ErrorLogger()

class InvalidGradeError(Exception):
    def __init__(self, row, config):
        super().__init__(f"{row[0]},{row[1]} - grade {row[2]} outside of range [{config['min_grade']}, {config['max_grade']}]")
        error_logger.log(f"{row[0]},{row[1]} - grade {row[2]} outside of range [{config['min_grade']}, {config['max_grade']}]") 


def load_valid_courses():
    with open("valid_courses.json", "r", encoding="utf-8") as f:
        config = json.load(f)
        assert 'min_grade' in config and 'max_grade' in config, "config needs min_grade and max_grade"
        assert config['min_grade'] <= config['max_grade'], "min_grade must be <= max_grade"
        return config

def read_grades(config):
    # requirements:
    # 1. read
    # 2. convert to float safely
    #   a. handle conversion/validation errors
    grades = []
    valid_count = 0
    invalid_count = 0
    valid = False
    with open("grades.csv", 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        assert len(header) >= 3, "grades.csv must have at least id,name,grade columns"
        for row in reader:

            try:
                grade = float(row[2])
            except ValueError:
                # print(row[0])
                error_logger.log(f"{row[0]},{row[1]} - invalid grade '{row[2]}' (ValueError)")
                invalid_count += 1
                continue
            
            try:
                if grade < config['min_grade'] or grade > config['max_grade']:
                    raise InvalidGradeError(row, config)
            except InvalidGradeError:
                invalid_count += 1
                continue
            else:
                id = row[0]
                name = row[1]
                grades.append({
                    "student_id": id,
                    "name" : name,
                    "grade": grade
                })
                valid_count += 1
                valid = True
                if valid:
                    print(f"Processed {name}: {grade}")
                print(f"Processed row {valid_count + invalid_count}")
    
    print(f"Processed grades.csv:\n{valid_count} grades saved to valid_grades.json\n{invalid_count} errors logged to grade_errors.log")
    return grades

def write_grades(grades):
    with open("valid_grades.json", "w", encoding="utf-8") as f:
        json.dump(grades, f, indent=2)

def main():
    config = load_valid_courses()
    g = read_grades(config)
    write_grades(g)


if __name__ == "__main__":
    main()