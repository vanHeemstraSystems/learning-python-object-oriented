"""
Encapsulation Examples
Demonstrates data hiding, properties, and access control.
"""


# ============================================================================
# Example 1: Private Attributes with Name Mangling
# ============================================================================

class BankAccount:
    """Demonstrates private attributes and controlled access."""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder  # Public
        self._balance = initial_balance       # Protected
        self.__account_number = self._generate_account_number()  # Private
        self.__pin = None
    
    def set_pin(self, pin):
        """Set PIN with validation."""
        if not isinstance(pin, str) or len(pin) != 4:
            raise ValueError("PIN must be 4 digits")
        if not pin.isdigit():
            raise ValueError("PIN must contain only digits")
        self.__pin = pin
    
    def verify_pin(self, pin):
        """Verify PIN without exposing it."""
        return self.__pin == pin
    
    def deposit(self, amount, pin):
        """Deposit money with PIN verification."""
        if not self.verify_pin(pin):
            raise ValueError("Invalid PIN")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
        return True
    
    def withdraw(self, amount, pin):
        """Withdraw money with PIN and balance check."""
        if not self.verify_pin(pin):
            raise ValueError("Invalid PIN")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return True
    
    def get_balance(self, pin):
        """Get balance with PIN verification."""
        if not self.verify_pin(pin):
            raise ValueError("Invalid PIN")
        return self._balance
    
    def _generate_account_number(self):
        """Protected helper method."""
        import random
        return f"NL{random.randint(1000000000, 9999999999)}"
    
    def get_account_info(self):
        """Public information without sensitive data."""
        return {
            "holder": self.account_holder,
            "account_number": self.__account_number  # Can access own private
        }


print("=" * 70)
print("Example 1: Private Attributes and Access Control")
print("=" * 70)

account = BankAccount("Willem van Heemstra", 1000)
account.set_pin("1234")

print(f"Account holder: {account.account_holder}")
print(f"Balance: €{account.get_balance('1234')}")

# Deposit
account.deposit(500, "1234")
print(f"After deposit: €{account.get_balance('1234')}")

# Direct access to protected (works but discouraged)
print(f"Protected balance: €{account._balance}")

# Direct access to private (name mangled)
try:
    print(account.__account_number)
except AttributeError as e:
    print(f"✗ Cannot access private: {e}")

# Access via name mangling (possible but very discouraged)
print(f"Via mangling: {account._BankAccount__account_number}")

# Wrong PIN
try:
    account.withdraw(100, "0000")
except ValueError as e:
    print(f"✗ Wrong PIN: {e}")


# ============================================================================
# Example 2: Properties with Validation
# ============================================================================

