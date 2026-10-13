// Syntax-check stub for the Adafruit BME280 Arduino library.
#pragma once
#include "Arduino.h"
#include "Wire.h"
class Adafruit_BME280 {
public:
    enum sensor_sampling { SAMPLING_NONE, SAMPLING_X1, SAMPLING_X2, SAMPLING_X4, SAMPLING_X8, SAMPLING_X16 };
    enum sensor_mode { MODE_SLEEP = 0, MODE_FORCED = 1, MODE_NORMAL = 3 };
    enum sensor_filter { FILTER_OFF, FILTER_X2, FILTER_X4, FILTER_X8, FILTER_X16 };
    enum standby_duration { STANDBY_MS_0_5, STANDBY_MS_1000 = 5 };
    bool begin(uint8_t addr = 0x77, TwoWire *theWire = &Wire);
    void setSampling(sensor_mode mode = MODE_NORMAL, sensor_sampling tempSampling = SAMPLING_X16,
                     sensor_sampling pressSampling = SAMPLING_X16, sensor_sampling humSampling = SAMPLING_X16,
                     sensor_filter filter = FILTER_OFF, standby_duration duration = STANDBY_MS_0_5);
    bool takeForcedMeasurement(); float readTemperature(); float readPressure(); float readHumidity();
};
