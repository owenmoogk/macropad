#include <Arduino.h>

int buttonsPin[] = {2, 3, 4, A3, A2, 6, A1, A0, 8, A5, A4};

void setup() {
    Serial.begin(9600);
    for(int i = 0; i < 11; i++) {
        pinMode(buttonsPin[i], INPUT_PULLUP);
    }
}

void loop() {
    for(int i = 0; i < 11; i++) {
        if (digitalRead(buttonsPin[i]) == 0) {
            Serial.print(i+1);
            Serial.print(", ");
        }
    }
    Serial.println();
}