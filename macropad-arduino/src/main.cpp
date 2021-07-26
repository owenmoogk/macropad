#include <Arduino.h>

const int buttonPin = 2;

int buttonState = 0;
int oldState = 0;
int startedHeldTime = 0;

void setup() {
	Serial.begin(9600);
	pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {

	oldState = buttonState;
	buttonState = digitalRead(buttonPin);
	
	if (buttonState == 0) {
		if (oldState == 1){
			Serial.println("p");
			startedHeldTime = millis();
		}
		if (startedHeldTime + 600 < millis()){
			Serial.println('p');
			delay(30);
		}
	}
}
