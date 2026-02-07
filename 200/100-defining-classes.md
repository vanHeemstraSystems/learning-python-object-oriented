# 100 - Defining Classes

## Overview

A class is a blueprint for creating objects in Python. It encapsulates data (attributes) and behavior (methods) into a single, reusable structure. Think of a class as a template or a cookie cutter that defines the shape and characteristics of objects you'll create from it.

## Basic Syntax

```python
class ClassName:
    """Docstring describing the class."""
    
    # Class body
    pass
```

### Naming Conventions

- Use **PascalCase** (CapitalizedWords) for class names
- Make names descriptive and noun-based
- Avoid abbreviations unless universally understood

**Good examples:**
```python
class CloudEngineer:
    pass

class InternalDeveloperPlatform:
    pass

class AzureResourceGroup:
    pass
```

**Bad examples:**
```python
class cloud_engineer:  # Wrong: should be PascalCase
    pass

class CE:  # Wrong: unclear abbreviation
    pass

class process_data:  # Wrong: verb-based, sounds like function
    pass
```

## Class Components

### 1. Docstring

Every class should have a docstring immediately after the class definition:

```python
class BankAccount:
    """
    Represents a bank account with basic operations.
    
    This class provides functionality for deposits, withdrawals,
    and balance inquiries for a standard checking account.
    
    Attributes:
        account_holder (str): Name of the account holder
        balance (float): Current account balance in euros
        account_number (str): Unique account identifier
    """
    pass
```

### 2. Class Attributes

Variables defined at the class level, shared by all instances:

```python
class CloudService:
    """Represents a cloud service."""
    
    # Class attributes
    supported_regions = ["westeurope", "northeurope", "eastus"]
    service_type = "PaaS"
    
    def __init__(self, name):
        self.name = name  # Instance attribute
```

### 3. The `__init__()` Method

The constructor method that initializes new instances:

```python
class Employee:
    """Represents an employee."""
    
    def __init__(self, name, role, salary):
        """
        Initialize a new employee.
        
        Args:
            name (str): Employee's full name
            role (str): Job title or role
            salary (float): Annual salary in euros
        """
        self.name = name
        self.role = role
        self.salary = salary
```

### 4. Instance Methods

Functions that operate on instance data:

```python
class Rectangle:
    """Represents a rectangle."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate and return the area."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate and return the perimeter."""
        return 2 * (self.width + self.height)
    
    def scale(self, factor):
        """Scale the rectangle by a given factor."""
        self.width *= factor
        self.height *= factor
```

## Complete Class Example

```python
class KubernetesCluster:
    """
    Represents a Kubernetes cluster configuration.
    
    This class manages the basic configuration and operations
    for a Kubernetes cluster in Azure (AKS).
    
    Attributes:
        name (str): Cluster name
        node_count (int): Number of worker nodes
        region (str): Azure region
        version (str): Kubernetes version
    """
    
    # Class attributes
    supported_versions = ["1.28", "1.29", "1.30"]
    default_region = "westeurope"
    
    def __init__(self, name, node_count=3, region=None, version="1.30"):
        """
        Initialize a new Kubernetes cluster.
        
        Args:
            name (str): Unique cluster name
            node_count (int, optional): Number of nodes. Defaults to 3.
            region (str, optional): Azure region. Defaults to class default.
            version (str, optional): K8s version. Defaults to "1.30".
            
        Raises:
            ValueError: If version is not supported
        """
        if version not in self.supported_versions:
            raise ValueError(f"Unsupported version: {version}")
        
        self.name = name
        self.node_count = node_count
        self.region = region or self.default_region
        self.version = version
        self.status = "pending"
        self.namespaces = ["default", "kube-system"]
    
    def scale_nodes(self, new_count):
        """
        Scale the cluster to a new node count.
        
        Args:
            new_count (int): Desired number of nodes
            
        Returns:
            str: Status message
        """
        if new_count < 1:
            return "Cluster must have at least 1 node"
        
        old_count = self.node_count
        self.node_count = new_count
        return f"Scaled from {old_count} to {new_count} nodes"
    
    def add_namespace(self, namespace):
        """
        Add a namespace to the cluster.
        
        Args:
            namespace (str): Namespace name
        """
        if namespace not in self.namespaces:
            self.namespaces.append(namespace)
    
    def get_info(self):
        """
        Get cluster information.
        
        Returns:
            dict: Cluster configuration details
        """
        return {
            "name": self.name,
            "nodes": self.node_count,
            "region": self.region,
            "version": self.version,
            "status": self.status,
            "namespaces": len(self.namespaces)
        }
    
    def __repr__(self):
        """Return a developer-friendly representation."""
        return (
            f"KubernetesCluster(name='{self.name}', "
            f"nodes={self.node_count}, region='{self.region}')"
        )
```

