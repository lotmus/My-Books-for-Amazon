/* Syntax-check stub for the Pico SDK SIO block. */
#pragma once
#include <stdint.h>
typedef struct { uint32_t cpuid, gpio_in, gpio_hi_in, _pad0, gpio_out, gpio_set, gpio_clr, gpio_togl, gpio_oe, gpio_oe_set, gpio_oe_clr, gpio_oe_togl; } sio_hw_t;
#define sio_hw ((volatile sio_hw_t *)0xd0000000u)
