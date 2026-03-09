#** This file contains the main ALPR pipeline **#

# Import necessary libraries for image processing and OCR, as well as the plate detection function from the detector module
import cv2
import pytesseract
from alpr.detector import detect_plates

# This function processes a single video frame to detect license plates and extract text from them using OCR
def process_frame(frame):
    plates = detect_plates(frame)
    results = []
    
    # Loop through the detected license plate candidates
    # extract the image of each candidate
    # use Tesseract OCR to read the text from the plate image
    # Store the bounding box and the extracted text in the results list for further use.
    for plate in plates:
        plate_img = plate['image']
        text = pytesseract.image_to_string(plate_img, config='--psm 8')
        results.append({
            'bbox': plate['bbox'],
            'text': text.strip()
        })

    return results