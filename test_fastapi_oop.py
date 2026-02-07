"""
Unit and Integration Tests for FastAPI OOP Example

Demonstrates:
- Unit testing service layer with mocked repositories
- Integration testing API endpoints
- Testing validation logic
- Testing business logic in domain models
"""

import pytest
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock
from typing import List

from fastapi.testclient import TestClient
from fastapi_oop_example import (
    app,
    Engineer,
    EngineerService,
    IEngineerRepository,
    InMemoryEngineerRepository,
    EngineerNotFoundError,
    EngineerAlreadyExistsError,
    CertificationLevel,
    CloudPlatform,
    EngineerCreate,
    EngineerUpdate,
    CertificationCreate,
)


# ============================================================================
# DOMAIN MODEL TESTS
# ============================================================================

class TestEngineerDomainModel:
    """Test the Engineer domain entity business logic."""
    
    def test_engineer_initialization(self):
        """Test engineer object creation."""
        engineer = Engineer(
            id=1,
            name="Test Engineer",
            email="test@example.com",
            specialty="Testing",
            hourly_rate=100,
            certification_level=CertificationLevel.MID
        )
        
        assert engineer.id == 1
        assert engineer.name == "Test Engineer"
        assert engineer.certifications == []
        assert engineer.is_available is True
    
    def test_add_certification(self):
        """Test adding certifications to an engineer."""
        engineer = Engineer(
            id=1,
            name="Test",
            email="test@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID
        )
        
        engineer.add_certification("AZ-104")
        assert "AZ-104" in engineer.certifications
        
        # Adding duplicate should not duplicate
        engineer.add_certification("AZ-104")
        assert engineer.certifications.count("AZ-104") == 1
    
    def test_calculate_monthly_revenue(self):
        """Test revenue calculation."""
        engineer = Engineer(
            id=1,
            name="Test",
            email="test@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID
        )
        
        # Default 160 hours
        assert engineer.calculate_monthly_revenue() == 16000
        
        # Custom hours
        assert engineer.calculate_monthly_revenue(140) == 14000
    
    def test_can_work_on_platform(self):
        """Test platform certification checking."""
        engineer = Engineer(
            id=1,
            name="Test",
            email="test@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID,
            certifications=["AZ-104", "AZ-700", "AWS-SAA"]
        )
        
        assert engineer.can_work_on_platform(CloudPlatform.AZURE) is True
        assert engineer.can_work_on_platform(CloudPlatform.AWS) is True
        assert engineer.can_work_on_platform(CloudPlatform.GCP) is False
    
    def test_to_dict(self):
        """Test dictionary serialization."""
        created_at = datetime(2026, 2, 7, 10, 0, 0)
        engineer = Engineer(
            id=1,
            name="Test",
            email="test@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID,
            created_at=created_at
        )
        
        result = engineer.to_dict()
        
        assert result["id"] == 1
        assert result["name"] == "Test"
        assert result["certification_level"] == "mid"
        assert result["created_at"] == created_at.isoformat()


# ============================================================================
# REPOSITORY TESTS
# ============================================================================

