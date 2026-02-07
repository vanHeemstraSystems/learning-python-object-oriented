# 200 - Classes and Objects

Classes are the fundamental building blocks of object-oriented programming in Python. A class serves as a blueprint for creating objects (instances), defining their attributes and behaviors.

## Overview

This section covers:
- How to define and structure classes
- Creating and working with objects
- Understanding instance vs. class attributes
- Different types of methods (instance, class, static)
- The constructor pattern with `__init__()`
- The `self` parameter and its purpose

## Contents

### [100 - Defining Classes](./100-defining-classes.md)
Learn the basic syntax for creating classes in Python, naming conventions, and class structure.

### [200 - Creating Objects](./200-creating-objects.md)
Understand object instantiation, the relationship between classes and objects, and managing multiple instances.

### [300 - Instance Attributes](./300-instance-attributes.md)
Work with attributes that belong to individual objects, including initialization and modification.

### [400 - Class Attributes](./400-class-attributes.md)
Explore attributes shared across all instances of a class and their use cases.

### [500 - Methods](./500-methods.md)
Master instance methods, class methods (`@classmethod`), and static methods (`@staticmethod`).

### [600 - Constructors](./600-constructors.md)
Deep dive into `__init__()`, initialization patterns, and default parameters.

## Key Concepts

### What is a Class?

A class is a user-defined data structure that contains:
- **Attributes**: Variables that store data
- **Methods**: Functions that define behavior

```python
class Dog:
    """A simple class representing a dog."""
    
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor (instance initializer)
    def __init__(self, name, age):
        # Instance attributes (unique to each object)
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
```

### What is an Object?

An object is a specific instance of a class with its own data:

```python
# Creating objects (instances)
beau = Dog("Beau", 5)
elvis = Dog("Elvis", 3)

print(beau.name)      # "Beau"
print(elvis.bark())   # "Elvis says Woof!"
```

### The `self` Parameter

`self` represents the instance calling the method:
- Always the first parameter of instance methods
- Automatically passed by Python (you don't pass it explicitly)
- Allows access to instance attributes and other methods

## Practical Examples

### Example 1: Simple Class Definition

```python
class BankAccount:
    """Represents a basic bank account."""
    
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance
    
    def get_balance(self):
        return f"Account balance: €{self.balance}"
```

**Usage:**
```python
account = BankAccount("Willem van Heemstra", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # "Account balance: €1300"
```

### Example 2: Class vs Instance Attributes

```python
class CloudEngineer:
    """Represents a cloud engineer."""
    
    # Class attribute - shared by all instances
    cloud_platforms = ["Azure", "AWS", "GCP"]
    
    def __init__(self, name, specialty):
        # Instance attributes - unique to each object
        self.name = name
        self.specialty = specialty
        self.certifications = []
    
    def add_certification(self, cert):
        self.certifications.append(cert)
    
    @classmethod
    def get_platforms(cls):
        """Class method - operates on the class itself."""
        return cls.cloud_platforms
    
    @staticmethod
    def validate_cert_code(code):
        """Static method - doesn't need class or instance."""
        return code.startswith("AZ-") or code.startswith("AWS-")
```

**Usage:**
```python
engineer1 = CloudEngineer("Willem", "DevSecOps")
engineer2 = CloudEngineer("Sabine", "Architecture")

engineer1.add_certification("AZ-104")
engineer1.add_certification("AZ-700")

print(engineer1.certifications)  # ["AZ-104", "AZ-700"]
print(engineer2.certifications)  # []

print(CloudEngineer.get_platforms())  # ["Azure", "AWS", "GCP"]
print(CloudEngineer.validate_cert_code("AZ-305"))  # True
```

## Common Patterns

### 1. Builder Pattern with Constructor

```python
class ProjectConfig:
    def __init__(self, name, description="", team_size=1, budget=0):
        self.name = name
        self.description = description
        self.team_size = team_size
        self.budget = budget
```

### 2. Factory Class Method

```python
class Employee:
    def __init__(self, name, role, hourly_rate):
        self.name = name
        self.role = role
        self.hourly_rate = hourly_rate
    
    @classmethod
    def from_contract(cls, name, role, contract_details):
        """Alternative constructor from contract details."""
        hourly_rate = contract_details.get("hourly_rate", 0)
        return cls(name, role, hourly_rate)
```

### 3. Counting Instances

```python
class Server:
    instance_count = 0
    
    def __init__(self, name):
        self.name = name
        Server.instance_count += 1
    
    @classmethod
    def get_instance_count(cls):
        return cls.instance_count
```

## Best Practices

1. **Use clear, descriptive class names** (PascalCase convention)
   ```python
   class InternalDeveloperPlatform:  # Good
   class idp:  # Bad - unclear, not PascalCase
   ```

2. **Initialize all instance attributes in `__init__()`**
   ```python
   def __init__(self, name):
       self.name = name
       self.created_at = None  # Initialize even if None
   ```

3. **Use class attributes for shared constants**
   ```python
   class AzureRegion:
       REGIONS = ["westeurope", "northeurope", "eastus"]
   ```

4. **Document your classes with docstrings**
   ```python
   class KubernetesCluster:
       """
       Represents a Kubernetes cluster configuration.
       
       Attributes:
           name (str): Cluster identifier
           node_count (int): Number of nodes
           region (str): Azure region
       """
   ```

5. **Keep methods focused and cohesive**
   - Each method should do one thing well
   - Avoid god objects with too many responsibilities

## Exercises

See `examples/` directory for:
- `simple_class.py`: Basic class creation and usage
- `class_vs_instance.py`: Comparing class and instance attributes
- `constructor_examples.py`: Various constructor patterns

## Common Mistakes to Avoid

1. **Forgetting `self` in method definitions**
   ```python
   def bark():  # Wrong - missing self
       print("Woof!")
   ```

2. **Modifying class attributes via instance**
   ```python
   engineer1.cloud_platforms.append("Oracle")  # Affects ALL instances!
   ```

3. **Not initializing instance attributes**
   ```python
   def __init__(self, name):
       self.name = name
       # self.age not initialized - may cause AttributeError later
   ```

## Next Steps

After mastering classes and objects, proceed to:
- **Section 300: Encapsulation** - Learn to protect data
- **Section 400: Inheritance** - Reuse code through class hierarchies
- **Section 700: Magic Methods** - Customize class behavior

## Additional Resources

- Python Official Tutorial: [Classes](https://docs.python.org/3/tutorial/classes.html)
- Real Python: [Object-Oriented Programming in Python 3](https://realpython.com/python3-object-oriented-programming/)
- PEP 8: [Class Names](https://pep8.org/#class-names)

---

[Back to Main README](../README.md)
