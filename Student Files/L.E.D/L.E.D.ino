//These are premade packages that we use in this project
//In order to use them, we must tell our program to include them when compiling
#include <Adafruit_GFX.h>
#include <Adafruit_NeoMatrix.h>

//Define the matrix - We are using the Adafruit matrix package and this is how that package requires the matrix to be defined
//In the first like, the 8s represent the dimensions of the matrix. The 6 represents the arduino pin the matrix is plugged into
Adafruit_NeoMatrix matrix = Adafruit_NeoMatrix(8, 8, 6,
  NEO_MATRIX_TOP     + NEO_MATRIX_RIGHT +
  NEO_MATRIX_COLUMNS + NEO_MATRIX_PROGRESSIVE,
  NEO_GRB            + NEO_KHZ800);

//Define the arduino pin used by the sound sensor
#define sensorPin A5

//Define variables that are used in the code
int val;
int prevVal;

//This is how you can define lists
//These two lists are lists of points on the matrix
//We can use lists to make patterns by telling the program to light
//all the points in the list as a certain colour
int reds[] = {2,3,6,8,11,12,13,14,16,17,18,21,22,25,27,28,30,31,33,36,38,41,42,43,46,49,54,58,59,60,61};
int yellows[] = {19,20,26,29,34,35,37,44,45,50,51,52,53};

//This function use the above two lists to display a pattern on the matrix
//To display this pattern, put fireball() in the main loop
void fireball(){
  for (int i = 0; i < (sizeof(reds)/sizeof(int)); i ++){

    matrix.setPixelColor(reds[i],237,27,36);
  }
  for (int i = 0; i < (sizeof(yellows)/sizeof(int)); i++){
    matrix.setPixelColor(yellows[i],254,242,0);
  }
}

//A function that gets a random number from 1 to 255 and returns the number
int randomNum(){
  int randNum = random(1,266);
  Serial.println(randNum);
  return randNum;
}

//This code runs only once, before entering the main loop
void setup() {
  Serial.begin(9600); //Start the serial monitor so you can print outputs

  //Initiate the matrix
  matrix.begin();
  matrix.setBrightness(40);

  val = 0; //Initiate this variable to be zero
  prevVal = 0; //Initiate this variable to be zero
}

//Main loop. When uploaded to the arduino, this code runs repeatedly 
void loop() {
  //Get input from the sound sensor.
  //The sensor gives an integer value which represents the intensitity of the sound
  val = analogRead(sensorPin);

  //Get three random numbers using the random number function defined above
  int num1 = randomNum();
  int num2 = randomNum();
  int num3 = randomNum();

  //If the sound intensitiy goes up or down by more than 7, the matrix changes colour
  if ((val - prevVal) > 7 || (prevVal - val) > 7){
    //Go through each point on the matrix and change it's colour
    for (int j=0; j < 64;j++){
      //Use the random numbers we found as the values to determine the colour
      matrix.setPixelColor(j,num1,num2,num3);
    }
  }

  //Since we make changes based on the change in sound intensity, we must keep track of the
  //previous value used so we can compare it to the next value we get
  prevVal = val;
  
  //Display the matrix. 
  //This must always be put to display changes made to the matrix
  //Just setting the pixel colour does not cause the change to appear on the matrix
  matrix.show(); 
  
  delay(100); //Sleep the code - This is necessary for the code to be able to display properly on the matrix
}
