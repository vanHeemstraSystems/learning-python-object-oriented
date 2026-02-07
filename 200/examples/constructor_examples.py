"""
Constructor Examples
Demonstrates various constructor patterns and initialization techniques.
"""

from datetime import datetime
from typing import Optional, List


class BasicConstructor:
    """Simple constructor with required parameters."""
    
    def __init__(self, name, age):
        """
        Basic initialization.
        
        Args:
            name (str): Person's name
            age (int): Person's age
        """
        self.name = name
        self.age = age


class DefaultParameters:
    """Constructor with default parameter values."""
    
    def __init__(self, name, role="Engineer", hourly_rate=100, active=True):
        """
        Initialize with default values.
        
        Args:
            name (str): Employee name
            role (str): Job role (default: "Engineer")
            hourly_rate (float): Billing rate (default: 100)
            active (bool): Employment status (default: True)
        """
        self.name = name
        self.role = role
        self.hourly_rate = hourly_rate
        self.active = active


class ValidationConstructor:
    """Constructor with input validation."""
    
    def __init__(self, email, age, certification_level):
        """
        Initialize with validation.
        
        Args:
            email (str): Valid email address
            age (int): Age (must be 18-70)
            certification_level (str): Must be 'junior', 'mid', or 'senior'
            
        Raises:
            ValueError: If validation fails
        """
        # Email validation
        if "@" not in email or "." not in email:
            raise ValueError(f"Invalid email format: {email}")
        
        # Age validation
        if not 18 <= age <= 70:
            raise ValueError(f"Age must be between 18 and 70, got: {age}")
        
        # Level validation
        valid_levels = ["junior", "mid", "senior"]
        if certification_level not in valid_levels:
            raise ValueError(
                f"Level must be one of {valid_levels}, got: {certification_level}"
            )
        
        self.email = email
        self.age = age
        self.certification_level = certification_level


class ComplexInitialization:
    """Constructor that performs complex initialization."""
    
    def __init__(self, project_name, start_date=None):
        """
        Initialize with computed attributes.
        
        Args:
            project_name (str): Name of the project
            start_date (datetime, optional): Project start date
        """
        self.project_name = project_name
        self.start_date = start_date or datetime.now()
        
        # Computed attributes
        self.project_id = self._generate_project_id()
        self.team_members = []
        self.milestones = {}
        self.status = "planning"
        
        # Initialize with default milestones
        self._setup_default_milestones()
    
    def _generate_project_id(self):
        """Generate a unique project ID."""
        timestamp = self.start_date.strftime("%Y%m%d")
        name_part = self.project_name[:4].upper()
        return f"PRJ-{name_part}-{timestamp}"
    
    def _setup_default_milestones(self):
        """Set up default project milestones."""
        self.milestones = {
            "kickoff": None,
            "design": None,
            "implementation": None,
            "testing": None,
            "deployment": None
        }


class AlternativeConstructors:
    """Class with multiple constructor patterns using class methods."""
    
    def __init__(self, name, email, department, salary):
        """
        Primary constructor.
        
        Args:
            name (str): Employee name
            email (str): Email address
            department (str): Department name
            salary (float): Annual salary
        """
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary
    
    @classmethod
    def from_contract_dict(cls, contract_data):
        """
        Alternative constructor from contract dictionary.
        
        Args:
            contract_data (dict): Contract information
            
        Returns:
            AlternativeConstructors: New instance
        """
        return cls(
            name=contract_data["full_name"],
            email=contract_data["contact_email"],
            department=contract_data["assigned_dept"],
            salary=contract_data["annual_salary"]
        )
    
    @classmethod
    def from_csv_row(cls, csv_row):
        """
        Alternative constructor from CSV data.
        
        Args:
            csv_row (str): Comma-separated values
            
        Returns:
            AlternativeConstructors: New instance
        """
        parts = csv_row.split(",")
        return cls(
            name=parts[0].strip(),
            email=parts[1].strip(),
            department=parts[2].strip(),
            salary=float(parts[3].strip())
        )
    
    @classmethod
    def create_cloud_engineer(cls, name, email, hourly_rate):
        """
        Factory method for cloud engineers.
        
        Args:
            name (str): Engineer name
            email (str): Email address
            hourly_rate (float): Hourly billing rate
            
        Returns:
            AlternativeConstructors: Cloud engineer instance
        """
        annual_salary = hourly_rate * 40 * 52  # Approximate annual
        return cls(name, email, "Cloud Engineering", annual_salary)


class TypeHintedConstructor:
    """Constructor with type hints for better IDE support."""
    
    def __init__(
        self,
        name: str,
        certifications: Optional[List[str]] = None,
        years_experience: int = 0,
        skills: Optional[List[str]] = None
    ) -> None:
        """
        Initialize with type hints.
        
        Args:
            name: Engineer's name
            certifications: List of certification codes
            years_experience: Years of professional experience
            skills: List of technical skills
        """
        self.name = name
        self.certifications = certifications or []
        self.years_experience = years_experience
        self.skills = skills or []
    
    def add_certification(self, cert: str) -> None:
        """Add a certification."""
        self.certifications.append(cert)
    
    def add_skill(self, skill: str) -> None:
        """Add a technical skill."""
        if skill not in self.skills:
            self.skills.append(skill)


