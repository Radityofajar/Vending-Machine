#include <AccelStepper.h>

#define dirPinVertikal 7
#define stepPinVertikal 8
#define dirPinHorizontal 9
#define stepPinHorizontal 10

AccelStepper stepperv(AccelStepper::DRIVER, stepPinVertikal, dirPinVertikal);
AccelStepper stepperh(AccelStepper::DRIVER, stepPinHorizontal, dirPinHorizontal);


void setup() {
  // put your setup code here, to run once:
  stepperv.setMaxSpeed(2400.0); //2400 rpm atau 40 rps
  stepperv.setAcceleration(240.0);

  stepperh.setMaxSpeed(2400.0); //2400 rpm atau 40 rps
  stepperh.setAcceleration(240.0);
}

void move(int stepv, int steph){
  stepperv.moveTo(stepv);
  stepperv.moveTo(steph);
  while(!stepperv.run() || !stepperh.run());
}

void loop() {
  move(100,100);
  delay(100);
  move(0,0);
  delay(1000);
  move(200,0);
  delay(100);
  move(0,0);
  delay(1000);
  // put your main code here, to run repeatedly:
}
