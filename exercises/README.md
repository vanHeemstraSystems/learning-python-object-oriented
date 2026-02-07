# Exercises

This directory contains hands-on exercises to reinforce your understanding of Python object-oriented programming. Exercises are organized by difficulty level and topic area.

## Directory Structure

```
exercises/
├── README.md (this file)
├── beginner/         # Fundamental OOP concepts
├── intermediate/     # Inheritance, polymorphism, design
└── advanced/         # Design patterns, advanced techniques
```

## How to Use These Exercises

1. **Read the problem description** carefully
2. **Try solving it yourself** before looking at solutions
3. **Run your code** and test with different inputs
4. **Compare with provided solutions** (when available)
5. **Refactor and improve** your initial solution

## Beginner Exercises

### Exercise 1: Dog Class
**Topic:** Basic class definition, `__init__()`, instance methods

Create a `Dog` class with the following:
- Attributes: `name`, `breed`, `age`
- Methods: `bark()`, `birthday()`, `get_info()`

```python
# Expected usage:
buddy = Dog("Buddy", "Golden Retriever", 3)
print(buddy.bark())        # "Buddy says Woof!"
buddy.birthday()           # Increases age by 1
print(buddy.get_info())    # "Buddy is a 4-year-old Golden Retriever"
```

### Exercise 2: Bank Account
**Topic:** Encapsulation, instance methods, validation

Create a `BankAccount` class:
- Attributes: `account_holder`, `balance` (starts at 0)
- Methods: `deposit()`, `withdraw()`, `get_balance()`
- Validation: Don't allow withdrawals greater than balance

```python
# Expected usage:
account = BankAccount("Willem van Heemstra")
account.deposit(1000)
account.withdraw(300)
print(account.get_balance())  # 700
```

### Exercise 3: Rectangle
**Topic:** Attributes, computed properties, methods

Create a `Rectangle` class:
- Attributes: `width`, `height`
- Methods: `area()`, `perimeter()`, `is_square()`

```python
# Expected usage:
rect = Rectangle(5, 10)
print(rect.area())         # 50
print(rect.perimeter())    # 30
print(rect.is_square())    # False
```

### Exercise 4: Student Grade Tracker
**Topic:** Lists as attributes, methods for data manipulation

Create a `Student` class:
- Attributes: `name`, `grades` (list)
- Methods: `add_grade()`, `get_average()`, `get_letter_grade()`

```python
# Expected usage:
student = Student("Alice")
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)
print(student.get_average())        # 85.0
print(student.get_letter_grade())   # "B"
```

### Exercise 5: Shopping Cart
**Topic:** Class and instance attributes, list operations

Create a `ShoppingCart` class:
- Class attribute: `tax_rate = 0.21` (VAT)
- Instance attributes: `items` (list of tuples: (name, price))
- Methods: `add_item()`, `remove_item()`, `get_subtotal()`, `get_total()`

```python
# Expected usage:
cart = ShoppingCart()
cart.add_item("Book", 25.00)
cart.add_item("Pen", 2.50)
print(cart.get_subtotal())  # 27.50
print(cart.get_total())     # 33.28 (including 21% VAT)
```

## Intermediate Exercises

### Exercise 6: Employee Hierarchy
**Topic:** Inheritance, method overriding

Create an `Employee` base class and `Manager`, `Engineer`, `Intern` subclasses:
- Base class: `name`, `salary`, `get_details()`
- `Manager`: additional `department` attribute, override `get_details()`
- `Engineer`: additional `programming_languages` list
- `Intern`: additional `supervisor` attribute

### Exercise 7: Shape Polymorphism
**Topic:** Polymorphism, abstract methods

Create abstract `Shape` class with subclasses `Circle`, `Rectangle`, `Triangle`:
- Abstract method: `area()`
- Each subclass implements `area()` appropriately
- Create a function that calculates total area of mixed shapes

### Exercise 8: Vehicle Fleet
**Topic:** Composition vs inheritance

Create a vehicle fleet management system:
- `Vehicle` base class
- `Car`, `Truck`, `Motorcycle` subclasses
- `Fleet` class that manages multiple vehicles
- Include methods for adding vehicles, calculating total value, etc.

