#include <AccelStepper.h>
#include <MultiStepper.h>

#define dirPinStepperV 2
#define stepPinStepperV 3
#define dirPinStepperH 4
#define stepPinStepperH 5

AccelStepper stepperv(AccelStepper::DRIVER, stepPinStepperV, dirPinStepperV);
AccelStepper stepperh(AccelStepper::DRIVER, stepPinStepperH, dirPinStepperH);
MultiStepper steppers;
int incomingByte;     //input pembeli

void setup() {
  Serial.begin(115200);

  stepperv.setMaxSpeed(1450); //set max speed nanti diatur
  stepperh.setMaxSpeed(1450); 

  steppers.addStepper(stepperv);//motor vertikal
  steppers.addStepper(stepperh); //motor horizontal
}

void koordinat(int z, int x){
  long posisi[2];
  posisi[0] = z; // stepper vertikal
  posisi[1] = x; //stepper horizontal
  steppers.moveTo(posisi);
  steppers.runSpeedToPosition(); 
  delay(400);
}

void loop() {
    if (Serial.available() > 0) {
      incomingByte = Serial.read();
  switch(incomingByte){
    case 'a': 
      koordinat(11445, 7260);
      //swing ambil
      koordinat(0, 7260);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
       
   case 'b': 
      koordinat(9747, 7260);
      //swing ambil
      koordinat(0, 7260);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
    
    case 'c':
      koordinat(8050,7260);
      //swing ambil
      koordinat(0, 7260);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
      
    case 'd': 
      koordinat(6353, 7260);
      //swing ambil
      koordinat(0, 7260);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
    
    case 'e':
      koordinat(4655, 7260);
      //swing ambil
      koordinat(0, 7260);
      //swing taruh
      koordinat(0, 0);    
      Serial.print("done");
      break;
    
    case 'f':
      koordinat(2958, 7260);
      //swing ambil
      koordinat(0, 7260);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
    
    case 'g':
      koordinat(1261, 7260);
      //swing ambil
      koordinat(0, 7260);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
    
    case 'h':
      koordinat(11445, 4840);
      //swing ambil
      koordinat(0, 4840);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
      
    case 'i':
      koordinat(9747, 4840);
      //swing ambil
      koordinat(0, 4840);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
      
    case 'j':
      koordinat(8050, 4840);
      //swing ambil
      koordinat(0, 4840);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
      
    case 'k':
      koordinat(6353, 4840);
      //swing ambil
      koordinat(0, 4840);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
      
    case 'l':
      koordinat(4655, 4840);
      //swing ambil
      koordinat(0, 4840);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
      
    case 'm':
      koordinat(2958, 4840);
      //swing ambil
      koordinat(0, 4840);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
      
    case 'n':
      koordinat(1261, 4840);
      //swing ambil
      koordinat(0, 4840);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;

    case 'o':
      koordinat(11445, 2420);
      //swing ambil
      koordinat(0, 2420);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
      
    case 'p':
      koordinat(9747, 2420);
      //swing ambil
      koordinat(0, 2420);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
 
    case 'q':
      koordinat(8050, 2420);
      //swing ambil
      koordinat(0, 2420);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
      
    case 'r':
      koordinat(6353, 2420);
      //swing ambil
      koordinat(0, 2420);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
      
    case 's':
      koordinat(4655, 2420);
      //swing ambil
      koordinat(0, 2420);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
      
    case 't':
      koordinat(2958, 2420);
      //swing ambil
      koordinat(0, 2420);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
      
    case 'u':
      koordinat(1261, 2420);
      //swing ambil
      koordinat(0, 2420);
      //swing taruh
      koordinat(0, 0);
      Serial.print("done");
      break;
      
    case 'v':
      koordinat(11445, 0);
      //swing ambil
      koordinat(0, 0);
      Serial.print("done");
      //swing taruh
      break;
      
    case 'w':
      koordinat(9747, 0);
      //swing ambil
      koordinat(0, 0);
      Serial.print("done");
      //swing taruh
      break;
      
    case 'x':
      koordinat(8050, 0);
      //swing ambil
      koordinat(0, 0);
      Serial.print("done");
      //swing taruh
      break;
      
    case 'y':
      koordinat(6353, 0);
      //swing ambil
      koordinat(0, 0);
      Serial.print("done");
      //swing taruh
      break;
      
    case 'z':
      koordinat(4655, 0);
      //swing ambil
      koordinat(0, 0);
      Serial.print("done");
      //swing taruh
      break;
      
    case 'A':
      koordinat(2958, 0);
      //swing ambil
      koordinat(0, 0);
      Serial.print("done");
      //swing taruh
      break;
      
    case 'B':
      koordinat(1260, 0);
      //swing ambil
      koordinat(0, 0);
      Serial.print("done");
      //swing taruh
      break;
    }
  }
}
