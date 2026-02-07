# FastAPI with Object-Oriented Programming

This comprehensive example demonstrates how to build a production-ready REST API using FastAPI with proper object-oriented design patterns.

## Overview

A cloud engineering team management API showcasing:

- **Repository Pattern** - Abstraction layer for data access
- **Service Layer Pattern** - Business logic separation
- **Dependency Injection** - FastAPI's DI system
- **Singleton Pattern** - Single repository manager instance
- **Domain Models** - Rich business entities with logic
- **Pydantic Validation** - Type-safe request/response handling
- **Custom Exceptions** - Domain-specific error handling
- **Enum Types** - Type-safe constants

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    FastAPI Endpoints                     │
│            (HTTP Request/Response Handling)              │
└─────────────────────┬───────────────────────────────────┘
                      │ Depends()
                      ▼
┌─────────────────────────────────────────────────────────┐
│                   Service Layer                          │
│              (Business Logic & Rules)                    │
│              - EngineerService                           │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                 Repository Pattern                       │
│            (Data Access Abstraction)                     │
│   IEngineerRepository ← InMemoryEngineerRepository      │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                   Domain Models                          │
│           (Business Entities & Logic)                    │
│              - Engineer                                  │
└─────────────────────────────────────────────────────────┘
```

## Installation

### Prerequisites

```bash
Python 3.8+
```

### Dependencies

```bash
pip install fastapi uvicorn[standard] pydantic[email]
```

Or use the requirements file:

```bash
pip install -r requirements-fastapi.txt
```

## Running the Application

```bash
# Run the application
python fastapi_oop_example.py

# Or using uvicorn directly
uvicorn fastapi_oop_example:app --reload
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

## API Endpoints

### Engineers

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/engineers` | Create new engineer |
| GET | `/engineers` | List all engineers |
| GET | `/engineers/{id}` | Get specific engineer |
| PATCH | `/engineers/{id}` | Update engineer |
| DELETE | `/engineers/{id}` | Delete engineer |

### Certifications

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/engineers/{id}/certifications` | Add certification |

### Queries

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/engineers?available_only=true` | Filter available engineers |
| GET | `/engineers/platform/{platform}` | Find engineers by platform |

### Reports

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/reports/revenue` | Revenue potential report |

## Usage Examples

### 1. List All Engineers

```bash
curl http://localhost:8000/engineers
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Willem van Heemstra",
    "email": "willem@rockstars.com",
    "specialty": "DevSecOps",
    "hourly_rate": 116.0,
    "certification_level": "senior",
    "certifications": ["AZ-104", "AZ-700"],
    "is_available": true,
    "created_at": "2026-02-07T10:30:00"
  }
]
```

### 2. Create New Engineer

```bash
curl -X POST http://localhost:8000/engineers \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Sarah Developer",
    "email": "sarah@rockstars.com",
    "specialty": "Cloud Native",
    "hourly_rate": 105,
    "certification_level": "mid"
  }'
```

### 3. Add Certification

```bash
curl -X POST http://localhost:8000/engineers/1/certifications \
  -H "Content-Type: application/json" \
  -d '{
    "cert_code": "AZ-305",
    "platform": "azure"
  }'
```

### 4. Find Azure Engineers

```bash
curl http://localhost:8000/engineers/platform/azure
```

### 5. Update Engineer

```bash
curl -X PATCH http://localhost:8000/engineers/1 \
  -H "Content-Type: application/json" \
  -d '{
    "hourly_rate": 120,
    "is_available": false
  }'
```

### 6. Get Revenue Report

```bash
curl http://localhost:8000/reports/revenue
```

**Response:**
```json
{
  "total_available_engineers": 2,
  "total_monthly_revenue_potential": 40160.0,
  "by_certification_level": {
    "junior": {
      "count": 0,
      "monthly_revenue": 0
    },
    "mid": {
      "count": 0,
      "monthly_revenue": 0
    },
    "senior": {
      "count": 1,
      "monthly_revenue": 18560.0
    },
    "expert": {
      "count": 1,
      "monthly_revenue": 21600.0
    }
  }
}
```

## OOP Patterns Explained

### 1. Repository Pattern

**Purpose:** Abstract data access logic

```python
class IEngineerRepository(ABC):
    """Interface defining data operations"""
    
    @abstractmethod
    async def create(self, engineer: Engineer) -> Engineer:
        pass
    
    @abstractmethod
    async def get_by_id(self, engineer_id: int) -> Optional[Engineer]:
        pass
```

**Benefits:**
- Swap implementations (memory → database) without changing business logic
- Easy to mock for testing
- Single source of truth for data operations

### 2. Service Layer Pattern

**Purpose:** Encapsulate business logic

```python
class EngineerService:
    """Business logic layer"""
    
    def __init__(self, repository: IEngineerRepository):
        self.repository = repository
    
    async def create_engineer(self, data: EngineerCreate) -> Engineer:
        """Business rules for creating engineers"""
        engineer = Engineer(...)
        return await self.repository.create(engineer)
```

**Benefits:**
- Business rules separate from HTTP handling
- Reusable across different interfaces (API, CLI, etc.)
- Easier to test business logic

### 3. Dependency Injection

**Purpose:** Provide dependencies without tight coupling

```python
def get_engineer_service(
    repository: IEngineerRepository = Depends(get_engineer_repository)
) -> EngineerService:
    return EngineerService(repository)

@app.post("/engineers")
async def create_engineer(
    data: EngineerCreate,
    service: EngineerService = Depends(get_engineer_service)
):
    return await service.create_engineer(data)
```

**Benefits:**
- Loose coupling between components
- Easy to substitute implementations for testing
- FastAPI handles dependency lifecycle

