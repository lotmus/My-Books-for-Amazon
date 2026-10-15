// ESP32-S3 sensor node: wake every 10 minutes or on PIR motion, do the work, sleep.
// RTC_DATA_ATTR variables survive deep sleep; everything else restarts from scratch.
#include <stdint.h>
#include "esp_attr.h"                  // RTC_DATA_ATTR
#include "esp_sleep.h"
#include "esp_log.h"
#include "driver/gpio.h"

#define PIR_GPIO     GPIO_NUM_5            // an RTC-capable pin (GPIO 0..21 on the S3)
#define INTERVAL_US  (10ULL * 60 * 1000000)

static const char *TAG = "node";
RTC_DATA_ATTR static uint32_t boots;
RTC_DATA_ATTR static uint32_t motion_events;

void app_main(void)
{
    boots++;
    esp_sleep_wakeup_cause_t cause = esp_sleep_get_wakeup_cause();
    if (cause == ESP_SLEEP_WAKEUP_EXT0) motion_events++;
    ESP_LOGI(TAG, "boot %lu, cause %d, motion %lu", (unsigned long)boots, (int)cause,
             (unsigned long)motion_events);

    // ... read the BME280, send one MQTT or LoRa message (Chapters 17 and 18) ...

    ESP_ERROR_CHECK(esp_sleep_enable_timer_wakeup(INTERVAL_US));
    ESP_ERROR_CHECK(esp_sleep_enable_ext0_wakeup(PIR_GPIO, 1));   // wake on PIR high
    ESP_LOGI(TAG, "sleeping");
    esp_deep_sleep_start();                                       // does not return
}
