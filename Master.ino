#include <AccelStepper.h>
#include <MultiStepper.h>

#define dirPinStepperV 2
#define stepPinStepperV 3
#define dirPinStepperH 4
#define stepPinStepperH 5
#define dirPinSwing 6
#define stepPinSwing 7
#define limitSwitchv 8
#define limitSwitchh 9

AccelStepper stepperv(AccelStepper::DRIVER, stepPinStepperV, dirPinStepperV);
AccelStepper stepperh(AccelStepper::DRIVER, stepPinStepperH, dirPinStepperH);
AccelStepper swing(AccelStepper::DRIVER, stepPinSwing, dirPinSwing);
MultiStepper steppers;

bool data;
byte incomingByte;
byte previousincomingByte;
int pin[] = {22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53};


void setup() {
  Serial.begin(9600);

  stepperv.setMaxSpeed(1500);
  stepperh.setMaxSpeed(1500);

  steppers.addStepper(stepperv);
  steppers.addStepper(stepperh);
  steppers.addStepper(swing);
  
  for(int i=0; i<28; i++){
    pinMode(pin[i], INPUT_PULLUP);
  }

  pinMode(limitSwitchv, INPUT_PULLUP);
  pinMode(limitSwitchh, INPUT_PULLUP);

  homing();
  deteksi();
  
}

void homing() {
  while(digitalRead(limitSwitchv) != 0){
    stepperv.setSpeed(-800);
    stepperv.runSpeed();
    stepperv.setCurrentPosition(0);
  }
  //koordinat(200, 0, 0); //steps dari limit switch vertikal
  //stepperv.setCurrentPosition(0);
  
  while(digitalRead(limitSwitchh) != 0){
    stepperh.setSpeed(-800);
    stepperh.runSpeed();
    stepperh.setCurrentPosition(0);
  }
  //koordinat(0, 200, 0); //steps dari limit switch horizontal
  //stepperh.setCurrentPosition(0);
}

void koordinat(int y, int x, int z){
  long posisi[3];
  posisi[0] = y;
  posisi[1] = x;
  posisi[2] = z;
  steppers.moveTo(posisi);
  steppers.runSpeedToPosition();
  delay(400);
}

void deteksi(){
    for(int j=0; j<28; j++){
      data = digitalRead(pin[j]);
      Serial.println(data);
  }
}

