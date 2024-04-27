# FastAPI Project

## Overview

This is a sample FastAPI project demonstrating how to build high-performance APIs with Python using FastAPI.

## Features

- **Fast**: Utilizes Python's async capabilities for high concurrency and speed.
- **Automatic API Documentation**: Generates interactive API documentation (Swagger UI) based on code's type hints.
- **Validation and Serialization**: Data validation and serialization using Pydantic.
- **Dependency Injection**: Supports reusable components and automatic dependency injection.
- **WebSocket Support**: Built-in support for WebSocket endpoints.
- **Security**: Authentication, authorization, and security features, such as OAuth2 authentication and CORS handling.
- **Background Tasks**: Define and execute background tasks asynchronously.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/godwintheophilus-github/python-fast-api.git
    cd python-fast-api
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip3 install -r requirements.txt
    ```

## Usage

1. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

    This command starts the FastAPI application using Uvicorn with automatic reloading enabled.

2. Open your web browser and navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to view the interactive API documentation.

3. Test the API endpoints using the provided documentation or tools like Postman or cURL.


