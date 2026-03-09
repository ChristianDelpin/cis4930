"""
CIS-4930 Introduction to Python, Spring 2026
Homework : 3
Student Name: Christian Delpin
Student ID: CAD23J
Section: 3
Submission Date: [03-01-2026]
"""


# given
sales = [
{"title": "Python Tricks", "price": 30.0, "genre": "Programming",
"copies": 2},
{"title": "Gardening 101", "price": 18.5, "genre": "Hobby",
"copies": 1},
{"title": "Deep Learning", "price": 45.0, "genre": "Programming",
"copies": 1},
{"title": "Time Management", "price": 22.0, "genre": "Self-help",
"copies": 3},
{"title": "Fluent Python", "price": 40.0, "genre": "Programming",
"copies": 1},
]


def was_sold(sales, title):
    # Time complexity: O(n) where n is the number of sales records.
    for sale in sales:
        if sale["title"] == title:
            return True
    return False

def find_first_by_genre(sales, genre):
    # Worst case time complexity: O(n) where n is the number of sales records.
    index = 0
    for sale in sales:
        if sale["genre"] == genre:
            return index
        index += 1
    return None

def top_revenue(sales):
    # Time complexity: O(n log n) where n = len(sales)
    
    # key: (-revenue, title) so that primary sort is revenue descending
    # and secondary is title ascending (alphabetical)
    return sorted(sales, key=lambda s: (-(s.get("price", 0) * s.get("copies", 0)), s.get("title", "")))


def unique_genres(sales):
        """Return an alphabetically-sorted list of unique genres from `sales`.

        Implementation notes:
        - Use a `set` to collect seen genres because average-case membership
            tests and inserts are O(1), making it efficient when repeatedly
            checking whether we've already encountered a genre while scanning
            the `sales` list.
        - After building the set of unique genres, convert it to a sorted
            list before returning.

        Time complexity:
        - Building the set: O(n) where n = len(sales) (each record visited once,
            and each insert/lookup is O(1) average-case).
        - Sorting the unique genres: O(m log m) where m = number of unique genres.
        - Overall: O(n + m log m).
        """

        # `set()` is efficient for repeated checks because it hashes items when checking if it's in the set, meaning average case of o(1) time complexity.
        # Total time complexity for building and sorting is O(n + m log m) where n = len(sales) and m = number of unique genres.
        #                                                   O(n) for building, O(m log m) for sorting
        seen = set()
        for s in sales:
                genre = s.get("genre")
                if genre is not None:
                        seen.add(genre)
        return sorted(seen)


# Scale Analysis

# Is single `was_sold()` call with linear scan acceptable in practice?
# No. Since sales grow linearly at 100k/day, it will take an extreme amount of time to scan through all sales for the current O(n) complexity.

# If the owner calls `was_sold()` thousands of times daily, what design change? Why (complexity terms)?
# Modify the function to use the `set` data struct, meaning O(1) average case complexity on checking if a title was sold.
# This would significantly reduce time taken for each func call, especially if sales grow with the previous 100k/day rate.


print(was_sold(sales, "Python Tricks")) # True
print(find_first_by_genre(sales, "Programming")) # 0
print(unique_genres(sales)) # ['Hobby','Programming', 'Self-help']