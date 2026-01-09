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

## 🧠 OpenCV Internship Notes – Core Image Processing (Practical)

### 1. Image & Pixel Basics (OpenCV View)

An image in OpenCV is a NumPy array.

```python
img = cv2.imread("image.jpeg")
```

**Type:** `numpy.ndarray`

**Shape:** `(height, width, channels)`

```python
h, w, c = img.shape
```

---

### 2. Pixel Coordinate System

OpenCV uses a matrix-style coordinate system:

- **Origin** → top-left corner
- **Access pattern** → `img[y][x]`
- **x increases** → right
- **y increases** → downward

**Important Coordinates**

| Location | Coordinate |
|----------|-----------|
| Top-left | (0, 0) |
| Top-right | (w-1, 0) |
| Bottom-left | (0, h-1) |
| Bottom-right | (w-1, h-1) |

**Reason for -1:** indexing starts at 0.

---

### 3. Color Channels (BGR / ARGB)

**BGR in OpenCV**

OpenCV stores color images in BGR order.

```python
b, g, r = img[y][x]
```

Each channel:
- **Range:** 0 → 255
- **Total values:** 256

**ARGB (32-bit Pixel)**

| Channel | Bits |
|---------|------|
| Alpha | 8 |
| Red | 8 |
| Green | 8 |
| Blue | 8 |

Total = 32 bits per pixel

Used mainly in images with transparency (PNG).

---

### 4. Bit Depth

**8-bit per channel**

$2^8 = 256$ intensity values

| Image Type | Bits per Pixel |
|-----------|----------------|
| Grayscale | 8 |
| RGB | 24 |
| ARGB | 32 |

---

### 5. Grayscale Conversion (Manual)

Grayscale removes color information and keeps intensity only.

**Logic Used**

$$\text{Gray} = \frac{R + G + B}{3}$$

**Implementation**

```python
avg = (int(b) + int(g) + int(r)) // 3
img2[y][x] = (avg, avg, avg)
```

**Key Insight:** When R = G = B, the pixel appears gray.

---

### 6. Binarization (Black & White)

Binarization converts a grayscale image into only two values:

- **Black** → 0
- **White** → 255

**Threshold Logic**

```python
if avg > 127:
    img2[y][x] = (255, 255, 255)
else:
    img2[y][x] = (0, 0, 0)
```

Threshold 127 is a mid-point; adjustable based on lighting.

---

### 7. Color Filtering (Red / Green / Blue)

Used to isolate individual color channels.

**Example: Red Filter**

```python
img2[y][x] = (0, 0, r)
```

Similarly:
- **Green** → `(0, g, 0)`
- **Blue** → `(b, 0, 0)`

---

### 8. Mirror Image (Flip)

**Horizontal Mirror (Left ↔ Right)**

```python
img2[y][w - 1 - x] = img[y][x]
```

**Vertical Mirror (Top ↔ Bottom)**

```python
img2[h - 1 - y][x] = img[y][x]
```

---

### 9. Image Rotation (Manual)

**90° Clockwise Rotation**

Mapping: $(y, x) → (x, h - 1 - y)$

```python
img2 = np.zeros((w, h, c), dtype=np.uint8)

for y in range(h):
    for x in range(w):
        img2[x][h - 1 - y] = img[y][x]
```

---

*Last Updated: January 9, 2026*
