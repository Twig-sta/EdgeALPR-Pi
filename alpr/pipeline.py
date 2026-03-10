# pipeline.py
import cv2
import pytesseract
from alpr.detector import detect_plates
from alpr.utils import save_plate_image, crop_plate_characters

VALID_PLATE_CHARACTERS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')

def filter_plate_text(text):
    return ''.join(c.upper() for c in text if c.upper() in VALID_PLATE_CHARACTERS)

def process_frame(frame):
    results = []
    plates = detect_plates(frame)

    for plate in plates:
        plate_img = plate['image']
        margin = 2
        plate_img = plate_img[margin:-margin, margin:-margin]

        # OCR preprocessing
        gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3,3), 0)
        _, gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        gray = crop_plate_characters(gray)
        gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

        # Save debug OCR image
        cv2.imwrite(f"debug_plate_{plate['bbox'][0]}_{plate['bbox'][1]}.jpg", gray)

        # OCR
        text = pytesseract.image_to_string(
            gray,
            config='--psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        ).strip()
        text = filter_plate_text(text)
        if len(text) < 4:
            text = ""

        image_path = None
        if text:
            image_path = save_plate_image(plate_img)

        results.append({
            "bbox": plate["bbox"],
            "text": text,
            "image": image_path
        })

    return results