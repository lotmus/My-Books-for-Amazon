// Syntax-check stub for RadioLib 6.x/7.x (SX1276 subset).
#pragma once
#include "Arduino.h"
#define RADIOLIB_ERR_NONE 0
#define RADIOLIB_SX127X_SYNC_WORD 0x12
class Module { public: Module(uint32_t cs, uint32_t irq, uint32_t rst, uint32_t gpio); };
class SX1276 {
public:
    SX1276(Module *mod);
    int16_t begin(float freq = 434.0, float bw = 125.0, uint8_t sf = 9, uint8_t cr = 7,
                  uint8_t syncWord = RADIOLIB_SX127X_SYNC_WORD, int8_t power = 10, uint16_t preambleLength = 8, uint8_t gain = 0);
    int16_t transmit(uint8_t *data, size_t len, uint8_t addr = 0);
};
