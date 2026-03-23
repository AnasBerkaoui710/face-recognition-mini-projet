# Face Recognition System (Python)

## 📌 Project Overview
This project implements a **basic face recognition system** using Python. It detects faces from a webcam stream and identifies individuals by comparing them with a local database.

The system is designed for applications such as:
- Security systems
- Access control
- Attendance tracking
- Surveillance

---

## ❓ Problem Statement
How to build a system capable of:
- Detecting faces in real time  
- Recognizing individuals from a database  
- Displaying their information if found  
- Indicating when a person is unknown  

---

## 🎯 Objectives

### Main Objective
Develop a **simple and functional face recognition system**.

### Secondary Objectives
- Detect faces in images or video streams  
- Compare detected faces with stored data  
- Display user information (name, ID, etc.)  
- Handle unknown individuals  

---

## ⚙️ Features

### Core Features
- Face detection (real-time)
- Face recognition using encoding
- Identification (known / unknown)
- Live webcam display with annotations

### Additional Features
- Multiple face detection
- Bounding boxes around faces
- Display of recognition results on screen

---

## 🛠️ Technologies Used

- **Python**
- **OpenCV (cv2)** – Face detection and video processing  
- **NumPy** – Numerical operations  
- **face_recognition** *(or MediaPipe alternative)* – Face encoding and comparison  

---

## 🧠 System Architecture

### Input
- Webcam video stream or image

### Processing Pipeline
1. Capture frame  
2. Detect face(s)  
3. Extract facial features (encoding)  
4. Compare with database  

### Output
- Display recognized person's info  
- Or show: `"Unknown person"`

---

## 🗂️ Database Structure

The system uses a **local database**:
