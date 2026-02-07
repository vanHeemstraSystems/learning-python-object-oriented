"""
Class vs Instance Attributes
Demonstrates the difference between class and instance attributes.
"""


class CloudEngineer:
    """Represents a cloud engineer with certifications."""
    
    # Class attributes - shared across ALL instances
    cloud_platforms = ["Azure", "AWS", "GCP"]
    total_engineers = 0
    
    def __init__(self, name, specialty, hourly_rate):
        """
        Initialize a cloud engineer.
        
        Args:
            name (str): Engineer's name
            specialty (str): Area of expertise
            hourly_rate (float): Billing rate per hour
        """
        # Instance attributes - unique to each object
        self.name = name
        self.specialty = specialty
        self.hourly_rate = hourly_rate
        self.certifications = []  # Each engineer has their own list
        
        # Increment class attribute
        CloudEngineer.total_engineers += 1
    
    def add_certification(self, cert_code):
        """Add a certification to this engineer's record."""
        self.certifications.append(cert_code)
        return f"{self.name} earned certification: {cert_code}"
    
    def calculate_monthly_revenue(self, hours_per_month):
        """Calculate potential monthly revenue."""
        return self.hourly_rate * hours_per_month
    
    @classmethod
    def get_total_engineers(cls):
        """Return the total number of engineer instances created."""
        return cls.total_engineers
    
    @classmethod
    def add_platform(cls, platform):
        """Add a new cloud platform to the class-level list."""
        if platform not in cls.cloud_platforms:
            cls.cloud_platforms.append(platform)
            return f"Added {platform} to supported platforms"
        return f"{platform} already in supported platforms"
    
    @staticmethod
    def validate_cert_code(code):
        """
        Validate certification code format.
        Static method - doesn't need instance or class data.
        """
        valid_prefixes = ["AZ-", "AWS-", "GCP-", "CKAD-", "CKA-"]
        return any(code.startswith(prefix) for prefix in valid_prefixes)


class TeamRockstarsProject:
    """Represents a Team Rockstars client project."""
    
    # Class attribute - shared revenue model
    revenue_split = {"rockstars": 0.30, "engineer": 0.70}
    active_projects = 0
    
    def __init__(self, project_name, client_name, engineer_count):
        """
        Initialize a project.
        
        Args:
            project_name (str): Name of the project
            client_name (str): Client organization name
            engineer_count (int): Number of engineers assigned
        """
        self.project_name = project_name
        self.client_name = client_name
        self.engineer_count = engineer_count
        self.hours_logged = 0
        self.is_active = True
        
        TeamRockstarsProject.active_projects += 1
    
    def log_hours(self, hours, hourly_rate):
        """
        Log billable hours for the project.
        
        Args:
            hours (float): Hours worked
            hourly_rate (float): Billing rate per hour
            
        Returns:
            dict: Revenue breakdown
        """
        self.hours_logged += hours
        total_revenue = hours * hourly_rate
        
        return {
            "total": total_revenue,
            "rockstars_share": total_revenue * self.revenue_split["rockstars"],
            "engineer_share": total_revenue * self.revenue_split["engineer"]
        }
    
    @classmethod
    def update_revenue_split(cls, rockstars_pct):
        """
        Update the company-wide revenue split.
        This affects ALL projects (class attribute).
        
        Args:
            rockstars_pct (float): Percentage for Team Rockstars (0-1)
        """
        if 0 <= rockstars_pct <= 1:
            cls.revenue_split = {
                "rockstars": rockstars_pct,
                "engineer": 1 - rockstars_pct
            }
            return f"Revenue split updated: {rockstars_pct*100}% / {(1-rockstars_pct)*100}%"
        return "Invalid percentage"


