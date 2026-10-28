# 🎯 Object Detection & Tracking

<p align="center">
  <strong>Detect. Track. Understand.</strong>
  <br />
  A computer vision project that detects and tracks multiple objects in video using YOLO11, OpenCV, and ByteTrack.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV" />
  <img src="https://img.shields.io/badge/YOLO11-111F68?style=for-the-badge" alt="YOLO11" />
  <img src="https://img.shields.io/badge/ByteTrack-Multi--Object%20Tracking-orange?style=for-the-badge" alt="ByteTrack" />
</p>

---

## 📌 Overview

**Object Detection & Tracking** is a computer vision project that identifies objects in video footage and tracks their identities across consecutive frames.

Built with a pretrained **YOLO11n** model and the **ByteTrack** tracking algorithm, the project processes video frame by frame and visualizes detected objects with bounding boxes, class labels, confidence scores, and tracking IDs.

Developed as part of the **CodeAlpha AI Internship**, this project demonstrates practical applications of object detection, video processing, and multi-object tracking using Python.

## ✨ Key Features

- 🎯 **Object Detection:** Detect multiple objects using a pretrained YOLO11 model.
- 🆔 **Multi-Object Tracking:** Associate detections across frames using ByteTrack.
- 📦 **Bounding Boxes:** Visualize the location of detected objects.
- 🏷️ **Class Labels:** Display predicted categories, such as people, cars, and other supported classes.
- 📊 **Confidence Scores:** Show the confidence associated with each detection.
- 🔢 **Tracking IDs:** Identify tracked objects across consecutive frames.
- 🎥 **Video Processing:** Process local video files frame by frame.
- 💾 **Video Export:** Save annotated footage for later review.

## 🎬 Demo

<!-- Add a GIF or screenshot of the actual project output here. -->

<p align="center">
  <em>Example: object detection and tracking with bounding boxes and tracking IDs.</em>
</p>

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Ultralytics YOLO11 | Object detection |
| OpenCV | Video input, frame processing, and video output |
| ByteTrack | Multi-object tracking |

## ⚙️ How It Works

The application follows a simple computer vision pipeline:

1. **Model Initialization** — Load the pretrained YOLO11n model.
2. **Video Input** — Open the selected video file.
3. **Object Detection** — Predict object classes, bounding boxes, and confidence scores for each frame.
4. **Object Tracking** — Use ByteTrack to associate detections across frames.
5. **Visualization** — Annotate frames with bounding boxes, class labels, confidence scores, and tracking IDs.
6. **Video Export** — Save the annotated frames as an output video.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or a version compatible with the installed dependencies.
- pip.
- A local video file for testing.
- An internet connection for downloading model weights on the first run, if they are not available locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Khaledelsafy123/CodeAlpha_ObjectDetectionAndTracking.git
cd CodeAlpha_ObjectDetectionAndTracking
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```cmd
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python main.py
```

When prompted, enter the path to your input video:

```text
Enter video path: sample.mp4
```

You can enter a full file path if the video is stored in another directory.

After processing, the annotated video is saved to:

```text
output/tracked_video.mp4
```

> Make sure the input path and output directory behavior match your current implementation.

## 🧪 Additional Scripts

### Object Detection

```bash
python detect.py
```

Demonstrates object detection on a sample image.

### Object Tracking

```bash
python track.py
```

Demonstrates object tracking on a sample video.

## 📊 Understanding the Output

| Component | Description |
|---|---|
| Bounding Box | Indicates the detected object's location in the frame |
| Class Label | Displays the predicted object category |
| Confidence Score | Indicates the model's confidence in a detection |
| Tracking ID | Identifies a tracked object across frames |

Tracking IDs help associate the same object across consecutive frames. However, an ID may change if the object is lost, becomes occluded, or is incorrectly associated with another detection.

## 📂 Project Structure

```text
CodeAlpha_ObjectDetectionAndTracking/
│
├── main.py
├── detect.py
├── track.py
├── requirements.txt
├── README.md
│
└── output/
    └── tracked_video.mp4
```

The `output/` directory and model weights may be generated or downloaded at runtime. The structure above is illustrative; adjust it to match the files included in the repository.

## 🔬 Technical Details

### Detection vs. Tracking

**Object Detection** identifies objects and predicts their locations independently in individual frames.

**Object Tracking** associates detections across frames to maintain object identities over time.

Combining the two allows the application to follow multiple objects throughout a video instead of treating every frame as an isolated image.

### Detection Model

**YOLO11n** is the lightweight nano variant of YOLO11. The project uses pretrained weights for inference rather than training a new detection model from scratch.

### Tracking Algorithm

**ByteTrack** associates object detections across video frames. Its tracking performance depends on detection quality, object visibility, motion, and the configuration used.

### Confidence Threshold

The current scripts use a detection confidence threshold of `0.25`.

This setting controls which predictions are retained. It is not a measurement of the model's overall accuracy.

## ⚠️ Limitations

- Detection quality depends on lighting, resolution, object size, and occlusion.
- Tracking identities may change when objects disappear or become difficult to distinguish.
- Processing speed depends on the input video and available hardware.
- The main application processes saved video files rather than providing live webcam tracking.
- The project has not established benchmark accuracy or tracking metrics unless separately evaluated.

## 🔮 Future Improvements

- Add real-time webcam detection and tracking.
- Evaluate performance using suitable detection and tracking metrics.
- Add configurable confidence thresholds and tracker settings.
- Build a simple interface for selecting input videos.
- Compare tracking algorithms on the same video sequences.
- Optimize inference performance for different hardware configurations.

## 👨‍💻 Author

**Khaled Elsafy**

Computer Science Student | AI & Machine Learning

[GitHub Profile](https://github.com/Khaledelsafy123)

---

<p align="center">
  <sub>Built with Python and Computer Vision</sub>
</p>
