// STM32 HAL: an independent watchdog of about 1 s, fed only when every task has reported in.
#include "stm32f4xx_hal.h"

IWDG_HandleTypeDef hiwdg;
static volatile uint32_t alive_flags;          // one bit per task
#define ALL_TASKS 0x07u                         // three tasks must check in

void watchdog_init(void)
{
    hiwdg.Instance = IWDG;
    hiwdg.Init.Prescaler = IWDG_PRESCALER_32;   // LSI 32 kHz / 32 = 1 kHz
    hiwdg.Init.Reload = 999;                    // (999 + 1) / 1 kHz = 1.0 s
    HAL_IWDG_Init(&hiwdg);                      // starts at once; cannot be stopped
}

void task_alive(uint32_t bit) { __disable_irq(); alive_flags |= bit; __enable_irq(); }

void watchdog_service(void)                     // call from the lowest-priority loop, every ~250 ms
{
    if ((alive_flags & ALL_TASKS) == ALL_TASKS) {
        alive_flags = 0;
        HAL_IWDG_Refresh(&hiwdg);
    }                                           // otherwise: let the watchdog reset the chip
}