class TestInMemoryEngineerRepository:
    """Test the in-memory repository implementation."""
    
    @pytest.mark.asyncio
    async def test_create_engineer(self):
        """Test creating an engineer."""
        repo = InMemoryEngineerRepository()
        engineer = Engineer(
            id=0,
            name="Test",
            email="test@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID
        )
        
        result = await repo.create(engineer)
        
        assert result.id == 1
        assert result.name == "Test"
    
    @pytest.mark.asyncio
    async def test_create_duplicate_email(self):
        """Test creating engineer with duplicate email raises error."""
        repo = InMemoryEngineerRepository()
        
        engineer1 = Engineer(
            id=0,
            name="Test1",
            email="test@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID
        )
        await repo.create(engineer1)
        
        engineer2 = Engineer(
            id=0,
            name="Test2",
            email="test@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID
        )
        
        with pytest.raises(EngineerAlreadyExistsError):
            await repo.create(engineer2)
    
    @pytest.mark.asyncio
    async def test_get_by_id(self):
        """Test retrieving engineer by ID."""
        repo = InMemoryEngineerRepository()
        engineer = Engineer(
            id=0,
            name="Test",
            email="test@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID
        )
        created = await repo.create(engineer)
        
        result = await repo.get_by_id(created.id)
        
        assert result is not None
        assert result.id == created.id
        assert result.email == "test@example.com"
    
    @pytest.mark.asyncio
    async def test_get_by_id_not_found(self):
        """Test retrieving non-existent engineer returns None."""
        repo = InMemoryEngineerRepository()
        
        result = await repo.get_by_id(999)
        
        assert result is None
    
    @pytest.mark.asyncio
    async def test_get_by_email(self):
        """Test retrieving engineer by email."""
        repo = InMemoryEngineerRepository()
        engineer = Engineer(
            id=0,
            name="Test",
            email="test@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID
        )
        await repo.create(engineer)
        
        result = await repo.get_by_email("test@example.com")
        
        assert result is not None
        assert result.email == "test@example.com"
    
    @pytest.mark.asyncio
    async def test_get_all(self):
        """Test retrieving all engineers."""
        repo = InMemoryEngineerRepository()
        
        for i in range(3):
            engineer = Engineer(
                id=0,
                name=f"Test{i}",
                email=f"test{i}@example.com",
                specialty="Cloud",
                hourly_rate=100,
                certification_level=CertificationLevel.MID
            )
            await repo.create(engineer)
        
        result = await repo.get_all()
        
        assert len(result) == 3
    
    @pytest.mark.asyncio
    async def test_update_engineer(self):
        """Test updating an engineer."""
        repo = InMemoryEngineerRepository()
        engineer = Engineer(
            id=0,
            name="Test",
            email="test@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID
        )
        created = await repo.create(engineer)
        
        created.hourly_rate = 120
        result = await repo.update(created)
        
        assert result.hourly_rate == 120
    
    @pytest.mark.asyncio
    async def test_update_nonexistent_engineer(self):
        """Test updating non-existent engineer raises error."""
        repo = InMemoryEngineerRepository()
        engineer = Engineer(
            id=999,
            name="Test",
            email="test@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID
        )
        
        with pytest.raises(EngineerNotFoundError):
            await repo.update(engineer)
    
    @pytest.mark.asyncio
    async def test_delete_engineer(self):
        """Test deleting an engineer."""
        repo = InMemoryEngineerRepository()
        engineer = Engineer(
            id=0,
            name="Test",
            email="test@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID
        )
        created = await repo.create(engineer)
        
        result = await repo.delete(created.id)
        
        assert result is True
        assert await repo.get_by_id(created.id) is None
    
    @pytest.mark.asyncio
    async def test_find_available(self):
        """Test finding available engineers."""
        repo = InMemoryEngineerRepository()
        
        # Create available engineer
        eng1 = Engineer(
            id=0,
            name="Available",
            email="available@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID,
            is_available=True
        )
        await repo.create(eng1)
        
        # Create unavailable engineer
        eng2 = Engineer(
            id=0,
            name="Busy",
            email="busy@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID,
            is_available=False
        )
        await repo.create(eng2)
        
        result = await repo.find_available()
        
        assert len(result) == 1
        assert result[0].is_available is True


# ============================================================================
# SERVICE LAYER TESTS (with mocked repository)
# ============================================================================

