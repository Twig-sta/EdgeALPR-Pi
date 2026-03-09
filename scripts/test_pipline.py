#** This script is for testing the ALPR pipeline with a single frame from the camera. **#

# It imports the CameraService to capture a frame from the camera and the process_frame function from the ALPR pipeline to detect license plates and extract text
# The results are printed to the console for verification.
from services.camera_service import CameraService
from alpr.pipeline import process_frame

camera = CameraService()

frame = camera.get_frame()

results = process_frame(frame)

for r in results:
    print(f"Plate: {r['text']} | Image: {r['image']}")