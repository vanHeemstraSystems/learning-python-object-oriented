"""
FastAPI with OOP Design Patterns
Demonstrates object-oriented programming principles in a real-world FastAPI application.

This example shows:
- Repository pattern (abstraction)
- Dependency injection
- Service layer pattern
- Pydantic models (data validation)
- Error handling with custom exceptions
- Singleton pattern for database connection
"""

from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum
from abc import ABC, abstractmethod
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr, Field, validator


# ============================================================================
# DOMAIN MODELS (Pydantic for validation, OOP for business logic)
# ============================================================================

class CertificationLevel(str, Enum):
    """Enumeration for certification levels."""
    JUNIOR = "junior"
    MID = "mid"
    SENIOR = "senior"
    EXPERT = "expert"


class CloudPlatform(str, Enum):
    """Enumeration for cloud platforms."""
    AZURE = "azure"
    AWS = "aws"
    GCP = "gcp"


# Pydantic models for request/response validation
class EngineerBase(BaseModel):
    """Base schema for engineer data."""
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    specialty: str
    hourly_rate: float = Field(..., gt=0, le=500)
    certification_level: CertificationLevel
    
    @validator('hourly_rate')
    def validate_rate(cls, v, values):
        """Ensure hourly rate aligns with certification level."""
        level = values.get('certification_level')
        if level == CertificationLevel.JUNIOR and v > 100:
            raise ValueError('Junior rate should not exceed €100/hour')
        elif level == CertificationLevel.SENIOR and v < 100:
            raise ValueError('Senior rate should be at least €100/hour')
        return v


class EngineerCreate(EngineerBase):
    """Schema for creating a new engineer."""
    pass


