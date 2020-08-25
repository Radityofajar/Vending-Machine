//control 1 stepper motor using A4988 driver module

#define dirPin 2
#define stepPin 3

void setup(){
  pinMode(dirPin, OUTPUT);
  pinMode(stepPin, OUTPUT);
}

//function moveUp
void moveUp(int steps){
  digitalWrite(dirPin, HIGH);
  for(int x = 0; x < steps; x++){
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(1000);
  }
}

//function moveDown
void moveDown(int steps){
  digitalWrite(dirPin, LOW);
  for(int x = 0; x < steps; x++){
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(1000);
  }
}

void loop(){
  while(true){
  
    moveUp(400);
    delay(500);
    moveDown(400);
    delay(500);

    moveUp(800);
    delay(500);
    moveDown(800);
    delay(500);
    
    moveUp(1000);
    delay(500);
    moveDown(1000);
    delay(500);
  }
}
