"""
Simple Class Examples
Demonstrates basic class creation and object instantiation.
"""


class Dog:
    """A simple class representing a dog."""
    
    # Class attribute - shared by all instances
    species = "Canis familiaris"
    
    def __init__(self, name, age, breed):
        """
        Initialize a new Dog instance.
        
        Args:
            name (str): The dog's name
            age (int): The dog's age in years
            breed (str): The dog's breed
        """
        # Instance attributes - unique to each object
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self):
        """Return the dog's bark."""
        return f"{self.name} says Woof!"
    
    def description(self):
        """Return a formatted description of the dog."""
        return f"{self.name} is a {self.age}-year-old {self.breed}"
    
    def birthday(self):
        """Increment the dog's age by one year."""
        self.age += 1
        return f"Happy birthday {self.name}! Now {self.age} years old."


class CloudProject:
    """Represents a cloud infrastructure project."""
    
    # Class attribute
    supported_clouds = ["Azure", "AWS", "GCP"]
    
    def __init__(self, name, cloud_provider, budget):
        """
        Initialize a cloud project.
        
        Args:
            name (str): Project name
            cloud_provider (str): Cloud platform (Azure, AWS, GCP)
            budget (float): Project budget in euros
        """
        if cloud_provider not in self.supported_clouds:
            raise ValueError(f"Unsupported cloud provider: {cloud_provider}")
        
        self.name = name
        self.cloud_provider = cloud_provider
        self.budget = budget
        self.resources = []
    
    def add_resource(self, resource):
        """Add a resource to the project."""
        self.resources.append(resource)
        return f"Added {resource} to {self.name}"
    
    def get_resource_count(self):
        """Return the number of resources in the project."""
        return len(self.resources)
    
    def project_summary(self):
        """Return a summary of the project."""
        return {
            "name": self.name,
            "cloud": self.cloud_provider,
            "budget": f"€{self.budget:,.2f}",
            "resources": self.get_resource_count()
        }


def main():
    """Demonstrate basic class usage."""
    
    print("=" * 60)
    print("Dog Class Examples")
    print("=" * 60)
    
    # Create two dog instances
    beau = Dog("Beau", 5, "Dachshund")
    elvis = Dog("Elvis", 3, "Dachshund")
    
    # Access instance attributes
    print(f"\nDog 1: {beau.name}, Age: {beau.age}, Breed: {beau.breed}")
    print(f"Dog 2: {elvis.name}, Age: {elvis.age}, Breed: {elvis.breed}")
    
    # Access class attribute
    print(f"\nBoth dogs are: {Dog.species}")
    print(f"Beau's species: {beau.species}")
    print(f"Elvis's species: {elvis.species}")
    
    # Call instance methods
    print(f"\n{beau.bark()}")
    print(f"{elvis.bark()}")
    
    print(f"\n{beau.description()}")
    print(f"{elvis.description()}")
    
    # Modify instance
    print(f"\n{beau.birthday()}")
    print(f"Updated description: {beau.description()}")
    
    print("\n" + "=" * 60)
    print("CloudProject Class Examples")
    print("=" * 60)
    
    # Create project instances
    atlas = CloudProject("Atlas IDP", "Azure", 150000)
    backup = CloudProject("Backup System", "AWS", 50000)
    
    # Add resources
    print(f"\n{atlas.add_resource('AKS Cluster')}")
    print(f"{atlas.add_resource('Azure KeyVault')}")
    print(f"{atlas.add_resource('Azure DevOps Pipeline')}")
    
    print(f"\n{backup.add_resource('S3 Bucket')}")
    print(f"{backup.add_resource('Lambda Function')}")
    
    # Get summaries
    print(f"\nAtlas Project Summary:")
    for key, value in atlas.project_summary().items():
        print(f"  {key.capitalize()}: {value}")
    
    print(f"\nBackup Project Summary:")
    for key, value in backup.project_summary().items():
        print(f"  {key.capitalize()}: {value}")
    
    # Display supported clouds
    print(f"\nSupported cloud platforms: {', '.join(CloudProject.supported_clouds)}")


if __name__ == "__main__":
    main()
