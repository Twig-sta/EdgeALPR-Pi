import cv2

def draw_detections(frame, detections):
    for det in detections:
        x, y, w, h, = det['bbox']
        text = det["text"]

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2   
        )

        cv2.rectangle(
            frame,
            (x, y - 30),
            (x + w, y),
            (0, 255, 0),
            -1  
        )

        cv2.putText(
            frame,
            text,
            (x + 5, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 0),
            2
        )   

    return frame