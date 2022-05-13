import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('check.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(img, config=config, lang='eng'))