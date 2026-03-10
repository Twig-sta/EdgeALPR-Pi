import json
from datetime import datetime

Log_FILE = "logs/detections.json"

def log_detection(plate_text, image_path):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "plate": plate_text,
        "image": image_path
    }
    
    try:
        with open(Log_FILE, 'r') as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open(Log_FILE, 'w') as f:
        json.dump(data, f, indent=2)  
    