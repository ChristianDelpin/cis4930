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


class Logger:
    def __init__(self, config_path='config.json'):
        with open(config_path, 'r') as f:
            config = json.load(f)
        self.log_file = open(config['log_file'], 'a')
    
    def log(self, message, log_type="PROCESS"):
        self.log_file.write(f"[{datetime.datetime.now()}] {log_type}: {message}\n")
        self.log_file.flush()

logger = Logger()

def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
        logger.log(f"Loaded configuration")
        return config

def parse_attendees():
    attendees = []
    with open("attendees_raw.txt", "r", encoding="utf-8") as f:
       for line in f:
           parts = line.strip().split(",")
           attendees.append({
               "id": parts[0],
               "name": parts[1],
               "email": parts[2]
           })
    logger.log(f"Loaded {len(attendees)} attendees from attendees_raw.txt")
    return attendees

def new_registrations(attendees):
    with open("new_registrations.csv", "r", newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)

        count = 0
        for row in reader:
            if row[0] in [a["id"] for a in attendees]:
                continue
            attendees.append({
                "id": row[0],
                "name": row[1],
                "email": row[2]
            })
            count += 1
    logger.log(f"Merged {count} new attendees from new_registrations.csv")
    return attendees

def create_attendees_json(attendees):
    with open("attendees_final.json", "w", encoding="utf-8") as f:
        json.dump(attendees, f, indent=2, ensure_ascii=False)
    logger.log(f"Wrote {len(attendees)} total attendees to attendees_final.json")

def vip_report(config, attendees):
    count = 0
    with open("vip_report.txt", "w", encoding="utf-8") as f:
        for vip_id in config.get("vip_ids", []):
            found = False
            for a in attendees:
                if a["id"] == vip_id:
                    f.write(f"{vip_id}: {a['name']} <{a['email']}>\n")
                    found = True
                    count += 1
                    break
            if not found:
                f.write(f"{vip_id}: NOT FOUND\n")
    logger.log(f"Wrote VIP report for {count} IDs to vip_report.txt")

def main():
    config = load_config()
    attendees = parse_attendees()
    attendees = new_registrations(attendees)
    create_attendees_json(attendees)
    vip_report(config, attendees)

if __name__ == "__main__":
    main()