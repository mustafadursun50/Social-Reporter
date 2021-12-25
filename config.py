#import cv2
from facial_emotion_recognition import EmotionRecognition
from pytesseract import pytesseract

frame_width = 0
frame_height = 0
my_video = ""
output_path = ""
emotion_model = None
time_to_leave_in_sec = 0
lectureKeyWords = []
path_tesseract = ""
incas_dir = ""

def init():
    global frame_width
    global frame_height
    global incas_dir
    global output_path
    global emotion_model
    global time_to_leave_in_sec
    global lectureKeyWords
    global path_tesseract
    incas_dir = "C:/Users/mustdur/Documents/Master/Masterarbeit/Dev/input/"
    #frame_width = my_video.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_width = 1920
    #frame_height = my_video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    frame_height = 1080
    output_path = "C:/Users/mustdur/Documents/Master/Masterarbeit/Dev/output/"
    emotion_model = EmotionRecognition(device='cpu', gpu_id=0)
    time_to_leave_in_sec = 5
    lectureKeyWords = open("C:/Users/mustdur/Documents/Master/Masterarbeit/Dev/keywords.txt", "r").read().split(";")
    path_tesseract = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
    pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"