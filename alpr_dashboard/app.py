from flask import Flask, render_template, Response, redirect, url_for
from picamera2 import Picamera2
import cv2
import os
import time

app = Flask(__name__)

# Initialize camera
picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration())
picam2.start()

def generate_frames():
    while True:
        frame = picam2.capture_array()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    image_folder = "static/captured_images"
    images = os.listdir(image_folder)
    images = sorted(images, reverse=True)
    return render_template('index.html', images=images)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture')
def capture():
    print("CAPTURE ROUTE TRIGGERED")

    frame = picam2.capture_array()

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"capture_{timestamp}.jpg"
    filepath = os.path.join("static/captured_images", filename)

    print("Saving to:", filepath)

    success = cv2.imwrite(filepath, frame)
    print("Write success:", success)

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
