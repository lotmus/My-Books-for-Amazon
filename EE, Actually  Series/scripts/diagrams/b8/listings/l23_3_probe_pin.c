// Measure an ISR's duration with a spare GPIO and a scope or logic analyzer (ESP-IDF, ESP32-S3).
// Writing the set and clear registers directly costs a few CPU cycles, far less than gpio_set_level().
#include "driver/gpio.h"
#include "esp_attr.h"
#include "soc/gpio_reg.h"
#include "soc/soc.h"

#define PROBE_PIN 21                                   // a free pin from the spec's pin table
#define PROBE_HIGH() REG_WRITE(GPIO_OUT_W1TS_REG, 1u << PROBE_PIN)
#define PROBE_LOW()  REG_WRITE(GPIO_OUT_W1TC_REG, 1u << PROBE_PIN)

void probe_init(void)
{
    gpio_config_t io = {
        .pin_bit_mask = 1ULL << PROBE_PIN,
        .mode = GPIO_MODE_OUTPUT,
    };
    gpio_config(&io);
    PROBE_LOW();
}

void IRAM_ATTR sensor_isr(void *arg)
{
    PROBE_HIGH();                                      // pulse width on the scope = ISR time
    /* ... the ISR's real work: read a register, give a semaphore ... */
    PROBE_LOW();
}
