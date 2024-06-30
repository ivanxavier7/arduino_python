int potPin=A0;
float potValue=0.0;
int DL=1000;

void setup() {
  pinMode(potPin, INPUT);
  Serial.begin(115200);
}

void loop() {
  potValue=analogRead(potPin);
  Serial.print("Potentiometer Value: ");
  Serial.println((potValue/1023)*5);

  delay(DL);
}
