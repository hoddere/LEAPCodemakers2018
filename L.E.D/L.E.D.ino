#include <Adafruit_GFX.h>
#include <Adafruit_NeoMatrix.h>

Adafruit_NeoMatrix matrix = Adafruit_NeoMatrix(8, 8, 6,
  NEO_MATRIX_TOP     + NEO_MATRIX_RIGHT +
  NEO_MATRIX_COLUMNS + NEO_MATRIX_PROGRESSIVE,
  NEO_GRB            + NEO_KHZ800);

int sensorPin = 1;
int val = 0;

void setup() {
  Serial.begin(9600);
  matrix.begin();
  matrix.setBrightness(40);
}

void loop() {
  matrix.fillScreen(0);
  for (int i = 0; i < 64; i++){
    matrix.setPixelColor(i,255,0,0);
  }
  
  val = analogRead(sensorPin);
  Serial.println(val); 
  for (int j = 0; j < 64; j++){
    if (val%2 == 0){
      matrix.setPixelColor(j,0,val,val);
    }
    else{
      matrix.setPixelColor(j,255,val,val);
    }
    
  }  

  matrix.show();
  delay(100);
}
