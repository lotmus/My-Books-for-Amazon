/* Syntax-check stub for the Raspberry Pi Pico SDK. */
#pragma once
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#define PICO_DEFAULT_LED_PIN 25
#define GPIO_OUT 1
#define GPIO_IN 0
void stdio_init_all(void); void gpio_init(unsigned); void gpio_set_dir(unsigned, bool); void gpio_put(unsigned, bool); void sleep_ms(uint32_t);
