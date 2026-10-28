# 🎯 Object Detection & Tracking

<p align="center">
  <strong>Detect. Track. Understand.</strong>
  <br />
  A computer vision project for detecting and tracking multiple objects in video using YOLO11, OpenCV, and ByteTrack.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV" />
  <img src="https://img.shields.io/badge/YOLO11-111F68?style=for-the-badge" alt="YOLO11" />
  <img src="https://img.shields.io/badge/ByteTrack-Multi--Object%20Tracking-orange?style=for-the-badge" alt="ByteTrack" />
</p>

---

## 📌 Overview

Object Detection & Tracking is a computer vision project that identifies objects in video footage and follows them across consecutive frames.

The project uses a pretrained **YOLO11** model to detect objects and **ByteTrack** to associate detections across frames. Each detection can be visualized with a bounding box, a class label, a confidence score, and a tracking ID.

Developed as part of the **CodeAlpha AI Internship**, this project explores practical applications of object detection, video processing, and multi-object tracking.

## ✨ Key Features

| Feature | Description |
|---|---|
| 🎯 Object Detection | Detect objects using a pretrained YOLO11 model. |
| 🆔 Object Tracking | Associate detected objects across video frames using ByteTrack. |
| 📦 Bounding Boxes | Visualize the location of detected objects. |
| 🏷️ Class Labels | Identify object categories such as cars and people. |
| 📊 Confidence Scores | Display the model's confidence for each detection. |
| 🔢 Tracking IDs | Help identify and follow tracked objects across frames. |
| 🎥 Video Processing | Process local video files and export annotated videos. |
| 💾 Result Export | Save processed footage for later inspection. |

## ⚙️ How It Works

The processing pipeline follows these steps:

1. **Load the model** — Initialize the pretrained YOLO11 detection model.
2. **Read the video** — Open the input video and process it frame by frame.
3. **Detect objects** — Identify objects and predict their bounding boxes.
4. **Track objects** — Use ByteTrack to associate detections across consecutive frames.
5. **Visualize predictions** — Draw bounding boxes, class labels, confidence scores, and tracking IDs.
6. **Export the result** — Write the annotated frames to an output video.

## 🧰 Tech Stack

- **Python** — Main programming language.
- **Ultralytics YOLO11** — Pretrained object detection model.
- **OpenCV** — Video input, frame processing, and video output.
- **ByteTrack** — Multi-object tracking algorithm.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or a compatible Python version supported by the installed dependencies.
- pip package manager.
- A video file for testing.
- An internet connection for the initial model download, if the model weights are not already available locally.

### 1. Clone the repository

```bash
git clone https://github.com/Khaledelsafy123/CodeAlpha_ObjectDetectionAndTracking.git
cd CodeAlpha_ObjectDetectionAndTracking
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```cmd
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## ▶️ Run the Project

### Process a local video

Run the main application:

```bash
python main.py
```

When prompted, enter the path to your video:

```text
Enter video path: sample.mp4
```

You can also provide a full path to a video stored elsewhere on your computer.

After processing, the annotated video is saved to:

```text
output/tracked_video.mp4
```

### Run object detection

```bash
python detect.py
```

This script demonstrates object detection on a sample image.

### Run object tracking

```bash
python track.py
```

This script demonstrates object tracking on a sample video.

## 🎬 Understanding the Output

The annotated video contains visual information that helps interpret the model's predictions.

- **Bounding Box:** The rectangular region surrounding a detected object.
- **Class Label:** The predicted category of the object, such as `car` or `person`.
- **Confidence Score:** The model's confidence in its detection.
- **Tracking ID:** An identifier used to associate a tracked object across video frames.

Tracking IDs help maintain object identities across frames, but tracking can occasionally fail when objects are occluded, leave the frame, or become difficult to distinguish.

## 📂 Project Structure

```text
CodeAlpha_ObjectDetectionAndTracking/
│
├── main.py              # Process and track objects in local videos
├── detect.py            # Object detection demonstration
├── track.py             # Object tracking demonstration
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
│
├── output/
│   └── tracked_video.mp4
│
└── yolo11n.pt            # Pretrained model weights, if included locally
```

*The output folder and model weights may be created or downloaded at runtime, depending on your setup.*

## 🔬 Technical Notes

### Detection vs. Tracking

**Object Detection** identifies objects independently in each frame. It predicts their categories and locations.

**Object Tracking** associates detections over time, allowing the system to follow objects across consecutive frames.

Combining both techniques provides more useful video analysis than detecting objects in isolated frames alone.

### Model and Tracker

- **YOLO11n:** The nano variant of YOLO11, selected as a lightweight pretrained detection model.
- **ByteTrack:** Associates detections across frames to maintain tracking identities.
- **Confidence threshold:** The current scripts use `0.25` as the detection confidence threshold.

The detection threshold affects which predictions are retained; it does not represent the model's overall accuracy.

## ⚠️ Current Limitations

- Detection quality depends on video resolution, lighting, object size, and occlusion.
- Tracking IDs may change when an object is lost and later detected again.
- Processing speed depends on the hardware and input video.
- The current main script processes a saved video and exports the result; it is not a live webcam application.

## 🔮 Future Improvements

- Add real-time webcam detection and tracking.
- Evaluate detection and tracking performance on different videos.
- Add configurable confidence thresholds and tracker settings.
- Provide a simple graphical interface for selecting videos.
- Compare tracking algorithms under different conditions.

## 👨‍💻 Author

**Khaled Elsafy**

Computer Science Student | AI & Machine Learning

[GitHub Profile](https://github.com/Khaledelsafy123)

---

<p align="center">
  <sub>Built with Python and Computer Vision.</sub>
</p>
