# Flask User REST API

## Project Description
A simple REST API developed using Python and Flask to manage user information. It supports creating, viewing, updating, and deleting users.

## Features
- GET – Retrieve all users.
- GET by ID – Retrieve a specific user.
- POST – Add a new user.
- PUT – Update existing user details.
- DELETE – Remove a user.
- JSON responses and HTTP status codes.
- Error handling for missing users and invalid input.

## Technologies Used
- Python
- Flask
- REST API
- JSON
- Postman / cURL
- Visual Studio Code

## Installation

Install Flask:

```bash
python -m pip install flask
```

## How to Run

Start the application:

```bash
python app.py
```

The API runs at:

`http://127.0.0.1:5000`

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /users | Get all users |
| GET | /users/1 | Get a user by ID |
| POST | /users | Create a user |
| PUT | /users/1 | Update a user |
| DELETE | /users/1 | Delete a user |

## Storage
User information is stored in a Python dictionary (in-memory storage). Data resets when the server restarts.

## Python Concepts Used
- Flask routes
- HTTP methods
- JSON handling
- Dictionaries
- Functions
- Conditional statements
- Exception and error handling

## Internship
Python Developer Internship – Task 4