class EngineerUpdate(BaseModel):
    """Schema for updating an engineer (all fields optional)."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    specialty: Optional[str] = None
    hourly_rate: Optional[float] = Field(None, gt=0, le=500)
    certification_level: Optional[CertificationLevel] = None
    is_available: Optional[bool] = None


class EngineerResponse(EngineerBase):
    """Schema for engineer response."""
    id: int
    certifications: List[str]
    is_available: bool
    created_at: datetime
    
    class Config:
        orm_mode = True


class CertificationCreate(BaseModel):
    """Schema for adding a certification."""
    cert_code: str = Field(..., min_length=2, max_length=20)
    platform: CloudPlatform


# Domain entity (business logic)
class Engineer:
    """
    Domain entity representing a cloud engineer.
    Contains business logic separate from data validation.
    """
    
    def __init__(
        self,
        id: int,
        name: str,
        email: str,
        specialty: str,
        hourly_rate: float,
        certification_level: CertificationLevel,
        certifications: Optional[List[str]] = None,
        is_available: bool = True,
        created_at: Optional[datetime] = None
    ):
        self.id = id
        self.name = name
        self.email = email
        self.specialty = specialty
        self.hourly_rate = hourly_rate
        self.certification_level = certification_level
        self.certifications = certifications or []
        self.is_available = is_available
        self.created_at = created_at or datetime.now()
    
    def add_certification(self, cert_code: str) -> None:
        """Add a certification if not already present."""
        if cert_code not in self.certifications:
            self.certifications.append(cert_code)
    
    def calculate_monthly_revenue(self, hours_per_month: int = 160) -> float:
        """Calculate potential monthly revenue."""
        return self.hourly_rate * hours_per_month
    
    def can_work_on_platform(self, platform: CloudPlatform) -> bool:
        """Check if engineer has certifications for a platform."""
        platform_prefixes = {
            CloudPlatform.AZURE: "AZ-",
            CloudPlatform.AWS: "AWS-",
            CloudPlatform.GCP: "GCP-"
        }
        prefix = platform_prefixes.get(platform, "")
        return any(cert.startswith(prefix) for cert in self.certifications)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "specialty": self.specialty,
            "hourly_rate": self.hourly_rate,
            "certification_level": self.certification_level.value,
            "certifications": self.certifications,
            "is_available": self.is_available,
            "created_at": self.created_at.isoformat()
        }


# ============================================================================
# CUSTOM EXCEPTIONS
# ============================================================================

class EngineerNotFoundError(Exception):
    """Raised when an engineer is not found."""
    pass


class EngineerAlreadyExistsError(Exception):
    """Raised when attempting to create duplicate engineer."""
    pass


class ValidationError(Exception):
    """Raised when business validation fails."""
    pass


# ============================================================================
# REPOSITORY PATTERN (Abstraction for data access)
# ============================================================================

class IEngineerRepository(ABC):
    """Abstract interface for engineer data access."""
    
    @abstractmethod
    async def create(self, engineer: Engineer) -> Engineer:
        """Create a new engineer."""
        pass
    
    @abstractmethod
    async def get_by_id(self, engineer_id: int) -> Optional[Engineer]:
        """Retrieve engineer by ID."""
        pass
    
    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[Engineer]:
        """Retrieve engineer by email."""
        pass
    
    @abstractmethod
    async def get_all(self) -> List[Engineer]:
        """Retrieve all engineers."""
        pass
    
    @abstractmethod
    async def update(self, engineer: Engineer) -> Engineer:
        """Update an existing engineer."""
        pass
    
    @abstractmethod
    async def delete(self, engineer_id: int) -> bool:
        """Delete an engineer."""
        pass
    
    @abstractmethod
    async def find_available(self) -> List[Engineer]:
        """Find all available engineers."""
        pass


class InMemoryEngineerRepository(IEngineerRepository):
    """
    In-memory implementation of engineer repository.
    In production, this would be replaced with SQLAlchemy or similar.
    """
    
    def __init__(self):
        self._engineers: Dict[int, Engineer] = {}
        self._next_id: int = 1
    
    async def create(self, engineer: Engineer) -> Engineer:
        """Create a new engineer."""
        # Check for duplicate email
        existing = await self.get_by_email(engineer.email)
        if existing:
            raise EngineerAlreadyExistsError(f"Engineer with email {engineer.email} already exists")
        
        engineer.id = self._next_id
        self._engineers[self._next_id] = engineer
        self._next_id += 1
        return engineer
    
    async def get_by_id(self, engineer_id: int) -> Optional[Engineer]:
        """Retrieve engineer by ID."""
        return self._engineers.get(engineer_id)
    
    async def get_by_email(self, email: str) -> Optional[Engineer]:
        """Retrieve engineer by email."""
        for engineer in self._engineers.values():
            if engineer.email == email:
                return engineer
        return None
    
    async def get_all(self) -> List[Engineer]:
        """Retrieve all engineers."""
        return list(self._engineers.values())
    
    async def update(self, engineer: Engineer) -> Engineer:
        """Update an existing engineer."""
        if engineer.id not in self._engineers:
            raise EngineerNotFoundError(f"Engineer {engineer.id} not found")
        self._engineers[engineer.id] = engineer
        return engineer
    
    async def delete(self, engineer_id: int) -> bool:
        """Delete an engineer."""
        if engineer_id in self._engineers:
            del self._engineers[engineer_id]
            return True
        return False
    
    async def find_available(self) -> List[Engineer]:
        """Find all available engineers."""
        return [eng for eng in self._engineers.values() if eng.is_available]


# ============================================================================
# SINGLETON PATTERN (Database/Repository instance)
# ============================================================================

class RepositoryManager:
    """
    Singleton manager for repository instances.
    Ensures single instance of repositories across the application.
    """
    _instance = None
    _engineer_repository: Optional[IEngineerRepository] = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @property
    def engineer_repository(self) -> IEngineerRepository:
        """Get the engineer repository instance."""
        if self._engineer_repository is None:
            self._engineer_repository = InMemoryEngineerRepository()
        return self._engineer_repository


# ============================================================================
# SERVICE LAYER (Business logic)
# ============================================================================

class EngineerService:
    """
    Service layer for engineer business logic.
    Separates business rules from HTTP handling.
    """
    
    def __init__(self, repository: IEngineerRepository):
        self.repository = repository
    
    async def create_engineer(self, engineer_data: EngineerCreate) -> Engineer:
        """Create a new engineer with validation."""
        engineer = Engineer(
            id=0,  # Will be assigned by repository
            name=engineer_data.name,
            email=engineer_data.email,
            specialty=engineer_data.specialty,
            hourly_rate=engineer_data.hourly_rate,
            certification_level=engineer_data.certification_level
        )
        
        return await self.repository.create(engineer)
    
    async def get_engineer(self, engineer_id: int) -> Engineer:
        """Get engineer by ID, raising exception if not found."""
        engineer = await self.repository.get_by_id(engineer_id)
        if not engineer:
            raise EngineerNotFoundError(f"Engineer {engineer_id} not found")
        return engineer
    
    async def update_engineer(
        self,
        engineer_id: int,
        update_data: EngineerUpdate
    ) -> Engineer:
        """Update engineer with partial data."""
        engineer = await self.get_engineer(engineer_id)
        
        # Update only provided fields
        update_dict = update_data.dict(exclude_unset=True)
        for field, value in update_dict.items():
            setattr(engineer, field, value)
        
        return await self.repository.update(engineer)
    
    async def delete_engineer(self, engineer_id: int) -> bool:
        """Delete an engineer."""
        # Verify exists first
        await self.get_engineer(engineer_id)
        return await self.repository.delete(engineer_id)
    
    async def add_certification(
        self,
        engineer_id: int,
        cert_data: CertificationCreate
    ) -> Engineer:
        """Add a certification to an engineer."""
        engineer = await self.get_engineer(engineer_id)
        engineer.add_certification(cert_data.cert_code)
        return await self.repository.update(engineer)
    
    async def find_engineers_for_platform(
        self,
        platform: CloudPlatform
    ) -> List[Engineer]:
        """Find available engineers certified for a platform."""
        all_engineers = await self.repository.get_all()
        return [
            eng for eng in all_engineers
            if eng.is_available and eng.can_work_on_platform(platform)
        ]
    
    async def get_revenue_report(self) -> Dict[str, Any]:
        """Generate revenue potential report."""
        engineers = await self.repository.get_all()
        
        total_monthly = sum(
            eng.calculate_monthly_revenue()
            for eng in engineers
            if eng.is_available
        )
        
        by_level = {}
        for level in CertificationLevel:
            level_engineers = [
                eng for eng in engineers
                if eng.certification_level == level and eng.is_available
            ]
            by_level[level.value] = {
                "count": len(level_engineers),
                "monthly_revenue": sum(eng.calculate_monthly_revenue() for eng in level_engineers)
            }
        
        return {
            "total_available_engineers": len([e for e in engineers if e.is_available]),
            "total_monthly_revenue_potential": total_monthly,
            "by_certification_level": by_level
        }


# ============================================================================
# DEPENDENCY INJECTION
# ============================================================================

def get_repository_manager() -> RepositoryManager:
    """Dependency for repository manager."""
    return RepositoryManager()


def get_engineer_repository(
    manager: RepositoryManager = Depends(get_repository_manager)
) -> IEngineerRepository:
    """Dependency for engineer repository."""
    return manager.engineer_repository


def get_engineer_service(
    repository: IEngineerRepository = Depends(get_engineer_repository)
) -> EngineerService:
    """Dependency for engineer service."""
    return EngineerService(repository)


# ============================================================================
# FASTAPI APPLICATION
# ============================================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager."""
    # Startup: seed some initial data
    repo_manager = RepositoryManager()
    repo = repo_manager.engineer_repository
    
    # Create sample engineers
    sample_engineers = [
        Engineer(
            id=0,
            name="Willem van Heemstra",
            email="willem@rockstars.com",
            specialty="DevSecOps",
            hourly_rate=116,
            certification_level=CertificationLevel.SENIOR,
            certifications=["AZ-104", "AZ-700"],
            is_available=True
        ),
        Engineer(
            id=0,
            name="Alice Chen",
            email="alice@rockstars.com",
            specialty="Cloud Architecture",
            hourly_rate=135,
            certification_level=CertificationLevel.EXPERT,
            certifications=["AZ-305", "AWS-SAA", "GCP-PCA"],
            is_available=True
        ),
        Engineer(
            id=0,
            name="Bob Johnson",
            email="bob@rockstars.com",
            specialty="Kubernetes",
            hourly_rate=90,
            certification_level=CertificationLevel.MID,
            certifications=["CKAD", "CKA"],
            is_available=False
        )
    ]
    
    for engineer in sample_engineers:
        try:
            await repo.create(engineer)
        except EngineerAlreadyExistsError:
            pass  # Already exists from previous run
    
    print("✓ Application started with sample data")
    
    yield
    
    # Shutdown
    print("✓ Application shutting down")


