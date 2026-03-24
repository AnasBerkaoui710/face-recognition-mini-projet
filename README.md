# Face Recognition Mini Project

## Overview
A simple yet effective face recognition system built with Python and OpenCV. This mini project demonstrates the full pipeline: capturing face datasets, training a recognizer model, and performing real-time identification via webcam.

## Features
- Webcam-based face dataset collection for multiple users.
- LBPH (Local Binary Pattern Histograms) face recognizer training.
- Real-time face detection and recognition with confidence scoring.
- Uses pre-trained Haar cascades for robust frontal face detection.

## Project Structure
```
face-recognition-mini-projet/
├── haarcascade_frontalface_default.xml  # OpenCV face detection model
├── dataset/                            # Captured user face images (e.g., user.1.1.jpg)
├── trainer/                            # Trained model output (trainer.yml)
├── create_dataset.py                   # Script to capture training images
├── trainer.py                          # Model training script
└── recognition.py                      # Real-time recognition script
```

## Requirements
```bash
pip install opencv-python numpy
```
- Python 3.6+
- Download `haarcascade_frontalface_default.xml` from [OpenCV GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades) if not included.

## Quick Start

### 1. Collect Dataset
```bash
python create_dataset.py
```
- Enter user ID (e.g., "Anas") when prompted.
- Position face in frame; captures 100 images automatically.
- Repeat for each user; images save to `dataset/`.

### 2. Train Model
```bash
python trainer.py
```
- Loads all images from `dataset/`.
- Trains and saves `trainer.yml` in `trainer/`.

### 3. Run Recognition
```bash
python recognition.py
```
- Opens webcam feed.
- Detects faces, matches against trained model.
- Displays ID and confidence (e.g., "Anas - 92.5%").

## How It Works
1. **Detection**: Haar cascade identifies face regions in grayscale frames.
2. **Training**: LBPH extracts texture patterns from resized face crops.
3. **Recognition**: Compares live detections against trained model; threshold ~100 for matches.

**Sample Code Snippet** (from `recognition.py`):
```python
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

# In video loop
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h), conf in zip(faces, predictions):
    if conf < 100:
        id_ = labels[id]
        cv2.putText(frame, f"{id_} [{conf:.0f}]", (x,y-10), FONT, 0.9, GREEN, 2)
```

## Performance Tips
- Use 80-150 images per person for better accuracy.
- Ensure consistent lighting during capture and recognition.
- Frontal faces yield highest confidence scores.

## Limitations
- Struggles with extreme angles, poor lighting, or occlusions.
- Single model file; retrain fully for new users.
- CPU-intensive for high-res video.

## Future Enhancements
- Integrate `face_recognition` library for dlib-based embeddings.
- Add GUI with Tkinter or Streamlit.
- Support multi-face tracking and database storage.

## Author
**Prof. Anas Berkaoui**  
Beni Mellal, Morocco  
[GitHub Profile](https://github.com/AnasBerkaoui710)

## License
MIT License - feel free to use and modify for educational purposes.
