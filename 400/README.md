# 400 - Inheritance

Inheritance is a mechanism that allows you to create new classes based on existing classes, inheriting their attributes and methods. It's a cornerstone of code reuse and hierarchical organization in object-oriented programming.

## Overview

This section covers:
- Single inheritance
- Multiple inheritance
- Method Resolution Order (MRO)
- The `super()` function
- Method overriding
- Composition vs. Inheritance

## Contents

### [100 - Single Inheritance](./100-single-inheritance.md)
Creating child classes from a single parent class.

### [200 - Multiple Inheritance](./200-multiple-inheritance.md)
Inheriting from multiple parent classes simultaneously.

### [300 - Method Resolution Order](./300-method-resolution-order.md)
Understanding how Python resolves method calls in inheritance hierarchies.

### [400 - Super Function](./400-super-function.md)
Using `super()` to call parent class methods properly.

### [500 - Composition vs Inheritance](./500-composition-vs-inheritance.md)
When to use inheritance and when to prefer composition.

## What is Inheritance?

Inheritance allows a class (child/derived class) to inherit attributes and methods from another class (parent/base class). The child class can:
- **Reuse** code from the parent
- **Extend** functionality with new methods
- **Override** parent methods with custom behavior

```python
class Employee:  # Parent/Base class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_info(self):
        return f"{self.name}: €{self.salary}/year"

class Engineer(Employee):  # Child/Derived class
    def __init__(self, name, salary, programming_languages):
        super().__init__(name, salary)  # Call parent constructor
        self.programming_languages = programming_languages
    
    def code(self):
        """New method specific to Engineer."""
        return f"{self.name} codes in {', '.join(self.programming_languages)}"

# Usage
eng = Engineer("Willem", 120000, ["Python", "Go", "Rust"])
print(eng.get_info())  # Inherited method
print(eng.code())      # Engineer-specific method
```

## Key Terminology

| Term | Definition |
|------|------------|
| **Base class** | Parent class being inherited from |
| **Derived class** | Child class that inherits |
| **Superclass** | Another term for base/parent class |
| **Subclass** | Another term for derived/child class |
| **Override** | Replace a parent method with child version |
| **Extend** | Add new functionality to inherited class |
| **super()** | Function to call parent class methods |

## Single Inheritance

The most common form - one child inherits from one parent.

```python
class CloudResource:
    """Base class for all cloud resources."""
    
    def __init__(self, name, cloud_provider):
        self.name = name
        self.cloud_provider = cloud_provider
        self.active = True
    
    def deactivate(self):
        self.active = False
        return f"{self.name} deactivated"
    
    def get_info(self):
        status = "Active" if self.active else "Inactive"
        return f"{self.name} on {self.cloud_provider} [{status}]"


class VirtualMachine(CloudResource):
    """Specialized resource: Virtual Machine."""
    
    def __init__(self, name, cloud_provider, cpu_cores, memory_gb):
        super().__init__(name, cloud_provider)
        self.cpu_cores = cpu_cores
        self.memory_gb = memory_gb
    
    def get_specs(self):
        return f"{self.cpu_cores} cores, {self.memory_gb}GB RAM"
    
    def get_info(self):
        """Override parent method."""
        base_info = super().get_info()
        return f"{base_info} - {self.get_specs()}"


class StorageBucket(CloudResource):
    """Specialized resource: Storage."""
    
    def __init__(self, name, cloud_provider, size_gb):
        super().__init__(name, cloud_provider)
        self.size_gb = size_gb
    
    def get_info(self):
        """Override parent method."""
        base_info = super().get_info()
        return f"{base_info} - {self.size_gb}GB storage"


# Usage
vm = VirtualMachine("atlas-vm", "Azure", 4, 16)
bucket = StorageBucket("backup-storage", "AWS", 1000)

print(vm.get_info())      # Uses overridden method
print(bucket.get_info())  # Uses overridden method

# Both inherit deactivate()
vm.deactivate()
print(vm.get_info())
```

**Benefits:**
- Code reuse (both VM and Storage share CloudResource code)
- Consistent interface (all resources have `get_info()`, `deactivate()`)
- Easy to extend (add new resource types easily)

## Multiple Inheritance

Python allows inheriting from multiple parent classes.

