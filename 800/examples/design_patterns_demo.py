"""
Design Patterns Examples
Common patterns in Python.
"""

# Example 1: Singleton
class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"Singleton - same instance: {db1 is db2}")

# Example 2: Factory
class AnimalFactory:
    @staticmethod
    def create(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

dog = AnimalFactory.create("dog")
print(f"Factory - dog says: {dog.speak()}")

# Example 3: Observer
class NewsAgency:
    def __init__(self):
        self.subscribers = []
    
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
    
    def publish(self, news):
        for sub in self.subscribers:
            sub.update(news)

class Subscriber:
    def __init__(self, name):
        self.name = name
    
    def update(self, news):
        print(f"{self.name} received: {news}")

agency = NewsAgency()
sub1 = Subscriber("Alice")
sub2 = Subscriber("Bob")
agency.subscribe(sub1)
agency.subscribe(sub2)
agency.publish("Breaking news!")

# Example 4: Strategy
class SortStrategy:
    def sort(self, data):
        raise NotImplementedError

class BubbleSort(SortStrategy):
    def sort(self, data):
        return sorted(data)  # Simplified

class QuickSort(SortStrategy):
    def sort(self, data):
        return sorted(data, reverse=False)

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def sort(self, data):
        return self.strategy.sort(data)

sorter = Sorter(BubbleSort())
print(f"Strategy - sorted: {sorter.sort([3, 1, 2])}")
