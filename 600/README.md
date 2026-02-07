# 600 - Abstraction

Abstraction means hiding complex implementation details and exposing only essential features. In Python, this is achieved through abstract base classes (ABCs) and protocols.

## Overview

This section covers:
- Abstract Base Classes (ABC)
- The `abc` module
- `@abstractmethod` decorator
- Protocols and structural subtyping
- Interface design

## What is Abstraction?

Abstraction provides:
- **Interface definition** - What a class must do
- **Implementation hiding** - How it does it is hidden
- **Consistency** - All implementations follow the same contract

```python
from abc import ABC, abstractmethod

class CloudProvider(ABC):
    """Abstract interface - defines what all providers must do."""
    
    @abstractmethod
    def deploy_vm(self, config):
        """All providers must implement this."""
        pass
    
    @abstractmethod
    def get_pricing(self):
        """All providers must implement this."""
        pass

class Azure(CloudProvider):
    def deploy_vm(self, config):
        return f"Azure VM deployed: {config}"
    
    def get_pricing(self):
        return {"vm": 100, "storage": 20}

class AWS(CloudProvider):
    def deploy_vm(self, config):
        return f"AWS EC2 deployed: {config}"
    
    def get_pricing(self):
        return {"vm": 95, "storage": 18}

# Cannot instantiate abstract class
# provider = CloudProvider()  # TypeError

# Must implement all abstract methods
azure = Azure()  # OK
aws = AWS()      # OK
```

## Abstract Base Classes

### Basic ABC

```python
from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    """Abstract base for database connections."""
    
    @abstractmethod
    def connect(self):
        """Connect to database."""
        pass
    
    @abstractmethod
    def execute(self, query):
        """Execute a query."""
        pass
    
    @abstractmethod
    def close(self):
        """Close connection."""
        pass
    
    # Concrete method - can have implementation
    def is_connected(self):
        """Default implementation."""
        return hasattr(self, '_connection') and self._connection is not None

class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        self._connection = "PostgreSQL connection"
        return "Connected to PostgreSQL"
    
    def execute(self, query):
        return f"Executing on PostgreSQL: {query}"
    
    def close(self):
        self._connection = None
        return "PostgreSQL connection closed"

class MongoDBConnection(DatabaseConnection):
    def connect(self):
        self._connection = "MongoDB connection"
        return "Connected to MongoDB"
    
    def execute(self, query):
        return f"Executing on MongoDB: {query}"
    
    def close(self):
        self._connection = None
        return "MongoDB connection closed"
```

### Abstract Properties

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    @property
    @abstractmethod
    def salary(self):
        """All employees must have salary property."""
        pass
    
    @abstractmethod
    def calculate_bonus(self):
        """All employees must implement bonus calculation."""
        pass

class Engineer(Employee):
    def __init__(self, base_salary):
        self._salary = base_salary
    
    @property
    def salary(self):
        return self._salary
    
    def calculate_bonus(self):
        return self._salary * 0.15

class Manager(Employee):
    def __init__(self, base_salary):
        self._salary = base_salary
    
    @property
    def salary(self):
        return self._salary
    
    def calculate_bonus(self):
        return self._salary * 0.25
```

## Real-World Example: Notification System

```python
from abc import ABC, abstractmethod
from typing import List

class Notification(ABC):
    """Abstract base for all notification types."""
    
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        """Send notification to recipient."""
        pass
    
    @abstractmethod
    def validate_recipient(self, recipient: str) -> bool:
        """Validate recipient format."""
        pass
    
    def prepare_message(self, message: str) -> str:
        """Concrete method - default behavior."""
        return f"[{self.__class__.__name__}] {message}"

class EmailNotification(Notification):
    def send(self, recipient: str, message: str) -> bool:
        if not self.validate_recipient(recipient):
            return False
        prepared = self.prepare_message(message)
        print(f"Email to {recipient}: {prepared}")
        return True
    
    def validate_recipient(self, recipient: str) -> bool:
        return "@" in recipient and "." in recipient

class SMSNotification(Notification):
    def send(self, recipient: str, message: str) -> bool:
        if not self.validate_recipient(recipient):
            return False
        prepared = self.prepare_message(message)
        print(f"SMS to {recipient}: {prepared}")
        return True
    
    def validate_recipient(self, recipient: str) -> bool:
        return recipient.startswith("+") and len(recipient) >= 10

class PushNotification(Notification):
    def send(self, recipient: str, message: str) -> bool:
        if not self.validate_recipient(recipient):
            return False
        prepared = self.prepare_message(message)
        print(f"Push to device {recipient}: {prepared}")
        return True
    
    def validate_recipient(self, recipient: str) -> bool:
        return len(recipient) == 36  # UUID format

class NotificationService:
    """Uses abstraction - works with any Notification."""
    
    def __init__(self):
        self.channels: List[Notification] = []
    
    def add_channel(self, channel: Notification):
        self.channels.append(channel)
    
    def broadcast(self, recipients: dict, message: str):
        """Send via all channels."""
        for channel in self.channels:
            channel_type = channel.__class__.__name__
            recipient = recipients.get(channel_type.replace("Notification", "").lower())
            if recipient:
                channel.send(recipient, message)

# Usage
service = NotificationService()
service.add_channel(EmailNotification())
service.add_channel(SMSNotification())
service.add_channel(PushNotification())

recipients = {
    "email": "user@example.com",
    "sms": "+31612345678",
    "push": "550e8400-e29b-41d4-a716-446655440000"
}

service.broadcast(recipients, "System maintenance in 1 hour")
```

## Protocols (Python 3.8+)

Structural subtyping without inheritance:

```python
from typing import Protocol

class Drawable(Protocol):
    """Protocol - defines interface without inheritance."""
    
    def draw(self) -> str:
        ...

class Circle:
    """Doesn't inherit from Drawable, but matches protocol."""
    def draw(self) -> str:
        return "Drawing circle"

class Square:
    """Also matches protocol."""
    def draw(self) -> str:
        return "Drawing square"

def render(shape: Drawable) -> None:
    """Works with anything matching Drawable protocol."""
    print(shape.draw())

# Both work - structural typing
render(Circle())
render(Square())
```

## Benefits of Abstraction

1. **Enforced Contracts** - All implementations must follow interface
2. **Interchangeable Components** - Swap implementations easily
3. **Clear Design** - Interfaces document expectations
4. **Testability** - Easy to mock abstract interfaces

## Best Practices

✅ **DO:**
- Use ABCs for core interfaces
- Keep abstract methods focused
- Document expected behavior
- Provide concrete helper methods in ABC

❌ **DON'T:**
- Create too many abstract methods
- Use ABCs for simple cases (duck typing is fine)
- Put implementation in abstract methods

---

[Back to Main README](../README.md)
