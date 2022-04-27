#include <Arduino.h>

// pins used: 2,3,4,6,8,A0,A1,A2,A3,A4,A5

// 0,1,2
// 3,4,5
// 6,7,8
// 9,10

int buttonsPin[] = {2, 3, 4, A3, A2, 6, A1, A0, 8, A5, A4};
bool keyPressed = false;

void setup()
{
    Serial.begin(9600);
    // for(int i = 0; i < 11; i++) {
    //     pinMode(buttonsPin[i], INPUT_PULLUP);
    // }
    for (int i=1; i<20; i++){
        pinMode(i, INPUT_PULLUP);
    }
}

void loop()
{

    if (keyPressed){
        keyPressed = false;
        for (int i = 0; i < 11; i++) {
            if (digitalRead(buttonsPin[i]) == 0) {
                keyPressed = true;
            }
        }
    }

    if (!keyPressed){
        for(int i = 0; i < 11; i++) {

            if (digitalRead(buttonsPin[i]) == 0) {

                keyPressed = true;

                // playback
                if (i == 0){
                    Serial.println("prev");
                }
                if (i == 1){
                    Serial.println("pause");
                }
                if (i == 2){
                    Serial.println("skip");
                }

                // master volume controls
                if (i == 3){
                    Serial.println("volumeUp");
                }
                if (i == 6){
                    Serial.println("volumeDown");
                }

                // discord volume controls
                if(i == 4){
                    Serial.println("discordUp");
                }
                if(i == 7){
                    Serial.println("discordDown");
                }

                // spotify volume controls
                if (i == 5){
                    Serial.println("spotifyUp");
                }
                if (i == 8){
                    Serial.println("spotifyDown");
                }


                // shortcuts
                if (i == 9){
                    Serial.println("stickyCaps");
                }
                if (i == 10){
                    Serial.println("paste");
                }
                
            }
        }

    }

    delay(30);
}
