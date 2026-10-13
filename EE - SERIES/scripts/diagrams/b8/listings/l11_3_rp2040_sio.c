// RP2040: the SDK call and the register write it becomes (Pico SDK).
// sio_hw points at the single-cycle I/O block at 0xd0000000.
#include "pico/stdlib.h"
#include "hardware/structs/sio.h"

#define PIN_A 2
#define PIN_B 3

int main(void)
{
    gpio_init(PIN_A);
    gpio_init(PIN_B);
    gpio_set_dir(PIN_A, GPIO_OUT);
    gpio_set_dir(PIN_B, GPIO_OUT);
    const uint32_t mask = (1u << PIN_A) | (1u << PIN_B);
    for (;;) {
        gpio_put(PIN_A, 1);            // SDK: inline function writing the SIO set register
        sio_hw->gpio_clr = 1u << PIN_A;// direct: GPIO_OUT_CLR at offset 0x018
        sio_hw->gpio_togl = mask;      // both pins flip in the same cycle
    }
}
