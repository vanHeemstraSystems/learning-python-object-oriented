"""
Inheritance Examples
Demonstrates single inheritance, multiple inheritance, and MRO.
"""

from abc import ABC, abstractmethod


# ============================================================================
# Example 1: Single Inheritance Hierarchy
# ============================================================================

class CloudResource:
    """Base class for all cloud resources."""
    
    resource_count = 0  # Class attribute
    
    def __init__(self, name, cloud_provider, region):
        self.name = name
        self.cloud_provider = cloud_provider
        self.region = region
        self.active = True
        self.tags = {}
        CloudResource.resource_count += 1
    
    def activate(self):
        """Activate the resource."""
        self.active = True
        return f"{self.name} activated"
    
    def deactivate(self):
        """Deactivate the resource."""
        self.active = False
        return f"{self.name} deactivated"
    
    def add_tag(self, key, value):
        """Add a tag to the resource."""
        self.tags[key] = value
    
    def get_info(self):
        """Get resource information."""
        status = "Active" if self.active else "Inactive"
        return f"{self.name} ({self.cloud_provider}/{self.region}) [{status}]"
    
    def __str__(self):
        return self.get_info()


class VirtualMachine(CloudResource):
    """Virtual Machine resource."""
    
    def __init__(self, name, cloud_provider, region, cpu_cores, memory_gb, os):
        super().__init__(name, cloud_provider, region)
        self.cpu_cores = cpu_cores
        self.memory_gb = memory_gb
        self.os = os
        self.running = False
    
    def start(self):
        """Start the VM."""
        if not self.active:
            return "Cannot start inactive VM"
        self.running = True
        return f"{self.name} started"
    
    def stop(self):
        """Stop the VM."""
        self.running = False
        return f"{self.name} stopped"
    
    def get_specs(self):
        """Get VM specifications."""
        return f"{self.cpu_cores} cores, {self.memory_gb}GB RAM, {self.os}"
    
    def get_info(self):
        """Override parent method."""
        base_info = super().get_info()  # Call parent version
        run_status = "Running" if self.running else "Stopped"
        return f"{base_info} - {self.get_specs()} [{run_status}]"


class KubernetesCluster(CloudResource):
    """Kubernetes cluster resource."""
    
    def __init__(self, name, cloud_provider, region, node_count, k8s_version):
        super().__init__(name, cloud_provider, region)
        self.node_count = node_count
        self.k8s_version = k8s_version
        self.namespaces = ["default", "kube-system"]
    
    def scale(self, new_node_count):
        """Scale the cluster."""
        if new_node_count < 1:
            return "Cluster must have at least 1 node"
        old_count = self.node_count
        self.node_count = new_node_count
        return f"Scaled from {old_count} to {new_node_count} nodes"
    
    def add_namespace(self, namespace):
        """Add a namespace."""
        if namespace not in self.namespaces:
            self.namespaces.append(namespace)
    
    def get_info(self):
        """Override parent method."""
        base_info = super().get_info()
        return f"{base_info} - {self.node_count} nodes, v{self.k8s_version}"


print("=" * 70)
print("Example 1: Single Inheritance")
print("=" * 70)

# Create instances
vm = VirtualMachine("atlas-vm", "Azure", "westeurope", 4, 16, "Ubuntu 22.04")
cluster = KubernetesCluster("atlas-aks", "Azure", "northeurope", 3, "1.28")

# Use inherited methods
vm.add_tag("environment", "production")
vm.add_tag("team", "atlas")
cluster.add_tag("environment", "production")

# Use specific methods
print(vm.start())
print(cluster.scale(5))

# Polymorphism - both use overridden get_info()
print(f"\nVM Info: {vm.get_info()}")
print(f"Cluster Info: {cluster.get_info()}")

# Class attribute shared across all instances
print(f"\nTotal cloud resources created: {CloudResource.resource_count}")


# ============================================================================
# Example 2: Multiple Inheritance and Mixins
# ============================================================================

class Loggable:
    """Mixin for logging functionality."""
    
    def log(self, message, level="INFO"):
        """Log a message."""
        print(f"[{level}] {self.__class__.__name__}: {message}")


class Serializable:
    """Mixin for serialization."""
    
    def to_dict(self):
        """Convert to dictionary."""
        return {
            k: v for k, v in self.__dict__.items()
            if not k.startswith('_') and not callable(v)
        }
    
    def from_dict(self, data):
        """Load from dictionary."""
        for key, value in data.items():
            setattr(self, key, value)


class Validatable:
    """Mixin for validation."""
    
    def validate(self):
        """Validate object state."""
        errors = []
        
        # Check for required attributes
        required = getattr(self, '_required_fields', [])
        for field in required:
            if not hasattr(self, field) or getattr(self, field) is None:
                errors.append(f"Missing required field: {field}")
        
        return errors if errors else True


class Employee(Loggable, Serializable, Validatable):
    """Employee with multiple mixins."""
    
    _required_fields = ['name', 'employee_id', 'email']
    
    def __init__(self, name, employee_id, email, department=None):
        self.name = name
        self.employee_id = employee_id
        self.email = email
        self.department = department
        self.log(f"Created employee: {name}", "INFO")
    
    def update_department(self, department):
        """Update department with logging."""
        old = self.department
        self.department = department
        self.log(f"Department changed: {old} -> {department}")


class CloudEngineer(Employee):
    """Engineer with additional capabilities from mixins."""
    
    _required_fields = Employee._required_fields + ['specialty']
    
    def __init__(self, name, employee_id, email, specialty, certifications=None):
        super().__init__(name, employee_id, email, "Engineering")
        self.specialty = specialty
        self.certifications = certifications or []
    
    def add_certification(self, cert):
        """Add certification with logging."""
        self.certifications.append(cert)
        self.log(f"Added certification: {cert}", "INFO")


