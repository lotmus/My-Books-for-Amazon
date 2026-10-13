// Blink an external LED on GPIO 4 of an ESP32-S3 (ESP-IDF 5.x).
// Wire: GPIO 4 -> 330 ohm -> LED anode, LED cathode -> GND.
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/gpio.h"

#define LED_GPIO GPIO_NUM_4

void app_main(void)
{
    gpio_reset_pin(LED_GPIO);
    gpio_set_direction(LED_GPIO, GPIO_MODE_OUTPUT);
    int level = 0;
    while (1) {
        level = !level;
        gpio_set_level(LED_GPIO, level);
        vTaskDelay(pdMS_TO_TICKS(500));   // 0.5 s on, 0.5 s off
    }
}