```python
class Loggable:
    """Mixin for logging functionality."""
    
    def log(self, message):
        print(f"[LOG] {self.__class__.__name__}: {message}")


class Serializable:
    """Mixin for serialization."""
    
    def to_dict(self):
        return {
            k: v for k, v in self.__dict__.items()
            if not k.startswith('_')
        }


class Employee:
    """Base employee class."""
    
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id


class CloudEngineer(Employee, Loggable, Serializable):
    """Engineer with logging and serialization."""
    
    def __init__(self, name, employee_id, certifications):
        super().__init__(name, employee_id)
        self.certifications = certifications
    
    def add_certification(self, cert):
        self.certifications.append(cert)
        self.log(f"Added certification: {cert}")


# Usage
engineer = CloudEngineer("Willem", "E1001", ["AZ-104", "AZ-700"])

# From Employee
print(engineer.name)

# From Loggable
engineer.log("Starting deployment")

# From Serializable
print(engineer.to_dict())

# Own method
engineer.add_certification("AZ-305")
```

**Use Cases for Multiple Inheritance:**
- Mixins (small, focused functionality)
- Combining unrelated capabilities
- Interface implementation

## Method Resolution Order (MRO)

When a class inherits from multiple parents, Python uses the C3 linearization algorithm to determine method resolution order.

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):  # Multiple inheritance
    pass

# What happens when we call D().method()?
d = D()
print(d.method())  # "B"

# Check the MRO
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, 
#  <class '__main__.A'>, <class 'object'>)

# Or more readable:
print(D.mro())
```

**Rules:**
1. Search in the child class first
2. Then search in parent classes from left to right
3. Never search a parent before all its children
4. Preserve ordering from parent class list

## The `super()` Function

`super()` provides access to methods in parent classes.

### Basic Usage

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        return f"{self.brand} {self.model} starting..."

class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  # Call parent __init__
        self.battery_capacity = battery_capacity
    
    def start(self):
        base_start = super().start()  # Call parent method
        return f"{base_start} (Electric mode)"

ev = ElectricVehicle("Tesla", "Model 3", 75)
print(ev.start())  # "Tesla Model 3 starting... (Electric mode)"
```

### With Multiple Inheritance

```python
class Base1:
    def __init__(self):
        print("Base1.__init__")
        super().__init__()

class Base2:
    def __init__(self):
        print("Base2.__init__")
        super().__init__()

class Derived(Base1, Base2):
    def __init__(self):
        print("Derived.__init__")
        super().__init__()

d = Derived()
# Output:
# Derived.__init__
# Base1.__init__
# Base2.__init__

# super() follows the MRO!
print(Derived.__mro__)
```

## Method Overriding

Child classes can replace parent methods entirely.

```python
class Report:
    """Base report class."""
    
    def generate(self):
        return "Generic report"
    
    def send(self, recipient):
        content = self.generate()
        return f"Sending to {recipient}: {content}"


class DetailedReport(Report):
    """Override generate() for detailed report."""
    
    def generate(self):
        return "Detailed report with charts and analysis"


class QuickReport(Report):
    """Override both methods."""
    
    def generate(self):
        return "Quick summary"
    
    def send(self, recipient):
        # Completely different implementation
        content = self.generate()
        return f"Quick send to {recipient}: {content}"


# Usage
detailed = DetailedReport()
quick = QuickReport()

print(detailed.send("manager@company.com"))
print(quick.send("team@company.com"))
```

## Extending Parent Methods

Sometimes you want to add to parent behavior, not replace it:

```python
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def calculate_salary(self):
        return self.base_salary


class SalesEmployee(Employee):
    def __init__(self, name, base_salary, commission_rate):
        super().__init__(name, base_salary)
        self.commission_rate = commission_rate
        self.sales = 0
    
    def calculate_salary(self):
        """Extend parent calculation."""
        base = super().calculate_salary()  # Get parent result
        commission = self.sales * self.commission_rate
        return base + commission  # Add to it


sales_person = SalesEmployee("Alice", 50000, 0.05)
sales_person.sales = 100000

print(sales_person.calculate_salary())  # 50000 + 5000 = 55000
```

## Composition vs. Inheritance

**Inheritance** = "is-a" relationship
**Composition** = "has-a" relationship

### When to Use Inheritance

