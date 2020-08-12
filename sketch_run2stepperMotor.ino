//control 2 stepper motor using A4988 driver module

#define dirPinVertikal 0
#define stepPinVertikal 1
#define dirPinHorizontal 2
#define stepPinHorizontal 3

#define button1 4
#define button2 5
#define button3 6

#define microSwitchV 7
#define microSwitchH 8

int buttonPressed;

void setup(){
  pinMode(dirPinVertikal, OUTPUT);
  pinMode(stepPinVertikal, OUTPUT);
  pinMode(dirPinHorizontal, OUTPUT);
  pinMode(stepPinHorizontal, OUTPUT);

  pinMode(button1, INPUT_PULLUP);
  pinMode(button2, INPUT_PULLUP);
  pinMode(button3, INPUT_PULLUP);

  pinMode(microSwitchV, INPUT_PULLUP);
  pinMode(microSwitchH, INPUT_PULLUP);

//vertikal starting point
digitalWrite(dirPinVertikal, HIGH);
while(true){
  if(digitalRead(microSwitchV)==LOW){
    moveUp(70);
    break;
  }
  digitalWrite(stepPinVertikal, HIGH);
  delayMicroseconds(300);
  digitalWrite(stepPinVertikal, LOW);
  delayMicroseconds(300);
}

//horizontal starting point
digitalWrite(dirPinHorizontal, LOW);
while(true){
  if(digitalRead(microSwitchH)==LOW){
    moveRight(350);
    break;
  }
  digitalWrite(stepPinHorizontal, HIGH);
  delayMicroseconds(300);
  digitalWrite(stepPinHorizontal, LOW);
  delayMicroseconds(300);
}
}

//function moveUp
void moveUp(int steps){
  digitalWrite(dirPinVertikal, LOW);
  for(int x = 0; x < steps; x++){
    digitalWrite(stepPinVertikal, HIGH);
    delayMicroseconds(300);
    digitalWrite(stepPinVertikal, LOW);
    delayMicroseconds(300);
  }
}

//function moveRight
void moveRight(int steps){
  digitalWrite(dirPinHorizontal, HIGH);
  for(int x = 0; x < steps; x++){
    digitalWrite(stepPinHorizontal, HIGH);
    delayMicroseconds(300);
    digitalWrite(stepPinHorizontal, LOW);
    delayMicroseconds(300);
  }
}

//function moveLeft
void moveLeft(int steps){
  digitalWrite(dirPinHorizontal, LOW);
  for(int x = 0; x < steps; x++){
    digitalWrite(stepPinHorizontal, HIGH);
    delayMicroseconds(300);
    digitalWrite(stepPinHorizontal, LOW);
    delayMicroseconds(300);
  }
}

//function moveDown
void moveDown(int steps){
  digitalWrite(dirPinVertikal, HIGH);
  for(int x = 0; x < steps; x++){
    digitalWrite(stepPinVertikal, HIGH);
    delayMicroseconds(300);
    digitalWrite(stepPinVertikal, LOW);
    delayMicroseconds(300);
  }
}

void loop(){
  while(true){
    if(digitalRead(button1)==LOW){
      buttonPressed = 1;
      break;
    }
    if(digitalRead(button2)==LOW){
      buttonPressed = 2;
      break;
    }
    if(digitalRead(button3)==LOW){
      buttonPressed = 3;
      break;
    }
  }

  switch(buttonPressed){

    case 1:
    moveUp(200);
    delay(200);
    moveRight(200);
    delay(300);

    moveLeft(200);
    delay(200);
    moveDown(200);
    break;


    case 2:
    moveUp(400);
    delay(200);
    moveRight(400);
    delay(300);

    moveLeft(400);
    delay(200);
    moveDown(400);
    break;


    case 3:
    moveUp(600);
    delay(200);
    moveRight(600);
    delay(300);

    moveLeft(600);
    delay(200);
    moveDown(600);
    break;
  }
}
