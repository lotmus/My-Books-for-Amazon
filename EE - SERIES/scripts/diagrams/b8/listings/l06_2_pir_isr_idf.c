// PIR motion sensor on GPIO 5 of an ESP32-S3 (ESP-IDF 5.x): the interrupt only
// queues an event; a task does the slow work (logging, display, camera).
#include <stdint.h>
#include "freertos/FreeRTOS.h"
#include "freertos/queue.h"
#include "freertos/task.h"
#include "driver/gpio.h"
#include "esp_log.h"
#include "esp_timer.h"

#define PIR_GPIO GPIO_NUM_5
static const char *TAG = "pir";
static QueueHandle_t pir_queue;

static void IRAM_ATTR pir_isr(void *arg)
{
    int64_t t_us = esp_timer_get_time();          // ISR-safe timestamp
    BaseType_t woken = pdFALSE;
    xQueueSendFromISR(pir_queue, &t_us, &woken);  // never block in an ISR
    if (woken) portYIELD_FROM_ISR();
}

static void pir_task(void *arg)
{
    int64_t t_us;
    for (;;) {
        if (xQueueReceive(pir_queue, &t_us, portMAX_DELAY) == pdTRUE)
            ESP_LOGI(TAG, "motion at %lld ms", (long long)(t_us / 1000));
    }
}

void app_main(void)
{
    pir_queue = xQueueCreate(8, sizeof(int64_t));
    const gpio_config_t cfg = {
        .pin_bit_mask = 1ULL << PIR_GPIO,
        .mode = GPIO_MODE_INPUT,
        .pull_up_en = GPIO_PULLUP_DISABLE,
        .pull_down_en = GPIO_PULLDOWN_ENABLE,     // PIR output idles low
        .intr_type = GPIO_INTR_POSEDGE,           // motion = rising edge
    };
    ESP_ERROR_CHECK(gpio_config(&cfg));
    ESP_ERROR_CHECK(gpio_install_isr_service(0));
    ESP_ERROR_CHECK(gpio_isr_handler_add(PIR_GPIO, pir_isr, NULL));
    xTaskCreate(pir_task, "pir", 3072, NULL, 5, NULL);
}
