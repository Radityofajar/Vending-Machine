int incomingByte;      // variable stores  serial data

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
  }
    if (incomingByte == '1') {
      Serial.println("High");
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == '0') {
      Serial.println("LOW");
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
    }
 }
