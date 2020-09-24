#include <AccelStepper.h>
#include <MultiStepper.h>

#define dirPinStepperV 2
#define stepPinStepperV 3
#define dirPinStepperH 4
#define stepPinStepperH 5
#define limitSwitchv 8

AccelStepper stepperv(AccelStepper::DRIVER, stepPinStepperV, dirPinStepperV);
AccelStepper stepperh(AccelStepper::DRIVER, stepPinStepperH, dirPinStepperH);
MultiStepper steppers;

bool data;
byte incomingByte;
byte previousincomingByte;
int pin[] = {22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53};


void setup() {
  Serial.begin(115200);
  
  pinMode(LED_BUILTIN, OUTPUT);

  stepperv.setMaxSpeed(1000);
  stepperh.setMaxSpeed(1000);

  steppers.addStepper(stepperv);
  steppers.addStepper(stepperh);
  
  pinMode(limitSwitchv, INPUT_PULLUP);
  //homing();
  deteksi();
  
  for(int i=0; i<28; i++){
    pinMode(pin[i], INPUT_PULLUP);
  }
}

void homing(){
  while(digitalRead(limitSwitchv) != 0){
    stepperv.setSpeed(-800);
    stepperv.runSpeed();
    stepperv.setCurrentPosition(0);
  }
  //koordinat(200, 0, 0); //steps dari limit switch vertikal
  //stepperv.setCurrentPosition(0);
}

void koordinat(int z, int x){
  long posisi[2];
  posisi[0] = z;
  posisi[1] = x;
  steppers.moveTo(posisi);
  steppers.runSpeedToPosition();
  delay(400);
}

void deteksi(){
  for(int y=0; y<1; y++){
    for(int j=0; j<28; j++){
      data = digitalRead(pin[j]);
      Serial.println(data);
    }
  }
}

void loop() {
  if (Serial.available() > 0) {
    previousincomingByte = incomingByte;
    incomingByte = Serial.read();
    if (incomingByte ==  'Y'){
      digitalWrite(LED_BUILTIN, LOW);
      delay(500);
    switch(previousincomingByte){
      case 'a':
      koordinat(11445, 7260);
      //swing ambil
      koordinat(0, 7260);
      //swing taruh
      koordinat(0, 0);
      //homing();
      break;

      case 'b': 
      koordinat(9747, 7260);
      //swing ambil
      koordinat(0, 7260);
      //swing taruh
      koordinat(0, 0);
      homing();
      break;
    
    case 'c':
      koordinat(8050,7260);
      //swing ambil
      koordinat(0, 7260);
      //swing taruh
      koordinat(0, 0);
      homing();
      break;
      
    case 'd': 
      koordinat(6353, 7260);
      //swing ambil
      koordinat(0, 7260);
      //swing taruh
      koordinat(0, 0);
      homing();
      break;
    
    case 'e':
      koordinat(4655, 7260);
      //swing ambil
      koordinat(0, 7260);
      //swing taruh
      koordinat(0, 0);
      homing();    
      break;
    
    case 'f':
      koordinat(2958, 7260);
      //swing ambil
      koordinat(0, 7260);
      //swing taruh
      koordinat(0, 0);
      homing();
      break;
    
    case 'g':
      koordinat(1261, 7260);
      //swing ambil
      koordinat(0, 7260);
      //swing taruh
      koordinat(0, 0);
      homing();
      break;
    
    case 'h':
      koordinat(1145, 4840);
      //swing ambil
      koordinat(0, 4840);
      //swing taruh
      koordinat(0, 0);
      homing();
      break;
      
    case 'i':
      koordinat(9747, 4840);
      //swing ambil
      koordinat(0, 4840);
      //swing taruh
      koordinat(0, 0);
      homing();
      break;
      
    case 'j':
      koordinat(8050, 4840);
      //swing ambil
      koordinat(0, 4840);
      //swing taruh
      koordinat(0, 0);
      homing();
      break;
      
    case 'k':
      koordinat(6353, 4840);
      //swing ambil
      koordinat(0, 4840);
      //swing taruh
      koordinat(0, 0);
      homing();
      break;
      
    case 'l':
      koordinat(4655, 4840);
      //swing ambil
      koordinat(0, 4840);
      //swing taruh
      koordinat(0, 0);
      homing();
      break;
      
    case 'm':
      koordinat(2958, 4840);
      //swing ambil
      koordinat(0, 4840);
      //swing taruh
      koordinat(0, 0);
      homing();
      break;
      
    case 'n':
      koordinat(1261, 4840);
      //swing ambil
      koordinat(0, 4840);
      //swing taruh
      koordinat(0, 0);
     homing();
      break;

    case 'o':
      koordinat(11445, 2420);
      //swing ambil
      koordinat(0, 2420);
      //swing taruh
      koordinat(0, 0);
      homing();
      break;
      
    case 'p':
      koordinat(9747, 2420);
      //swing ambil
      koordinat(0, 2420);
      //swing taruh
      koordinat(0, 0);
     homing();
      break;
 
    case 'q':
      koordinat(8050, 2420);
      //swing ambil
      koordinat(0, 2420);
      //swing taruh
      koordinat(0, 0);
     homing();
      break;
      
    case 'r':
      koordinat(6353, 2420);
      //swing ambil
      koordinat(0, 2420);
      //swing taruh
      koordinat(0, 0);
      homing();
      break;
      
    case 's':
      koordinat(4655, 2420);
      //swing ambil
      koordinat(0, 2420);
      //swing taruh
      koordinat(0, 0);
      homing();
      break;
      
    case 't':
      koordinat(2958, 2420);
      //swing ambil
      koordinat(0, 0);
      homing();
      break;
      
    case 'u':
      koordinat(1261, 2420);
      //swing ambil
      koordinat(0, 2420);
      //swing taruh
      koordinat(0, 0);
      homing();
      break;
      
    case 'v':
      koordinat(11445, 0);
      //swing ambil
      koordinat(0, 0);
      homing();
      break;
      
    case 'w':
      koordinat(9747, 0);
      //swing ambil
      koordinat(0, 0);
      homing();
      break;
      
    case 'x':
      koordinat(8050, 0);
      //swing ambil
      koordinat(0, 0);
     homing();
      break;
      
    case 'y':
      koordinat(6353, 0);
      //swing ambil
      koordinat(0, 0);
      //swing taruh
      homing();
      break;
      
    case 'z':
      koordinat(4655, 0);
      //swing ambil
      koordinat(0, 0);
      //swing taruh
      homing();
      break;
      
    case 'A':
      koordinat(2958, 0);
      //swing ambil
      koordinat(0,0);
      //swing taruh
      homing();
      break;
      
    case 'B':
      koordinat(1260, 0);
      //swing ambil
      koordinat(0, 0);
      //swing taruh
      homing();
      break;
      }  
    }
    if(incomingByte == 'N'){
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      koordinat(0,0);
    }
    deteksi();
    
   //else{
    //digitalWrite(LED_BUILTIN, HIGH);
    //delay(1000);
    //}
  }
 }