class Engineer:
    """Demonstrates @property decorator for controlled access."""
    
    def __init__(self, name, hourly_rate, years_experience=0):
        self._name = name
        self._hourly_rate = hourly_rate
        self._years_experience = years_experience
        self._certifications = []
    
    @property
    def name(self):
        """Get engineer name."""
        return self._name
    
    @property
    def hourly_rate(self):
        """Get hourly rate."""
        return self._hourly_rate
    
    @hourly_rate.setter
    def hourly_rate(self, value):
        """Set hourly rate with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("Hourly rate must be a number")
        if value < 0:
            raise ValueError("Hourly rate cannot be negative")
        if value > 500:
            raise ValueError("Hourly rate exceeds maximum of €500/hour")
        self._hourly_rate = value
    
    @property
    def years_experience(self):
        """Get years of experience."""
        return self._years_experience
    
    @years_experience.setter
    def years_experience(self, value):
        """Set years of experience with validation."""
        if not isinstance(value, int):
            raise TypeError("Years must be an integer")
        if value < 0:
            raise ValueError("Years cannot be negative")
        if value > 50:
            raise ValueError("Years seems unrealistic")
        self._years_experience = value
    
    @property
    def certifications(self):
        """Get certifications (read-only list copy)."""
        return self._certifications.copy()
    
    def add_certification(self, cert):
        """Add certification through method."""
        if cert not in self._certifications:
            self._certifications.append(cert)
    
    @property
    def annual_salary(self):
        """Computed property - read-only."""
        return self._hourly_rate * 40 * 52
    
    @property
    def seniority_level(self):
        """Computed property based on experience."""
        if self._years_experience < 2:
            return "Junior"
        elif self._years_experience < 5:
            return "Mid-level"
        elif self._years_experience < 10:
            return "Senior"
        else:
            return "Expert"


print("\n" + "=" * 70)
print("Example 2: Properties with Validation")
print("=" * 70)

willem = Engineer("Willem van Heemstra", 116, 29)
willem.add_certification("AZ-104")
willem.add_certification("AZ-700")

# Access like attributes
print(f"Name: {willem.name}")
print(f"Rate: €{willem.hourly_rate}/hour")
print(f"Experience: {willem.years_experience} years")
print(f"Level: {willem.seniority_level}")

# Computed property
print(f"Annual salary: €{willem.annual_salary:,.0f}")

# Update with validation
willem.hourly_rate = 120
print(f"New rate: €{willem.hourly_rate}/hour")

# Invalid updates
try:
    willem.hourly_rate = -10
except ValueError as e:
    print(f"✗ Validation error: {e}")

try:
    willem.hourly_rate = 600
except ValueError as e:
    print(f"✗ Validation error: {e}")

# Read-only computed property
try:
    willem.annual_salary = 200000
except AttributeError as e:
    print(f"✗ Cannot set read-only property: {e}")

# Certifications are protected from direct modification
certs = willem.certifications
certs.append("FAKE-CERT")  # Modifies the copy, not original
print(f"Original certifications still safe: {willem.certifications}")


# ============================================================================
# Example 3: Lazy Loading with Properties
# ============================================================================

class DatabaseConnection:
    """Demonstrates lazy loading pattern."""
    
    def __init__(self, connection_string):
        self._connection_string = connection_string
        self._connection = None  # Not connected yet
        print(f"DatabaseConnection created (not connected)")
    
    @property
    def connection(self):
        """Lazy load connection - only connects when accessed."""
        if self._connection is None:
            print(f"Establishing connection to {self._connection_string}...")
            self._connection = f"Connected to {self._connection_string}"
        return self._connection
    
    def execute(self, query):
        """Execute query - automatically connects if needed."""
        return f"{self.connection} - Executing: {query}"


print("\n" + "=" * 70)
print("Example 3: Lazy Loading")
print("=" * 70)

db = DatabaseConnection("postgres://localhost:5432/production")
print("Object created, but not connected yet")

# Connection established only when first accessed
result = db.execute("SELECT * FROM users")
print(result)

# Subsequent calls reuse existing connection
result = db.execute("SELECT * FROM orders")
print(result)


# ============================================================================
# Example 4: Dependent Properties
# ============================================================================

class Rectangle:
    """Demonstrates properties that depend on each other."""
    
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
    
    @property
    def area(self):
        """Computed from width and height."""
        return self._width * self._height
    
    @property
    def perimeter(self):
        """Computed from width and height."""
        return 2 * (self._width + self._height)
    
    @property
    def diagonal(self):
        """Computed using Pythagorean theorem."""
        import math
        return math.sqrt(self._width ** 2 + self._height ** 2)
    
    @property
    def is_square(self):
        """Computed boolean property."""
        return self._width == self._height
    
    def scale(self, factor):
        """Scale rectangle - dependent properties auto-update."""
        self._width *= factor
        self._height *= factor


print("\n" + "=" * 70)
print("Example 4: Dependent Properties")
print("=" * 70)

rect = Rectangle(5, 10)
print(f"Rectangle: {rect.width}x{rect.height}")
print(f"Area: {rect.area}")
print(f"Perimeter: {rect.perimeter}")
print(f"Diagonal: {rect.diagonal:.2f}")
print(f"Is square: {rect.is_square}")

# Change dimensions - all properties update automatically
rect.width = 10
print(f"\nAfter changing width to 10:")
print(f"Area: {rect.area}")
print(f"Is square: {rect.is_square}")

# Scale
rect.scale(2)
print(f"\nAfter scaling by 2:")
print(f"Dimensions: {rect.width}x{rect.height}")
print(f"Area: {rect.area}")


# ============================================================================
# Example 5: Property with Setter Side Effects
# ============================================================================

class CacheManager:
    """Demonstrates properties with side effects."""
    
    def __init__(self):
        self._cache_enabled = False
        self._cache = {}
        self._cache_hits = 0
        self._cache_misses = 0
    
    @property
    def cache_enabled(self):
        return self._cache_enabled
    
    @cache_enabled.setter
    def cache_enabled(self, value):
        """Setting this property has side effects."""
        old_value = self._cache_enabled
        self._cache_enabled = value
        
        if old_value != value:
            if value:
                print("✓ Cache enabled")
            else:
                print("✓ Cache disabled")
                self.clear_cache()
    
    def clear_cache(self):
        """Clear all cached data."""
        self._cache.clear()
        print(f"  Cache cleared ({len(self._cache)} items removed)")
    
    def get(self, key):
        """Get value from cache."""
        if not self._cache_enabled:
            return None
        
        if key in self._cache:
            self._cache_hits += 1
            return self._cache[key]
        else:
            self._cache_misses += 1
            return None
    
    def set(self, key, value):
        """Set value in cache."""
        if self._cache_enabled:
            self._cache[key] = value
    
    @property
    def stats(self):
        """Read-only statistics."""
        total = self._cache_hits + self._cache_misses
        hit_rate = (self._cache_hits / total * 100) if total > 0 else 0
        return {
            "hits": self._cache_hits,
            "misses": self._cache_misses,
            "hit_rate": f"{hit_rate:.1f}%",
            "size": len(self._cache)
        }


print("\n" + "=" * 70)
print("Example 5: Properties with Side Effects")
print("=" * 70)

cache = CacheManager()

# Enable cache - triggers side effect
cache.cache_enabled = True

# Use cache
cache.set("user:1", {"name": "Alice"})
cache.set("user:2", {"name": "Bob"})

print(f"Retrieved: {cache.get('user:1')}")
print(f"Retrieved: {cache.get('user:1')}")  # Hit
print(f"Retrieved: {cache.get('user:3')}")  # Miss

print(f"\nCache stats: {cache.stats}")

# Disable cache - triggers clearing
cache.cache_enabled = False

print(f"After disabling: {cache.stats}")
