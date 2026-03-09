#** This file contains the main ALPR pipeline **#

# Import necessary libraries for image processing and OCR, as well as the plate detection function from the detector module
import cv2
import pytesseract
from detector import detect_plates
from utils import save_plate_image
from logger import log_detection 

# This function processes a single video frame to detect license plates and extract text from them using OCR
def process_frame(frame):
    plates = detect_plates(frame)
    results = []
    
    # Loop through each detected plate, extract the image, convert it to grayscale, and use Tesseract OCR to read the text. 
    # If text is found, save the plate image and log the detection.
    for plate in plates:
        plate_img = plate['image']
        gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)  
        text = pytesseract.image_to_string(gray, config='--psm 8').strip()

        if text:
            image_path = save_plate_image(plate_img)
            log_detection(text, image_path)
        
        results.append({
            'bbox': plate["bbox"],
            'text': text,
            'image': image_path
        })