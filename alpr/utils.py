#**Utility functions for ALPR preprocessing**#

import cv2 # OpenCV for image processing

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