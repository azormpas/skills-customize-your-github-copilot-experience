# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a REST API using the FastAPI framework to practice building endpoints, handling JSON data, and validating input with Pydantic models.

## 📝 Tasks

### 🛠️ FastAPI Project Setup

#### Description
Set up a FastAPI application and define the main application object.

#### Requirements
Completed program should:
- Create a FastAPI app instance.
- Include a root endpoint at `/` that returns a welcome message.
- Use `uvicorn` or a similar tool to run the app locally.

### 🛠️ Create CRUD-style Endpoints

#### Description
Implement endpoints to create and retrieve items using path and query parameters.

#### Requirements
Completed program should:
- Add a `POST /items/` endpoint to create a new item.
- Add a `GET /items/{item_id}` endpoint to return item details.
- Store items in an in-memory data structure for this assignment.
- Return clear JSON responses for both success and missing-item cases.

### 🛠️ Validate Input with Pydantic

#### Description
Use Pydantic models to validate request data and ensure API input is structured correctly.

#### Requirements
Completed program should:
- Define a Pydantic `BaseModel` for item payloads.
- Require fields such as `name`, `description`, `price`, and `in_stock`.
- Return validation errors automatically when invalid data is submitted.

## 💡 Skills Practiced
- REST API design
- FastAPI routing
- JSON request/response handling
- Input validation with Pydantic
- Python web app structure
