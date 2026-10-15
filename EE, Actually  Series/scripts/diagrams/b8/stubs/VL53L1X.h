// Syntax-check stub for the Pololu VL53L1X Arduino library.
#pragma once
#include "Arduino.h"
class VL53L1X {
public:
    enum DistanceMode { Short, Medium, Long, Unknown };
    bool init(bool io_2v8 = true); void setTimeout(uint16_t); bool setDistanceMode(DistanceMode);
    bool setMeasurementTimingBudget(uint32_t budget_us); void startContinuous(uint32_t period_ms);
    uint16_t read(bool blocking = true); bool timeoutOccurred();
};