void loop() {
  delay(100);
  if (Serial.available() > 0) {
    previousincomingByte = incomingByte;
    incomingByte = Serial.read();
    if (incomingByte == 'R') {
      deteksi();
    }
      if (incomingByte ==  'Y'){
        delay(500);
        switch(previousincomingByte){
          case 'a':
            koordinat(11445, 0, 0);
            koordinat(11445, 0, 100);//swing ambil
            koordinat(0, 0, 100);
            koordinat(0, 0, 0); //swing taruh

          break;

          case 'b':
            koordinat(11445, 2420, 0);
            koordinat(11645, 2420, 100);//swing ambil
            koordinat(0, 2420, 100);
            koordinat(0, 2420, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 'c':
            koordinat(11445, 4840, 0);
            koordinat(11645, 4840, 100);//swing ambil
            koordinat(0, 4840, 100);
            koordinat(0, 4840, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 'd':
            koordinat(11445, 7260, 0); //berangkat
            koordinat(11645, 7260, 100);//swing ambil
            koordinat(0, 7260, 100);
            koordinat(0, 7260, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 'e':
            koordinat(9747, 0, 0);
            koordinat(9947, 0, 100);//swing ambil
            koordinat(0, 0, 100);
            koordinat(0, 0, 0);//swing taruh

          break;

          case 'f':
            koordinat(9747, 2420, 0);
            koordinat(9947, 2420, 100);//swing ambil
            koordinat(0, 2420, 100);
            koordinat(0, 2420, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 'g':
            koordinat(9747, 4840, 0);
            koordinat(9947, 4840, 100);//swing ambil
            koordinat(0, 4840, 100);
            koordinat(0, 4840, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 'h': 
            koordinat(9747, 7260, 0);
            koordinat(9947, 7260, 100);//swing ambil
            koordinat(0, 7260, 100);
            koordinat(0, 7260, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 'i':
            koordinat(8050, 0, 0);
            koordinat(8250, 0, 100);//swing ambil
            koordinat(0, 0, 100);
            koordinat(0, 0, 0);

          break;

          case 'j':
            koordinat(8050, 2420, 0);
            koordinat(8250, 2420, 100);//swing ambil
            koordinat(0, 2420, 100);
            koordinat(0, 2420, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 'k':
            koordinat(8050, 4840, 0);
            koordinat(8250, 4840, 100);//swing ambil
            koordinat(0, 4840, 100);
            koordinat(0, 4840, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 'l':
            koordinat(8050,7260, 0);
            koordinat(8250,7260, 100);//swing ambil
            koordinat(0, 7260, 100);
            koordinat(0, 7260, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 'm':
            koordinat(6353, 0, 0);
            koordinat(6553, 0, 100);//swing ambil
            koordinat(0, 0, 100);
            koordinat(0, 0, 0);//swing taruh

          break;

          case 'n':
            koordinat(6353, 2420, 0);
            koordinat(6553, 2420, 100);//swing ambil
            koordinat(0, 2420, 100);
            koordinat(0, 2420, 0);//swing taruh
            koordinat(0, 0, 0);

            break;

          case 'o':
            koordinat(6353, 4840, 0);
            koordinat(6553, 4840, 100);//swing ambil
            koordinat(0, 4840, 100);
            koordinat(0, 4840, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 'p': 
            koordinat(6353, 7260, 0);
            koordinat(6553, 7260, 100);//swing ambil
            koordinat(0, 7260, 100);
            koordinat(0, 7260, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 'q':
            koordinat(4655, 0, 0);
            koordinat(4855, 0, 100);//swing ambil
            koordinat(0, 0, 100);
            koordinat(0, 0, 0);//swing taruh

          break;

          case 'r':
            koordinat(4655, 2420, 0);
            koordinat(4855, 2420, 100);//swing ambil
            koordinat(0, 2420, 100);
            koordinat(0, 2420, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 's':
            koordinat(4655, 4840, 0);
            koordinat(4855, 4840, 100);//swing ambil
            koordinat(0, 4840, 100);
            koordinat(0, 4840, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 't':
            koordinat(4655, 7260, 0);
            koordinat(4855, 7260, 100);//swing ambil
            koordinat(0, 7260, 100);
            koordinat(0, 7260, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 'u':
            koordinat(2958, 0, 0);
            koordinat(3158, 0, 100);//swing ambil
            koordinat(0, 0, 100);
            koordinat(0, 0, 0);//swing taruh

          break;

          case 'v':
            koordinat(2958, 2420, 0);
            koordinat(3158, 2420, 100);//swing ambil
            koordinat(0, 2420, 100);
            koordinat(0, 2420, 0);
            koordinat(0, 0, 0);

          break;

          case 'w':
            koordinat(2958, 4840, 0);
            koordinat(3158, 4840, 100);//swing ambil
            koordinat(0, 4840, 100);
            koordinat(0, 4840, 0);//swing taruh
            koordinat(0, 0, 0);

            break;

          case 'x':
            koordinat(2958, 7260, 0);
            koordinat(3158, 7260, 100);//swing ambil
            koordinat(0, 7260, 100);
            koordinat(0, 7260, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 'y':
            koordinat(1261, 0, 0);
            koordinat(1461, 0, 100);//swing ambil
            koordinat(0, 0, 100);
            koordinat(0, 0, 0);//swing taruh

          break;

          case 'z':
            koordinat(1261, 2420, 0);
            koordinat(1461, 2420, 100);//swing ambil
            koordinat(0, 2420, 100);
            koordinat(0, 2420, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 'A':
            koordinat(1261, 4840, 0);
            koordinat(1461, 4840, 100);//swing ambil
            koordinat(0, 4840, 100);
            koordinat(0, 4840, 0);//swing taruh
            koordinat(0, 0, 0);

          break;

          case 'B':
            koordinat(1261, 7260, 0);
            koordinat(1461, 7260, 100);//swing ambil
            koordinat(0, 7260, 100);
            koordinat(0, 7260, 0);//swing taruh
            koordinat(0, 0, 0);

          break;    
        }  
      }

      if(incomingByte == 'N'){
        koordinat(0,0, 0);
      }
      deteksi();
    }
   }
