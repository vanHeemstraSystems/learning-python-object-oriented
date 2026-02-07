# 100 - Introduction to OOP

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around objects rather than functions and logic. This section introduces the fundamental concepts that form the foundation of OOP in Python.

## Overview

This section covers:
- What is Object-Oriented Programming?
- The four pillars of OOP
- OOP vs. Procedural Programming
- Benefits and use cases
- When to use OOP

## Contents

### [100 - OOP Concepts](./100-oop-concepts.md)
Core concepts including objects, classes, and the fundamental principles of OOP.

### [200 - Procedural vs OOP](./200-procedural-vs-oop.md)
Compare programming paradigms with practical examples showing when each approach works best.

### [300 - Benefits of OOP](./300-benefits-of-oop.md)
Understand the advantages of OOP: reusability, maintainability, scalability, and more.

## What is Object-Oriented Programming?

OOP is a programming paradigm based on the concept of "objects" that contain:
- **Data** (attributes/properties)
- **Behavior** (methods/functions)

Instead of writing programs as a sequence of instructions, OOP organizes code into self-contained units (objects) that interact with each other.

## The Four Pillars of OOP

### 1. Encapsulation
**Bundling data and methods that operate on that data within a single unit.**

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected data
    
    def deposit(self, amount):
        """Method that operates on the data"""
        self._balance += amount
    
    def get_balance(self):
        """Controlled access to data"""
        return self._balance
```

**Benefits:**
- Data protection
- Controlled access
- Implementation hiding

### 2. Inheritance
**Creating new classes based on existing classes, inheriting their attributes and methods.**

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Engineer(Employee):
    def __init__(self, name, salary, programming_languages):
        super().__init__(name, salary)
        self.programming_languages = programming_languages
```

**Benefits:**
- Code reuse
- Hierarchical organization
- Extensibility

### 3. Polymorphism
**Different classes can be used through the same interface, with each class providing its own implementation.**

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())  # Works with any object that has speak()

animal_sound(Dog())  # "Woof!"
animal_sound(Cat())  # "Meow!"
```

**Benefits:**
- Flexible code
- Interface consistency
- Runtime behavior

### 4. Abstraction
**Hiding complex implementation details and showing only essential features.**

```python
from abc import ABC, abstractmethod

class CloudProvider(ABC):
    @abstractmethod
    def deploy_vm(self, config):
        """Deploy a virtual machine"""
        pass

class Azure(CloudProvider):
    def deploy_vm(self, config):
        # Azure-specific implementation
        print(f"Deploying VM on Azure: {config}")

class AWS(CloudProvider):
    def deploy_vm(self, config):
        # AWS-specific implementation
        print(f"Deploying VM on AWS: {config}")
```

**Benefits:**
- Simplified interface
- Implementation flexibility
- Reduced complexity

## Real-World Analogy

Think of a **car**:

- **Encapsulation**: The engine is hidden under the hood. You don't need to know how it works internally.
- **Inheritance**: A sports car and an SUV both inherit from the general concept of "car" (wheels, engine, steering).
- **Polymorphism**: Different cars respond to "accelerate" differently (sports car vs. electric car).
- **Abstraction**: You use simple interfaces (pedals, steering wheel) without knowing the complex mechanics.

## Key Terminology

| Term | Definition | Example |
|------|------------|---------|
| **Class** | Blueprint for creating objects | `class Dog:` |
| **Object** | Instance of a class | `my_dog = Dog()` |
| **Attribute** | Data stored in an object | `my_dog.name` |
| **Method** | Function defined in a class | `my_dog.bark()` |
| **Instance** | Specific object created from a class | `beau = Dog("Beau")` |
| **Constructor** | Special method to initialize objects | `__init__(self)` |

## Why Python is Great for OOP

Python's features that support OOP:

1. **Everything is an object** - Even functions and classes
2. **Dynamic typing** - Flexible object creation
3. **Multiple inheritance** - Inherit from multiple classes
4. **Magic methods** - Customize behavior (`__init__`, `__str__`, etc.)
5. **Properties** - Controlled attribute access
6. **ABC module** - Abstract base classes
7. **Dataclasses** - Simplified class creation (Python 3.7+)

## When to Use OOP

### ✅ Good Use Cases

- **Complex applications** with many interrelated parts
- **Modeling real-world entities** (users, products, transactions)
- **Frameworks and libraries** that need extensibility
- **Large codebases** requiring organization
- **Team projects** needing clear interfaces
- **Long-term maintenance** where code will evolve

### ❌ When to Avoid OOP

- **Simple scripts** with straightforward logic
- **Data processing pipelines** that are purely functional
- **Performance-critical code** where overhead matters
- **Small utilities** that don't need abstraction

## OOP in Python vs Other Languages

| Feature | Python | Java | C++ |
|---------|--------|------|-----|
| Multiple Inheritance | ✅ Yes | ❌ No (interfaces only) | ✅ Yes |
| Private Members | Convention (`_attr`) | Enforced (`private`) | Enforced (`private`) |
| Everything is Object | ✅ Yes | ❌ No (primitives) | ❌ No |
| Duck Typing | ✅ Yes | ❌ No | ❌ No |
| Dynamic Classes | ✅ Yes | ❌ No | ❌ No |

Python's approach is more flexible and "Pythonic" - it trusts developers to use features responsibly.

## Basic Example: From Procedural to OOP

### Procedural Approach

```python
# Data and functions are separate
engineer_name = "Willem"
engineer_certs = ["AZ-104", "AZ-700"]
engineer_rate = 116

