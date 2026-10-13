// BME280 over I2C on the ESP32-S3 with the ESP-IDF 5.x i2c_master driver.
// Spec: SDA GPIO 8, SCL GPIO 9, external 4.7k pull-ups, 400 kHz, address 0x76,
// every transfer times out after 50 ms.
#include <stdint.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/i2c_master.h"
#include "esp_log.h"

#define BME280_ADDR   0x76
#define REG_CHIP_ID   0xD0
#define REG_CTRL_HUM  0xF2
#define REG_CTRL_MEAS 0xF4
#define REG_DATA      0xF7      // press[3], temp[3], hum[2]
#define I2C_TIMEOUT_MS 50

static const char *TAG = "bme280";

static esp_err_t write_reg(i2c_master_dev_handle_t dev, uint8_t reg, uint8_t val)
{
    const uint8_t buf[2] = { reg, val };
    return i2c_master_transmit(dev, buf, sizeof buf, I2C_TIMEOUT_MS);
}

void app_main(void)
{
    const i2c_master_bus_config_t bus_cfg = {
        .i2c_port = I2C_NUM_0, .sda_io_num = GPIO_NUM_8, .scl_io_num = GPIO_NUM_9,
        .clk_source = I2C_CLK_SRC_DEFAULT, .glitch_ignore_cnt = 7,
        .flags.enable_internal_pullup = false,           // external 4.7k fitted
    };
    i2c_master_bus_handle_t bus;
    ESP_ERROR_CHECK(i2c_new_master_bus(&bus_cfg, &bus));
    const i2c_device_config_t dev_cfg = {
        .dev_addr_length = I2C_ADDR_BIT_LEN_7, .device_address = BME280_ADDR,
        .scl_speed_hz = 400000,
    };
    i2c_master_dev_handle_t dev;
    ESP_ERROR_CHECK(i2c_master_bus_add_device(bus, &dev_cfg, &dev));

    uint8_t reg = REG_CHIP_ID, id = 0;
    esp_err_t err = i2c_master_transmit_receive(dev, &reg, 1, &id, 1, I2C_TIMEOUT_MS);
    if (err != ESP_OK || id != 0x60) {
        ESP_LOGE(TAG, "no BME280 (err %d, id 0x%02x)", err, id);
        return;                                          // spec: report, do not hang
    }
    ESP_ERROR_CHECK(write_reg(dev, REG_CTRL_HUM, 0x01));  // humidity x1 first
    ESP_ERROR_CHECK(write_reg(dev, REG_CTRL_MEAS, 0x27)); // T x1, P x1, normal mode

    for (;;) {
        uint8_t d[8];
        reg = REG_DATA;
        if (i2c_master_transmit_receive(dev, &reg, 1, d, sizeof d, I2C_TIMEOUT_MS) == ESP_OK) {
            int32_t adc_T = ((int32_t)d[3] << 12) | ((int32_t)d[4] << 4) | (d[5] >> 4);
            ESP_LOGI(TAG, "raw T %ld", (long)adc_T);    // compensate with Listing 9.3
        } else {
            ESP_LOGW(TAG, "read failed");
        }
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}