**Usage:**
```python
# Create a cluster
atlas_cluster = KubernetesCluster(
    name="atlas-aks-prod",
    node_count=5,
    region="northeurope"
)

# Use instance methods
atlas_cluster.scale_nodes(7)
atlas_cluster.add_namespace("atlas-dev")
atlas_cluster.add_namespace("atlas-staging")

# Get information
info = atlas_cluster.get_info()
print(info)
# {'name': 'atlas-aks-prod', 'nodes': 7, 'region': 'northeurope', 
#  'version': '1.30', 'status': 'pending', 'namespaces': 4}

# Developer representation
print(repr(atlas_cluster))
# KubernetesCluster(name='atlas-aks-prod', nodes=7, region='northeurope')
```

## Class Design Principles

### 1. Single Responsibility Principle

Each class should have one clear purpose:

```python
# Good: Single responsibility
class EmailValidator:
    """Validates email addresses."""
    
    def is_valid(self, email):
        return "@" in email and "." in email

class EmailSender:
    """Sends emails."""
    
    def send(self, to, subject, body):
        # Email sending logic
        pass
```

```python
# Bad: Multiple responsibilities
class EmailHandler:
    """Does both validation and sending - too much!"""
    
    def is_valid(self, email):
        pass
    
    def send(self, to, subject, body):
        pass
```

### 2. Cohesion

Keep related functionality together:

```python
class DatabaseConnection:
    """
    Manages database connectivity.
    All methods relate to the connection.
    """
    
    def __init__(self, host, database):
        self.host = host
        self.database = database
        self.connection = None
    
    def connect(self):
        """Establish connection."""
        pass
    
    def disconnect(self):
        """Close connection."""
        pass
    
    def is_connected(self):
        """Check connection status."""
        pass
```

### 3. Encapsulation

Hide internal implementation details:

```python
class SecurePassword:
    """Manages passwords securely."""
    
    def __init__(self):
        self._hashed_password = None  # Protected attribute
    
    def set_password(self, plain_text):
        """Hash and store the password."""
        self._hashed_password = self._hash(plain_text)
    
    def verify_password(self, plain_text):
        """Verify a password attempt."""
        return self._hash(plain_text) == self._hashed_password
    
    def _hash(self, text):
        """Private method for hashing."""
        # Hashing logic here
        return hash(text)
```

## Empty Classes

Sometimes you need a simple data container:

```python
class Point:
    """Represents a 2D point."""
    pass

# Usage
p = Point()
p.x = 10
p.y = 20
```

But it's better to use a proper initialization:

```python
class Point:
    """Represents a 2D point."""
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
```

Or even better, use a dataclass (Python 3.7+):

```python
from dataclasses import dataclass

@dataclass
class Point:
    """Represents a 2D point."""
    x: float = 0.0
    y: float = 0.0
```

## Common Patterns

### 1. Configuration Class

```python
class AppConfig:
    """Application configuration."""
    
    def __init__(self):
        self.debug = False
        self.database_url = "localhost:5432"
        self.log_level = "INFO"
        self.max_retries = 3
```

### 2. Service Class

```python
class NotificationService:
    """Handles notifications."""
    
    def __init__(self, api_key):
        self.api_key = api_key
    
    def send_email(self, to, message):
        """Send email notification."""
        pass
    
    def send_sms(self, phone, message):
        """Send SMS notification."""
        pass
```

### 3. Model Class

```python
class User:
    """Represents a system user."""
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.now()
        self.is_active = True
```

## Best Practices

1. **Always include a docstring** explaining the class purpose
2. **Initialize all attributes in `__init__()`** to avoid AttributeError
3. **Use type hints** for better code clarity (Python 3.5+)
4. **Keep classes focused** on a single responsibility
5. **Use meaningful names** that clearly describe the class purpose
6. **Document complex logic** with inline comments
7. **Follow PEP 8** style guidelines

## Quick Reference

```python
class ClassName:
    """Class docstring."""
    
    # Class attribute
    class_var = "shared value"
    
    def __init__(self, param1, param2):
        """Constructor docstring."""
        # Instance attributes
        self.param1 = param1
        self.param2 = param2
    
    def instance_method(self):
        """Instance method docstring."""
        return self.param1
    
    @classmethod
    def class_method(cls):
        """Class method docstring."""
        return cls.class_var
    
    @staticmethod
    def static_method():
        """Static method docstring."""
        return "No access to class/instance"
```

## Next Steps

- Learn about [creating objects](./200-creating-objects.md) from classes
- Understand [instance attributes](./300-instance-attributes.md) in detail
- Explore [different types of methods](./500-methods.md)

---

[Back to Section 200 README](./README.md) | [Main README](../README.md)
