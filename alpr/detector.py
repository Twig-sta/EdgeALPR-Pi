#**This file detects license plate candidates in the preprocessed image**#

#import necessary libraries cv2 for image processing and the utility functions for preprocessing and edge detection
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

        # contour area
        area = cv2.contourArea(c)

        # remove tiny contours
        if area < 800:
            continue

        x, y, w, h = cv2.boundingRect(c)

        if h == 0:
            continue

        aspect_ratio = w / float(h)

        # license plates are usually wider than tall
        if aspect_ratio < 1.5 or aspect_ratio > 6:
            continue

        # remove very small boxes
        if w < 60 or h < 20:
            continue

        # remove extremely large boxes
        if w > frame.shape[1] * 0.9:
            continue

        plate_img = frame[y:y+h, x:x+w]

        candidates.append({
            "bbox": (x, y, w, h),
            "image": plate_img
        })
    
    print("Contours found:", len(contours))
    print("License plate candidates found:", len(candidates))

    return candidates
