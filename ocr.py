import easyocr
import pyttsx3
import cv2
from picamera2 import Picamera2
import numpy as np

reader = easyocr.Reader(['en'], gpu=False)
engine = pyttsx3.init()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (640, 480)}))
picam2.start()


def detect_and_speak_text(frame):
    result = reader.readtext(frame)
    detected_text = ' '.join([text[1] for text in result])
    if detected_text:
        engine.say(detected_text)
        engine.runAndWait()
        print("Detected Text: ", detected_text)
    else:
        print("No text detected.")


while True:
    frame = picam2.capture_array()
    detect_and_speak_text(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
