// Syntax-check stub for the Arduino Wire library (arduino-esp32 3.x).
#pragma once
#include "Arduino.h"
class TwoWire {
public:
    bool begin(int sda = -1, int scl = -1, uint32_t frequency = 0);
    void beginTransmission(uint8_t); size_t write(uint8_t); uint8_t endTransmission(bool sendStop = true);
    uint8_t requestFrom(uint8_t, uint8_t); int read();
};
extern TwoWire Wire;
