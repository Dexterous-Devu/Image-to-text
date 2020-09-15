
_author_ : "@rockdevu"

import pytesseract as pytess    # pip install pytesseract :- https://pypi.org/project/pytesseract/
from PIL import Image

pytess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Download this file from this website :- https://github.com/UB-Mannheim/tesseract/wiki

img = Image.open('image.jpg')
txt = pytess.image_to_string(img)

with open('content.txt', 'w') as f:
    f.write(txt)
f.close()