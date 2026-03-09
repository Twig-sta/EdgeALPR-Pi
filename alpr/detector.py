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
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)
        area = w * h
        
        # Filter for typical license plate dimensions: aspect ratio between 2-5, minimum area, and size constraints
        if 2 <= aspect_ratio <= 5 and area > 500 and w >= 50 and h >= 20 and w <= 300 and h <= 100:
            plate_img = frame[y:y+h, x:x+w]

            #Store the bounding box and the corresponding image of the candidate license plate for further processing
            candidates.append({
                'bbox': (x, y, w, h),
                'image': plate_img
            })
   
    return candidates
