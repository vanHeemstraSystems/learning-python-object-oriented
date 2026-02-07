"""
Best Practices Examples
SOLID principles and clean code.
"""

from abc import ABC, abstractmethod

# Example 1: Single Responsibility Principle
class User:
    """Only handles user data."""
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserValidator:
    """Only handles validation."""
    @staticmethod
    def validate(user):
        return "@" in user.email

class UserRepository:
    """Only handles storage."""
    def save(self, user):
        print(f"Saved {user.name}")

user = User("Alice", "alice@example.com")
if UserValidator.validate(user):
    UserRepository().save(user)

# Example 2: Dependency Inversion
class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(MessageSender):
    def send(self, message):
        print(f"Email: {message}")

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender  # Depends on abstraction
    
    def notify(self, message):
        self.sender.send(message)

service = NotificationService(EmailSender())
service.notify("Hello!")

# Example 3: Proper encapsulation
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

account = BankAccount(100)
account.deposit(50)
print(f"Balance: €{account.balance}")

# Example 4: Type hints
def calculate_total(items: list[dict]) -> float:
    """Calculate total with type hints."""
    return sum(item['price'] for item in items)

items = [{'name': 'Book', 'price': 10}, {'name': 'Pen', 'price': 2}]
print(f"Total: €{calculate_total(items)}")
