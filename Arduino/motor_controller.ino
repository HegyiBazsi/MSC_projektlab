/*
 Name:		motor_controller.ino
 Created:	9/20/2019 9:02:04 AM
 Author:	Richard Radli
*/

#include <AFMotor.h>                    
AF_DCMotor left(3, MOTOR34_1KHZ);       
AF_DCMotor right(4, MOTOR34_1KHZ);

void forward() {
	right.setSpeed(255);
	right.run(FORWARD);
	left.setSpeed(255);
	left.run(FORWARD);
}

void backward() {
	right.setSpeed(255);
	right.run(FORWARD);
	left.setSpeed(255);
	left.run(FORWARD);
}

void goingLeft() {
	right.setSpeed(255);
	right.run(FORWARD);
	left.setSpeed(0);
	left.run(RELEASE);
}

void goingRight() {
	right.setSpeed(0);
	right.run(RELEASE);
	left.setSpeed(255);
	left.run(FORWARD);
}

void stop() {
	right.setSpeed(0);
	right.run(RELEASE);
	left.setSpeed(0);
	left.run(RELEASE);
}

// the setup function runs once when you press reset or power the board
void setup() {

}

// the loop function runs over and over again until power down or reset
void loop() {
  
}
