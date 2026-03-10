# detector.py
import cv2
from alpr.utils import preprocess_image, detect_edges

def detect_plates(frame, debug=True):
    """
    Detect candidate license plates with robust contour detection
    """
    gray = preprocess_image(frame)
    edges = detect_edges(gray)

    if debug:
        cv2.imshow("Edges", edges)
        cv2.waitKey(1)

    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    candidates = []
    debug_img = frame.copy()

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        aspect_ratio = w / float(h)
        area = w * h

        # Basic plate heuristics
        if area < 2000:  # ignore tiny boxes
            continue
        if aspect_ratio < 2.0 or aspect_ratio > 6.0:
            continue
        if w > frame.shape[1] * 0.9:
            continue

        candidates.append({"bbox": (x, y, w, h), "image": frame[y:y+h, x:x+w]})

        if debug:
            cv2.rectangle(debug_img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if debug:
        cv2.imshow("Plate Candidates", debug_img)
        cv2.waitKey(1)

    print(f"Contours found: {len(contours)} | Plate candidates: {len(candidates)}")
    return candidates