# Nexonica Internship 2026

This repository contains all the tasks, assignments, mini-projects, and experiments completed during my internship at Nexonica in 2026.

## Tech Stack
- Python
- Flask
- REST APIs
- AI Tools & Concepts
- Git & GitHub

## Repository Structure
- Weekly folders contain daily internship tasks and learning notes
- Mini-projects include complete, working implementations
- Each project includes documentation and usage instructions

## Objective
To gain hands-on industry experience, strengthen backend and API development skills, and apply AI concepts to solve real-world problems.

> Note: This repository does not contain any confidential or proprietary company data.

---

## 📌 API (Application Programming Interface)

### 🔹 Definition

API (Application Programming Interface) is a set of rules that allows two software applications to communicate with each other.

### 🔹 Simple Meaning

An API acts as a bridge between a client and a server, allowing the client to request data or services and receive a response in a standard format (usually JSON).

### 🔹 How API Works

1. Client sends a request to the API
2. API processes the request
3. Server performs the required operation
4. API sends the response back to the client

### 🔹 Example

**Request:**
```
GET /users/1
```

**Response:**
```json
{
  "id": 1,
  "name": "Tanmay",
  "role": "Developer"
}
```

### 🔹 Uses of API

- Connect frontend and backend
- Allow mobile apps to communicate with servers
- Enable third-party integrations
- Build scalable applications

---

## 📌 Flask

### 🔹 Definition

Flask is a lightweight Python web framework used to build web applications and REST APIs.

## 📌 How to Install Flask

### 🔹 Step 1: Check Python Installation
```bash
python --version
```

### 🔹 Step 2: Install Flask
```bash
pip install flask
```

### 🔹 Step 3: Verify Flask Installation
```bash
flask --version
```

### 🔹 Step 4: Create First Flask App

Create a file `app.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

### 🔹 Step 5: Run Flask Application
```bash
python app.py
```

Open browser and go to:
```
http://127.0.0.1:5000/
```
