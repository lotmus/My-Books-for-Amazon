// Reviewed version: BME280 to USB serial as "t,h,p", a version command, and a debounced mark button.
#include <Wire.h>
#include <Adafruit_BME280.h>

const int PIN_SDA = 8, PIN_SCL = 9, PIN_BUTTON = 0;
const uint8_t BME_ADDR = 0x76;
const uint32_t PERIOD_MS = 1000, DEBOUNCE_MS = 30;

Adafruit_BME280 bme;
bool sensor_ok = false;
volatile uint32_t button_edge_ms = 0;          // set by the ISR, handled in loop()
volatile bool button_edge = false;
String rx;

void IRAM_ATTR onButton() {                     // ISR: record and leave
  button_edge_ms = millis();
  button_edge = true;
}

bool startSensor() {
  if (!bme.begin(BME_ADDR, &Wire)) return false;
  bme.setSampling(Adafruit_BME280::MODE_FORCED,
                  Adafruit_BME280::SAMPLING_X1, Adafruit_BME280::SAMPLING_X1,
                  Adafruit_BME280::SAMPLING_X1, Adafruit_BME280::FILTER_OFF);
  return true;
}

void setup() {
  Serial.begin(115200);
  Wire.begin(PIN_SDA, PIN_SCL, 400000);
  pinMode(PIN_BUTTON, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(PIN_BUTTON), onButton, FALLING);
  sensor_ok = startSensor();
}

void handleSerial() {
  while (Serial.available()) {
    char c = (char)Serial.read();
    if (c == '\n') {
      rx.trim();
      if (rx == "version") Serial.print("fw 1.0.0\r\n");
      rx = "";
    } else if (rx.length() < 32) {
      rx += c;
    }
  }
}

void handleButton() {
  if (button_edge && millis() - button_edge_ms >= DEBOUNCE_MS) {
    button_edge = false;
    if (digitalRead(PIN_BUTTON) == LOW) Serial.print("mark\r\n");   // still pressed: real press
  }
}

void loop() {
  static uint32_t last = 0;
  handleSerial();
  handleButton();
  if (millis() - last < (sensor_ok ? PERIOD_MS : 2000)) return;
  last = millis();
  if (!sensor_ok) {
    Serial.print("error,bme280\r\n");
    sensor_ok = startSensor();
    return;
  }
  if (!bme.takeForcedMeasurement()) { sensor_ok = false; return; }
  char line[48];
  snprintf(line, sizeof line, "%.2f,%.1f,%.2f\r\n",
           bme.readTemperature(), bme.readHumidity(), bme.readPressure() / 100.0f);
  Serial.print(line);
}
