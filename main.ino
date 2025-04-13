#include <Servo.h>

Servo servoX;
Servo servoY;
int posX = 90;  // Initial position
int posY = 90;

void setup() {
    Serial.begin(9600);
    servoX.attach(9);  // Connect X servo to pin 9
    servoY.attach(10); // Connect Y servo to pin 10
    servoX.write(posX);
    servoY.write(posY);
}

void loop() {
    if (Serial.available() > 0) {
        String data = Serial.readStringUntil('\n');  // Read until newline
        int commaIndex = data.indexOf(',');
        if (commaIndex > 0) {
            int xValue = data.substring(0, commaIndex).toInt();
            int yValue = data.substring(commaIndex + 1).toInt();
            
            // Validate range (0-180)
            if (xValue >= 0 && xValue <= 180 && yValue >= 0 && yValue <= 180) {
                servoX.write(xValue);
                servoY.write(yValue);
                Serial.print("ServoX: "); Serial.print(xValue);
                Serial.print(" ServoY: "); Serial.println(yValue);
            }
        }
    }
}
