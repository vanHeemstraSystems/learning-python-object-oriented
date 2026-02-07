# 500 - Polymorphism

Polymorphism means "many forms" - the ability to use objects of different types through a common interface. In Python, polymorphism is achieved through method overriding, operator overloading, and duck typing.

## Overview

This section covers:
- Method overriding and polymorphism
- Operator overloading
- Duck typing
- Type hints and protocols

## What is Polymorphism?

Polymorphism allows you to:
- Call the same method on different objects
- Get behavior specific to each object's type
- Write flexible, reusable code

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Tweet!"

# Polymorphic function - works with any object that has speak()
def animal_sound(animal):
    print(animal.speak())

animals = [Dog(), Cat(), Bird()]
for animal in animals:
    animal_sound(animal)  # Different behavior based on object type
```

## Method Overriding

Child classes provide specific implementations:

```python
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Subclass must implement")

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing €{amount} via credit card"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing €{amount} via PayPal"

class CryptoProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing €{amount} via cryptocurrency"

# Polymorphic usage
processors = [CreditCardProcessor(), PayPalProcessor(), CryptoProcessor()]

for processor in processors:
    print(processor.process_payment(100))  # Each processes differently
```

## Operator Overloading

Make custom classes work with Python operators:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Override + operator."""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Override - operator."""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Override * operator (scalar multiplication)."""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """Override == operator."""
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        """Override str() function."""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """Override repr() function."""
        return f"Vector(x={self.x}, y={self.y})"

# Use operators naturally
v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2      # Uses __add__
v4 = v2 - v1      # Uses __sub__
v5 = v1 * 3       # Uses __mul__
print(v1 == v2)   # Uses __eq__
print(v3)         # Uses __str__
```

**Common Magic Methods for Operators:**

| Operator | Method | Example |
|----------|--------|---------|
| `+` | `__add__` | `a + b` |
| `-` | `__sub__` | `a - b` |
| `*` | `__mul__` | `a * b` |
| `/` | `__truediv__` | `a / b` |
| `==` | `__eq__` | `a == b` |
| `<` | `__lt__` | `a < b` |
| `>` | `__gt__` | `a > b` |
| `len()` | `__len__` | `len(a)` |
| `str()` | `__str__` | `str(a)` |
| `repr()` | `__repr__` | `repr(a)` |

## Duck Typing

"If it walks like a duck and quacks like a duck, it's a duck."

Python doesn't check types - it checks if methods exist:

```python
class Duck:
    def quack(self):
        return "Quack!"
    
    def fly(self):
        return "Flying with wings"

class Person:
    def quack(self):
        return "I'm imitating a duck!"
    
    def fly(self):
        return "I can't fly, but I can jump"

class Airplane:
    def quack(self):
        return "Airplanes don't quack"
    
    def fly(self):
        return "Flying with engines"

def duck_test(thing):
    """Works with anything that has quack() and fly()."""
    print(thing.quack())
    print(thing.fly())
    print()

# All work - no inheritance needed!
duck_test(Duck())
duck_test(Person())
duck_test(Airplane())
```

## Real-World Example: Cloud Providers

```python
class AzureProvider:
    def deploy_vm(self, config):
        return f"Deploying Azure VM: {config['name']}"
    
    def get_cost(self, resources):
        return sum(r.get('cost', 0) for r in resources) * 1.0  # Azure pricing

class AWSProvider:
    def deploy_vm(self, config):
        return f"Deploying AWS EC2: {config['name']}"
    
    def get_cost(self, resources):
        return sum(r.get('cost', 0) for r in resources) * 0.95  # AWS pricing

class GCPProvider:
    def deploy_vm(self, config):
        return f"Deploying GCP Compute: {config['name']}"
    
    def get_cost(self, resources):
        return sum(r.get('cost', 0) for r in resources) * 0.90  # GCP pricing

class MultiCloudDeployer:
    """Works with any cloud provider through polymorphism."""
    
    def __init__(self, provider):
        self.provider = provider
    
    def deploy(self, config):
        return self.provider.deploy_vm(config)
    
    def calculate_cost(self, resources):
        return self.provider.get_cost(resources)

# Same deployer, different behaviors
azure = MultiCloudDeployer(AzureProvider())
aws = MultiCloudDeployer(AWSProvider())
gcp = MultiCloudDeployer(GCPProvider())

config = {"name": "prod-vm", "size": "large"}
resources = [{"cost": 100}, {"cost": 50}]

print(azure.deploy(config))
print(f"Azure cost: €{azure.calculate_cost(resources)}")

print(aws.deploy(config))
print(f"AWS cost: €{aws.calculate_cost(resources)}")

print(gcp.deploy(config))
print(f"GCP cost: €{gcp.calculate_cost(resources)}")
```

## Benefits of Polymorphism

1. **Flexibility** - Add new types without changing existing code
2. **Maintainability** - Changes localized to specific classes
3. **Testability** - Easy to mock objects for testing
4. **Extensibility** - New implementations don't break old code

## Best Practices

✅ **DO:**
- Design interfaces that work across types
- Use duck typing for flexibility
- Override operators when it makes sense
- Keep polymorphic interfaces consistent

❌ **DON'T:**
- Overload operators in unexpected ways
- Create complex inheritance just for polymorphism
- Rely on type checking (use duck typing instead)

---

[Back to Main README](../README.md)
