# ** This file contains the main ALPR pipeline **#

import cv2
import pytesseract
from alpr.detector import detect_plates
from alpr.utils import save_plate_image
from alpr.logger import log_detection 

# Valid characters that appear on license plates: uppercase letters, numbers, and hyphens
VALID_PLATE_CHARACTERS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')

# Filter OCR output to only include valid license plate characters
def filter_plate_text(text):
    filtered = ''.join(char.upper() for char in text if char.upper() in VALID_PLATE_CHARACTERS)
    return filtered

# This function processes a single video frame to detect license plates and extract text from them using OCR
def process_frame(frame):
    results = []

    plates = detect_plates(frame)

    for plate in plates:
        plate_img = plate['image']

        gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray, config='--psm 8').strip()
        
        # Filter text to only include valid license plate characters
        text = filter_plate_text(text)

        image_path = None

        if text:
            image_path = save_plate_image(plate_img)
            log_detection(text, image_path)

        results.append({
            'bbox': plate["bbox"],
            'text': text,
            'image': image_path
        })

    return results
    return results