"""
Procedural vs Object-Oriented Programming
Demonstrates the difference between paradigms using a cloud resource management example.
"""


# ============================================================================
# PROCEDURAL APPROACH
# ============================================================================

print("=" * 70)
print("PROCEDURAL PROGRAMMING APPROACH")
print("=" * 70)

# Global data structures
resources = []
total_monthly_cost = 0


def create_resource(name, cloud_provider, monthly_cost, resource_type):
    """Create a new cloud resource (procedural style)."""
    resource = {
        "name": name,
        "cloud": cloud_provider,
        "cost": monthly_cost,
        "type": resource_type,
        "active": True
    }
    resources.append(resource)
    global total_monthly_cost
    total_monthly_cost += monthly_cost
    return resource


def deactivate_resource(name):
    """Deactivate a resource."""
    for resource in resources:
        if resource["name"] == name and resource["active"]:
            resource["active"] = False
            global total_monthly_cost
            total_monthly_cost -= resource["cost"]
            return True
    return False


def get_resources_by_cloud(cloud_provider):
    """Get all resources for a specific cloud provider."""
    return [r for r in resources if r["cloud"] == cloud_provider and r["active"]]


def calculate_total_cost():
    """Calculate total monthly cost."""
    return sum(r["cost"] for r in resources if r["active"])


def get_resource_summary():
    """Get summary of all resources."""
    summary = {}
    for resource in resources:
        if resource["active"]:
            cloud = resource["cloud"]
            if cloud not in summary:
                summary[cloud] = {"count": 0, "cost": 0}
            summary[cloud]["count"] += 1
            summary[cloud]["cost"] += resource["cost"]
    return summary


# Usage
print("\nCreating resources:")
create_resource("atlas-aks-prod", "Azure", 500, "AKS Cluster")
create_resource("atlas-keyvault", "Azure", 50, "Key Vault")
create_resource("backup-s3", "AWS", 100, "S3 Bucket")
create_resource("monitoring-vm", "Azure", 200, "Virtual Machine")

print(f"Total resources: {len(resources)}")
print(f"Total monthly cost: €{calculate_total_cost()}")

print("\nResources by cloud:")
for cloud in ["Azure", "AWS"]:
    cloud_resources = get_resources_by_cloud(cloud)
    print(f"{cloud}: {len(cloud_resources)} resources")

print("\nDeactivating monitoring-vm...")
deactivate_resource("monitoring-vm")
print(f"New total cost: €{calculate_total_cost()}")

print("\nResource summary:")
for cloud, info in get_resource_summary().items():
    print(f"{cloud}: {info['count']} resources, €{info['cost']}/month")


# ============================================================================
# OBJECT-ORIENTED APPROACH
# ============================================================================

print("\n" + "=" * 70)
print("OBJECT-ORIENTED PROGRAMMING APPROACH")
print("=" * 70)


class CloudResource:
    """Represents a cloud infrastructure resource."""
    
    def __init__(self, name, cloud_provider, monthly_cost, resource_type):
        """
        Initialize a cloud resource.
        
        Args:
            name (str): Resource name
            cloud_provider (str): Cloud platform (Azure, AWS, GCP)
            monthly_cost (float): Monthly cost in euros
            resource_type (str): Type of resource (VM, Storage, etc.)
        """
        self.name = name
        self.cloud_provider = cloud_provider
        self.monthly_cost = monthly_cost
        self.resource_type = resource_type
        self.active = True
    
    def deactivate(self):
        """Deactivate this resource."""
        self.active = False
    
    def activate(self):
        """Activate this resource."""
        self.active = True
    
    def get_annual_cost(self):
        """Calculate annual cost."""
        return self.monthly_cost * 12 if self.active else 0
    
    def __str__(self):
        """String representation."""
        status = "Active" if self.active else "Inactive"
        return f"{self.name} ({self.resource_type}) on {self.cloud_provider} - €{self.monthly_cost}/month [{status}]"
    
    def __repr__(self):
        """Developer representation."""
        return f"CloudResource('{self.name}', '{self.cloud_provider}', {self.monthly_cost}, '{self.resource_type}')"