class TestEngineerService:
    """Test the service layer with mocked dependencies."""
    
    @pytest.mark.asyncio
    async def test_create_engineer(self):
        """Test creating engineer through service."""
        # Mock repository
        mock_repo = AsyncMock(spec=IEngineerRepository)
        mock_repo.create.return_value = Engineer(
            id=1,
            name="Test",
            email="test@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID
        )
        
        service = EngineerService(mock_repo)
        engineer_data = EngineerCreate(
            name="Test",
            email="test@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID
        )
        
        result = await service.create_engineer(engineer_data)
        
        assert result.id == 1
        assert result.name == "Test"
        mock_repo.create.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_get_engineer(self):
        """Test getting engineer through service."""
        mock_repo = AsyncMock(spec=IEngineerRepository)
        mock_repo.get_by_id.return_value = Engineer(
            id=1,
            name="Test",
            email="test@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID
        )
        
        service = EngineerService(mock_repo)
        result = await service.get_engineer(1)
        
        assert result.id == 1
        mock_repo.get_by_id.assert_called_once_with(1)
    
    @pytest.mark.asyncio
    async def test_get_engineer_not_found(self):
        """Test getting non-existent engineer raises error."""
        mock_repo = AsyncMock(spec=IEngineerRepository)
        mock_repo.get_by_id.return_value = None
        
        service = EngineerService(mock_repo)
        
        with pytest.raises(EngineerNotFoundError):
            await service.get_engineer(999)
    
    @pytest.mark.asyncio
    async def test_update_engineer(self):
        """Test updating engineer through service."""
        existing_engineer = Engineer(
            id=1,
            name="Original",
            email="original@example.com",
            specialty="Cloud",
            hourly_rate=100,
            certification_level=CertificationLevel.MID
        )
        
        mock_repo = AsyncMock(spec=IEngineerRepository)
        mock_repo.get_by_id.return_value = existing_engineer
        mock_repo.update.return_value = existing_engineer
        
        service = EngineerService(mock_repo)
        update_data = EngineerUpdate(hourly_rate=120)
        
        result = await service.update_engineer(1, update_data)
        
        assert result.hourly_rate == 120
        assert result.name == "Original"  # Unchanged
        mock_repo.update.assert_called_once()


# ============================================================================
# API INTEGRATION TESTS
# ============================================================================

@pytest.fixture
def client():
    """Create test client."""
    return TestClient(app)


class TestEngineerAPI:
    """Integration tests for the API endpoints."""
    
    def test_list_engineers(self, client):
        """Test listing all engineers."""
        response = client.get("/engineers")
        
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    
    def test_create_engineer(self, client):
        """Test creating engineer via API."""
        engineer_data = {
            "name": "API Test Engineer",
            "email": "apitest@example.com",
            "specialty": "Testing",
            "hourly_rate": 105,
            "certification_level": "mid"
        }
        
        response = client.post("/engineers", json=engineer_data)
        
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "API Test Engineer"
        assert data["email"] == "apitest@example.com"
        assert "id" in data
    
    def test_create_engineer_validation_error(self, client):
        """Test validation errors on create."""
        invalid_data = {
            "name": "Test",
            "email": "invalid-email",  # Invalid email
            "specialty": "Testing",
            "hourly_rate": 100,
            "certification_level": "mid"
        }
        
        response = client.post("/engineers", json=invalid_data)
        
        assert response.status_code == 422  # Validation error
    
    def test_get_engineer(self, client):
        """Test getting specific engineer."""
        response = client.get("/engineers/1")
        
        assert response.status_code in [200, 404]
        if response.status_code == 200:
            data = response.json()
            assert "id" in data
            assert "name" in data
    
    def test_get_nonexistent_engineer(self, client):
        """Test getting non-existent engineer returns 404."""
        response = client.get("/engineers/9999")
        
        assert response.status_code == 404
    
    def test_revenue_report(self, client):
        """Test revenue report endpoint."""
        response = client.get("/reports/revenue")
        
        assert response.status_code == 200
        data = response.json()
        assert "total_available_engineers" in data
        assert "total_monthly_revenue_potential" in data
        assert "by_certification_level" in data


# ============================================================================
# RUN TESTS
# ============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
