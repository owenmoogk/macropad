#include <Arduino.h>

// pins used: 2,3,4,6,8,14,15,16,17,18,19

// 1,2,3
// 4,5,6
// 7,8,9
// 10,11
const int
    pin1 = 2,
    pin2 = 3,
    pin3 = 4,

    pin6 = 6,

    pin7 = 15,
    pin8 = 14,
    pin9 = 8,

    pin10 = 11
;

void setup()
{
    Serial.begin(9600);

    pinMode(pin1, INPUT_PULLUP);
    pinMode(pin2, INPUT_PULLUP);
    pinMode(pin3, INPUT_PULLUP);
    pinMode(pin6, INPUT_PULLUP);
    pinMode(pin7, INPUT_PULLUP);
    pinMode(pin8, INPUT_PULLUP);
    pinMode(pin9, INPUT_PULLUP);
    pinMode(pin10, INPUT_PULLUP);
}

void loop()
{

    Serial.print(digitalRead(pin1));
    Serial.print(digitalRead(pin2));
    Serial.print(digitalRead(pin3));

    Serial.print(digitalRead(pin6));

    Serial.print(digitalRead(pin7));
    Serial.print(digitalRead(pin8));
    Serial.print(digitalRead(pin9));

    Serial.println(digitalRead(pin10));

    delay(100);
}
