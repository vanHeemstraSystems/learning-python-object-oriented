# 300 - Encapsulation

Encapsulation is the bundling of data and methods that operate on that data within a single unit (class), while restricting direct access to some of the object's components. It's one of the fundamental principles of object-oriented programming.

## Overview

This section covers:
- Access modifiers and naming conventions
- Properties and decorators
- Getters and setters
- Data validation and protection
- Name mangling in Python

## Contents

### [100 - Access Modifiers](./100-access-modifiers.md)
Understanding public, protected, and private attributes in Python.

### [200 - Properties](./200-properties.md)
Using the `@property` decorator for elegant attribute access.

### [300 - Getters and Setters](./300-getters-setters.md)
Traditional getter/setter patterns and their Python equivalents.

### [400 - Data Hiding](./400-data-hiding.md)
Techniques for protecting internal implementation details.

## What is Encapsulation?

Encapsulation means:
1. **Bundling** data (attributes) and methods together in a class
2. **Controlling** access to the internal state
3. **Hiding** implementation details from the outside world

Think of it like a capsule that contains medicine - you don't need to know what's inside to use it safely.

## Python's Approach to Encapsulation

Unlike languages like Java or C++, Python doesn't enforce access restrictions. Instead, it uses **naming conventions** to indicate intent:

| Convention | Meaning | Access |
|------------|---------|--------|
| `name` | Public | Full access from anywhere |
| `_name` | Protected | Internal use, but accessible |
| `__name` | Private | Name mangled, harder to access |

**Important:** These are conventions, not enforced restrictions. Python follows the philosophy: "We're all consenting adults here."

## Basic Example

```python
class BankAccount:
    """Example demonstrating encapsulation."""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder  # Public
        self._balance = initial_balance       # Protected
        self.__account_number = self._generate_account_number()  # Private
    
    def deposit(self, amount):
        """Public method to modify protected data."""
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """Controlled access with validation."""
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    def get_balance(self):
        """Getter for protected balance."""
        return self._balance
    
    def _generate_account_number(self):
        """Protected helper method."""
        import random
        return f"NL{random.randint(1000000000, 9999999999)}"
    
    def __str__(self):
        """Public interface."""
        return f"Account: {self.account_holder}, Balance: €{self._balance}"


# Usage
account = BankAccount("Willem van Heemstra", 1000)

# Public access
print(account.account_holder)  # ✓ OK

# Controlled access through methods
account.deposit(500)           # ✓ OK
print(account.get_balance())   # ✓ OK

# Direct access to "protected" (still works, but discouraged)
print(account._balance)        # ✓ Works but violates convention

# Direct modification (dangerous!)
account._balance = 999999      # ⚠️ Breaks encapsulation

# Private attribute access (name mangled)
# print(account.__account_number)  # ✗ AttributeError
print(account._BankAccount__account_number)  # ✓ Still accessible via name mangling
```

## Using Properties

Properties provide a Pythonic way to encapsulate attributes:

```python
class Engineer:
    """Engineer class with properties."""
    
    def __init__(self, name, hourly_rate):
        self._name = name
        self._hourly_rate = hourly_rate
    
    @property
    def name(self):
        """Getter for name."""
        return self._name
    
    @property
    def hourly_rate(self):
        """Getter for hourly rate."""
        return self._hourly_rate
    
    @hourly_rate.setter
    def hourly_rate(self, value):
        """Setter with validation."""
        if value < 0:
            raise ValueError("Hourly rate cannot be negative")
        if value > 500:
            raise ValueError("Hourly rate seems too high")
        self._hourly_rate = value
    
    @property
    def annual_salary(self):
        """Computed property (read-only)."""
        return self._hourly_rate * 40 * 52  # 40 hours/week, 52 weeks


# Usage
engineer = Engineer("Willem", 116)

# Access like attributes, but with control
print(engineer.name)           # Calls getter
print(engineer.hourly_rate)    # Calls getter
print(engineer.annual_salary)  # Computed value

# Setting with validation
engineer.hourly_rate = 120     # Calls setter with validation

# Invalid operations
# engineer.hourly_rate = -10   # ✗ ValueError
# engineer.annual_salary = 100000  # ✗ AttributeError (read-only)
```

## Benefits of Encapsulation

### 1. Data Validation

```python
class Project:
    def __init__(self, name):
        self._name = name
        self._team_size = 1
    
    @property
    def team_size(self):
        return self._team_size
    
    @team_size.setter
    def team_size(self, value):
        if not isinstance(value, int):
            raise TypeError("Team size must be an integer")
        if value < 1:
            raise ValueError("Team must have at least 1 member")
        if value > 100:
            raise ValueError("Team size exceeds maximum of 100")
        self._team_size = value
```

### 2. Implementation Changes Without Breaking Code

```python
class Temperature:
    """Temperature class - can change internal storage without affecting users."""
    
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed on-the-fly from celsius."""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Convert and store as celsius."""
        self._celsius = (value - 32) * 5/9

# Could later change to store fahrenheit internally
# without breaking existing code that uses celsius property
```

