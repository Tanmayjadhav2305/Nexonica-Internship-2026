# Internship Notes

## API â€“ Application Programming Interface

API stands for Application Programming Interface.

It is used to connect:
- Mobile Interface
- Web Interface

These interfaces are connected through APIs.

### Technologies Used for API Development

- Python (Flask)
- Django
- Java (Spring Boot)
- PHP
- Express.js
- Node.js

### Data Formats

APIs exchange data using:
- JSON
- XML

**Example (JSON):**
```json
{
  "name": "tj"
}
```

---

## ORM â€“ Object Relational Mapping

ORM stands for Object Relational Mapping.

It is used to manage the relationship between objects and database tables.

---

## HTTP

- **Default HTTP port number:** 80
- **Purpose:** HTTP is used for communication between client and server

---

## API Testing Tool

- **Thunder Client**

---

## HTTP Commands (Methods)

- **GET** â€“ Retrieve data
- **POST** â€“ Insert data
- **PUT** â€“ Update data
- **PATCH** â€“ Partial update

---

## Flask Installation Command

```bash
pip install flask
```

---

## QUESTIONS

### 1. What is meant by API?

API (Application Programming Interface) is a mechanism that allows different software applications to communicate with each other.

### 2. How to install Flask library (Steps)

**Step 1:** Check Python installation
```bash
python --version
```

**Step 2:** Install Flask
```bash
pip install flask
```

**Step 3:** Verify installation
```bash
flask --version
```

---

## SESSION PROJECT

### Session Management in Flask

Sessions are used to store user-specific data across multiple requests. In Flask, sessions allow you to maintain state for individual users.

#### How Sessions are Created in Python Flask

**Step 1: Import Flask and session**
```python
from flask import Flask, session
```

**Step 2: Set secret key (required for session encryption)**
```python
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Must be set for sessions to work
```

**Step 3: Store data in session**
```python
@app.route('/login', methods=['POST'])
def login():
    session['username'] = 'john_doe'  # Store user data
    session['user_id'] = 123
    return 'Session created'
```

**Step 4: Access session data**
```python
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']  # Retrieve stored data
        return f'Welcome {username}'
    return 'Not logged in'
```

**Step 5: Clear/delete session**
```python
@app.route('/logout')
def logout():
    session.clear()  # Clears all session data
    return 'Logged out'
```

#### Key Features of Flask Sessions

- **Server-side storage:** Session data is stored on the server
- **Client-side cookies:** Session ID is sent to client as a cookie
- **Automatic serialization:** Flask automatically converts Python objects to JSON
- **Expiration:** Sessions expire based on timeout settings
- **Encryption:** Data is encrypted using the secret key

#### Example: Complete Session Implementation

```python
from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret123'

@app.route('/set-session')
def set_session():
    session['user'] = 'Alice'
    session['role'] = 'admin'
    return 'Session set'

@app.route('/get-session')
def get_session():
    user = session.get('user', 'Guest')
    return f'Current user: {user}'

@app.route('/delete-session')
def delete_session():
    session.pop('user', None)
    return 'Session cleared'
```

---

### Exception Handling

Exception handling is used to gracefully manage runtime errors and prevent program crashes.

#### Try-Catch-Throw-Finally Block

- **try:** Code that might throw an exception
- **catch:** Handles the exception if one occurs
- **throw:** Used to explicitly throw an exception
- **finally:** Block that executes regardless of exception

---

### Memory Size for Data Types

| Data Type | Size (in bytes) |
|-----------|-----------------|
| int       | 4-8             |
| float     | 4               |
| double    | 8               |
| char      | 1-2             |

---

### Table of Contents (TOC) Concepts

TOC represents the main topics or sections within a document or module for easy navigation.

---

### Final and Static Keywords

- **final:** Prevents modification, overriding, or inheritance
- **static:** Class-level members shared across all instances

---

### Pattern Recognition: Regular Expressions

Regular expressions (RE) are patterns for matching and extracting data.

#### Example: Tracking ID Pattern

**Pattern:** `[T][0-9]{8}`
**Example:** T10394756

#### Use Cases

1. **Shipment Tracking** – Track packages
2. **Employee ID Validation** – Verify IDs
3. **Transaction ID Extraction** – Extract references
4. **Inventory Management** – Track products
5. **Logistics Systems** – Monitor goods
6. **Support Tickets** – Extract ticket numbers

````
