from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model.track(
    source="https://github.com/ultralytics/assets/releases/download/v0.0.0/solutions_ci_demo.mp4",
    show=False,
    save=True,
    tracker="bytetrack.yaml",
    conf=0.25
)

print("Object tracking completed successfully!")