class MutableDefaultPitfall:
    """Demonstrates the mutable default argument pitfall."""
    
    # WRONG WAY - Don't do this!
    def __init__(self, name, skills=[]):  # Mutable default!
        self.name = name
        self.skills = skills  # Same list shared across instances!


class MutableDefaultFixed:
    """Correct way to handle mutable defaults."""
    
    def __init__(self, name, skills=None):
        self.name = name
        self.skills = skills if skills is not None else []


def main():
    """Demonstrate various constructor patterns."""
    
    print("=" * 70)
    print("CONSTRUCTOR PATTERNS")
    print("=" * 70)
    
    print(f"\n{'1. Basic Constructor':-^70}")
    person = BasicConstructor("Willem", 55)
    print(f"Name: {person.name}, Age: {person.age}")
    
    print(f"\n{'2. Default Parameters':-^70}")
    emp1 = DefaultParameters("Alice")
    emp2 = DefaultParameters("Bob", "Senior Engineer", 150)
    emp3 = DefaultParameters("Carol", hourly_rate=125, active=False)
    
    print(f"Employee 1: {emp1.name}, {emp1.role}, €{emp1.hourly_rate}/hr")
    print(f"Employee 2: {emp2.name}, {emp2.role}, €{emp2.hourly_rate}/hr")
    print(f"Employee 3: {emp3.name}, {emp3.role}, €{emp3.hourly_rate}/hr, Active: {emp3.active}")
    
    print(f"\n{'3. Validation in Constructor':-^70}")
    try:
        valid = ValidationConstructor("willem@example.com", 55, "senior")
        print(f"✓ Valid engineer created: {valid.email}")
    except ValueError as e:
        print(f"✗ Error: {e}")
    
    try:
        invalid = ValidationConstructor("bad-email", 25, "senior")
    except ValueError as e:
        print(f"✗ Caught expected error: {e}")
    
    try:
        invalid_age = ValidationConstructor("test@example.com", 15, "junior")
    except ValueError as e:
        print(f"✗ Caught expected error: {e}")
    
    print(f"\n{'4. Complex Initialization':-^70}")
    project = ComplexInitialization("Atlas IDP Platform")
    print(f"Project: {project.project_name}")
    print(f"Project ID: {project.project_id}")
    print(f"Status: {project.status}")
    print(f"Milestones: {list(project.milestones.keys())}")
    
    print(f"\n{'5. Alternative Constructors (Class Methods)':-^70}")
    
    # Using primary constructor
    emp_direct = AlternativeConstructors(
        "Willem van Heemstra",
        "willem@rockstars.com",
        "Cloud Engineering",
        120000
    )
    print(f"Direct: {emp_direct.name} - {emp_direct.department}")
    
    # Using from_contract_dict
    contract = {
        "full_name": "Sabine Manager",
        "contact_email": "sabine@company.com",
        "assigned_dept": "Security",
        "annual_salary": 130000
    }
    emp_contract = AlternativeConstructors.from_contract_dict(contract)
    print(f"From contract: {emp_contract.name} - {emp_contract.department}")
    
    # Using from_csv_row
    csv_data = "Jan Developer, jan@company.com, Development, 110000"
    emp_csv = AlternativeConstructors.from_csv_row(csv_data)
    print(f"From CSV: {emp_csv.name} - {emp_csv.department}")
    
    # Using factory method
    emp_engineer = AlternativeConstructors.create_cloud_engineer(
        "Alice Engineer",
        "alice@rockstars.com",
        116
    )
    print(f"Cloud Engineer: {emp_engineer.name} - €{emp_engineer.salary:,.0f}/year")
    
    print(f"\n{'6. Type-Hinted Constructor':-^70}")
    engineer = TypeHintedConstructor(
        name="Willem van Heemstra",
        certifications=["AZ-104", "AZ-700"],
        years_experience=29,
        skills=["Python", "Azure", "Kubernetes"]
    )
    print(f"Engineer: {engineer.name}")
    print(f"Certifications: {engineer.certifications}")
    print(f"Skills: {engineer.skills}")
    
    engineer.add_certification("AZ-305")
    engineer.add_skill("Crossplane")
    print(f"After additions: {engineer.certifications}, {engineer.skills}")
    
    print(f"\n{'7. PITFALL: Mutable Default Arguments':-^70}")
    
    print("\n⚠️  WRONG WAY (Mutable default []):")
    dev1 = MutableDefaultPitfall("Developer 1")
    dev2 = MutableDefaultPitfall("Developer 2")
    
    dev1.skills.append("Python")
    print(f"After dev1.skills.append('Python'):")
    print(f"  dev1.skills: {dev1.skills}")
    print(f"  dev2.skills: {dev2.skills}")  # Also has Python!
    print(f"  Same list? {dev1.skills is dev2.skills}")
    
    print("\n✓ CORRECT WAY (None default):")
    dev3 = MutableDefaultFixed("Developer 3")
    dev4 = MutableDefaultFixed("Developer 4")
    
    dev3.skills.append("Python")
    print(f"After dev3.skills.append('Python'):")
    print(f"  dev3.skills: {dev3.skills}")
    print(f"  dev4.skills: {dev4.skills}")  # Empty, as expected
    print(f"  Same list? {dev3.skills is dev4.skills}")


if __name__ == "__main__":
    main()
