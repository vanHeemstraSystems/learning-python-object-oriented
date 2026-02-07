# 900 - Best Practices

This section covers professional standards for writing clean, maintainable object-oriented Python code.

## SOLID Principles

### Single Responsibility Principle (SRP)
*A class should have only one reason to change.*

```python
# ❌ Bad: Multiple responsibilities
class Employee:
    def calculate_salary(self):
        pass
    
    def save_to_database(self):
        pass
    
    def generate_report(self):
        pass

# ✅ Good: Separate responsibilities
class Employee:
    def calculate_salary(self):
        pass

class EmployeeRepository:
    def save(self, employee):
        pass

class EmployeeReportGenerator:
    def generate(self, employee):
        pass
```

### Open/Closed Principle (OCP)
*Open for extension, closed for modification.*

```python
# ✅ Good: Extend behavior without modifying
class Notification:
    def send(self, message):
        raise NotImplementedError

class EmailNotification(Notification):  # Extend
    def send(self, message):
        print(f"Email: {message}")

class SMSNotification(Notification):  # Extend
    def send(self, message):
        print(f"SMS: {message}")

# Add new types without modifying existing code
```

### Liskov Substitution Principle (LSP)
*Subclasses should be substitutable for their base classes.*

```python
# ❌ Bad: Violates LSP
class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        raise Exception("Can't fly!")  # Breaks contract

# ✅ Good: Proper abstraction
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def swim(self):
        return "Swimming"
```

### Interface Segregation Principle (ISP)
*Don't force classes to implement unused interfaces.*

```python
# ❌ Bad: Fat interface
class Worker:
    def work(self):
        pass
    
    def eat(self):
        pass

class Robot(Worker):  # Robots don't eat!
    def work(self):
        return "Working"
    
    def eat(self):
        raise NotImplementedError

# ✅ Good: Segregated interfaces
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        return "Working"
    
    def eat(self):
        return "Eating"

class Robot(Workable):
    def work(self):
        return "Working"
```

### Dependency Inversion Principle (DIP)
*Depend on abstractions, not concretions.*

```python
# ❌ Bad: Depends on concrete class
class EmailSender:
    def send(self, message):
        print(f"Email: {message}")

class NotificationService:
    def __init__(self):
        self.sender = EmailSender()  # Concrete dependency

# ✅ Good: Depends on abstraction
from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(MessageSender):
    def send(self, message):
        print(f"Email: {message}")

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender  # Abstract dependency
```

## Code Organization

### Class Structure

```python
class WellOrganizedClass:
    """
    Clear docstring explaining purpose.
    
    Attributes:
        public_attr: Description
        _protected_attr: Description
    """
    
    # 1. Class attributes
    CLASS_CONSTANT = "value"
    
    # 2. Initialization
    def __init__(self, param):
        self.public_attr = param
        self._protected_attr = []
    
    # 3. Magic methods
    def __str__(self):
        return f"Object: {self.public_attr}"
    
    def __repr__(self):
        return f"WellOrganizedClass({self.public_attr!r})"
    
    # 4. Properties
    @property
    def computed_value(self):
        return len(self._protected_attr)
    
    # 5. Public methods
    def public_method(self):
        """Public interface."""
        return self._helper_method()
    
    # 6. Protected/Private methods
    def _helper_method(self):
        """Internal implementation."""
        return "result"
```

## Naming Conventions

```python
# Classes: PascalCase
class CloudResource:
    pass

# Functions/methods: snake_case
def calculate_total():
    pass

# Constants: UPPER_SNAKE_CASE
MAX_CONNECTIONS = 100

# Private: _leading_underscore
class Example:
    def __init__(self):
        self._internal = "private"
    
    def _helper_method(self):
        pass

# Name mangling: __double_underscore
class Example:
    def __init__(self):
        self.__really_private = "mangled"
```

## Type Hints

```python
from typing import List, Dict, Optional, Union

class Engineer:
    def __init__(
        self,
        name: str,
        certifications: Optional[List[str]] = None
    ) -> None:
        self.name: str = name
        self.certifications: List[str] = certifications or []
    
    def add_certification(self, cert: str) -> None:
        self.certifications.append(cert)
    
    def get_cert_count(self) -> int:
        return len(self.certifications)
    
    def to_dict(self) -> Dict[str, Union[str, List[str]]]:
        return {
            "name": self.name,
            "certifications": self.certifications
        }
```

## Documentation

```python
class DatabaseConnection:
    """
    Manages database connections with automatic cleanup.
    
    This class provides a context manager interface for database
    connections, ensuring proper resource cleanup even if errors occur.
    
    Attributes:
        host (str): Database host address
        port (int): Database port number
        connected (bool): Current connection status
    
    Example:
        >>> with DatabaseConnection("localhost", 5432) as db:
        ...     db.execute("SELECT * FROM users")
    
    Note:
        Always use as a context manager to ensure cleanup.
    """
    
    def __init__(self, host: str, port: int = 5432) -> None:
        """
        Initialize database connection parameters.
        
        Args:
            host: Database server hostname or IP
            port: Database server port (default: 5432)
        
        Raises:
            ValueError: If port is outside valid range
        """
        if not 1 <= port <= 65535:
            raise ValueError(f"Invalid port: {port}")
        
        self.host = host
        self.port = port
        self.connected = False
    
    def execute(self, query: str) -> List[Dict]:
        """
        Execute SQL query and return results.
        
        Args:
            query: SQL query string
        
        Returns:
            List of dictionaries containing query results
        
        Raises:
            RuntimeError: If not connected to database
        """
        if not self.connected:
            raise RuntimeError("Not connected to database")
        
        # Implementation here
        return []
```

## Testing OOP Code

```python
import unittest
from unittest.mock import Mock, patch

class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
    
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
    
    def get_balance(self):
        return self._balance


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """Runs before each test."""
        self.account = BankAccount(100)
    
    def test_initial_balance(self):
        account = BankAccount(50)
        self.assertEqual(account.get_balance(), 50)
    
    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)
    
    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)
    
    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 70)
    
    def test_withdraw_insufficient(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)
```

## Common Anti-Patterns to Avoid

### God Object
```python
# ❌ Bad: Does everything
class Application:
    def handle_request(self):
        pass
    def access_database(self):
        pass
    def send_email(self):
        pass
    def generate_report(self):
        pass
    # ... 50 more methods

# ✅ Good: Focused classes
class RequestHandler:
    pass
class DatabaseAccess:
    pass
class EmailService:
    pass
class ReportGenerator:
    pass
```

### Anemic Domain Model
```python
# ❌ Bad: Just data, no behavior
class Order:
    def __init__(self):
        self.items = []
        self.total = 0

# Behavior lives elsewhere
def calculate_total(order):
    return sum(item.price for item in order.items)

# ✅ Good: Data and behavior together
class Order:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def calculate_total(self):
        return sum(item.price for item in self.items)
```

## Quick Reference Checklist

### Class Design
- [ ] Single responsibility
- [ ] Clear, descriptive name
- [ ] Comprehensive docstring
- [ ] Type hints on methods
- [ ] Proper encapsulation
- [ ] No god objects

### Methods
- [ ] Do one thing well
- [ ] Clear names
- [ ] Type hints
- [ ] Docstrings for public methods
- [ ] Proper error handling

### Code Quality
- [ ] Follows PEP 8
- [ ] No code duplication
- [ ] Appropriate comments
- [ ] Tests written
- [ ] Type checking passes

---

[Back to Main README](../README.md)
