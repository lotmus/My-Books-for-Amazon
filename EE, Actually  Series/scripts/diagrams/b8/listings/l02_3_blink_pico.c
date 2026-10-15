// Blink the on-board LED of a Raspberry Pi Pico (Pico SDK).
// GPIO 25 is the LED on the original Pico; the Pico W routes it through the radio chip.
#include <stdio.h>
#include "pico/stdlib.h"

#define LED_PIN 25

int main(void)
{
    stdio_init_all();               // printf over USB serial
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
    unsigned n = 0;
    while (true) {
        gpio_put(LED_PIN, 1);
        sleep_ms(500);
        gpio_put(LED_PIN, 0);
        sleep_ms(500);
        printf("blink %u\n", ++n);
    }
}
