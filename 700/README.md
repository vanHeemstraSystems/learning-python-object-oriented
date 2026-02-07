# 700 - Magic Methods (Dunder Methods)

Magic methods (also called dunder methods for "double underscore") are special methods that Python calls automatically to implement built-in behavior. They let you customize how your classes work with Python's syntax and built-in functions.

## Overview

This section covers:
- Object lifecycle (`__init__`, `__new__`, `__del__`)
- String representation (`__str__`, `__repr__`)
- Comparison operators (`__eq__`, `__lt__`, etc.)
- Container methods (`__len__`, `__getitem__`, etc.)
- Context managers (`__enter__`, `__exit__`)
- Callable objects (`__call__`)

## Common Magic Methods

### String Representation

```python
class Engineer:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
    
    def __str__(self):
        """Called by str() and print() - user-friendly."""
        return f"{self.name} (€{self.rate}/hour)"
    
    def __repr__(self):
        """Called by repr() - developer-friendly, unambiguous."""
        return f"Engineer(name='{self.name}', rate={self.rate})"

eng = Engineer("Willem", 116)
print(str(eng))   # "Willem (€116/hour)"
print(repr(eng))  # "Engineer(name='Willem', rate=116)"
print(eng)        # Calls __str__
```

### Comparison Operators

```python
class Version:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch
    
    def __eq__(self, other):
        """Equal to (==)."""
        return (self.major, self.minor, self.patch) == \
               (other.major, other.minor, other.patch)
    
    def __lt__(self, other):
        """Less than (<)."""
        return (self.major, self.minor, self.patch) < \
               (other.major, other.minor, other.patch)
    
    def __le__(self, other):
        """Less than or equal (<=)."""
        return self == other or self < other
    
    def __gt__(self, other):
        """Greater than (>)."""
        return not self <= other
    
    def __ge__(self, other):
        """Greater than or equal (>=)."""
        return not self < other
    
    def __ne__(self, other):
        """Not equal (!=)."""
        return not self == other
    
    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"

v1 = Version(1, 2, 3)
v2 = Version(1, 3, 0)

print(v1 < v2)   # True
print(v1 == v2)  # False
print(v1 >= v2)  # False
```

### Arithmetic Operators

```python
class Money:
    def __init__(self, amount, currency="EUR"):
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        """Addition (+)."""
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other):
        """Subtraction (-)."""
        if self.currency != other.currency:
            raise ValueError("Cannot subtract different currencies")
        return Money(self.amount - other.amount, self.currency)
    
    def __mul__(self, multiplier):
        """Multiplication (*)."""
        return Money(self.amount * multiplier, self.currency)
    
    def __truediv__(self, divisor):
        """Division (/)."""
        return Money(self.amount / divisor, self.currency)
    
    def __str__(self):
        return f"{self.currency}{self.amount:.2f}"

price = Money(100)
total = price * 3        # €300.00
per_item = total / 3     # €100.00
combined = price + Money(50)  # €150.00
```

### Container Methods

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self._songs = []
    
    def __len__(self):
        """Called by len()."""
        return len(self._songs)
    
    def __getitem__(self, index):
        """Called by playlist[index]."""
        return self._songs[index]
    
    def __setitem__(self, index, value):
        """Called by playlist[index] = value."""
        self._songs[index] = value
    
    def __delitem__(self, index):
        """Called by del playlist[index]."""
        del self._songs[index]
    
    def __contains__(self, song):
        """Called by 'song in playlist'."""
        return song in self._songs
    
    def __iter__(self):
        """Called by for loops."""
        return iter(self._songs)
    
    def append(self, song):
        self._songs.append(song)

playlist = Playlist("Favorites")
playlist.append("Song 1")
playlist.append("Song 2")
playlist.append("Song 3")

print(len(playlist))           # 3
print(playlist[0])             # "Song 1"
print("Song 2" in playlist)    # True

for song in playlist:          # Uses __iter__
    print(song)
