"""
Comprehensive OOP Exercises with Solutions
Covers all sections: 100-900

Run individual exercises or all at once.
"""

import sys
from abc import ABC, abstractmethod


# ============================================================================
# BEGINNER EXERCISES (Sections 100-200)
# ============================================================================

print("=" * 70)
print("BEGINNER EXERCISES")
print("=" * 70)

# Exercise 1: Create a Dog class
print("\n--- Exercise 1: Dog Class ---")

class Dog:
    """Simple Dog class with basic methods."""
    
    species = "Canis familiaris"
    
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! Now {self.age} years old."
    
    def get_info(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}"


# Test
beau = Dog("Beau", 5, "Dachshund")
elvis = Dog("Elvis", 3, "Dachshund")

print(beau.bark())
print(beau.get_info())
print(beau.birthday())
print(f"Species: {Dog.species}")


# Exercise 2: BankAccount with validation
print("\n--- Exercise 2: Bank Account ---")

class BankAccount:
    """Bank account with deposits and withdrawals."""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self._balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            return "Amount must be positive"
        self._balance += amount
        return f"Deposited €{amount}. New balance: €{self._balance}"
    
    def withdraw(self, amount):
        if amount <= 0:
            return "Amount must be positive"
        if amount > self._balance:
            return "Insufficient funds"
        self._balance -= amount
        return f"Withdrew €{amount}. New balance: €{self._balance}"
    
    def get_balance(self):
        return f"Account balance: €{self._balance}"


# Test
account = BankAccount("Willem van Heemstra", 1000)
print(account.deposit(500))
print(account.withdraw(300))
print(account.get_balance())


# Exercise 3: Rectangle
print("\n--- Exercise 3: Rectangle ---")

class Rectangle:
    """Rectangle with area and perimeter calculations."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        return self.width == self.height


# Test
rect = Rectangle(5, 10)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
print(f"Is square: {rect.is_square()}")


# ============================================================================
# INTERMEDIATE EXERCISES (Sections 300-600)
# ============================================================================

print("\n" + "=" * 70)
print("INTERMEDIATE EXERCISES")
print("=" * 70)

# Exercise 4: Employee Hierarchy
print("\n--- Exercise 4: Employee Hierarchy ---")

class Employee:
    """Base employee class."""
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_details(self):
        return f"{self.name}: €{self.salary}/year"
    
    def calculate_bonus(self):
        return self.salary * 0.10


class Manager(Employee):
    """Manager with department."""
    
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def get_details(self):
        base = super().get_details()
        return f"{base} (Manager, {self.department})"
    
    def calculate_bonus(self):
        return self.salary * 0.20


class Engineer(Employee):
    """Engineer with programming languages."""
    
    def __init__(self, name, salary, languages):
        super().__init__(name, salary)
        self.languages = languages
    
    def get_details(self):
        base = super().get_details()
        langs = ", ".join(self.languages)
        return f"{base} (Engineer: {langs})"


# Test
manager = Manager("Alice", 120000, "Engineering")
engineer = Engineer("Bob", 100000, ["Python", "Go", "Rust"])

print(manager.get_details())
print(f"Bonus: €{manager.calculate_bonus()}")
print(engineer.get_details())
print(f"Bonus: €{engineer.calculate_bonus()}")


# Exercise 5: Shape Polymorphism
print("\n--- Exercise 5: Shape Polymorphism ---")

class Shape(ABC):
    """Abstract base class for shapes."""
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle implementation."""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle implementation."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    """Triangle implementation."""
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        import math
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c


def total_area(shapes):
    """Calculate total area of mixed shapes."""
    return sum(shape.area() for shape in shapes)


# Test
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

print(f"Total area: {total_area(shapes):.2f}")
for i, shape in enumerate(shapes, 1):
    print(f"Shape {i}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")


# ============================================================================
# ADVANCED EXERCISES (Sections 700-900)
# ============================================================================

print("\n" + "=" * 70)
print("ADVANCED EXERCISES")
print("=" * 70)

# Exercise 6: Singleton Pattern
print("\n--- Exercise 6: Singleton Logger ---")

class Logger:
    """Singleton logger implementation."""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.logs = []
    
    def log(self, message, level="INFO"):
        entry = f"[{level}] {message}"
        self.logs.append(entry)
        print(entry)
    
    def get_logs(self):
        return self.logs.copy()


# Test
logger1 = Logger()
logger2 = Logger()

print(f"Same instance: {logger1 is logger2}")

logger1.log("Application started", "INFO")
logger2.log("User logged in", "INFO")

print(f"Total logs: {len(logger1.get_logs())}")


# Exercise 7: Observer Pattern
print("\n--- Exercise 7: Observer Pattern ---")

class Subject:
    """Observable subject."""
    
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)
    
    def set_state(self, state):
        self._state = state
        self.notify()
    
    def get_state(self):
        return self._state


class Observer(ABC):
    """Abstract observer."""
    
    @abstractmethod
    def update(self, subject):
        pass


class ConcreteObserver(Observer):
    """Concrete observer implementation."""
    
    def __init__(self, name):
        self.name = name
    
    def update(self, subject):
        print(f"{self.name} received update: {subject.get_state()}")


# Test
subject = Subject()
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.attach(observer1)
subject.attach(observer2)

subject.set_state("State A")
subject.set_state("State B")


# Exercise 8: Context Manager
print("\n--- Exercise 8: File Manager Context Manager ---")

class FileManager:
    """Context manager for file operations."""
    
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening {self.filename} in mode '{self.mode}'")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print(f"Closing {self.filename}")
            self.file.close()
        return False  # Don't suppress exceptions


# Test (create temp file first)
with open('/tmp/test.txt', 'w') as f:
    f.write("Hello, World!")

with FileManager('/tmp/test.txt', 'r') as f:
    content = f.read()
    print(f"Content: {content}")


# Exercise 9: Magic Methods
print("\n--- Exercise 9: Vector with Magic Methods ---")

class Vector:
    """2D Vector with operator overloading."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    
    def magnitude(self):
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)


# Test
v1 = Vector(3, 4)
v2 = Vector(1, 2)

v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * 2

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v3}")
print(f"v1 - v2: {v4}")
print(f"v1 * 2: {v5}")
print(f"v1 magnitude: {v1.magnitude()}")
print(f"v1 == v2: {v1 == v2}")


# Exercise 10: SOLID Principles
print("\n--- Exercise 10: SOLID Principles ---")

# Single Responsibility Principle
class User:
    """User data only."""
    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserRepository:
    """User storage only."""
    def __init__(self):
        self.users = []
    
    def save(self, user):
        self.users.append(user)
    
    def find_by_email(self, email):
        return next((u for u in self.users if u.email == email), None)


class EmailService:
    """Email sending only."""
    def send(self, to, subject, body):
        print(f"Sending email to {to}: {subject}")


# Open/Closed Principle
class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount):
        pass


class CreditCardProcessor(PaymentProcessor):
    def process(self, amount):
        return f"Processing €{amount} via credit card"


class PayPalProcessor(PaymentProcessor):
    def process(self, amount):
        return f"Processing €{amount} via PayPal"


# Test
user_repo = UserRepository()
email_service = EmailService()

user = User("Alice", "alice@example.com")
user_repo.save(user)

found = user_repo.find_by_email("alice@example.com")
if found:
    email_service.send(found.email, "Welcome", "Welcome to our service!")

processors = [CreditCardProcessor(), PayPalProcessor()]
for processor in processors:
    print(processor.process(100))


print("\n" + "=" * 70)
print("ALL EXERCISES COMPLETED!")
print("=" * 70)
