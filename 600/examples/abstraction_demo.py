"""
Abstraction Examples
Abstract base classes and interfaces.
"""

from abc import ABC, abstractmethod

# Example 1: Abstract database connection
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def execute(self, query):
        pass

class PostgreSQL(Database):
    def connect(self):
        return "Connected to PostgreSQL"
    
    def execute(self, query):
        return f"PostgreSQL: {query}"

class MongoDB(Database):
    def connect(self):
        return "Connected to MongoDB"
    
    def execute(self, query):
        return f"MongoDB: {query}"

# Test
dbs = [PostgreSQL(), MongoDB()]
for db in dbs:
    print(db.connect())
    print(db.execute("SELECT * FROM users"))

# Example 2: Abstract notification
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Email: {message}")

class SMSNotifier(Notifier):
    def send(self, message):
        print(f"SMS: {message}")

# Send via all channels
notifiers = [EmailNotifier(), SMSNotifier()]
for notifier in notifiers:
    notifier.send("System alert!")
