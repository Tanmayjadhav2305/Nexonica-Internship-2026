import re
from PyPDF2 import PdfReader

text = ""

reader = PdfReader("exam_style_seat_numbers.pdf")
for page in reader.pages:
    text += page.extract_text()

pattern = r"T[0-9]{8}"

result = re.findall(pattern, text)

if result:
    print(result)
else:
    print("not found")
