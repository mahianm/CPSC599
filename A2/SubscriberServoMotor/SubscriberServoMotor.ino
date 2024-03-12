#include <Servo.h>

Servo myServo;  

void setup() {
  Serial.begin(9600);  
  myServo.attach(8);    
  myServo.write(0);     
}

void loop() {
  if (Serial.available() > 0) {
    int servo_moves = Serial.parseInt();  
    for (int i = 0; i < servo_moves; i++) {
      for(int angle = 0; angle <= 95; angle++) {
        myServo.write(angle);   
        delay(10);  
      }
      delay(500); 
      
      for(int angle = 95; angle >= 0; angle--) {
        myServo.write(angle);  
        delay(10);  
      }
      delay(500);  
    }
  }
}