```python
# Good: Engineer IS-A Employee
class Employee:
    def __init__(self, name):
        self.name = name

class Engineer(Employee):  # ✓ Makes sense
    def __init__(self, name, languages):
        super().__init__(name)
        self.languages = languages
```

### When to Use Composition

```python
# Bad: Engine is not a type of Car
class Car(Engine):  # ✗ Doesn't make sense
    pass

# Good: Car HAS-A Engine
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return "Engine running"

class Car:  # ✓ Composition
    def __init__(self, engine):
        self.engine = engine  # Has-a relationship
    
    def start(self):
        return self.engine.start()
```

### Favor Composition Example

```python
class EmailSender:
    """Handles email sending."""
    def send(self, to, subject, body):
        print(f"Sending email to {to}: {subject}")

class SMSSender:
    """Handles SMS sending."""
    def send(self, phone, message):
        print(f"Sending SMS to {phone}: {message}")

class NotificationService:
    """Uses composition instead of inheritance."""
    
    def __init__(self):
        self.email_sender = EmailSender()
        self.sms_sender = SMSSender()
    
    def send_notification(self, user, message):
        # Use composed objects
        self.email_sender.send(user.email, "Notification", message)
        if user.phone:
            self.sms_sender.send(user.phone, message)

# This is more flexible than inheriting from EmailSender or SMSSender
```

**Advantages of Composition:**
- More flexible
- Easier to change at runtime
- Avoids complex inheritance hierarchies
- Clearer "has-a" relationships

## isinstance() and issubclass()

Check inheritance relationships:

```python
class Employee:
    pass

class Engineer(Employee):
    pass

class Manager(Employee):
    pass

eng = Engineer()
mgr = Manager()

# isinstance - check if object is instance of class
print(isinstance(eng, Engineer))   # True
print(isinstance(eng, Employee))   # True (parent class)
print(isinstance(eng, Manager))    # False

# issubclass - check if class inherits from another
print(issubclass(Engineer, Employee))  # True
print(issubclass(Engineer, Manager))   # False
print(issubclass(Engineer, Engineer))  # True
```

## Abstract Base Classes (Preview)

Inheritance works great with abstract base classes (covered in Section 600):

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base - cannot instantiate."""
    
    @abstractmethod
    def area(self):
        """All shapes must implement area()."""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Implementation required."""
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Implementation required."""
        return self.width * self.height

# shape = Shape()  # ✗ TypeError - can't instantiate abstract class
circle = Circle(5)  # ✓ OK
print(circle.area())
```

## Best Practices

### ✅ DO

- Use inheritance for "is-a" relationships
- Keep inheritance hierarchies shallow (2-3 levels max)
- Use `super()` for calling parent methods
- Override methods to specialize behavior
- Document what child classes should/must override

### ❌ DON'T

- Create deep inheritance hierarchies (>3 levels)
- Use inheritance just for code reuse (consider composition)
- Change method signatures when overriding
- Forget to call `super().__init__()` in constructors
- Inherit from multiple concrete classes (prefer one concrete + mixins)

## Common Patterns

### 1. Template Method Pattern

```python
class DataProcessor:
    """Base class with template method."""
    
    def process(self, data):
        """Template method - defines algorithm structure."""
        cleaned = self.clean(data)
        transformed = self.transform(cleaned)
        return self.output(transformed)
    
    def clean(self, data):
        """Default implementation."""
        return data.strip()
    
    def transform(self, data):
        """Must override."""
        raise NotImplementedError
    
    def output(self, data):
        """Default implementation."""
        return data


class UpperCaseProcessor(DataProcessor):
    def transform(self, data):
        """Specific implementation."""
        return data.upper()

class ReverseProcessor(DataProcessor):
    def transform(self, data):
        """Different implementation."""
        return data[::-1]
```

### 2. Hierarchical Specialization

```python
class CloudResource:
    """Top level."""
    pass

class Compute(CloudResource):
    """Second level."""
    pass

class VirtualMachine(Compute):
    """Third level - specific type."""
    pass

class Container(Compute):
    """Another third level option."""
    pass
```

## Next Steps

- **Section 500 - Polymorphism** - Multiple forms through inheritance
- **Section 600 - Abstraction** - Abstract base classes
- **Section 800 - Design Patterns** - Patterns using inheritance

---

[Back to Main README](../README.md)
