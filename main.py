from ultralytics import YOLO
import cv2
from pathlib import Path

# Load the YOLO model
model = YOLO("yolo11n.pt")

# Ask the user to enter a video path
video_path = input("Enter video path: ").strip().strip('"')

if not Path(video_path).is_file():
    print("Error: Video file not found.")
    raise SystemExit(1)

# Open the video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    raise SystemExit(1)

# Create output folder
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

output_path = output_dir / "tracked_video.mp4"

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if fps <= 0 or width <= 0 or height <= 0:
    cap.release()
    print("Error: Invalid video properties.")
    raise SystemExit(1)

# Prepare output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter(
    str(output_path), fourcc, fps, (width, height)
)

if not writer.isOpened():
    cap.release()
    print("Error: Could not create output video.")
    raise SystemExit(1)

# Process video frames
try:
    while cap.isOpened():
        success, frame = cap.read()

        if not success:
            break

        results = model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            conf=0.25,
            verbose=False
        )

        annotated_frame = results[0].plot()
        writer.write(annotated_frame)

finally:
    cap.release()
    writer.release()
    cv2.destroyAllWindows()

print(f"Tracking completed! Output saved to: {output_path.resolve()}")