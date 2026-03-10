# utils.py
import cv2
import os
from datetime import datetime
import numpy as np

CAPTURE_DIR = "dashboard/captures/"

def preprocess_image(frame):
    """
    Grayscale + CLAHE + small blur to enhance plate edges
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)
    gray = cv2.GaussianBlur(gray, (3,3), 0)
    return gray

def detect_edges(gray):
    """
    Detect edges and perform morphological operations to combine plate letters
    """
    edges = cv2.Canny(gray, 30, 100)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 3))
    edges = cv2.dilate(edges, kernel, iterations=1)
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    return edges

def save_plate_image(plate_img):
    if not os.path.exists(CAPTURE_DIR):
        os.makedirs(CAPTURE_DIR)
    filename = datetime.now().strftime("plate_%Y%m%d_%H%M%S.jpg")
    path = os.path.join(CAPTURE_DIR, filename)
    cv2.imwrite(path, plate_img)
    return path

def crop_plate_characters(gray):
    """
    Crop top and bottom rows that contain no characters
    """
    projection = gray.sum(axis=1)
    threshold = projection.mean()
    rows = [i for i, val in enumerate(projection) if val < threshold]

    if not rows:
        return gray

    top = max(min(rows) - 5, 0)
    bottom = min(max(rows) + 5, gray.shape[0])
    return gray[top:bottom, :]