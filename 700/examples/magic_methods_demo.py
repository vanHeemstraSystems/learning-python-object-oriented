"""
Magic Methods Examples
Operator overloading and special methods.
"""

# Example 1: String representation
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: €{self.price}"
    
    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

p = Product("Laptop", 1200)
print(str(p))
print(repr(p))

# Example 2: Comparison operators
class Version:
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor
    
    def __eq__(self, other):
        return self.major == other.major and self.minor == other.minor
    
    def __lt__(self, other):
        if self.major != other.major:
            return self.major < other.major
        return self.minor < other.minor

v1 = Version(1, 5)
v2 = Version(2, 0)
print(f"v1 < v2: {v1 < v2}")
print(f"v1 == v2: {v1 == v2}")

# Example 3: Container methods
class TodoList:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __contains__(self, item):
        return item in self.items
    
    def add(self, item):
        self.items.append(item)

todos = TodoList()
todos.add("Buy milk")
todos.add("Write code")
print(f"Length: {len(todos)}")
print(f"First: {todos[0]}")
print(f"Contains 'Write code': {'Write code' in todos}")

# Example 4: Context manager
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        import time
        elapsed = time.time() - self.start
        print(f"Elapsed: {elapsed:.2f}s")

with Timer():
    sum(range(1000000))
