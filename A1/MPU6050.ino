#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() {
  Serial.begin(9600);
  
  Wire.begin();
  mpu.initialize();
}

void loop() {
  int16_t ax, ay, az;
  
  // Read accelerometer values
  mpu.getAcceleration(&ax, &ay, &az);
  
  // Send accelerometer data via serial
  Serial.print(ax);
  Serial.print(",");
  Serial.print(ay);
  Serial.print(",");
  Serial.println(az);
  
  delay(100); // Adjust delay as needed
}
