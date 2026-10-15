// Arduino + RadioLib: send the 8-byte reading on an SX1276 (RFM95W) module from the ESP32-S3.
// EU 868 MHz, SF9, BW 125 kHz, CR 4/5; use 915 MHz in the Americas.
#include <Arduino.h>
#include <RadioLib.h>

// Pins: NSS, DIO0, RESET, DIO1 (from the spec's pin table)
SX1276 radio = new Module(10, 4, 5, 6);

extern void pack_reading(uint8_t out[8]);       // Listing 18.2, called with the latest reading

const uint32_t TX_INTERVAL_MS = 60000;           // one reading per minute
const uint32_t MIN_INTERVAL_MS = 12400;          // 1 % duty cycle for 123.9 ms airtime
static_assert(TX_INTERVAL_MS >= MIN_INTERVAL_MS, "interval breaks the 1 % duty-cycle limit");
uint32_t last_tx = 0;

void setup()
{
    Serial.begin(115200);
    int state = radio.begin(868.1f, 125.0, 9, 5, RADIOLIB_SX127X_SYNC_WORD, 14, 8);
    if (state != RADIOLIB_ERR_NONE) {
        Serial.printf("radio init failed, code %d\n", state);
        while (true) delay(1000);
    }
}

void loop()
{
    if (millis() - last_tx >= TX_INTERVAL_MS) {
        uint8_t buf[8];
        pack_reading(buf);
        uint32_t t0 = millis();
        int state = radio.transmit(buf, sizeof buf);
        last_tx = millis();
        Serial.printf("tx %s, %lu ms on air\n",
                      state == RADIOLIB_ERR_NONE ? "ok" : "failed", (unsigned long)(last_tx - t0));
    }
}
