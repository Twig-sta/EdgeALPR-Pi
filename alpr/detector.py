#**This file detects license plate candidates in the preprocessed image**#

#import necessary libraries cv2 for image processing and the utility functions for preprocessing and edge detection
from email.mime import image

import cv2 
from alpr.utils import preprocess_image, detect_edges 

#This function detects potential license plate regions in the input frame
def detect_plates(frame):
    #Preprocess the image and detect edges to find contours that may correspond to license plates
    processed = preprocess_image(frame)
    edges = detect_edges(processed)
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    candidates = []

    #Loop through the detected contours and filter them based on aspect ratio and area to identify potential license plate candidates
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
    
        # Aspect ratio filter (typical license plates)
        aspect_ratio = w / float(h)
        
        if aspect_ratio < 2 or aspect_ratio > 5:
            continue

        # Minimum size filter
        if w < 80 or h < 25:
            continue

        # Maximum size filter (to avoid huge rectangles)
        if w > 600 or h > 200:
            continue

        # Optional: area threshold
        area = w * h
        if area < 2000:
            continue

        # Candidate passes all filters
        plate_img = frame[y:y+h, x:x+w]

        candidates.append({
            "bbox": (x, y, w, h),
            "image": plate_img
        })
    
    return candidates
