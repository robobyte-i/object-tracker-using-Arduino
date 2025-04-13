import cv2
import serial
import numpy as np
import time

# Initialize Serial Communication (Adjust 'COM6' to your correct port)
try:
    arduino = serial.Serial('COM6', 9600, timeout=1)
    time.sleep(2)  # Wait for serial connection to establish
except serial.SerialException:
    print("Error: Could not open serial port. Check COM port.")
    exit()

# Open Video Capture
cap = cv2.VideoCapture(0)
ws, hs = 1280, 720
cap.set(3, ws)
cap.set(4, hs)

if not cap.isOpened():
    print("Error: Camera couldn't access!")
    exit()

# Initialize Object Tracker (CSRT)
tracker = cv2.TrackerCSRT_create()

# Read an initial frame for ROI selection
ret, frame = cap.read()
if not ret:
    print("Error: Could not read frame.")
    cap.release()
    cv2.destroyAllWindows()
    exit()

# Let the user select an object to track
bbox = cv2.selectROI("Tracking", frame, fromCenter=False, showCrosshair=True)
if bbox[2] > 0 and bbox[3] > 0:
    tracker.init(frame, bbox)
else:
    print("Invalid selection, exiting...")
    cap.release()
    cv2.destroyAllWindows()
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Frame not captured.")
        break

    success, bbox = tracker.update(frame)
    if success:
        x, y, w, h = map(int, bbox)
        obj_center_x = x + (w // 2)
        obj_center_y = y + (h // 2)

        # Draw bounding box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, (obj_center_x, obj_center_y), 15, (0, 0, 255), cv2.FILLED)
        cv2.putText(frame, "Tracking", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Map object position to servo range (0-180 degrees)
        servoX = int(np.interp(obj_center_x, [0, ws], [0, 180]))
        servoY = int(np.interp(obj_center_y, [0, hs], [0, 180]))

        # Send servo positions to Arduino
        command = f"{servoX},{servoY}\n"
        arduino.write(command.encode())
        print(f"Sent: {command}")  # Debugging output

    else:
        cv2.putText(frame, "Lost Tracking", (850, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

    cv2.imshow("Tracking", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press ESC to exit
        break

# Cleanup
arduino.close()
cap.release()
cv2.destroyAllWindows()
