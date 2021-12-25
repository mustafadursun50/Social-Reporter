from PIL import Image
from pytesseract import pytesseract


def convert(image):
    #img = Image.open("C:/Users/mustdur/Documents/Master/Masterarbeit/Dev/fotos/text.png")
    words = pytesseract.image_to_string(Image.fromarray(image)).strip().split()
    return words