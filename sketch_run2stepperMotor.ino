//control 2 stepper motor using A4988 driver module

#define dirPinVertikal 2
#define stepPinVertikal 3
#define dirPinHorizontal 4
#define stepPinHorizontal 5

void setup(){
  pinMode(dirPinVertikal, OUTPUT);
  pinMode(stepPinVertikal, OUTPUT);
  pinMode(dirPinHorizontal, OUTPUT);
  pinMode(stepPinHorizontal, OUTPUT);
}

//function moveUp
void moveUp(int steps){
  digitalWrite(dirPinVertikal, HIGH);
  for(int x = 0; x < steps; x++){
    digitalWrite(stepPinVertikal, HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPinVertikal, LOW);
    delayMicroseconds(1000);
  }
}

//function moveRight
void moveRight(int steps){
  digitalWrite(dirPinHorizontal, HIGH);
  for(int x = 0; x < steps; x++){
    digitalWrite(stepPinHorizontal, HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPinHorizontal, LOW);
    delayMicroseconds(1000);
  }
}

//function moveLeft
void moveLeft(int steps){
  digitalWrite(dirPinHorizontal, LOW);
  for(int x = 0; x < steps; x++){
    digitalWrite(stepPinHorizontal, HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPinHorizontal, LOW);
    delayMicroseconds(1000);
  }
}

//function moveDown
void moveDown(int steps){
  digitalWrite(dirPinVertikal, LOW);
  for(int x = 0; x < steps; x++){
    digitalWrite(stepPinVertikal, HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPinVertikal, LOW);
    delayMicroseconds(1000);
  }
}

void loop(){
  while(true){

    moveUp(1200);
    delay(500);
    moveRight(200);
    delay(500);

    moveLeft(200);
    delay(500);
    moveDown(1200);
    delay(500);

    moveUp(800);
    delay(500);
    moveRight(400);
    delay(500);

    moveLeft(400);
    delay(500);
    moveDown(800);
    delay(500);

    moveUp(400);
    delay(500);
    moveRight(600);
    delay(500);

    moveLeft(600);
    delay(500);
    moveDown(400);
    delay(500);
  }
}
