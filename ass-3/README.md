# Assignment 3: Vehicle Registration and Seat Number Extractor

## Overview
This assignment extracts Indian vehicle registration numbers and student seat numbers from text or PDF content using regular expressions.

---

## Part 1: Indian Vehicle Registration Number Extractor

### Description
The program uses Python's `re` module to find and extract all valid Indian vehicle registration numbers from a text string.

### Indian Vehicle Registration Format
Indian vehicle registration numbers follow the format: **XX YY ZZ NNNN**
- **XX**: State code (2 uppercase letters) - e.g., MH for Maharashtra
- **YY**: District/RTO code (2 digits) - e.g., 15
- **ZZ**: Category code (2 uppercase letters) - e.g., FL
- **NNNN**: Sequential number (4 digits) - e.g., 8285

### Example
- Valid registration: `MH 15 FL 8285`
- Input text: `RAM mh 15 JK 6245 car no. MH 15 FL 8285 car is here`
- Output: `['MH 15 JK 6245', 'MH 15 FL 8285']`

### How It Works
1. Defines a regex pattern: `r"[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}"`
   - `[A-Z]{2}`: Matches exactly 2 uppercase letters
   - `\s`: Matches a space
   - `[0-9]{2}`: Matches exactly 2 digits
   - `[A-Z]{2}`: Matches exactly 2 uppercase letters
   - `[0-9]{4}`: Matches exactly 4 digits

2. Uses `re.findall()` with `re.IGNORECASE` flag to find all matching patterns (case-insensitive)

3. Prints all found registration numbers or displays "not found" if none match

---

## Part 2: Seat Number Extraction Using Regular Expressions

### Description
This section extracts student seat numbers from text or PDF content using regular expressions.

### Seat Number Format
Seat numbers follow the format: **TNNNNNNNN**
- **T**: Fixed alphabet character
- **NNNNNNNN**: 8-digit numeric value

### Example
- Valid seat number: `T10394756`
- Input text: `Student seat numbers are T10394756 and T20495831`
- Output: `['T10394756', 'T20495831']`

### Regex Pattern Used
```regex
T[0-9]{8}
```

### How It Works
1. Extracts text from string or PDF using `PyPDF2`
2. Applies regex pattern to identify seat numbers
3. Displays all matched seat numbers

### Sample Python Code
```python
import re

text = "Seat numbers are T10394756 and T20495831"
pattern = r"T[0-9]{8}"
result = re.findall(pattern, text)

if result:
    print(result)
else:
    print("not found")
```

### Output
```
['T10394756', 'T20495831']
```

---

## Running the Program
```bash
python app.py        # For vehicle registration extraction
python seatno.py     # For seat number extraction from PDF
```

## Dependencies
- `re` - Python's built-in regular expression module
- `PyPDF2` - For PDF text extraction

## Conclusion
This assignment demonstrates how regular expressions can be used to extract structured information such as vehicle registration numbers and seat numbers from unstructured text data. Regular expressions are powerful tools for pattern matching and data extraction in various applications.
