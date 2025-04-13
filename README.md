# 🎯 Object Tracking with OpenCV and Arduino

This project demonstrates real-time object tracking using Python (OpenCV) and Arduino to physically follow the tracked object with servo motors.

## 🔧 Features

- Object tracking using **OpenCV CSRT Tracker**
- Real-time camera movement using **Arduino-controlled servos**
- Adjustable tracking based on selected ROI
- Simple serial communication between Python and Arduino
- Can be adapted to track a **ball**, **hand**, or **person**

---

## 🎥 Demo and Explaination

https://drive.google.com/file/d/1lNNuFg4Yxq6XTy5rsHVom9hgyrTNHtH0/view?usp=drive_link

---

## 🧰 Requirements

### Hardware:
- Arduino UNO/Nano
- 2x Servo Motors (for pan and tilt)
- USB Camera
- Arduino-compatible USB cable
- Breadboard + jumper wires

### Software:
- Python 3.x
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- PySerial (`pip install pyserial`)
- Arduino IDE

---

## ⚙️ How It Works

1. **Live video** is captured using a webcam.
2. You select an object to track using a mouse.
3. **OpenCV CSRT Tracker** updates the object's position.
4. The center of the object is mapped to **servo angles (0-180°)**.
5. Position data is sent via **serial** to Arduino.
6. Arduino moves the servos to follow the object.

---