print("\n" + "=" * 70)
print("Example 2: Multiple Inheritance (Mixins)")
print("=" * 70)

engineer = CloudEngineer(
    "Willem van Heemstra",
    "E1001",
    "willem@rockstars.com",
    "DevSecOps",
    ["AZ-104", "AZ-700"]
)

# From Loggable mixin
engineer.add_certification("AZ-305")

# From Serializable mixin
data = engineer.to_dict()
print(f"\nSerialized: {data}")

# From Validatable mixin
validation = engineer.validate()
print(f"Validation: {validation}")

# Check MRO (Method Resolution Order)
print(f"\nMRO: {[cls.__name__ for cls in CloudEngineer.__mro__]}")


# ============================================================================
# Example 3: Method Resolution Order (MRO)
# ============================================================================

class A:
    def method(self):
        print("A.method()")
        return "A"


class B(A):
    def method(self):
        print("B.method()")
        result = super().method()
        return f"B->{result}"


class C(A):
    def method(self):
        print("C.method()")
        result = super().method()
        return f"C->{result}"


class D(B, C):
    """Diamond inheritance - inherits from both B and C."""
    def method(self):
        print("D.method()")
        result = super().method()
        return f"D->{result}"


print("\n" + "=" * 70)
print("Example 3: Method Resolution Order (Diamond Problem)")
print("=" * 70)

d = D()
result = d.method()
print(f"\nResult: {result}")

# Show MRO
print(f"\nMRO for D: {[cls.__name__ for cls in D.__mro__]}")
print("D -> B -> C -> A -> object")


# ============================================================================
# Example 4: super() in Multiple Inheritance
# ============================================================================

class Logger:
    def __init__(self, log_file=None):
        self.log_file = log_file
        print(f"Logger.__init__ (log_file={log_file})")
        super().__init__()  # Continue MRO chain


class Authenticator:
    def __init__(self, auth_method="password"):
        self.auth_method = auth_method
        print(f"Authenticator.__init__ (auth_method={auth_method})")
        super().__init__()  # Continue MRO chain


class Service(Logger, Authenticator):
    """Service that logs and authenticates."""
    
    def __init__(self, name, log_file=None, auth_method="password"):
        self.name = name
        print(f"Service.__init__ (name={name})")
        # super() follows MRO: Service -> Logger -> Authenticator -> object
        super().__init__(log_file=log_file)
        # Note: auth_method should be passed as keyword arg
    
    def start(self):
        return f"Service {self.name} started (logs to {self.log_file}, auth via {self.auth_method})"


print("\n" + "=" * 70)
print("Example 4: super() in Multiple Inheritance")
print("=" * 70)

service = Service("API Gateway", log_file="gateway.log", auth_method="oauth")
print(f"\n{service.start()}")


# ============================================================================
# Example 5: Composition vs Inheritance
# ============================================================================

# Bad: Using inheritance when composition is better
class BadDesign_Engine:
    """Engine class."""
    def start(self):
        return "Engine started"
    
    def stop(self):
        return "Engine stopped"


class BadDesign_Car(BadDesign_Engine):
    """Car IS-A Engine? No! Car HAS-A Engine."""
    pass  # This is wrong!


# Good: Using composition
class Engine:
    """Engine class."""
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.running = False
    
    def start(self):
        self.running = True
        return f"{self.horsepower}HP {self.fuel_type} engine started"
    
    def stop(self):
        self.running = False
        return "Engine stopped"


class Transmission:
    """Transmission class."""
    def __init__(self, transmission_type):
        self.type = transmission_type
    
    def shift(self, gear):
        return f"Shifted to gear {gear}"


class Car:
    """Car HAS-A Engine and HAS-A Transmission."""
    
    def __init__(self, make, model, engine, transmission):
        self.make = make
        self.model = model
        self.engine = engine  # Composition
        self.transmission = transmission  # Composition
    
    def start(self):
        """Delegate to engine."""
        return self.engine.start()
    
    def drive(self):
        """Use both engine and transmission."""
        if not self.engine.running:
            return "Start the engine first!"
        return f"{self.make} {self.model} driving with {self.transmission.type} transmission"


print("\n" + "=" * 70)
print("Example 5: Composition vs Inheritance")
print("=" * 70)

# Create car with components
v8_engine = Engine(400, "Gasoline")
auto_trans = Transmission("Automatic")
car = Car("Tesla", "Model S", v8_engine, auto_trans)

print(car.start())
print(car.drive())

# Can swap components easily
electric_engine = Engine(600, "Electric")
car.engine = electric_engine
print(f"\nAfter engine swap: {car.start()}")


# ============================================================================
# Example 6: isinstance and issubclass
# ============================================================================

print("\n" + "=" * 70)
print("Example 6: isinstance() and issubclass()")
print("=" * 70)

# isinstance checks
print(f"vm is VirtualMachine: {isinstance(vm, VirtualMachine)}")
print(f"vm is CloudResource: {isinstance(vm, CloudResource)}")
print(f"vm is KubernetesCluster: {isinstance(vm, KubernetesCluster)}")

# issubclass checks
print(f"\nVirtualMachine is subclass of CloudResource: {issubclass(VirtualMachine, CloudResource)}")
print(f"VirtualMachine is subclass of VirtualMachine: {issubclass(VirtualMachine, VirtualMachine)}")
print(f"CloudResource is subclass of VirtualMachine: {issubclass(CloudResource, VirtualMachine)}")

# Check against tuple of classes
print(f"\nvm is instance of (VM, Cluster): {isinstance(vm, (VirtualMachine, KubernetesCluster))}")
