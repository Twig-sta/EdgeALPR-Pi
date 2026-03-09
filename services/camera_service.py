
import cv2

class CameraService:
    def __init__(self):
        # Initialize the camera service by opening a connection to the default camera (index 0)
        self.cap = cv2.VideoCapture(0)

    def get_frame(self):
        # Capture a single frame from the camera
        ret, frame = self.cap.read()
        if not ret:
            raise Exception("Failed to capture frame from camera")
        
        return frame