### 4. Singleton Pattern

**Purpose:** Single shared instance

```python
class RepositoryManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

**Benefits:**
- Shared state across requests
- Resource management (DB connections, etc.)
- Consistent configuration

### 5. Domain Models

**Purpose:** Rich entities with business logic

```python
class Engineer:
    """Domain entity with business methods"""
    
    def add_certification(self, cert_code: str) -> None:
        """Business logic for certifications"""
        if cert_code not in self.certifications:
            self.certifications.append(cert_code)
    
    def can_work_on_platform(self, platform: CloudPlatform) -> bool:
        """Domain knowledge encapsulated"""
        # Implementation...
```

**Benefits:**
- Business logic lives with the data
- Self-documenting code
- Easier to maintain and test

## Validation with Pydantic

Pydantic provides automatic validation:

```python
class EngineerCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr  # Validates email format
    hourly_rate: float = Field(..., gt=0, le=500)  # Must be 0-500
    
    @validator('hourly_rate')
    def validate_rate(cls, v, values):
        """Custom validation logic"""
        level = values.get('certification_level')
        if level == CertificationLevel.JUNIOR and v > 100:
            raise ValueError('Junior rate too high')
        return v
```

**Automatic Features:**
- Type checking
- Format validation
- Range validation
- Custom validators
- Automatic API documentation

## Error Handling

Custom domain exceptions map to HTTP status codes:

```python
# Domain exceptions
class EngineerNotFoundError(Exception):
    pass

# HTTP error mapping
@app.get("/engineers/{id}")
async def get_engineer(id: int):
    try:
        engineer = await service.get_engineer(id)
        return engineer
    except EngineerNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
```

## Testing

### Unit Testing Service Layer

```python
import pytest
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_create_engineer():
    # Mock repository
    mock_repo = AsyncMock(spec=IEngineerRepository)
    mock_repo.create.return_value = Engineer(...)
    
    # Test service
    service = EngineerService(mock_repo)
    result = await service.create_engineer(engineer_data)
    
    assert result.name == "Test Engineer"
    mock_repo.create.assert_called_once()
```

### Integration Testing API

```python
from fastapi.testclient import TestClient

def test_create_engineer_endpoint():
    client = TestClient(app)
    
    response = client.post("/engineers", json={
        "name": "Test Engineer",
        "email": "test@example.com",
        "specialty": "Testing",
        "hourly_rate": 100,
        "certification_level": "mid"
    })
    
    assert response.status_code == 201
    assert response.json()["name"] == "Test Engineer"
```

## Extending the Application

### Adding a New Entity

1. **Create Domain Model**
```python
class Project:
    def __init__(self, name: str, client: str):
        self.name = name
        self.client = client
```

2. **Create Pydantic Schemas**
```python
class ProjectCreate(BaseModel):
    name: str
    client: str
```

3. **Create Repository Interface**
```python
class IProjectRepository(ABC):
    @abstractmethod
    async def create(self, project: Project) -> Project:
        pass
```

4. **Create Service**
```python
class ProjectService:
    def __init__(self, repository: IProjectRepository):
        self.repository = repository
```

5. **Add Endpoints**
```python
@app.post("/projects")
async def create_project(
    data: ProjectCreate,
    service: ProjectService = Depends(get_project_service)
):
    return await service.create_project(data)
```

### Switching to Real Database

Replace `InMemoryEngineerRepository` with `SQLAlchemyEngineerRepository`:

```python
class SQLAlchemyEngineerRepository(IEngineerRepository):
    def __init__(self, session: Session):
        self.session = session
    
    async def create(self, engineer: Engineer) -> Engineer:
        db_engineer = EngineerModel(**engineer.to_dict())
        self.session.add(db_engineer)
        await self.session.commit()
        return engineer
```

No changes needed to:
- Service layer
- API endpoints
- Business logic

## Production Considerations

### 1. Database Connection Pooling

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = create_async_engine(
    "postgresql+asyncpg://user:pass@localhost/db",
    pool_size=20,
    max_overflow=10
)
```

### 2. Authentication & Authorization

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/engineers")
async def list_engineers(
    token: str = Depends(oauth2_scheme),
    service: EngineerService = Depends(get_engineer_service)
):
    # Verify token, check permissions
    pass
```

### 3. Rate Limiting

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.get("/engineers")
@limiter.limit("100/minute")
async def list_engineers():
    pass
```

### 4. Logging & Monitoring

```python
import logging

logger = logging.getLogger(__name__)

async def create_engineer(data: EngineerCreate):
    logger.info(f"Creating engineer: {data.email}")
    try:
        result = await service.create_engineer(data)
        logger.info(f"Engineer created: {result.id}")
        return result
    except Exception as e:
        logger.error(f"Failed to create engineer: {e}")
        raise
```

## Benefits of This Architecture

✅ **Testability** - Easy to unit test with mocked dependencies
✅ **Maintainability** - Clear separation of concerns
✅ **Scalability** - Swap implementations without affecting business logic
✅ **Type Safety** - Pydantic ensures data validation
✅ **Documentation** - Auto-generated OpenAPI docs
✅ **Flexibility** - Easy to extend with new features
✅ **Production-Ready** - Follows industry best practices

## Related Learning Materials

- [Section 400 - Inheritance](../400/README.md) - Base classes and extension
- [Section 600 - Abstraction](../600/README.md) - Abstract base classes
- [Section 800 - Design Patterns](../800/README.md) - Singleton, Repository patterns

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Repository Pattern](https://martinfowler.com/eaaCatalog/repository.html)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

---

**Part of the learning-python-object-oriented repository**

*Demonstrating production-ready OOP patterns in FastAPI*