class ResourceManager:
    """Manages a collection of cloud resources."""
    
    def __init__(self):
        """Initialize the resource manager."""
        self.resources = []
    
    def add_resource(self, resource):
        """Add a resource to management."""
        self.resources.append(resource)
    
    def create_resource(self, name, cloud_provider, monthly_cost, resource_type):
        """Create and add a new resource."""
        resource = CloudResource(name, cloud_provider, monthly_cost, resource_type)
        self.add_resource(resource)
        return resource
    
    def get_resource(self, name):
        """Get a resource by name."""
        for resource in self.resources:
            if resource.name == name:
                return resource
        return None
    
    def deactivate_resource(self, name):
        """Deactivate a resource by name."""
        resource = self.get_resource(name)
        if resource:
            resource.deactivate()
            return True
        return False
    
    def get_resources_by_cloud(self, cloud_provider):
        """Get all active resources for a cloud provider."""
        return [r for r in self.resources if r.cloud_provider == cloud_provider and r.active]
    
    def get_total_cost(self, active_only=True):
        """Calculate total monthly cost."""
        if active_only:
            return sum(r.monthly_cost for r in self.resources if r.active)
        return sum(r.monthly_cost for r in self.resources)
    
    def get_summary(self):
        """Get resource summary by cloud provider."""
        summary = {}
        for resource in self.resources:
            if resource.active:
                cloud = resource.cloud_provider
                if cloud not in summary:
                    summary[cloud] = {"count": 0, "cost": 0, "resources": []}
                summary[cloud]["count"] += 1
                summary[cloud]["cost"] += resource.monthly_cost
                summary[cloud]["resources"].append(resource.name)
        return summary
    
    def get_resource_count(self, active_only=True):
        """Get count of resources."""
        if active_only:
            return sum(1 for r in self.resources if r.active)
        return len(self.resources)
    
    def list_all_resources(self):
        """List all resources."""
        return self.resources


# Usage
print("\nCreating resources:")
manager = ResourceManager()

atlas_aks = manager.create_resource("atlas-aks-prod", "Azure", 500, "AKS Cluster")
atlas_kv = manager.create_resource("atlas-keyvault", "Azure", 50, "Key Vault")
backup_s3 = manager.create_resource("backup-s3", "AWS", 100, "S3 Bucket")
monitoring_vm = manager.create_resource("monitoring-vm", "Azure", 200, "Virtual Machine")

print(f"Total resources: {manager.get_resource_count()}")
print(f"Total monthly cost: €{manager.get_total_cost()}")

print("\nResources by cloud:")
for cloud in ["Azure", "AWS"]:
    cloud_resources = manager.get_resources_by_cloud(cloud)
    print(f"{cloud}: {len(cloud_resources)} resources")

print("\nDeactivating monitoring-vm...")
manager.deactivate_resource("monitoring-vm")
print(f"New total cost: €{manager.get_total_cost()}")

print("\nResource summary:")
for cloud, info in manager.get_summary().items():
    print(f"{cloud}: {info['count']} resources, €{info['cost']}/month")
    for resource_name in info['resources']:
        print(f"  - {resource_name}")

print("\nAll resources:")
for resource in manager.list_all_resources():
    print(f"  {resource}")


# ============================================================================
# COMPARISON AND ANALYSIS
# ============================================================================

print("\n" + "=" * 70)
print("COMPARISON: PROCEDURAL vs OOP")
print("=" * 70)

print("""
PROCEDURAL APPROACH:
Pros:
  ✓ Simple and straightforward for small scripts
  ✓ Less code overhead
  ✓ Easy to understand for beginners

Cons:
  ✗ Data and functions are disconnected
  ✗ Hard to manage as code grows
  ✗ Global state is risky
  ✗ Difficult to test individual components
  ✗ No encapsulation or data protection
  ✗ Hard to extend with new features

OBJECT-ORIENTED APPROACH:
Pros:
  ✓ Data and behavior are grouped together
  ✓ Clear structure and organization
  ✓ Easy to extend and maintain
  ✓ Encapsulation protects data
  ✓ Reusable components
  ✓ Easy to test with mocks
  ✓ Scales well to large codebases

Cons:
  ✗ More initial setup code
  ✗ Overkill for simple scripts
  ✗ Steeper learning curve

WHEN TO USE EACH:

Use PROCEDURAL when:
  • Writing small, one-off scripts
  • Simple data transformations
  • Quick utilities and tools
  • Performance is critical (less overhead)

Use OOP when:
  • Building applications (not just scripts)
  • Code will grow and evolve
  • Working in a team
  • Need to model real-world entities
  • Want reusable, maintainable code
  • Building frameworks or libraries
""")

print("\n" + "=" * 70)
print("KEY TAKEAWAY")
print("=" * 70)
print("""
OOP organizes code around "things" (objects) that have:
  1. State (attributes/data)
  2. Behavior (methods/functions)

This mirrors how we think about the real world, making code:
  • More intuitive
  • Easier to reason about
  • Better organized
  • More maintainable

The cloud resource example shows how OOP lets us:
  • Group related data (name, cost, cloud) with related behavior (deactivate, get_cost)
  • Create reusable components (CloudResource, ResourceManager)
  • Extend easily (could add new resource types, new managers)
  • Test independently (mock ResourceManager for testing)
""")
