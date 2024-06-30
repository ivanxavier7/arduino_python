#include <DHT_U.h>
#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11

DHT TH(DHTPIN, DHTTYPE);
float tempC=0.0;
float tempF=0.0;
float humidity=0.0;
int DL=1000;
int setTime=500;

void setup() {
  Serial.begin(115200);
  TH.begin();
  delay(setTime);
}

void loop() {
  tempC = TH.readTemperature();
  tempF = TH.readTemperature(true);
  humidity = TH.readHumidity();

  Serial.print("Temperature: ");
  Serial.print(tempC);
  Serial.print("C, ");
  Serial.print(tempF);
  Serial.print("F, ");
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println("%");

  delay(DL);
}