def main():
    """Demonstrate class vs instance attributes."""
    
    print("=" * 70)
    print("CLASS vs INSTANCE ATTRIBUTES")
    print("=" * 70)
    
    # Create engineer instances
    willem = CloudEngineer("Willem van Heemstra", "DevSecOps", 116)
    sabine = CloudEngineer("Sabine", "Security Architecture", 120)
    
    print(f"\n{'Instance Attributes (Unique to Each Object)':-^70}")
    
    # Each instance has its own attributes
    print(f"\nWillem's specialty: {willem.specialty}")
    print(f"Sabine's specialty: {sabine.specialty}")
    print(f"Willem's rate: €{willem.hourly_rate}/hour")
    print(f"Sabine's rate: €{sabine.hourly_rate}/hour")
    
    # Add certifications (instance-specific)
    willem.add_certification("AZ-104")
    willem.add_certification("AZ-700")
    sabine.add_certification("AZ-500")
    
    print(f"\nWillem's certifications: {willem.certifications}")
    print(f"Sabine's certifications: {sabine.certifications}")
    
    print(f"\n{'Class Attributes (Shared Across All Instances)':-^70}")
    
    # Class attributes are shared
    print(f"\nSupported platforms (via class): {CloudEngineer.cloud_platforms}")
    print(f"Supported platforms (via willem): {willem.cloud_platforms}")
    print(f"Supported platforms (via sabine): {sabine.cloud_platforms}")
    
    # Modifying class attribute affects all instances
    print(f"\n{CloudEngineer.add_platform('Oracle Cloud')}")
    
    print(f"\nAfter adding Oracle Cloud:")
    print(f"  Via CloudEngineer class: {CloudEngineer.cloud_platforms}")
    print(f"  Via willem instance: {willem.cloud_platforms}")
    print(f"  Via sabine instance: {sabine.cloud_platforms}")
    
    # Class method accessing class attribute
    print(f"\nTotal engineers created: {CloudEngineer.get_total_engineers()}")
    
    # Create another engineer
    jan = CloudEngineer("Jan", "Cloud Architecture", 125)
    print(f"After creating Jan: {CloudEngineer.get_total_engineers()} engineers")
    
    print(f"\n{'Static Method (No Class or Instance Data Needed)':-^70}")
    
    # Static method doesn't need instance or class
    test_codes = ["AZ-305", "INVALID-123", "AWS-SAA", "RANDOM"]
    
    print(f"\nValidating certification codes:")
    for code in test_codes:
        is_valid = CloudEngineer.validate_cert_code(code)
        status = "✓ Valid" if is_valid else "✗ Invalid"
        print(f"  {code}: {status}")
    
    print(f"\n{'Project Revenue Sharing Example':-^70}")
    
    # Create projects
    atlas = TeamRockstarsProject("Atlas IDP", "Confidential Client", 10)
    devops = TeamRockstarsProject("DevOps Pipeline", "Tech Corp", 5)
    
    print(f"\nInitial revenue split: {TeamRockstarsProject.revenue_split}")
    
    # Log hours and calculate revenue
    revenue = atlas.log_hours(40, 116)
    print(f"\nAtlas project - 40 hours @ €116/hour:")
    print(f"  Total revenue: €{revenue['total']:,.2f}")
    print(f"  Team Rockstars: €{revenue['rockstars_share']:,.2f}")
    print(f"  Engineer: €{revenue['engineer_share']:,.2f}")
    
    # Update class attribute - affects all instances
    print(f"\n{TeamRockstarsProject.update_revenue_split(0.35)}")
    
    # Same calculation with new split
    revenue_new = devops.log_hours(40, 116)
    print(f"\nDevOps project - 40 hours @ €116/hour (with new split):")
    print(f"  Total revenue: €{revenue_new['total']:,.2f}")
    print(f"  Team Rockstars: €{revenue_new['rockstars_share']:,.2f}")
    print(f"  Engineer: €{revenue_new['engineer_share']:,.2f}")
    
    print(f"\nActive projects: {TeamRockstarsProject.active_projects}")
    
    print(f"\n{'WARNING: Modifying Class Attributes via Instance':-^70}")
    
    # Demonstrate dangerous pattern
    print("\nDangerous: Modifying mutable class attribute via instance")
    print(f"Before: willem.cloud_platforms = {willem.cloud_platforms}")
    
    # This modifies the CLASS attribute, not instance!
    willem.cloud_platforms.append("IBM Cloud")
    
    print(f"After willem.cloud_platforms.append('IBM Cloud'):")
    print(f"  Willem's platforms: {willem.cloud_platforms}")
    print(f"  Sabine's platforms: {sabine.cloud_platforms}")
    print(f"  Jan's platforms: {jan.cloud_platforms}")
    print(f"  Class platforms: {CloudEngineer.cloud_platforms}")
    print("\n⚠️  All instances affected! This is usually not intended.")


if __name__ == "__main__":
    main()
