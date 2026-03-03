# EdgeALPR-Pi  
Offline Automatic License Plate Recognition System on Raspberry Pi

## Abstract

This project presents the design and implementation of an offline Automatic License Plate Recognition (ALPR) system deployed on a Raspberry Pi Zero 2 W. The system performs real-time license plate detection and character recognition using classical computer vision techniques and optical character recognition (OCR), without reliance on cloud-based services. The objective is to demonstrate an embedded edge-computing solution capable of operating independently in resource-constrained environments.

---

## 1. Introduction

Automatic License Plate Recognition systems are widely used in traffic monitoring, parking management, and security applications. Many commercial systems depend on cloud-based processing or high-performance computing resources.

This project explores the feasibility of implementing an end-to-end ALPR pipeline on low-power embedded hardware. The system integrates image acquisition, preprocessing, plate localization, OCR-based recognition, and local data logging within a self-contained environment.

---

## 2. System Objectives

The primary objectives of this project are:

- Capture images using a Raspberry Pi camera module  
- Detect license plate regions using computer vision techniques  
- Extract and recognize alphanumeric characters using OCR  
- Log recognized plate numbers with timestamps  
- Store captured plate images locally  
- Operate entirely offline  

---

## 3. System Architecture

The system follows a sequential processing pipeline:

Camera Input → Image Preprocessing → Plate Detection → Character Recognition → Data Logging → Local Interface

### 3.1 Image Acquisition  
Images are captured from the Raspberry Pi camera module.

### 3.2 Preprocessing  
Captured frames are:
- Converted to grayscale  
- Filtered using Gaussian blur to reduce noise  
- Processed using Canny edge detection  

### 3.3 Plate Localization  
Contours are extracted and filtered to identify rectangular regions consistent with license plate dimensions.

### 3.4 Optical Character Recognition  
The detected plate region is passed to Tesseract OCR for alphanumeric character extraction.

### 3.5 Data Logging  
Recognized plates are stored locally with timestamps. Corresponding images are saved for record-keeping and review.

---

## 4. Hardware Components

- Raspberry Pi Zero 2 W  
- Raspberry Pi Camera Module  
- Touchscreen display (for future interface expansion)  
- MicroSD storage  

---

## 5. Software Stack

- Python 3  
- OpenCV (image processing and contour detection)  
- Tesseract OCR (character recognition)  
- Flask (local dashboard interface)  
- Raspberry Pi OS  

---

## 6. Implementation Considerations

Because the system runs on constrained embedded hardware, several design considerations were addressed:

- Avoidance of computationally heavy deep learning models  
- Use of classical computer vision techniques for efficiency  
- Fully offline processing to eliminate network dependency  
- Local file-based logging instead of remote databases  

---

## 7. Current Status

The system is capable of:

- Capturing images from the camera  
- Performing grayscale conversion and noise reduction  
- Detecting rectangular regions resembling license plates  
- Extracting text using OCR  
- Logging plate numbers and storing images locally  

Further improvements are focused on increasing detection accuracy and optimizing performance.

---

## 8. Future Work

Planned enhancements include:

- Improved plate localization filtering  
- Multi-plate detection support  
- SQLite database integration  
- Dashboard search and filtering features  
- Performance benchmarking and accuracy evaluation  

---

## 9. Conclusion

This project demonstrates that a functional ALPR system can be implemented on low-power embedded hardware using classical computer vision techniques. By operating entirely offline, the system highlights the viability of edge-based intelligent systems in constrained environments.

---

## Author

Camilah Anguiano  
Senior Project – Embedded Computer Vision System
