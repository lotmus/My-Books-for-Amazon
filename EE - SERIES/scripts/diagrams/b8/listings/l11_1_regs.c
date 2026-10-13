// Register-level blink on an STM32F411 Nucleo (LED LD2 on PA5), no HAL.
// Addresses from the STM32F411 reference manual (RM0383).
#include <stddef.h>
#include <stdint.h>

typedef struct {
    volatile uint32_t MODER, OTYPER, OSPEEDR, PUPDR, IDR, ODR, BSRR, LCKR, AFR[2];
} gpio_regs_t;
_Static_assert(offsetof(gpio_regs_t, BSRR) == 0x18, "BSRR must be at offset 0x18");

#define RCC_AHB1ENR (*(volatile uint32_t *)0x40023830u)
#define GPIOA       ((gpio_regs_t *)0x40020000u)
#define LED_PIN     5u

static void delay(volatile uint32_t n) { while (n--) { } }

int main(void)
{
    RCC_AHB1ENR |= 1u << 0;                                // clock the GPIOA block first
    GPIOA->MODER = (GPIOA->MODER & ~(3u << (LED_PIN * 2))) // 2 mode bits per pin
                 | (1u << (LED_PIN * 2));                  // 01 = general-purpose output
    for (;;) {
        GPIOA->BSRR = 1u << LED_PIN;                       // set PA5: one write, no read
        delay(400000);
        GPIOA->BSRR = 1u << (LED_PIN + 16);                // reset PA5
        delay(400000);
    }
}
