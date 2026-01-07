import re

v1 = "RAM mh 15 JK 6245 car no. MH 15 FL 8285 car is here"

pattern = r"[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}"

result = re.findall(pattern, v1, re.IGNORECASE)

if result:
    print(result)
else:
    print("not found")