### 3. Computed Properties

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def area(self):
        """Computed property - no storage needed."""
        return self._width * self._height
    
    @property
    def perimeter(self):
        """Another computed property."""
        return 2 * (self._width + self._height)

rect = Rectangle(5, 10)
print(rect.area)       # 50 (computed)
print(rect.perimeter)  # 30 (computed)
```

### 4. Side Effects and Logging

```python
class ConfigManager:
    def __init__(self):
        self._config = {}
    
    @property
    def debug_mode(self):
        return self._config.get('debug', False)
    
    @debug_mode.setter
    def debug_mode(self, value):
        """Setter with side effects."""
        old_value = self._config.get('debug', False)
        self._config['debug'] = value
        
        # Side effect: logging
        if old_value != value:
            print(f"Debug mode changed: {old_value} -> {value}")
            
        # Side effect: configuration update
        if value:
            self._enable_verbose_logging()
    
    def _enable_verbose_logging(self):
        """Private helper method."""
        print("Verbose logging enabled")
```

## Access Levels in Detail

### Public Attributes

```python
class CloudResource:
    def __init__(self, name):
        self.name = name  # Public - access from anywhere
        self.cloud = "Azure"
        self.active = True
```

**Use when:** The attribute is part of the public interface.

### Protected Attributes (`_single_underscore`)

```python
class Engineer:
    def __init__(self, name):
        self._certifications = []  # Protected - internal use
        self._hourly_rate = 100
    
    def add_certification(self, cert):
        """Public method to modify protected data."""
        self._certifications.append(cert)
```

**Use when:** 
- The attribute is for internal use
- Subclasses might need access
- You want to signal "don't touch unless you know what you're doing"

### Private Attributes (`__double_underscore`)

```python
class SecureVault:
    def __init__(self):
        self.__secret_key = "xyz123"  # Private - name mangled
    
    def verify(self, key):
        return key == self.__secret_key

vault = SecureVault()
# vault.__secret_key  # ✗ AttributeError
# vault._SecureVault__secret_key  # Still accessible but discouraged
```

**Use when:**
- You want to avoid name conflicts in subclasses
- The attribute is truly internal and shouldn't be accessed directly

## Property Decorators

### Read-Only Property

```python
class Project:
    def __init__(self, name, created_at):
        self._name = name
        self._created_at = created_at
    
    @property
    def created_at(self):
        """Read-only property."""
        return self._created_at
    
    # No setter - property is read-only
```

### Read-Write Property

```python
class Project:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        """Getter."""
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter with validation."""
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
```

### Deletable Property

```python
class CachedData:
    def __init__(self):
        self._cache = None
    
    @property
    def cache(self):
        return self._cache
    
    @cache.setter
    def cache(self, value):
        self._cache = value
    
    @cache.deleter
    def cache(self):
        """Custom deletion behavior."""
        print("Clearing cache")
        self._cache = None

data = CachedData()
data.cache = "some data"
del data.cache  # Calls deleter
```

## Best Practices

### ✅ DO

```python
class GoodExample:
    def __init__(self, value):
        self._value = value  # Use leading underscore for internal
    
    @property
    def value(self):
        """Provide controlled access via property."""
        return self._value
    
    @value.setter
    def value(self, new_value):
        """Validate in setter."""
        if new_value < 0:
            raise ValueError("Value must be non-negative")
        self._value = new_value
```

### ❌ DON'T

```python
class BadExample:
    def __init__(self, value):
        self.value = value  # Public - no control
    
    def get_value(self):  # Java-style getter - not Pythonic
        return self.value
    
    def set_value(self, value):  # Java-style setter - use @property instead
        self.value = value
```

## Common Patterns

### 1. Lazy Loading

```python
class DataLoader:
    def __init__(self, filepath):
        self._filepath = filepath
        self._data = None  # Not loaded yet
    
    @property
    def data(self):
        """Load data only when accessed."""
        if self._data is None:
            print(f"Loading data from {self._filepath}")
            self._data = self._load_data()
        return self._data
    
    def _load_data(self):
        """Protected helper method."""
        # Expensive operation
        return {"loaded": "data"}
```

### 2. Dependent Properties

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def diameter(self):
        """Dependent on radius."""
        return self._radius * 2
    
    @property
    def area(self):
        """Also dependent on radius."""
        import math
        return math.pi * self._radius ** 2
```

### 3. Validation Chain

```python
class Employee:
    def __init__(self, name, email, salary):
        self._name = name
        self._email = email
        self._salary = salary
        self._validate()
    
    def _validate(self):
        """Central validation."""
        if not self._name:
            raise ValueError("Name required")
        if "@" not in self._email:
            raise ValueError("Invalid email")
        if self._salary < 0:
            raise ValueError("Salary must be positive")
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        """Revalidate on change."""
        self._salary = value
        self._validate()
```

## Next Steps

- **Section 400 - Inheritance** - How encapsulation works with subclasses
- **Section 600 - Abstraction** - Hiding implementation details
- **Section 200 - Classes and Objects** - Review class fundamentals

---

[Back to Main README](../README.md)
