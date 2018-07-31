#include <Adafruit_GFX.h>
#include <Adafruit_NeoMatrix.h>

Adafruit_NeoMatrix matrix = Adafruit_NeoMatrix(8, 8, 6,
  NEO_MATRIX_TOP     + NEO_MATRIX_RIGHT +
  NEO_MATRIX_COLUMNS + NEO_MATRIX_PROGRESSIVE,
  NEO_GRB            + NEO_KHZ800);

int sensorPin = 1;
int val = 0;
int prevVal;

int reds[] = {2,3,6,8,11,12,13,14,16,17,18,21,22,25,27,28,30,31,33,36,38,41,42,43,46,49,54,58,59,60,61};
int yellows[] = {19,20,26,29,34,35,37,44,45,50,51,52,53};

int reds2[] = {4,3,7,9,11,12,13,14,16,17,18,21,22,25,27,28,30,23,33,36,38,41,42,43,46,49,54,58,59,60,61};
int reds3[] = {10,4,5,8,11,12,13,14,15,16,17,18,21,22,25,27,28,30,31,33,36,38,41,42,43,46,49,54,58,59,60,61};

void fireball(){
  for (int i = 0; i < (sizeof(reds)/sizeof(int)); i ++){

    matrix.setPixelColor(reds[i],237,27,36);
  }
  for (int i = 0; i < (sizeof(yellows)/sizeof(int)); i++){
    matrix.setPixelColor(yellows[i],254,242,0);
  }
}

void fireball2(){
  for (int i = 0; i < (sizeof(reds2)/sizeof(int)); i ++){
    Serial.println(reds2[i]);
    matrix.setPixelColor(reds2[i],237,27,36);
  }
  for (int i = 0; i < (sizeof(yellows)/sizeof(int)); i++){
    //Serial.println("Pixel at " + yellows[i] + " is yellow");
    matrix.setPixelColor(yellows[i],254,242,0);
  }
}

void fireball3(){
  for (int i = 0; i < (sizeof(reds3)/sizeof(int)); i ++){
    Serial.println(reds3[i]);
    matrix.setPixelColor(reds3[i],237,27,36);
  }
  for (int i = 0; i < (sizeof(yellows)/sizeof(int)); i++){
    //Serial.println("Pixel at " + yellows[i] + " is yellow");
    matrix.setPixelColor(yellows[i],254,242,0);
  }
}

void fireballflip(){
  for (int i = 0; i < (sizeof(yellows)/sizeof(int)); i ++){
    Serial.println(reds[i]);
    matrix.setPixelColor(yellows[i],237,27,36);
  }
  for (int i = 0; i < (sizeof(reds)/sizeof(int)); i++){
    //Serial.println("Pixel at " + yellows[i] + " is yellow");
    matrix.setPixelColor(reds[i],254,242,0);
  }
}

int m_red[] = {0,1,2,3,8,9,10,11,16,17,18,19,24,25,26,27};
int m_green[] = {4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31};
int m_blue[] = {32,33,34,35,40,41,42,43,48,49,50,51,56,57,58,59};
int m_yellow[] = {36,37,38,39,44,45,46,47,52,53,54,55,60,61,62,63};

void microsoft(){
  for (int i = 0; i < (sizeof(m_red)/sizeof(int)); i ++){
    matrix.setPixelColor(m_red[i],243,83,37);
  }
  for (int i = 0; i < (sizeof(m_green)/sizeof(int)); i ++){
    matrix.setPixelColor(m_green[i],129,188,6);
  }
  for (int i = 0; i < (sizeof(m_blue)/sizeof(int)); i ++){
    matrix.setPixelColor(m_blue[i],5,166,240);
  }
  for (int i = 0; i < (sizeof(m_yellow)/sizeof(int)); i ++){
    matrix.setPixelColor(m_yellow[i],255,186,8);
  }
}

void microsoft2(){
  for (int i = 0; i < (sizeof(m_red)/sizeof(int)); i ++){
    matrix.setPixelColor(m_yellow[i],243,83,37);
  }
  for (int i = 0; i < (sizeof(m_green)/sizeof(int)); i ++){
    matrix.setPixelColor(m_red[i],129,188,6);
  }
  for (int i = 0; i < (sizeof(m_blue)/sizeof(int)); i ++){
    matrix.setPixelColor(m_green[i],5,166,240);
  }
  for (int i = 0; i < (sizeof(m_yellow)/sizeof(int)); i ++){
    matrix.setPixelColor(m_blue[i],255,186,8);
  }
}

int randomNum(){
  int randNum = random(1,266);
  Serial.println(randNum);
  return randNum;
}

void setup() {
  Serial.begin(9600);
  matrix.begin();
  matrix.setBrightness(50);
  prevVal = 0;
  matrix.fillScreen(0);
}

void clear(){
  for (int i = 0; i < 64; i++){
    matrix.setPixelColor(i,0,0,0);
  }
}

void loop() {
  //Basic Sound Reactive
  /*val = analogRead(sensorPin);
  for (int j = 0; j < 64; j++){
    if (val%3 == 0){
      matrix.setPixelColor(j,0,2*val,2*val);
    }
    else{
      matrix.setPixelColor(j,0,2*val,0);
    }
  } 
  matrix.show();*/
  
  /*for (int j = 15; j < 79; j++){
    matrix.setPixelColor(j-15,j,j*2,j*3); 
  }*/

  //Fireball flip animation 
  matrix.clear();
  fireball();
  matrix.show();
  delay(500);
  fireballflip();
  matrix.show();
  delay(500);
  
  /*val = analogRead(sensorPin);
  if (val%2 == 0){
    microsoft();
  }
  else{
    microsoft2();
  }
  matrix.show();
  delay(100);*/

  //Fireball gif - sound reactive
  /*val = analogRead(sensorPin);
    if (val%3 == 0){
      fireball();
      matrix.show();
    }
    else if (val%2 == 0){
      fireball2();
      matrix.show();
    }
    else{
      fireball3();
      matrix.show();
    }
  matrix.show(); 
  delay(10); */

  //Fireball flip - sound reactive
  /*val = analogRead(sensorPin);
  Serial.println(val);
  if (val%2 == 0){
    fireball();
  }
  else{
    fireballflip();
  }
  matrix.show();
  delay(100);*/
/*
  val = analogRead(sensorPin);
  int num1 = randomNum();
  int num2 = randomNum();
  int num3 = randomNum();

  //matrix.setBrightness(val-100);
  
  Serial.println(val);
  if ((val - prevVal) > 7 || (prevVal - val) > 7){
    for (int j=0; j < 64;j++){
      matrix.setPixelColor(j,num1,num2,num3);
    }
  }
  matrix.show();
  prevVal = val;
  delay(0.5);*/
}