app = FastAPI(
    title="Cloud Engineers API",
    description="OOP-based FastAPI application for managing cloud engineers",
    version="1.0.0",
    lifespan=lifespan
)


# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.post(
    "/engineers",
    response_model=EngineerResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Engineers"]
)
async def create_engineer(
    engineer_data: EngineerCreate,
    service: EngineerService = Depends(get_engineer_service)
):
    """Create a new cloud engineer."""
    try:
        engineer = await service.create_engineer(engineer_data)
        return engineer.to_dict()
    except EngineerAlreadyExistsError as e:
        raise HTTPException(status_code=409, detail=str(e))


@app.get(
    "/engineers",
    response_model=List[EngineerResponse],
    tags=["Engineers"]
)
async def list_engineers(
    available_only: bool = False,
    service: EngineerService = Depends(get_engineer_service)
):
    """List all engineers, optionally filter by availability."""
    if available_only:
        engineers = await service.repository.find_available()
    else:
        engineers = await service.repository.get_all()
    
    return [eng.to_dict() for eng in engineers]


@app.get(
    "/engineers/{engineer_id}",
    response_model=EngineerResponse,
    tags=["Engineers"]
)
async def get_engineer(
    engineer_id: int,
    service: EngineerService = Depends(get_engineer_service)
):
    """Get a specific engineer by ID."""
    try:
        engineer = await service.get_engineer(engineer_id)
        return engineer.to_dict()
    except EngineerNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.patch(
    "/engineers/{engineer_id}",
    response_model=EngineerResponse,
    tags=["Engineers"]
)
async def update_engineer(
    engineer_id: int,
    update_data: EngineerUpdate,
    service: EngineerService = Depends(get_engineer_service)
):
    """Update an engineer's information."""
    try:
        engineer = await service.update_engineer(engineer_id, update_data)
        return engineer.to_dict()
    except EngineerNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.delete(
    "/engineers/{engineer_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Engineers"]
)
async def delete_engineer(
    engineer_id: int,
    service: EngineerService = Depends(get_engineer_service)
):
    """Delete an engineer."""
    try:
        await service.delete_engineer(engineer_id)
    except EngineerNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.post(
    "/engineers/{engineer_id}/certifications",
    response_model=EngineerResponse,
    tags=["Certifications"]
)
async def add_certification(
    engineer_id: int,
    cert_data: CertificationCreate,
    service: EngineerService = Depends(get_engineer_service)
):
    """Add a certification to an engineer."""
    try:
        engineer = await service.add_certification(engineer_id, cert_data)
        return engineer.to_dict()
    except EngineerNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get(
    "/engineers/platform/{platform}",
    response_model=List[EngineerResponse],
    tags=["Engineers"]
)
async def find_engineers_by_platform(
    platform: CloudPlatform,
    service: EngineerService = Depends(get_engineer_service)
):
    """Find available engineers certified for a specific platform."""
    engineers = await service.find_engineers_for_platform(platform)
    return [eng.to_dict() for eng in engineers]


