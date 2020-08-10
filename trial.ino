#include<AccelStepper.h>

#define dirPinStepperV 2
#define stepPinStepperV 3
#define dirPinStepperH 4
#define stepPinStepperH 5

AccelStepper stepperV(AccelStepper::DRIVER, stepPinStepperV, dirPinStepperV);
AccelStepper stepperH(AccelStepper::DRIVER, stepPinStepperH, dirPinStepperH);

void setup() {
  stepperV.setMaxSpeed(1950.0);
  stepperV.setAcceleration(200.0);

  stepperH.setMaxSpeed(1950.0);
  stepperH.setAcceleration(200.0);

  Serial.begin(9600);
}

void koordinat(int Horizontal, int Vertikal){
  stepperV.moveTo(Vertikal);
  stepperH.moveTo(Horizontal);
  while(!stepperV.run() || !stepperH.run());
}

void loop() {
  Serial.println("Run Bersama");
  koordinat(200,200);
  delay(2000);
  Serial.println("Kembali ke posisi semula bersama");
  koordinat(0,0);
  delay(2000);
  Serial.println("Hanya vertikal");
  koordinat(0,200);
  delay(2000);
  Serial.println("Vertikal kembali ke posisi semula");
  koordinat(0,0);
  delay(2000);
  Serial.println("Hanya horizontal");
  koordinat(200,0);
  delay(2000);
  Serial.println("Horizontal kembali ke posisi semula");
  koordinat(0,0);
  delay(2000);
  Serial.println("Run Bersama");
  koordinat(200,200);
  delay(2000);
  Serial.println("Horizontal bergerak ke posisi semula");
  koordinat(0,200);
  delay(2000);
  Serial.println("Vertikal bergerak ke posisi semula");
  koordinat(0,0);
  delay(2000);
}
