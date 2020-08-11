//control 1 stepper motor using A4988 driver module

#define dirPin 0
#define stepPin 1

#define microSwitch 2

#define button1 3
#define button2 4
#define button3 5

int buttonPressed;

void setup(){
  pinMode(dirPin, OUTPUT);
  pinMode(stepPin, OUTPUT);

  pinMode(button1, INPUT_PULLUP);
  pinMode(button2, INPUT_PULLUP);
  pinMode(button3, INPUT_PULLUP);

  pinMode(microSwitch, INPUT_PULLUP);

  //kalibrasi posisi awal kontainer
  digitalWrite(dirPin, HIGH);
  while(true){
    if(digitalRead(microSwitch)==LOW){
      moveUp(70);
      break;
    }
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(300);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(300);
  }
}

//function moveUp
void moveUp(int steps){
  digitalWrite(dirPin, LOW);
  for(int x = 0; x < steps; x++){
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(300);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(300);
  }
}

//function moveDown
void moveDown(int steps){
  digitalWrite(dirPin, HIGH);
  for(int x = 0; x < steps; x++){
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(300);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(300);
  }
}

void loop(){
  while(true){
  if(digitalRead(button1)==LOW){
    buttonPressed = 1;
    //break;
  }
  if(digitalRead(button2)==LOW){
    buttonPressed = 2;
    //break;
  }
  if(digitalRead(button3)==LOW){
    buttonPressed = 3;
    //break;
  }

  switch(buttonPressed){
    case 1:
    moveUp(200);
    delay(200);
    moveDown(200);
    break;

    case 2:
    moveUp(400);
    delay(200);
    moveDown(400);
    break;

    case 3:
    moveUp(600);
    delay(200);
    moveDown(600);
    break;
  }
  }
}
