"""
CIS-4930 Introduction to Python, Spring 2026
Homework : 3
Student Name: Christian Delpin
Student ID: CAD23J
Section: 3
Submission Date: [03-01-2026]
"""

from abc import ABC, abstractmethod


class Movie:
    def __init__(self, title, duration, genre):
        self.title = title
        self.duration = duration
        self.genre = genre

        if duration > 60: # Change value here to determine what is "long" for a movie, as nothing is given in the documentation.
            self.ticket_price = 12
        else:
            self.ticket_price = 10

    def __str__(self):
        return f"{self.title} ({self.duration} min): {self.genre}"
    
    def __repr__(self):
        return f"Title: {self.title}, Duration: {self.duration}, Genre: {self.genre}, Ticket Price: ${self.ticket_price}"

class Customer:
    def __init__(self, name, member_id, favorite_genre = "Any", loyalty_points = 0):
        self.name = name
        self.member_id = member_id
        self.favorite_genre = favorite_genre
        self.showtimes = []
        self._loyalty_points = 0
        self.loyalty_points = loyalty_points

    def loves_genre(self, genre):
        return genre == self.favorite_genre # It's not specified how to check this, and this is the only way that makes sense with the givens.
    def buy_ticket(self, movie):
        pass # No specification how to do this. Am I meant to use loyalty points? Or check if sufficient money provided? Am I meant to return something? Do I add to showtimes?
    
    def __str__(self):
        return f"{self.name} ({self.favorite_genre} fan, {self.loyalty_points} pts)"
    
    def add_showtime(self, showtime):
        self.showtimes.append(showtime)

    @property
    def loyalty_points(self):
        return self._loyalty_points

    @loyalty_points.setter
    def loyalty_points(self, value):
        if value < 0:
            value = 0
        elif value > 10000:
            value = 10000
        self._loyalty_points = value

class VIPCustomer(Customer):
    
    def __init__(self, name, member_id, vip_tier, favorite_genre = "Any", loyalty_points = 0):
        super().__init__(name, member_id, favorite_genre, loyalty_points)
        self.vip_tier = vip_tier
    
    def perks(self): # No specification on what perks to give, so I just made some up.
        if self.vip_tier == "Diamond":
            return "Free popcorn and drinks, priority seating, and exclusive screenings."
        elif self.vip_tier == "Platinum":
            return "Priority seating and exclusive screenings."
        elif self.vip_tier == "Gold":
            return "Exclusive screenings."
        else:
            return "No perks available for this VIP tier."

    def __str__(self):
        return super().__str__() + f", VIP Tier: {self.vip_tier}"
    
class Showtime(ABC):
    def __init__(self, movie, price):
        self.movie = movie
        self.price = price

    @abstractmethod
    def revenue_potential(self):
       """Calculate revenue potential"""
       pass

    def __str__(self):
        return f"{type(self).__name__} for {getattr(self.movie, 'title', 'Unknown')} (${self.price})"

    def __repr__(self):
        return self.__str__()

class Matinee(Showtime):
    def __init__(self, movie):
        super().__init__(movie, 8)

    def revenue_potential(self):
        """Calculate revenue potential"""
        return self.price * 0.3 # Assuming 30% profit margin for simplicity, as no specification is given.

class EveningPremiere(Showtime):
    def __init__(self, movie):
        super().__init__(movie, movie.ticket_price)
    
    def revenue_potential(self):
        """Calculate revenue potential"""
        return self.price * 0.5 # Assuming 50% profit margin for simplicity, as no specification is given.

class TheaterManager:
    def __init__(self):
        self.movies = []
        self.customers = []
    
    def add_movie(self, movie): # Not specified to add this, but it seems like it's necessary since the vars would be useless
        """Add a movie to the theater manager's list of movies."""
        self.movies.append(movie)
    
    def add_customer(self, customer): # Not specified to add this, but it seems like it's necessary since the vars would be useless
        """Add a customer to the theater manager's list of customers."""
        self.customers.append(customer)
    
    def customers_who_love_action(self):
        """Return a list of customers whose favorite genre is 'Action'."""
        return [c for c in self.customers if c.loves_genre("Action")]

    def customer_loyalty_map(self):
        """Return a dict mapping customer member_id -> loyalty_points."""
        return {c.member_id: c.loyalty_points for c in self.customers}

    def yield_customer_showtimes_for_movie(self, movie_title):
        """Generator yielding (customer_name, showtime_type) for a given movie title.

        Example:
            for name, stype in manager.yield_customer_showtimes_for_movie("Inception"):
                print(name, stype)
        """
        for customer in self.customers:
            for showtime in customer.showtimes:
                if hasattr(showtime, 'movie') and getattr(showtime.movie, 'title', None) == movie_title:
                    yield (customer.name, type(showtime).__name__)

class main():
    manager = TheaterManager()

    movie1 = Movie("Inception", 148, "Action")
    movie2 = Movie("The Lion King", 88, "Animation")

    manager.add_movie(movie1)
    manager.add_movie(movie2)

    customer1 = Customer("Alice", "C001", "Action", 150)

    # INHERITANCE EXAMPLE
    customer2 = VIPCustomer("Bob", "C002", "Gold", "Animation", 300)

    print("INHERITANCE EXAMPLE:\n")


    manager.add_customer(customer1)
    manager.add_customer(customer2)

    for c in manager.customers:
        if isinstance(c, VIPCustomer):
            print(f"{c} - Perks: {c.perks()}")
        else:
            print(c)

    print() # just for spacing.

    showtime1 = Matinee(movie1)
    showtime2 = Matinee(movie2)
    showtime3 = EveningPremiere(movie1)
    showtime4 = EveningPremiere(movie2)

    customer1.add_showtime(showtime1)
    customer2.add_showtime(showtime2)
    customer2.add_showtime(showtime3)
    # ENCAPSULATION EXAMPLE
    print("ENCAPSULATION EXAMPLE:\n")
    customer1.loyalty_points = -50   # setter will clamp to 0
    customer2.loyalty_points = 20000 # setter will clamp to 10000

    print(customer1)
    print(customer2)

    # ABSTRACTION EXAMPLE
    print("\nABSTRACTION EXAMPLE:")
    total_revenue = sum(times.revenue_potential() for c in manager.customers for times in c.showtimes)
    print(f"\nTotal revenue potential: ${total_revenue:.2f}")

    # POLYMORPHISM EXAMPLE
    print("\nPOLYMORPHISM EXAMPLE:")
    
    print("\nCustomers who love Action movies:")
    for c in manager.customers_who_love_action():
        print(c)

    print("\nCustomer Loyalty Map:")
    loyalty_map = manager.customer_loyalty_map()
    for member_id, points in loyalty_map.items():
        print(f"{member_id}: {points} points")
    
    print("\nCustomer Showtimes for 'Inception':")
    for name, showtime_type in manager.yield_customer_showtimes_for_movie("Inception"):
        print(f"{name} has a {showtime_type} for Inception.")