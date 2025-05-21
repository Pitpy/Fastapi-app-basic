# FastAPI Installation Guide

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation Steps

1. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate
```

2. Install FastAPI with all dependencies:

```bash
pip install fastapi[standard]
```

Alternatively, you can install FastAPI without optional dependencies:

```bash
pip install fastapi
```

If you need to use FastAPI with a specific database or other libraries, you can install them separately. For example, to use FastAPI with SQLAlchemy:

````

3. Install ASGI server:

```bash
pip install uvicorn
````

## Running the Application

To run a FastAPI application:

```bash
uvicorn main:app --reload
```

## Testing the Installation

Visit http://127.0.0.1:8000/docs to see the automatic API documentation.

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [FastAPI GitHub Repository](https://github.com/tiangolo/fastapi)
