//These are premade packages that we use in this project
//In order to use them, we must tell our program to include them when compiling
#include <Adafruit_GFX.h>
#include <Adafruit_NeoMatrix.h>
#include "Joystick.h"

//Define the arduino pins used by the joystick
#define JOYSTICK_PIN_X A4 //JOYSTICK_PIN_X receives the input for the x direction
#define JOYSTICK_PIN_Y A5 //JOYSTICK_PIN_Y receives the input for the y direction
#define JOYSTICK_PIN_SW 10 //JOYSTICK_PIN_SW receives the input for the push button on the joystick

//Define the matrix - We are using the Adafruit matrix package and this is how that package requires the matrix to be defined
//In the first like, the 8s represent the dimensions of the matrix. The 6 represents the arduino pin the matrix is plugged into
Adafruit_NeoMatrix matrix = Adafruit_NeoMatrix(8, 8, 6,
  NEO_MATRIX_TOP     + NEO_MATRIX_RIGHT +
  NEO_MATRIX_COLUMNS + NEO_MATRIX_PROGRESSIVE,
  NEO_GRB            + NEO_KHZ800);

//Define the joystick - We are using a premade joystick package and this is how the package requires the joystick to be defined
Joystick joystick(JOYSTICK_PIN_X,JOYSTICK_PIN_Y,JOYSTICK_PIN_SW);

//Set initial position values of the joystick
int joystickX = 0;
int joystickY = 0;

//Define the joystick calibration variables
int joystickX_Cal;
int joystickY_Cal;

//Define the position variable
int pos;

void setup() {
  Serial.begin(9600); //Start the serial monitor so you can print outputs

  //Initiate the matrix
  matrix.begin();
  matrix.setBrightness(40);

  //Set the joystick calibration values
  joystickX_Cal = joystick.getX();
  joystickY_Cal = joystick.getY();
}

//Function which moves the dot left when the joystick is moved left
void joystickLEFT(){
  //Check if the dot is in the leftmost column. If it is don't change the position value
  if (pos%8 == 0){
    Serial.println("Cannot go left");
  }
  //The dot is not in the leftmost column so move it one to the left
  else{
    pos = pos - 1;
  }
}

//Function which moves the dot right the joystick is moved right
void joystickRIGHT(){
  //YOUR CODE GOES HERE
}

//Function which moves the dot down when the joystick is moved down
void joystickDOWN(){
  //CHeck if the dot is in the bottommost row. If it is, don't change the position value
  if ((pos + 8) > 63){
    Serial.println("Cannot go down");
  }
  //The dot is not in the bottom row so move it down a row
  else {
    pos = pos + 8;
  }
}

//Function which moves the dot up when the joystick is moved up
void joystickUP(){
  //YOUR CODE HERE
}

//Function which tells the program what to do when the joystick is pushed
void select(){
  //YOUR CODE HERE
}

void loop() {
  matrix.fillScreen(0); //Clear the matrix
  matrix.setPixelColor(pos,255,255,0); //Display the dot on the matrix at the value of pos
  matrix.show(); //Show the matrix
  
  //Check for input from joystick Read Joystick X,Y axis and press
  joystickX =  (joystick.getX() - joystickX_Cal); //Get X value of movement
  joystickY =  (joystick.getY() - joystickY_Cal); // Get Y value of movement
  bool joystickSW =  joystick.getSW(); //Get True if pressed, false otherwise

  //Call the correct function based on the input from the joystick
  //Changing the integer values used to compare to the joystick movement determines the sensitivity of the joystick. 
  //Lower the value to make it more sensitive, raise the values to make it more sensitive. I like the sensitivity at 300
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
  
  delay(150); //Sleep the code

  //YOUR CODE HERE
  //Add your own code to create a game of connect fourduino! You can add code into the main loop and create your own functions
  //Ask Emily or Jack if you need help! :) 
}