@app.get(
    "/reports/revenue",
    tags=["Reports"]
)
async def get_revenue_report(
    service: EngineerService = Depends(get_engineer_service)
):
    """Get revenue potential report."""
    return await service.get_revenue_report()


@app.get("/", tags=["Health"])
async def root():
    """API health check."""
    return {
        "status": "healthy",
        "service": "Cloud Engineers API",
        "version": "1.0.0"
    }


# ============================================================================
# RUN APPLICATION
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    print("""
    ╔══════════════════════════════════════════════════════════════════╗
    ║          Cloud Engineers API - OOP FastAPI Example               ║
    ╚══════════════════════════════════════════════════════════════════╝
    
    Starting server...
    API Documentation: http://localhost:8000/docs
    Alternative Docs:  http://localhost:8000/redoc
    
    OOP Patterns Demonstrated:
    ✓ Repository Pattern (data abstraction)
    ✓ Service Layer Pattern (business logic)
    ✓ Dependency Injection (FastAPI Depends)
    ✓ Singleton Pattern (RepositoryManager)
    ✓ Domain Models (Engineer entity)
    ✓ Data Validation (Pydantic)
    ✓ Exception Handling (custom exceptions)
    ✓ Enum Types (CertificationLevel, CloudPlatform)
    
    Try these endpoints:
    - GET    /engineers              - List all engineers
    - GET    /engineers/1            - Get specific engineer
    - POST   /engineers              - Create new engineer
    - PATCH  /engineers/1            - Update engineer
    - DELETE /engineers/1            - Delete engineer
    - POST   /engineers/1/certifications - Add certification
    - GET    /engineers/platform/azure   - Find Azure engineers
    - GET    /reports/revenue        - Revenue report
    """)
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
