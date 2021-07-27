#include <Arduino.h>

const int skipPin = 2;
const int pausePin = 3;
const int prevPin = 4;
const int irPin = 7;


int skipState, oldSkipState, pauseState, oldPauseState, prevState, oldPrevState;

// int startedHeldTime = 0;

void setup() {
	Serial.begin(9600);
	pinMode(skipPin, INPUT_PULLUP);
	pinMode(pausePin, INPUT_PULLUP);
	pinMode(prevPin, INPUT_PULLUP);
}

void loop() {

	oldSkipState = skipState;
	oldPauseState = pauseState;
	oldPrevState = prevState;

	skipState = digitalRead(skipPin);
	pauseState = digitalRead(pausePin);
	prevState = digitalRead(prevPin);

	if (oldSkipState != skipState && skipState == 0){
		Serial.println("skip");
	}
	if (oldPauseState != pauseState && pauseState == 0){
		Serial.println("pause");
	}
	if (oldPrevState != prevState && prevState == 0){
		Serial.println("prev");
	}


	// if (buttonState == 0) {
	// 	if (oldState == 1){
	// 		Serial.println("skip");
	// 		startedHeldTime = millis();
	// 	}
	// 	// if (startedHeldTime + 600 < millis()){
	// 	// 	Serial.println("skip");
	// 	// 	delay(30);
	// 	// }
	// }

	delay(30);
}