```

### Context Managers

```python
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        """Called when entering 'with' block."""
        print(f"Opening connection to {self.db_name}")
        self.connection = f"Connection to {self.db_name}"
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block."""
        print(f"Closing connection to {self.db_name}")
        self.connection = None
        # Return False to propagate exceptions
        return False
    
    def execute(self, query):
        if not self.connection:
            raise RuntimeError("Not connected")
        return f"Executing: {query}"

# Automatic resource management
with DatabaseConnection("production") as db:
    print(db.execute("SELECT * FROM users"))
# Connection automatically closed

# Equivalent to:
# db = DatabaseConnection("production")
# db.__enter__()
# try:
#     db.execute("SELECT * FROM users")
# finally:
#     db.__exit__(None, None, None)
```

### Callable Objects

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        """Makes instance callable like a function."""
        return value * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15

# The instance acts like a function!
print(callable(double))  # True
```

## Complete Example: Smart List

```python
class SmartList:
    """Enhanced list with additional features."""
    
    def __init__(self, items=None):
        self._items = list(items) if items else []
    
    # String representation
    def __str__(self):
        return f"SmartList({self._items})"
    
    def __repr__(self):
        return f"SmartList({self._items!r})"
    
    # Container methods
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value
    
    def __delitem__(self, index):
        del self._items[index]
    
    def __contains__(self, item):
        return item in self._items
    
    def __iter__(self):
        return iter(self._items)
    
    # Arithmetic
    def __add__(self, other):
        """Concatenate lists."""
        if isinstance(other, SmartList):
            return SmartList(self._items + other._items)
        return SmartList(self._items + list(other))
    
    def __mul__(self, times):
        """Repeat list."""
        return SmartList(self._items * times)
    
    # Comparison
    def __eq__(self, other):
        if isinstance(other, SmartList):
            return self._items == other._items
        return self._items == other
    
    # Boolean
    def __bool__(self):
        """False if empty."""
        return len(self._items) > 0
    
    # Append method
    def append(self, item):
        self._items.append(item)

# Usage
sl = SmartList([1, 2, 3])
print(len(sl))          # 3
print(sl[0])            # 1
print(2 in sl)          # True

sl2 = sl + [4, 5]       # SmartList([1, 2, 3, 4, 5])
sl3 = sl * 2            # SmartList([1, 2, 3, 1, 2, 3])

for item in sl:         # Iteration
    print(item)
```

## Magic Method Categories

### Object Lifecycle
- `__new__` - Create instance
- `__init__` - Initialize instance
- `__del__` - Cleanup when deleted

### Representation
- `__str__` - Informal string (user)
- `__repr__` - Official string (developer)
- `__format__` - Custom formatting
- `__bytes__` - Byte representation

### Comparison
- `__eq__` - Equal (==)
- `__ne__` - Not equal (!=)
- `__lt__` - Less than (<)
- `__le__` - Less or equal (<=)
- `__gt__` - Greater than (>)
- `__ge__` - Greater or equal (>=)

### Arithmetic
- `__add__` - Addition (+)
- `__sub__` - Subtraction (-)
- `__mul__` - Multiplication (*)
- `__truediv__` - Division (/)
- `__floordiv__` - Floor division (//)
- `__mod__` - Modulo (%)
- `__pow__` - Power (**)

### Containers
- `__len__` - Length
- `__getitem__` - Get item
- `__setitem__` - Set item
- `__delitem__` - Delete item
- `__contains__` - Membership test
- `__iter__` - Iterator
- `__next__` - Next item

### Context Management
- `__enter__` - Enter context
- `__exit__` - Exit context

### Callable
- `__call__` - Make callable

## Best Practices

✅ **DO:**
- Implement `__repr__` for debugging
- Implement `__str__` for user output
- Use `__eq__` for equality
- Implement context managers for resources

❌ **DON'T:**
- Implement magic methods with unexpected behavior
- Use `__del__` for critical cleanup (use context managers)
- Forget to handle edge cases

---

[Back to Main README](../README.md)