### Exercise 9: Library System
**Topic:** Multiple classes, relationships, encapsulation

Create a library management system:
- `Book` class: title, author, ISBN, available status
- `Member` class: name, member_id, borrowed_books list
- `Library` class: manages books and members, lending/returning

### Exercise 10: Custom Iterator
**Topic:** Magic methods, iteration protocol

Create a `Playlist` class that is iterable:
- Store songs (name, artist, duration)
- Implement `__iter__()` and `__next__()`
- Support `for` loops and `len()`

## Advanced Exercises

### Exercise 11: Singleton Logger
**Topic:** Design patterns (Singleton)

Implement a logging system using the Singleton pattern:
- Ensure only one logger instance exists
- Support different log levels (DEBUG, INFO, WARNING, ERROR)
- Write logs to file and/or console

### Exercise 12: Observer Pattern
**Topic:** Design patterns (Observer)

Create a stock market monitoring system:
- `Stock` class (observable) - price changes notify observers
- `Investor` class (observer) - gets notified of price changes
- Support multiple observers per stock

### Exercise 13: Decorator Pattern
**Topic:** Design patterns (Decorator)

Create a coffee shop ordering system:
- Base `Coffee` class
- Decorators: `Milk`, `Sugar`, `WhippedCream`, `CaramelSyrup`
- Each decorator adds cost and description
- Support chaining multiple decorators

### Exercise 14: Context Manager
**Topic:** Magic methods, resource management

Create a `DatabaseConnection` context manager:
- Implement `__enter__()` and `__exit__()`
- Support `with` statement
- Ensure proper connection cleanup

### Exercise 15: Custom Collection
**Topic:** Magic methods, operator overloading

Create a `Vector` class for mathematical operations:
- Support addition, subtraction, scalar multiplication
- Implement `__len__()`, `__getitem__()`, `__setitem__()`
- Support comparison operators
- Implement `__repr__()` and `__str__()`

## Solutions

Solutions are available in separate files within each difficulty directory. Try solving the exercises yourself before checking the solutions.

To check your solution:
```bash
# Run your solution
python beginner/my_solution.py

# Compare with provided solution
python beginner/solutions/exercise_01_solution.py
```

## Testing Your Solutions

Each exercise includes test cases. Run them using pytest:

```bash
# Install pytest if not already installed
pip install pytest

# Run all tests
pytest exercises/

# Run specific test file
pytest exercises/beginner/test_dog_class.py

# Run with coverage
pytest --cov=exercises exercises/
```

## Contributing Exercises

To add new exercises:

1. Write a clear problem description
2. Include example usage
3. Provide test cases
4. Add a solution with comments
5. Update this README

## Progress Tracking

Track your progress by checking off completed exercises:

**Beginner:**
- [ ] Exercise 1: Dog Class
- [ ] Exercise 2: Bank Account
- [ ] Exercise 3: Rectangle
- [ ] Exercise 4: Student Grade Tracker
- [ ] Exercise 5: Shopping Cart

**Intermediate:**
- [ ] Exercise 6: Employee Hierarchy
- [ ] Exercise 7: Shape Polymorphism
- [ ] Exercise 8: Vehicle Fleet
- [ ] Exercise 9: Library System
- [ ] Exercise 10: Custom Iterator

**Advanced:**
- [ ] Exercise 11: Singleton Logger
- [ ] Exercise 12: Observer Pattern
- [ ] Exercise 13: Decorator Pattern
- [ ] Exercise 14: Context Manager
- [ ] Exercise 15: Custom Collection

## Tips for Success

1. **Start simple** - Get basic functionality working first
2. **Test frequently** - Run your code after each small change
3. **Refactor** - Improve your code after it works
4. **Read the error messages** - They often tell you exactly what's wrong
5. **Use print statements** - Debug by printing intermediate values
6. **Ask for help** - If stuck, review the corresponding section in the main materials

## Additional Practice Resources

- [Python OOP Exercises](https://www.w3resource.com/python-exercises/class-exercises/)
- [Real Python Tutorials](https://realpython.com/)
- [LeetCode OOP Problems](https://leetcode.com/)
- [HackerRank Python OOP](https://www.hackerrank.com/domains/python)

---

[Back to Main README](../README.md)
