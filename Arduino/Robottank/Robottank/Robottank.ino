/**
 *  TaskScheduler Test
 *
 *  Initially only tasks 1 and 2 are enabled
 *  Task1 runs every 2 seconds 10 times and then stops
 *  Task2 runs every 3 seconds indefinitely
 *  Task1 enables Task3 at its first run
 *  Task3 run every 5 seconds
 *  Task1 disables Task3 on its last iteration and changed Task2 to run every 1/2 seconds
 *  At the end Task2 is the only task running every 1/2 seconds
 */


#include <TaskScheduler.h>
#include <AFMotor.h>   

//SOLENOID

//ULTRASOUND
// Define Trig and Echo pin:
#define trigPin 2
#define echoPin 3
// Define variables:
long duration;
int distance;
//MOTOR
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


// Callback methods prototypes
void t1Callback();
void t2Callback();
void t3Callback();

//Tasks
Task t4();
Task t1(2000, 10, &t1Callback);
Task t2(3000, TASK_FOREVER, &t2Callback);
Task t3(5000, TASK_FOREVER, &t3Callback);

Scheduler runner;


void t1Callback() {
	Serial.print("t1: ");
	Serial.println(millis());

	if (t1.isFirstIteration()) {
		runner.addTask(t3);
		t3.enable();
		Serial.println("t1: enabled t3 and added to the chain");
	}

	if (t1.isLastIteration()) {
		t3.disable();
		runner.deleteTask(t3);
		t2.setInterval(500);
		Serial.println("t1: disable t3 and delete it from the chain. t2 interval set to 500");
	}

}

void t2Callback() {
	Serial.print("t2: ");
	Serial.println(millis());
	pinMode(trigPin, OUTPUT);
	pinMode(echoPin, INPUT);
	//Begin Serial communication at a baudrate of 9600:
	Serial.begin(9600);
	// Clear the trigPin by setting it LOW:
	digitalWrite(trigPin, LOW);
	delayMicroseconds(5);
	// Trigger the sensor by setting the trigPin high for 10 microseconds:
	digitalWrite(trigPin, HIGH);
	delayMicroseconds(10);
	digitalWrite(trigPin, LOW);
	// Read the echoPin, pulseIn() returns the duration (length of the pulse) in microseconds:
	duration = pulseIn(echoPin, HIGH);
	// Calculate the distance:
	distance = duration * 0.034 / 2;
	// Print the distance on the Serial Monitor (Ctrl+Shift+M):
	Serial.print("Distance = ");
	Serial.print(distance);
	Serial.println(" cm");

	delay(50);

}

void t3Callback() {
	Serial.print("t3: ");
	Serial.println(millis());
	Serial.println("go");

}

void setup() {
	Serial.begin(115200);
	Serial.println("Scheduler TEST");

	runner.init();
	Serial.println("Initialized scheduler");

	runner.addTask(t1);
	Serial.println("added t1");

	runner.addTask(t2);
	Serial.println("added t2");

	delay(5000);

	t1.enable();
	Serial.println("Enabled t1");
	t2.enable();
	Serial.println("Enabled t2");
}


void loop() {
	runner.execute();
}