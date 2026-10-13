// ESP32-S3 one-shot ADC read with the chip's calibration (ESP-IDF 5.x).
// GPIO 4 is ADC1 channel 3 on the ESP32-S3.
#include <stdbool.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_adc/adc_oneshot.h"
#include "esp_adc/adc_cali.h"
#include "esp_adc/adc_cali_scheme.h"
#include "esp_log.h"

static const char *TAG = "adc";

void app_main(void)
{
    adc_oneshot_unit_handle_t adc;
    const adc_oneshot_unit_init_cfg_t ucfg = { .unit_id = ADC_UNIT_1 };
    ESP_ERROR_CHECK(adc_oneshot_new_unit(&ucfg, &adc));
    const adc_oneshot_chan_cfg_t ccfg = { .atten = ADC_ATTEN_DB_12, .bitwidth = ADC_BITWIDTH_12 };
    ESP_ERROR_CHECK(adc_oneshot_config_channel(adc, ADC_CHANNEL_3, &ccfg));

    adc_cali_handle_t cali;
    const adc_cali_curve_fitting_config_t kcfg = {
        .unit_id = ADC_UNIT_1, .chan = ADC_CHANNEL_3,
        .atten = ADC_ATTEN_DB_12, .bitwidth = ADC_BITWIDTH_12,
    };
    ESP_ERROR_CHECK(adc_cali_create_scheme_curve_fitting(&kcfg, &cali));

    while (true) {
        int raw = 0, mv = 0, sum_mv = 0;
        for (int i = 0; i < 16; i++) {
            ESP_ERROR_CHECK(adc_oneshot_read(adc, ADC_CHANNEL_3, &raw));
            ESP_ERROR_CHECK(adc_cali_raw_to_voltage(cali, raw, &mv));
            sum_mv += mv;
        }
        ESP_LOGI(TAG, "pin %d mV, cell %d mV", sum_mv / 16, 2 * sum_mv / 16);
        vTaskDelay(pdMS_TO_TICKS(5000));
    }
}
