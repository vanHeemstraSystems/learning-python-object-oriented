# 800 - Design Patterns

Design patterns are reusable solutions to common programming problems. They represent best practices refined over years of software development.

## Overview

This section covers classic design patterns in Python:
- Creational: Singleton, Factory, Builder
- Structural: Adapter, Decorator, Facade
- Behavioral: Observer, Strategy, Command

## Creational Patterns

### Singleton Pattern

Ensure only one instance exists:

```python
class DatabaseConnection:
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
        self.connection = "Database connection"

# Always returns same instance
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True
```

### Factory Pattern

Create objects without specifying exact class:

```python
class CloudResource:
    pass

class VM(CloudResource):
    def __init__(self, cpu, memory):
        self.cpu = cpu
        self.memory = memory

class Storage(CloudResource):
    def __init__(self, size):
        self.size = size

class ResourceFactory:
    @staticmethod
    def create_resource(resource_type, **kwargs):
        if resource_type == "vm":
            return VM(kwargs['cpu'], kwargs['memory'])
        elif resource_type == "storage":
            return Storage(kwargs['size'])
        raise ValueError(f"Unknown type: {resource_type}")

# Factory creates appropriate type
vm = ResourceFactory.create_resource("vm", cpu=4, memory=16)
storage = ResourceFactory.create_resource("storage", size=1000)
```

### Builder Pattern

Construct complex objects step by step:

```python
class Server:
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.storage = None
        self.os = None

class ServerBuilder:
    def __init__(self):
        self.server = Server()
    
    def set_cpu(self, cpu):
        self.server.cpu = cpu
        return self  # Return self for chaining
    
    def set_memory(self, memory):
        self.server.memory = memory
        return self
    
    def set_storage(self, storage):
        self.server.storage = storage
        return self
    
    def set_os(self, os):
        self.server.os = os
        return self
    
    def build(self):
        return self.server

# Fluent interface
server = (ServerBuilder()
    .set_cpu(8)
    .set_memory(32)
    .set_storage(500)
    .set_os("Ubuntu")
    .build())
```

## Structural Patterns

### Adapter Pattern

Make incompatible interfaces work together:

```python
class OldPrinter:
    def print_document(self, text):
        return f"Old printer: {text}"

class NewPrinter:
    def advanced_print(self, text, color, duplex):
        return f"New printer ({color}, duplex={duplex}): {text}"

class PrinterAdapter:
    """Adapts NewPrinter to OldPrinter interface."""
    def __init__(self, new_printer):
        self.printer = new_printer
    
    def print_document(self, text):
        # Adapt interface
        return self.printer.advanced_print(text, "black", False)

# Use both through same interface
old = OldPrinter()
new = PrinterAdapter(NewPrinter())

for printer in [old, new]:
    print(printer.print_document("Hello"))
```

### Decorator Pattern

Add behavior to objects dynamically:

```python
class Coffee:
    def cost(self):
        return 2.0
    
    def description(self):
        return "Coffee"

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost() + 0.5
    
    def description(self):
        return self._coffee.description() + ", Milk"

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost() + 0.2
    
    def description(self):
        return self._coffee.description() + ", Sugar"

# Build up decorators
coffee = Coffee()
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)

print(coffee.description())  # "Coffee, Milk, Sugar"
print(f"€{coffee.cost()}")   # €2.70
```

## Behavioral Patterns

### Observer Pattern

One-to-many dependency:

```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, event):
        for observer in self._observers:
            observer.update(event)

class StockPrice(Subject):
    def __init__(self, symbol):
        super().__init__()
        self.symbol = symbol
        self._price = 0
    
    def set_price(self, price):
        self._price = price
        self.notify({"symbol": self.symbol, "price": price})

class Investor:
    def __init__(self, name):
        self.name = name
    
    def update(self, event):
        print(f"{self.name} notified: {event['symbol']} = €{event['price']}")

# Usage
stock = StockPrice("ASML")
investor1 = Investor("Willem")
investor2 = Investor("Alice")

stock.attach(investor1)
stock.attach(investor2)

stock.set_price(850)  # Both investors notified
```

### Strategy Pattern

Encapsulate algorithms:

```python
class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError

class CreditCard(PaymentStrategy):
    def pay(self, amount):
        return f"Paid €{amount} with credit card"

class PayPal(PaymentStrategy):
    def pay(self, amount):
        return f"Paid €{amount} with PayPal"

class Crypto(PaymentStrategy):
    def pay(self, amount):
        return f"Paid €{amount} with cryptocurrency"

class ShoppingCart:
    def __init__(self, payment_strategy):
        self._strategy = payment_strategy
    
    def checkout(self, amount):
        return self._strategy.pay(amount)

# Change strategy at runtime
cart = ShoppingCart(CreditCard())
print(cart.checkout(100))

cart._strategy = PayPal()
print(cart.checkout(50))
```

### Command Pattern

Encapsulate requests:

```python
class Command:
    def execute(self):
        raise NotImplementedError

class DeployCommand(Command):
    def __init__(self, server):
        self.server = server
    
    def execute(self):
        return f"Deploying to {self.server}"

class BackupCommand(Command):
    def __init__(self, database):
        self.database = database
    
    def execute(self):
        return f"Backing up {self.database}"

class CommandQueue:
    def __init__(self):
        self.commands = []
    
    def add_command(self, command):
        self.commands.append(command)
    
    def execute_all(self):
        results = []
        for cmd in self.commands:
            results.append(cmd.execute())
        return results

# Queue and execute commands
queue = CommandQueue()
queue.add_command(DeployCommand("prod-server"))
queue.add_command(BackupCommand("main-db"))

for result in queue.execute_all():
    print(result)
```

## When to Use Each Pattern

| Pattern | Use When |
|---------|----------|
| **Singleton** | Need exactly one instance (config, connection pool) |
| **Factory** | Object creation is complex or varies |
| **Builder** | Constructing complex objects step-by-step |
| **Adapter** | Need to use incompatible interfaces |
| **Decorator** | Adding responsibilities without subclassing |
| **Observer** | One object changing affects many others |
| **Strategy** | Need interchangeable algorithms |
| **Command** | Need to queue, log, or undo operations |

## Best Practices

✅ **DO:**
- Use patterns to solve real problems
- Keep patterns simple
- Document which pattern you're using

❌ **DON'T:**
- Use patterns just to use them
- Over-engineer simple solutions
- Mix too many patterns

---

[Back to Main README](../README.md)
