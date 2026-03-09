import cv2
from alpr.pipeline import process_frame

image = cv2.imread("tests/images/BMW_license_plate.jpg")

results = process_frame(image)

print("Detection Results:")
print(results)

# Draw bounding boxes
for r in results:
    x,y,w,h = r["bbox"]
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Detection", image)
cv2.waitKey(0)