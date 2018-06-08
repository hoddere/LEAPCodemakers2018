#include <Adafruit_GFX.h>
#include <Adafruit_NeoMatrix.h>

#include "Joystick.h"

Adafruit_NeoMatrix matrix = Adafruit_NeoMatrix(8, 8, 6,
  NEO_MATRIX_TOP     + NEO_MATRIX_RIGHT +
  NEO_MATRIX_COLUMNS + NEO_MATRIX_PROGRESSIVE,
  NEO_GRB            + NEO_KHZ800);

#define JOYSTICK_PIN_VRX A4
#define JOYSTICK_PIN_VRY A5
#define JOYSTICK_PIN_SW 10 

int joystickX = 0;
int joystickY = 0;

int joystickX_Cal = 325;
int joystickY_Cal = 321; 

int pos = 0;
int turn = 1;
int player1spots[64];
int player1pos = 0;
int player2spots[64];
int player2pos = 0;


Joystick joystick(JOYSTICK_PIN_VRX,JOYSTICK_PIN_VRY,JOYSTICK_PIN_SW);

void setup() {
  Serial.begin(9600);
  
  matrix.begin();
  matrix.setBrightness(40);

  joystickX_Cal = joystick.getX();
  joystickY_Cal = joystick.getY();
}

void joystickLEFT(){
  if (pos == 1){
    pos -= 1;
  }
  else if (pos%8 == 0){
    Serial.println("Cannot go left");
  }
  else{
    pos -=1;
  }
}

void joystickRIGHT(){
  if ((pos + 1)%8 == 0){
    Serial.println("Cannot go right");
  }
  else{
    pos += 1;
  }
}

void joystickDOWN(){
  if ((pos + 8) > 63){
    Serial.println("Cannot go down");
  }
  else {
    pos += 8;
  }
}

void joystickUP(){
  if ((pos - 8) < 0){
    Serial.println("Cannot go up");
  }
  else{
    pos -= 8;
  }
}

void select(){
  if (turn == 1){
    player1spots[player1pos] = pos;
    player1pos++;
    turn = 2;
  }
  else{
    player2spots[player2pos] = pos;
    player2pos++;
    turn = 1;
  }
  Serial.println(turn);
  pos = 0;
}

void loop() {
  // Read Joystick X,Y axis and press
  joystickX =  (joystick.getX() - joystickX_Cal);
  joystickY =  (joystick.getY() - joystickY_Cal);
  
  bool joystickSW =  joystick.getSW();

  //Initiate Matrix 
  matrix.fillScreen(0);
  if (turn == 1){
    matrix.setPixelColor(pos,255,255,0);
  }
  else{
    matrix.setPixelColor(pos,0,255,255);
  }
  //matrix.setPixelColor(pos,0,255,0);

  if (joystickSW){
    select();
  }
  if (joystickX < -300){
    joystickLEFT();
  }
  if (joystickX > 300){
    joystickRIGHT();
  }
  if (joystickY > 300){
    joystickUP();
  }
  if (joystickY < -300){
    joystickDOWN();
  }

  //Display taken player spots
  for (int i = 0; i < player1pos; i++){
    matrix.setPixelColor(player1spots[i],255,0,0);
  }
  for (int i = 0; i <player2pos; i++){
    matrix.setPixelColor(player2spots[i],0,0,255);
  }

  matrix.show();
  delay(150);
  
}
