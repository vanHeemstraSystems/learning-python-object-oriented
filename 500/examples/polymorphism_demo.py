"""
Polymorphism Examples
Duck typing, operator overloading, and flexible interfaces.
"""

# Example 1: Polymorphic payment processing
class PaymentMethod:
    def process(self, amount):
        raise NotImplementedError

class CreditCard(PaymentMethod):
    def process(self, amount):
        return f"Charged €{amount} to credit card"

class Bitcoin(PaymentMethod):
    def process(self, amount):
        return f"Transferred €{amount} in Bitcoin"

def checkout(payment_method, amount):
    """Works with any payment method."""
    return payment_method.process(amount)

# Test
for method in [CreditCard(), Bitcoin()]:
    print(checkout(method, 100))

# Example 2: Duck typing
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm quacking like a duck!"

def make_it_quack(thing):
    """Duck typing - if it can quack, it's good enough."""
    return thing.quack()

print(make_it_quack(Duck()))
print(make_it_quack(Person()))

# Example 3: Operator overloading
class Money:
    def __init__(self, amount):
        self.amount = amount
    
    def __add__(self, other):
        return Money(self.amount + other.amount)
    
    def __str__(self):
        return f"€{self.amount}"

price1 = Money(50)
price2 = Money(30)
total = price1 + price2
print(f"Total: {total}")
