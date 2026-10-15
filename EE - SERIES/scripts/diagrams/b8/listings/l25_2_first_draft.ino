// The assistant's first answer, before review. It compiles. Find the problems before reading on.
#include <Wire.h>
#include <Adafruit_BME280.h>

Adafruit_BME280 bme;
volatile bool marked = false;

void IRAM_ATTR onButton() {
  delay(30);                                   // debounce
  Serial.println("mark");
}

void setup() {
  Serial.begin(9600);
  Wire.begin(21, 22);
  bme.begin();
  pinMode(0, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(0), onButton, FALLING);
}

void loop() {
  Serial.print(bme.readTemperature());
  Serial.print(",");
  Serial.print(bme.readHumidity());
  Serial.print(",");
  Serial.println(bme.readPressure());
  delay(1000);
}
