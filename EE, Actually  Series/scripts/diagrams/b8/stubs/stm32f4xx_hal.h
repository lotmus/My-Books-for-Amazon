/* Syntax-check stub for the STM32F4 HAL. */
#pragma once
#include <stdint.h>
typedef struct { volatile uint32_t MODER, OTYPER, OSPEEDR, PUPDR, IDR, ODR, BSRR, LCKR, AFR[2]; } GPIO_TypeDef;
typedef struct { volatile uint32_t KR, PR, RLR, SR; } IWDG_TypeDef;
#define GPIOA ((GPIO_TypeDef *)0x40020000u)
#define IWDG ((IWDG_TypeDef *)0x40003000u)
#define GPIO_PIN_5 ((uint16_t)0x0020)
#define GPIO_MODE_OUTPUT_PP 0x01u
#define GPIO_NOPULL 0x00u
#define GPIO_SPEED_FREQ_LOW 0x00u
typedef struct { uint32_t Pin, Mode, Pull, Speed, Alternate; } GPIO_InitTypeDef;
typedef enum { HAL_OK, HAL_ERROR } HAL_StatusTypeDef;
#define IWDG_PRESCALER_32 0x03u
typedef struct { uint32_t Prescaler, Reload, Window; } IWDG_InitTypeDef;
typedef struct { IWDG_TypeDef *Instance; IWDG_InitTypeDef Init; } IWDG_HandleTypeDef;
HAL_StatusTypeDef HAL_Init(void); void HAL_Delay(uint32_t);
void HAL_GPIO_Init(GPIO_TypeDef *, GPIO_InitTypeDef *); void HAL_GPIO_TogglePin(GPIO_TypeDef *, uint16_t);
HAL_StatusTypeDef HAL_IWDG_Init(IWDG_HandleTypeDef *); HAL_StatusTypeDef HAL_IWDG_Refresh(IWDG_HandleTypeDef *);
#define __HAL_RCC_GPIOA_CLK_ENABLE() do { } while (0)
static inline void __disable_irq(void) { } static inline void __enable_irq(void) { }
