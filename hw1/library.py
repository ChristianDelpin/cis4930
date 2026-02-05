from datetime import date

def days_overdue(due_date, today):
    if due_date is None:
        return 0
    if today > due_date:
        return (today - due_date).days
    return 0

def format_status(book):
    title = book.get('title', 'Unknown')
    status = book.get('status', 'unknown')
    due_date = book.get('due_date')

    parts = [f"{title} ({status})"]

    if due_date is not None:
        parts.append(f"Due: {due_date.strftime('%b %d, %Y')}")
        overdue_days = days_overdue(due_date, date.today())
        if overdue_days > 0:
            parts.append(f"({overdue_days} days overdue)")

    return " ".join(parts)

def print_inventory(inventory):
    for book in inventory:
        print(format_status(book))
    total = len(inventory)
    available = 0
    overdue = 0
    for b in inventory:
        status = b.get('status', 'unknown')
        if status == 'available':
            available += 1
        elif status == 'overdue':
            overdue += 1
    plural = 's' if total != 1 else ''
    print(f"\nSummary: {total} book{plural} total, {available} available, {overdue} overdue.\n")