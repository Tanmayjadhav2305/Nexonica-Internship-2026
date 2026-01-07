# Assignment 3: Indian Vehicle Registration Number Extractor

## Overview
This assignment extracts Indian vehicle registration numbers from a given text string using regular expressions.

## Description
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

## How It Works
1. Defines a regex pattern: `r"[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}"`
   - `[A-Z]{2}`: Matches exactly 2 uppercase letters
   - `\s`: Matches a space
   - `[0-9]{2}`: Matches exactly 2 digits
   - Pattern repeats for the complete format

2. Uses `re.findall()` with `re.IGNORECASE` flag to find all matching patterns (case-insensitive)

3. Prints all found registration numbers or displays "not found" if none match

## Running the Program
```bash
python app.py
```

## Output
```
['MH 15 JK 6245', 'MH 15 FL 8285']
```
