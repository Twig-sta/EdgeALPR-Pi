#** This script is for testing the ALPR pipeline with a single frame from the camera. **#

# It imports the CameraService to capture a frame from the camera and the process_frame function from the ALPR pipeline to detect license plates and extract text
# The results are printed to the console for verification.
import cv2
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from alpr.pipeline import process_frame
from alpr.visualization import draw_detections

image_path = "tests/images/BMW_license_plate.jpg"

frame = cv2.imread(image_path)

results = process_frame(frame)

print("Detection Results:")
print(results)

annotated = draw_detections(frame, results)

cv2.imshow("Plate Detection", annotated)

cv2.waitKey(0)
cv2.destroyAllWindows()