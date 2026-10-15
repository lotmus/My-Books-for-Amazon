// Servo on GPIO 15 of an ESP32-S3 with the LEDC PWM peripheral (ESP-IDF 5.x).
// 50 Hz, 14-bit duty: one step = 20 ms / 16384 = 1.22 us.
#include <stdint.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/ledc.h"

#define SERVO_GPIO   15
#define PERIOD_US    20000u
#define DUTY_BITS    LEDC_TIMER_14_BIT
#define DUTY_MAX     (1u << 14)
#define PULSE_MIN_US 1000u      // 0 degrees (check your servo's data sheet)
#define PULSE_MAX_US 2000u      // 180 degrees

static uint32_t angle_to_duty(float deg)
{
    if (deg < 0.0f)   deg = 0.0f;           // clamp: never drive past the end stops
    if (deg > 180.0f) deg = 180.0f;
    float us = PULSE_MIN_US + (PULSE_MAX_US - PULSE_MIN_US) * deg / 180.0f;
    return (uint32_t)(us * DUTY_MAX / PERIOD_US + 0.5f);   // round to nearest step
}

void app_main(void)
{
    const ledc_timer_config_t tcfg = {
        .speed_mode = LEDC_LOW_SPEED_MODE, .duty_resolution = DUTY_BITS,
        .timer_num = LEDC_TIMER_0, .freq_hz = 50, .clk_cfg = LEDC_AUTO_CLK,
    };
    ESP_ERROR_CHECK(ledc_timer_config(&tcfg));
    const ledc_channel_config_t ccfg = {
        .gpio_num = SERVO_GPIO, .speed_mode = LEDC_LOW_SPEED_MODE,
        .channel = LEDC_CHANNEL_0, .intr_type = LEDC_INTR_DISABLE,
        .timer_sel = LEDC_TIMER_0, .duty = angle_to_duty(90.0f), .hpoint = 0,
    };
    ESP_ERROR_CHECK(ledc_channel_config(&ccfg));
    for (;;) {
        for (int deg = 0; deg <= 180; deg += 45) {
            ESP_ERROR_CHECK(ledc_set_duty(LEDC_LOW_SPEED_MODE, LEDC_CHANNEL_0, angle_to_duty((float)deg)));
            ESP_ERROR_CHECK(ledc_update_duty(LEDC_LOW_SPEED_MODE, LEDC_CHANNEL_0));
            vTaskDelay(pdMS_TO_TICKS(1000));
        }
    }
}
