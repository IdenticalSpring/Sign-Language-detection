import cv2
from ultralytics import YOLO
import pyttsx3
from picamera2 import Picamera2
import numpy as np

model = YOLO('yolov8n.pt')

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (320, 240)}))
picam2.start()

engine = pyttsx3.init()

while True:
    frame = picam2.capture_array()

    results = model(frame)
    annotated_frame = results[0].plot()

    if results[0].boxes:
        detected_class = results[0].names[int(results[0].boxes[0].cls)]
        engine.say(f"There is {detected_class} before you")
        engine.runAndWait()

    cv2.imshow('YOLOv8n Pi Camera Inference', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
