// Two FreeRTOS tasks and a queue on the ESP32-S3 (ESP-IDF 5.x): the sensor task
// produces readings every 100 ms, the display task consumes them.
#include <stdint.h>
#include "freertos/FreeRTOS.h"
#include "freertos/queue.h"
#include "freertos/task.h"
#include "esp_log.h"

typedef struct { int32_t t_x100; uint32_t seq; } reading_t;

static const char *TAG = "rtos";
static QueueHandle_t q;

static void sensor_task(void *arg)
{
    TickType_t next = xTaskGetTickCount();
    uint32_t seq = 0;
    for (;;) {
        reading_t r = { .t_x100 = 2341, .seq = seq++ };   // stand-in for the BME280 read
        if (xQueueSend(q, &r, 0) != pdTRUE)               // never block the producer
            ESP_LOGW(TAG, "queue full, reading %lu dropped", (unsigned long)r.seq);
        vTaskDelayUntil(&next, pdMS_TO_TICKS(100));       // fixed rate, no drift
    }
}

static void display_task(void *arg)
{
    reading_t r;
    for (;;) {
        if (xQueueReceive(q, &r, pdMS_TO_TICKS(1000)) != pdTRUE) {
            ESP_LOGW(TAG, "no reading for 1 s");            // spec: detect a dead sensor task
            continue;
        }
        ESP_LOGI(TAG, "#%lu  %ld.%02ld C", (unsigned long)r.seq,
                 (long)(r.t_x100 / 100), (long)(r.t_x100 % 100));
        if (r.seq % 50 == 0)                               // stack check every 5 s
            ESP_LOGI(TAG, "display stack free: %u bytes",
                     (unsigned)uxTaskGetStackHighWaterMark(NULL));
    }
}

void app_main(void)
{
    q = xQueueCreate(16, sizeof(reading_t));
    // ESP-IDF stack sizes are in bytes; higher number = higher priority
    xTaskCreate(sensor_task, "sensor", 3072, NULL, 6, NULL);
    xTaskCreate(display_task, "display", 4096, NULL, 4, NULL);
}
