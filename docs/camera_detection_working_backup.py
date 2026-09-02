from ultralytics import YOLO
import cv2

# Load trained weapon detection model
model = YOLO(
    r"C:\AI_CCTV_Project\runs\weapon_detection_v1-2\weights\best.pt"
)

# Open laptop webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Could not open camera.")
    exit()

print("Camera started successfully.")
print("Press Q to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("ERROR: Could not read camera frame.")
        break

    # YOLO detection using RTX 3050
    results = model.predict(
        source=frame,
        conf=0.40,
        device=0,
        verbose=False
    )

    # Draw detection boxes
    annotated_frame = results[0].plot()

    # Display camera
    cv2.imshow("AI Smart CCTV - Weapon Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()