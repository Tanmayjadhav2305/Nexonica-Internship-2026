# 🚀 Internship Notes – API, Flask & Core CS Concepts

## 📌 API – Application Programming Interface

API (Application Programming Interface) is a bridge that allows two different software systems to communicate with each other.

### 🔗 Why APIs are Used?

APIs are used to connect:

- 📱 Mobile Applications
- 🌐 Web Applications
- 🖥️ Backend Services

These systems exchange data through APIs in a structured manner.

### 🛠️ Technologies Used for API Development

- Python – Flask
- Python – Django
- Java – Spring Boot
- JavaScript – Node.js
- JavaScript – Express.js
- PHP

### 📦 Data Formats Used in APIs

APIs exchange data using standard formats:

- **JSON (JavaScript Object Notation)** – Most commonly used
- **XML (Extensible Markup Language)**

#### Example (JSON)

```json
{
  "name": "tj"
}
```

---

## 🗄️ ORM – Object Relational Mapping

ORM (Object Relational Mapping) is a technique that connects:

- Object-oriented programming languages
- Relational databases

### ✅ Benefits of ORM

- Converts database tables into objects
- Reduces SQL queries
- Improves code readability and maintainability

**Examples:**
- SQLAlchemy (Python)
- Hibernate (Java)

---

## 🌐 HTTP – HyperText Transfer Protocol

HTTP is used for communication between client and server.

- **Default HTTP Port:** 80
- **Purpose:** Transfer data over the web

---

## 🧪 API Testing Tool

**Thunder Client** (VS Code Extension)

Used to test:
- API requests
- Responses
- Headers
- Status codes

---

## 🔁 HTTP Methods (Commands)

| Method | Description |
|--------|-------------|
| GET | Retrieve data |
| POST | Insert data |
| PUT | Update complete data |
| PATCH | Partial update |

---

## ⚙️ Flask Installation

### Step 1: Check Python Installation
```bash
python --version
```

### Step 2: Install Flask
```bash
pip install flask
```

### Step 3: Verify Flask Installation
```bash
flask --version
```

---

## 🔐 Session Management in Flask (Session Project)

Sessions allow storing user-specific data across multiple requests.

### 🔑 Steps to Create Sessions in Flask

#### Step 1: Import Required Modules
```python
from flask import Flask, session
```

#### Step 2: Set Secret Key
```python
app = Flask(__name__)
app.secret_key = 'your_secret_key'
```

#### Step 3: Store Data in Session
```python
@app.route('/login', methods=['POST'])
def login():
    session['username'] = 'john_doe'
    session['user_id'] = 123
    return 'Session created'
```

#### Step 4: Access Session Data
```python
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"Welcome {session['username']}"
    return 'Not logged in'
```

#### Step 5: Clear Session
```python
@app.route('/logout')
def logout():
    session.clear()
    return 'Logged out'
```

### 🔍 Key Features of Flask Sessions

- Server-side session handling
- Client stores session ID in cookies
- Automatic data serialization
- Secure encryption using secret key
- Supports session expiration

---

## ⚠️ Exception Handling

Exception handling prevents program crashes and ensures smooth execution.

### Components:

- **try** – Code that may cause an error
- **catch** – Handles exception
- **throw** – Raises an exception manually
- **finally** – Always executes

#### Example:
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Cleanup completed")
```

---

## 🧠 Memory Size of Data Types

| Data Type | Size (Bytes) |
|-----------|--------------|
| int | 4 – 8 |
| float | 4 |
| double | 8 |
| char | 1 – 2 |

---

## 📘 TOC – Theory of Computation

Theory of Computation (TOC) deals with:

- What problems can be solved using computers
- How efficiently they can be solved

### Core TOC Topics:

- Finite Automata (DFA/NFA)
- Regular Expressions
- Context-Free Grammars
- Pushdown Automata
- Turing Machines
- Decidability & Undecidability

---

## 🔒 Final & Static Keywords

### final
- Prevents modification
- Stops inheritance or overriding

### static
- Belongs to the class, not object
- Shared across all instances

---

## 🔎 Regular Expressions (Pattern Recognition)

Regular Expressions are used to match patterns in text.

### Example Pattern
```
[T][0-9]{8}
```

### Example Match
```
T10394756
```

### 💡 Real-World Use Cases

1. **Shipment Tracking** – Extract tracking numbers from logistics notifications
2. **Employee ID Validation** – Verify and extract employee tracking IDs
3. **Transaction Reference Extraction** – Pull transaction references from documents
4. **Inventory Management** – Extract product/item tracking codes
5. **Logistics Monitoring** – Track goods movement in supply chain
6. **Support Ticket Systems** – Extract ticket numbers from support emails

---

## ❓ Interview Questions

### 1️⃣ What is an API?

An API is a mechanism that allows different software applications to communicate and exchange data with each other.

### 2️⃣ How to Install Flask?

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

*Last Updated: January 7, 2026*
