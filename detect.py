from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolo11n.pt")

# Detect objects in a sample image
results = model.predict(
    source="https://ultralytics.com/images/bus.jpg",
    save=True,
    conf=0.25
)

print("Object detection completed successfully!")