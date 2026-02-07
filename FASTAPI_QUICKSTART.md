# FastAPI OOP Example - Quick Start Guide

Get the FastAPI example running in under 5 minutes.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements-fastapi.txt
```

Or install manually:

```bash
pip install fastapi uvicorn pydantic[email]
```

### 2. Run the Application

```bash
python fastapi_oop_example.py
```

You should see:

```
╔══════════════════════════════════════════════════════════════════╗
║          Cloud Engineers API - OOP FastAPI Example               ║
╚══════════════════════════════════════════════════════════════════╝

Starting server...
API Documentation: http://localhost:8000/docs
Alternative Docs:  http://localhost:8000/redoc
```

### 3. Open Your Browser

Navigate to: **http://localhost:8000/docs**

You'll see the interactive API documentation (Swagger UI).

## Try It Out (Interactive Docs)

### 1. List All Engineers

1. Click on `GET /engineers`
2. Click "Try it out"
3. Click "Execute"
4. See the pre-loaded sample data

### 2. Create a New Engineer

1. Click on `POST /engineers`
2. Click "Try it out"
3. Edit the request body:

```json
{
  "name": "Your Name",
  "email": "yourname@rockstars.com",
  "specialty": "Cloud Engineering",
  "hourly_rate": 110,
  "certification_level": "mid"
}
```

4. Click "Execute"
5. See the response with the created engineer

### 3. Add a Certification

1. Click on `POST /engineers/{engineer_id}/certifications`
2. Click "Try it out"
3. Enter `1` for engineer_id
4. Edit request body:

```json
{
  "cert_code": "AZ-305",
  "platform": "azure"
}
```

5. Click "Execute"

### 4. Find Azure Engineers

1. Click on `GET /engineers/platform/{platform}`
2. Click "Try it out"
3. Select `azure` from dropdown
4. Click "Execute"
5. See all engineers with Azure certifications

### 5. Get Revenue Report

1. Click on `GET /reports/revenue`
2. Click "Try it out"
3. Click "Execute"
4. See the revenue analysis

## Try It Out (Command Line)

### List Engineers

```bash
curl http://localhost:8000/engineers
```

### Create Engineer

```bash
curl -X POST http://localhost:8000/engineers \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Smith",
    "email": "jane@rockstars.com",
    "specialty": "Kubernetes",
    "hourly_rate": 115,
    "certification_level": "senior"
  }'
```

### Get Specific Engineer

```bash
curl http://localhost:8000/engineers/1
```

### Update Engineer

```bash
curl -X PATCH http://localhost:8000/engineers/1 \
  -H "Content-Type: application/json" \
  -d '{
    "hourly_rate": 125,
    "is_available": false
  }'
```

### Add Certification

```bash
curl -X POST http://localhost:8000/engineers/1/certifications \
  -H "Content-Type: application/json" \
  -d '{
    "cert_code": "AZ-500",
    "platform": "azure"
  }'
```

### Find Engineers by Platform

```bash
curl http://localhost:8000/engineers/platform/azure
```

### Get Revenue Report

```bash
curl http://localhost:8000/reports/revenue
```

## Run Tests

### Install Test Dependencies

```bash
pip install pytest pytest-asyncio httpx
```

### Run All Tests

```bash
pytest test_fastapi_oop.py -v
```

### Run Specific Test Class

```bash
pytest test_fastapi_oop.py::TestEngineerDomainModel -v
```

### Run with Coverage

```bash
pytest test_fastapi_oop.py --cov=fastapi_oop_example --cov-report=html
```

## Understanding the Code

### Key Files

- **`fastapi_oop_example.py`** - Main application (800+ lines)
- **`FASTAPI_README.md`** - Detailed documentation
- **`test_fastapi_oop.py`** - Comprehensive tests

### Architecture Overview

```
API Endpoints (FastAPI)
    ↓
Service Layer (Business Logic)
    ↓
Repository (Data Access)
    ↓
Domain Models (Entities)
```

### Key OOP Concepts Demonstrated

1. **Abstraction** - `IEngineerRepository` interface
2. **Encapsulation** - Business logic in `Engineer` class
3. **Dependency Injection** - FastAPI's `Depends()`
4. **Singleton** - `RepositoryManager`
5. **Validation** - Pydantic models

## Common Issues

### Port Already in Use

If port 8000 is taken:

```bash
# Run on different port
uvicorn fastapi_oop_example:app --port 8001
```

### Import Errors

Make sure you're in the correct directory:

```bash
# Should contain fastapi_oop_example.py
ls -la

# Run from this directory
python fastapi_oop_example.py
```

### Missing Dependencies

```bash
# Reinstall all dependencies
pip install -r requirements-fastapi.txt --upgrade
```

## Next Steps

1. **Read the full documentation:** `FASTAPI_README.md`
2. **Study the code:** Open `fastapi_oop_example.py` in your IDE
3. **Run the tests:** `pytest test_fastapi_oop.py -v`
4. **Modify the example:** Add new endpoints or features
5. **Learn the patterns:** Read about Repository and Service patterns

## Learning Path

After mastering this example:

1. **Section 400 - Inheritance** - Extend the Engineer class
2. **Section 600 - Abstraction** - More on abstract classes
3. **Section 800 - Design Patterns** - Patterns used in this example

## Resources

- **Interactive API Docs:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc
- **FastAPI Tutorial:** https://fastapi.tiangolo.com/tutorial/
- **Repository Pattern:** https://martinfowler.com/eaaCatalog/repository.html

## Questions?

The code is heavily commented. Read through:
1. Domain Models section
2. Repository Pattern section
3. Service Layer section
4. Dependency Injection section

Each section has detailed comments explaining the OOP concepts.

---

**Happy Learning! 🚀**

*Part of the learning-python-object-oriented repository*
