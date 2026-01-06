# User Authentication API

A simple Flask-based REST API for user registration and login functionality.

## Features

- **User Registration**: Register new users with name, email, and password
- **User Login**: Authenticate users with email and password
- **User Management**: View all registered users
- **Email Validation**: Prevents duplicate email registrations
- **Auto-incrementing IDs**: Automatic user ID assignment

## Installation

1. Install Flask:
```bash
pip install flask
```

2. Run the application:
```bash
python app.py
```

The API will start on `http://localhost:5000`

## API Endpoints

### 1. Register User
**POST** `/register`

Register a new user account.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword"
}
```

**Response (201 Created):**
```json
{
  "message": "User registered successfully",
  "user_id": 1
}
```

**Error Responses:**
- `400`: Missing required fields (name, email, password) or no JSON data
- `409`: Email already registered

---

### 2. Login User
**POST** `/login`

Authenticate a user with email and password.

**Request Body:**
```json
{
  "email": "john@example.com",
  "password": "securepassword"
}
```

**Response (200 OK):**
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

**Error Responses:**
- `400`: Missing required fields (email, password) or no JSON data
- `401`: Invalid email or password

---

### 3. Get All Users
**GET** `/users`

Retrieve all registered users (admin function).

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword"
  }
]
```

## Notes

- Passwords are stored in plain text (not recommended for production)
- User data is stored in memory (will be lost when the application stops)
- For production use, implement proper password hashing and use a database

## Usage Example

```bash
# Register a user
curl -X POST http://localhost:5000/register \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com","password":"pass123"}'

# Login
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"email":"alice@example.com","password":"pass123"}'

# Get all users
curl http://localhost:5000/users
```
