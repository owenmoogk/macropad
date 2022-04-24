#include <Arduino.h>

// pins used: 2,3,4,6,8,A0,A1,A2,A3,A4,A5

// 1,2,3
// 4,5,6
// 7,8,9
// 10,11
byte
    pin1 = 2,
    pin2 = 3,
    pin3 = 4,

    pin4 = A3,
    pin5 = A2,
    pin6 = 6,

    pin7 = A1,
    pin8 = A0,
    pin9 = 8,

    pin10 = A5,
    pin11 = A4
;

void setup()
{
    Serial.begin(9600);

    for (int i=1; i<20; i++){
        pinMode(i, INPUT_PULLUP);
    }
}

void loop()
{
    Serial.print(digitalRead(pin1));
    Serial.print(digitalRead(pin2));
    Serial.print(digitalRead(pin3));
    Serial.print(digitalRead(pin4));
    Serial.print(digitalRead(pin5));
    Serial.print(digitalRead(pin6));
    Serial.print(digitalRead(pin7));
    Serial.print(digitalRead(pin8));
    Serial.print(digitalRead(pin9));
    Serial.print(digitalRead(pin10));
    Serial.println(digitalRead(pin11));

    delay(30);
}