def add_certification(certs, cert):
    certs.append(cert)

def calculate_revenue(rate, hours):
    return rate * hours

# Usage
add_certification(engineer_certs, "AZ-305")
monthly = calculate_revenue(engineer_rate, 160)
```

**Problems:**
- Data and behavior are disconnected
- No relationship between related data
- Hard to manage multiple engineers
- Easy to make mistakes (wrong data passed to functions)

### Object-Oriented Approach

```python
class Engineer:
    def __init__(self, name, rate):
        self.name = name
        self.certifications = []
        self.rate = rate
    
    def add_certification(self, cert):
        self.certifications.append(cert)
    
    def calculate_revenue(self, hours):
        return self.rate * hours

# Usage
willem = Engineer("Willem", 116)
willem.add_certification("AZ-104")
willem.add_certification("AZ-700")
willem.add_certification("AZ-305")
monthly = willem.calculate_revenue(160)
```

**Benefits:**
- Data and behavior are together
- Clear relationship between related data
- Easy to manage multiple engineers
- Type safety through objects

## Common Misconceptions

### ❌ "OOP is always better"
Not true. Use the right tool for the job. Simple scripts don't need classes.

### ❌ "Everything must be a class"
Python supports multiple paradigms. Mix functional and OOP as needed.

### ❌ "Private members are truly private"
Python uses conventions (`_private`), not enforcement. Trust developers.

### ❌ "Inheritance is the primary way to reuse code"
Composition is often better than inheritance. "Favor composition over inheritance."

## Quick Reference

```python
# Define a class
class ClassName:
    """Docstring"""
    
    # Class attribute (shared)
    class_var = "shared"
    
    # Constructor
    def __init__(self, param):
        self.instance_var = param  # Instance attribute
    
    # Instance method
    def method(self):
        return self.instance_var
    
    # Class method
    @classmethod
    def class_method(cls):
        return cls.class_var
    
    # Static method
    @staticmethod
    def static_method():
        return "No access to instance or class"

# Create an object
obj = ClassName("value")

# Use the object
print(obj.method())
```

## Next Steps

After understanding these fundamentals:

1. **Section 200 - Classes and Objects** - Learn to create and use classes
2. **Section 300 - Encapsulation** - Master data protection
3. **Section 400 - Inheritance** - Build class hierarchies

## Practice Exercise

Try converting this procedural code to OOP:

```python
# Procedural: Manage cloud resources
resources = []

def create_resource(name, cloud, cost):
    resources.append({"name": name, "cloud": cloud, "cost": cost})

def total_cost():
    return sum(r["cost"] for r in resources)

def resources_by_cloud(cloud):
    return [r for r in resources if r["cloud"] == cloud]
```

**Challenge:** Create a `CloudResource` class and a `ResourceManager` class.

See `examples/basic_comparison.py` for the solution.

---

[Back to Main README](../README.md) | [Next: Section 200 - Classes and Objects](../200/README.md)
