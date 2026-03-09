#**Utility functions for ALPR preprocessing**#

# This module contains utility functions
import cv2 
import os
from importlib.resources import path
from datetime import datetime

# Directory to save captured license plate images
CAPTURE_DIR = "dashboard/captures/"

# Preprocess the image for better license plate detection 
# This function converts the image to grayscale and applies a Gaussian blur to reduce noise
def preprocess_image(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    blur = cv2.GaussianBlur(gray, (5, 5), 0) 

    return blur

# Detect edges in the preprocessed image using Canny edge detection
# This function takes the blurred grayscale image and applies the Canny edge detection algorithm to find edges
def detect_edges(image):
    edges = cv2.Canny(image, 100, 200) 

    return edges

# Save the detected license plate image to the captures directory with a timestamped filename
# This function checks if the captures directory exists, creates it if it doesn't, and saves the plate image with a filename that includes the current date and time
def save_plate_image(plate_img):
    if not os.path.exists(CAPTURE_DIR):
        os.makedirs(CAPTURE_DIR)

    filename = datetime.now().strftime("plate_%Y%m%d_%H%M%S.jpg")
    path = os.path.join(CAPTURE_DIR, filename)
    cv2.imwrite(path, plate_img)

    return path