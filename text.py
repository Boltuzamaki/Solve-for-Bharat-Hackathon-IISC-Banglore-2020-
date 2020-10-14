from PIL import Image
import pytesseract
img =Image.open ("sample.png")
text = pytesseract.image_to_string(img, config="")
print (text)
