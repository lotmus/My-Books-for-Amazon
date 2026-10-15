// Arduino framework (ESP32-S3): three jobs at three rates, none of them blocking.
#include <Arduino.h>

const int LED_PIN = 4;
const int BUTTON_PIN = 14;

unsigned long lastBlink = 0, lastSample = 0, lastReport = 0;
int presses = 0;
bool ledOn = false, lastButton = true;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Serial.begin(115200);
}

void loop() {
  unsigned long now = millis();
  if (now - lastSample >= 5) {            // every 5 ms: sample the button
    lastSample = now;
    bool b = digitalRead(BUTTON_PIN);
    if (lastButton && !b) presses++;      // falling edge (debounce as in Chapter 6)
    lastButton = b;
  }
  if (now - lastBlink >= 500) {           // every 500 ms: heartbeat LED
    lastBlink = now;
    ledOn = !ledOn;
    digitalWrite(LED_PIN, ledOn);
  }
  if (now - lastReport >= 1000) {         // every second: report
    lastReport = now;
    Serial.printf("presses: %d\n", presses);
  }
}
