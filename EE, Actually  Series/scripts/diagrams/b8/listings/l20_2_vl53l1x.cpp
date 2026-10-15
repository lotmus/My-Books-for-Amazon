// Arduino on the ESP32-S3: identify a VL53L1X by its 16-bit model-ID register,
// then range continuously with the Pololu VL53L1X library.
#include <Arduino.h>
#include <Wire.h>
#include <VL53L1X.h>

const uint8_t ADDR = 0x29;                 // 7-bit address (0x52 in 8-bit notation)
VL53L1X tof;

static int read_reg8(uint16_t reg)         // VL53L1X registers have 16-bit addresses
{
    Wire.beginTransmission(ADDR);
    Wire.write(reg >> 8);
    Wire.write(reg & 0xFF);
    if (Wire.endTransmission(false) != 0) return -1;   // repeated start
    if (Wire.requestFrom(ADDR, (uint8_t)1) != 1) return -1;
    return Wire.read();
}

void setup()
{
    Serial.begin(115200);
    Wire.begin(1, 2, 400000);              // SDA 1, SCL 2: the camera board uses 8 and 9
    int id = read_reg8(0x010F), type = read_reg8(0x0110);
    Serial.printf("model id 0x%02X (expect 0xEA), module type 0x%02X (expect 0xCC)\n", id, type);
    if (id != 0xEA || !tof.init()) {
        Serial.println("VL53L1X not found");
        while (true) delay(1000);
    }
    tof.setTimeout(500);
    tof.setDistanceMode(VL53L1X::Long);
    tof.setMeasurementTimingBudget(50000); // 50 ms, in microseconds
    tof.startContinuous(50);               // one measurement every 50 ms, 20 Hz
}

void loop()
{
    uint16_t mm = tof.read();              // waits for the next result
    if (tof.timeoutOccurred()) Serial.println("timeout");
    else Serial.printf("%u mm\n", mm);
}
