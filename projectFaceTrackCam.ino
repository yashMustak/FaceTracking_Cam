/*We used two servo to for left to right and up down movement of the camera*/

#include<Servo.h>
Servo myServo;      //Making instance of Servo motor class
Servo myServo1;
int servoPin1 = 7;  //connect servo motor pin for vertical motion into 7 pin of arduino
int servoPin2 = 8;  //connect servo motor pin for horizontal motion into 8 pin of arduino
void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin1);
  myServo1.attach(servoPin2);
  myServo.write(90);
  myServo1.write(90);
  delay(500);
}

byte pos, ip, ip1;
void loop() {
    while(Serial.available()>0){      //checking if the serial is available or not
      pos = Serial.read();        //getting the serial
      ip = myServo.read();        //getting the initial position of servo 1
      ip1 = myServo1.read();      //getting the initial position of servo 2
      if(pos=='D'){
        if(ip>0){
          myServo.write(ip-1);
          delay(20);
          }
        }
      if(pos=='U'){
        if(ip<180){
          myServo.write(ip+1);
          delay(20);
          }
        }
       if(pos=='R'){
        if(ip1>0){
          myServo1.write(ip-1);
          delay(20);
          }
        }
       if(pos=='L'){
        if(ip1<180){
          myServo1.write(ip+1);
          delay(20);                //processing the instruction from computer system
          }
        }
      }
}
