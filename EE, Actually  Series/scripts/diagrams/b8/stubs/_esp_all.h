/* Syntax-check stubs for ESP-IDF v5.x and FreeRTOS. Declarations follow the public IDF API;
   they exist only so gcc -fsyntax-only can check the book's listings. Not for building firmware. */
#pragma once
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdio.h>
typedef int esp_err_t;
#define ESP_OK 0
#define ESP_FAIL -1
const char *esp_err_to_name(esp_err_t);
#define ESP_ERROR_CHECK(x) do { esp_err_t e_ = (x); (void)e_; } while (0)
#define BIT0 0x01
#define BIT1 0x02
#define IRAM_ATTR
#define RTC_DATA_ATTR
/* log */
#define ESP_LOGI(tag, fmt, ...) printf(fmt, ##__VA_ARGS__)
#define ESP_LOGW(tag, fmt, ...) printf(fmt, ##__VA_ARGS__)
#define ESP_LOGE(tag, fmt, ...) printf(fmt, ##__VA_ARGS__)
/* FreeRTOS */
typedef uint32_t TickType_t; typedef int BaseType_t; typedef unsigned int UBaseType_t;
typedef void *QueueHandle_t; typedef void *TaskHandle_t; typedef void *EventGroupHandle_t; typedef uint32_t EventBits_t;
#define pdTRUE 1
#define pdFALSE 0
#define pdPASS 1
#define portMAX_DELAY 0xffffffffu
#define portTICK_PERIOD_MS 10
#define pdMS_TO_TICKS(ms) ((TickType_t)((ms) / portTICK_PERIOD_MS))
typedef void (*TaskFunction_t)(void *);
BaseType_t xTaskCreate(TaskFunction_t, const char *, uint32_t, void *, UBaseType_t, TaskHandle_t *);
BaseType_t xTaskCreatePinnedToCore(TaskFunction_t, const char *, uint32_t, void *, UBaseType_t, TaskHandle_t *, BaseType_t);
void vTaskDelay(TickType_t); void vTaskDelayUntil(TickType_t *, TickType_t); TickType_t xTaskGetTickCount(void);
UBaseType_t uxTaskGetStackHighWaterMark(TaskHandle_t); void vTaskDelete(TaskHandle_t);
QueueHandle_t xQueueCreate(UBaseType_t, UBaseType_t);
BaseType_t xQueueSend(QueueHandle_t, const void *, TickType_t); BaseType_t xQueueReceive(QueueHandle_t, void *, TickType_t);
BaseType_t xQueueSendFromISR(QueueHandle_t, const void *, BaseType_t *);
#define portYIELD_FROM_ISR(...) ((void)0)
EventGroupHandle_t xEventGroupCreate(void);
EventBits_t xEventGroupSetBits(EventGroupHandle_t, EventBits_t); EventBits_t xEventGroupClearBits(EventGroupHandle_t, EventBits_t);
EventBits_t xEventGroupWaitBits(EventGroupHandle_t, EventBits_t, BaseType_t, BaseType_t, TickType_t);
/* gpio */
typedef enum { GPIO_NUM_NC = -1, GPIO_NUM_0 = 0, GPIO_NUM_1, GPIO_NUM_2, GPIO_NUM_3, GPIO_NUM_4, GPIO_NUM_5, GPIO_NUM_6, GPIO_NUM_7,
    GPIO_NUM_8, GPIO_NUM_9, GPIO_NUM_10, GPIO_NUM_11, GPIO_NUM_12, GPIO_NUM_13, GPIO_NUM_14, GPIO_NUM_15, GPIO_NUM_16, GPIO_NUM_17,
    GPIO_NUM_18, GPIO_NUM_19, GPIO_NUM_20, GPIO_NUM_21, GPIO_NUM_38 = 38, GPIO_NUM_47 = 47, GPIO_NUM_48 = 48 } gpio_num_t;
typedef enum { GPIO_MODE_DISABLE, GPIO_MODE_INPUT, GPIO_MODE_OUTPUT, GPIO_MODE_INPUT_OUTPUT } gpio_mode_t;
typedef enum { GPIO_PULLUP_DISABLE, GPIO_PULLUP_ENABLE } gpio_pullup_t;
typedef enum { GPIO_PULLDOWN_DISABLE, GPIO_PULLDOWN_ENABLE } gpio_pulldown_t;
typedef enum { GPIO_INTR_DISABLE, GPIO_INTR_POSEDGE, GPIO_INTR_NEGEDGE, GPIO_INTR_ANYEDGE } gpio_int_type_t;
typedef struct { uint64_t pin_bit_mask; gpio_mode_t mode; gpio_pullup_t pull_up_en; gpio_pulldown_t pull_down_en; gpio_int_type_t intr_type; } gpio_config_t;
esp_err_t gpio_config(const gpio_config_t *); esp_err_t gpio_reset_pin(gpio_num_t);
esp_err_t gpio_set_direction(gpio_num_t, gpio_mode_t); esp_err_t gpio_set_level(gpio_num_t, uint32_t); int gpio_get_level(gpio_num_t);
typedef void (*gpio_isr_t)(void *);
esp_err_t gpio_install_isr_service(int); esp_err_t gpio_isr_handler_add(gpio_num_t, gpio_isr_t, void *);
#define DR_REG_GPIO_BASE 0x60004000
#define GPIO_OUT_W1TS_REG (DR_REG_GPIO_BASE + 0x8)
#define GPIO_OUT_W1TC_REG (DR_REG_GPIO_BASE + 0xC)
#define REG_WRITE(r, v) (*(volatile uint32_t *)(r) = (v))
/* timer, sleep, system */
int64_t esp_timer_get_time(void);
typedef enum { ESP_SLEEP_WAKEUP_UNDEFINED, ESP_SLEEP_WAKEUP_ALL, ESP_SLEEP_WAKEUP_EXT0, ESP_SLEEP_WAKEUP_EXT1, ESP_SLEEP_WAKEUP_TIMER } esp_sleep_wakeup_cause_t;
esp_err_t esp_sleep_enable_timer_wakeup(uint64_t); esp_err_t esp_sleep_enable_ext0_wakeup(gpio_num_t, int);
esp_sleep_wakeup_cause_t esp_sleep_get_wakeup_cause(void); void esp_deep_sleep_start(void);
void esp_restart(void);
/* ledc */
typedef enum { LEDC_LOW_SPEED_MODE } ledc_mode_t;
typedef enum { LEDC_TIMER_0, LEDC_TIMER_1 } ledc_timer_t;
typedef enum { LEDC_CHANNEL_0, LEDC_CHANNEL_1 } ledc_channel_t;
typedef enum { LEDC_TIMER_10_BIT = 10, LEDC_TIMER_13_BIT = 13, LEDC_TIMER_14_BIT = 14 } ledc_timer_bit_t;
typedef enum { LEDC_AUTO_CLK } ledc_clk_cfg_t;
typedef enum { LEDC_INTR_DISABLE } ledc_intr_type_t;
typedef struct { ledc_mode_t speed_mode; ledc_timer_bit_t duty_resolution; ledc_timer_t timer_num; uint32_t freq_hz; ledc_clk_cfg_t clk_cfg; } ledc_timer_config_t;
typedef struct { int gpio_num; ledc_mode_t speed_mode; ledc_channel_t channel; ledc_intr_type_t intr_type; ledc_timer_t timer_sel; uint32_t duty; int hpoint; } ledc_channel_config_t;
esp_err_t ledc_timer_config(const ledc_timer_config_t *); esp_err_t ledc_channel_config(const ledc_channel_config_t *);
esp_err_t ledc_set_duty(ledc_mode_t, ledc_channel_t, uint32_t); esp_err_t ledc_update_duty(ledc_mode_t, ledc_channel_t);
/* adc */
typedef enum { ADC_UNIT_1, ADC_UNIT_2 } adc_unit_t;
typedef enum { ADC_CHANNEL_0, ADC_CHANNEL_1, ADC_CHANNEL_2, ADC_CHANNEL_3 } adc_channel_t;
typedef enum { ADC_ATTEN_DB_0, ADC_ATTEN_DB_2_5, ADC_ATTEN_DB_6, ADC_ATTEN_DB_12 } adc_atten_t;
typedef enum { ADC_BITWIDTH_DEFAULT, ADC_BITWIDTH_12 = 12 } adc_bitwidth_t;
typedef struct adc_oneshot_unit_ctx_t *adc_oneshot_unit_handle_t;
typedef struct { adc_unit_t unit_id; int clk_src; int ulp_mode; } adc_oneshot_unit_init_cfg_t;
typedef struct { adc_atten_t atten; adc_bitwidth_t bitwidth; } adc_oneshot_chan_cfg_t;
esp_err_t adc_oneshot_new_unit(const adc_oneshot_unit_init_cfg_t *, adc_oneshot_unit_handle_t *);
esp_err_t adc_oneshot_config_channel(adc_oneshot_unit_handle_t, adc_channel_t, const adc_oneshot_chan_cfg_t *);
esp_err_t adc_oneshot_read(adc_oneshot_unit_handle_t, adc_channel_t, int *);
typedef struct adc_cali_scheme_t *adc_cali_handle_t;
typedef struct { adc_unit_t unit_id; adc_channel_t chan; adc_atten_t atten; adc_bitwidth_t bitwidth; } adc_cali_curve_fitting_config_t;
esp_err_t adc_cali_create_scheme_curve_fitting(const adc_cali_curve_fitting_config_t *, adc_cali_handle_t *);
esp_err_t adc_cali_raw_to_voltage(adc_cali_handle_t, int, int *);
/* i2c master (IDF 5.2+) */
typedef enum { I2C_NUM_0, I2C_NUM_1 } i2c_port_num_t;
typedef enum { I2C_CLK_SRC_DEFAULT } i2c_clock_source_t;
typedef enum { I2C_ADDR_BIT_LEN_7, I2C_ADDR_BIT_LEN_10 } i2c_addr_bit_len_t;
typedef struct i2c_master_bus_t *i2c_master_bus_handle_t;
typedef struct i2c_master_dev_t *i2c_master_dev_handle_t;
typedef struct { i2c_port_num_t i2c_port; gpio_num_t sda_io_num; gpio_num_t scl_io_num; i2c_clock_source_t clk_source; uint8_t glitch_ignore_cnt; int intr_priority; size_t trans_queue_depth; struct { uint32_t enable_internal_pullup: 1; } flags; } i2c_master_bus_config_t;
typedef struct { i2c_addr_bit_len_t dev_addr_length; uint16_t device_address; uint32_t scl_speed_hz; uint32_t scl_wait_us; } i2c_device_config_t;
esp_err_t i2c_new_master_bus(const i2c_master_bus_config_t *, i2c_master_bus_handle_t *);
esp_err_t i2c_master_bus_add_device(i2c_master_bus_handle_t, const i2c_device_config_t *, i2c_master_dev_handle_t *);
esp_err_t i2c_master_transmit(i2c_master_dev_handle_t, const uint8_t *, size_t, int);
esp_err_t i2c_master_transmit_receive(i2c_master_dev_handle_t, const uint8_t *, size_t, uint8_t *, size_t, int);
/* events, netif, wifi, nvs */
typedef const char *esp_event_base_t;
extern esp_event_base_t const WIFI_EVENT, IP_EVENT;
#define ESP_EVENT_ANY_ID -1
enum { WIFI_EVENT_STA_START = 2, WIFI_EVENT_STA_DISCONNECTED = 5 };
enum { IP_EVENT_STA_GOT_IP = 0 };
typedef void (*esp_event_handler_t)(void *, esp_event_base_t, int32_t, void *);
esp_err_t esp_event_loop_create_default(void);
esp_err_t esp_event_handler_register(esp_event_base_t, int32_t, esp_event_handler_t, void *);
esp_err_t esp_netif_init(void); void *esp_netif_create_default_wifi_sta(void);
typedef struct { int magic; } wifi_init_config_t;
#define WIFI_INIT_CONFIG_DEFAULT() { .magic = 0x1F2F3F4F }
typedef enum { WIFI_MODE_NULL, WIFI_MODE_STA } wifi_mode_t;
typedef enum { WIFI_IF_STA } wifi_interface_t;
typedef union { struct { uint8_t ssid[32]; uint8_t password[64]; } sta; } wifi_config_t;
esp_err_t esp_wifi_init(const wifi_init_config_t *); esp_err_t esp_wifi_set_mode(wifi_mode_t);
esp_err_t esp_wifi_set_config(wifi_interface_t, wifi_config_t *); esp_err_t esp_wifi_start(void); esp_err_t esp_wifi_connect(void);
esp_err_t nvs_flash_init(void);
/* mqtt */
typedef struct esp_mqtt_client *esp_mqtt_client_handle_t;
typedef struct { struct { struct { const char *uri; } address; } broker; } esp_mqtt_client_config_t;
enum { MQTT_EVENT_ERROR, MQTT_EVENT_CONNECTED, MQTT_EVENT_DISCONNECTED };
esp_mqtt_client_handle_t esp_mqtt_client_init(const esp_mqtt_client_config_t *);
esp_err_t esp_mqtt_client_register_event(esp_mqtt_client_handle_t, int32_t, esp_event_handler_t, void *);
esp_err_t esp_mqtt_client_start(esp_mqtt_client_handle_t);
int esp_mqtt_client_publish(esp_mqtt_client_handle_t, const char *, const char *, int, int, int);
/* ota */
typedef struct { int type; int subtype; uint32_t address; uint32_t size; char label[17]; } esp_partition_t;
typedef enum { ESP_OTA_IMG_NEW, ESP_OTA_IMG_PENDING_VERIFY, ESP_OTA_IMG_VALID, ESP_OTA_IMG_INVALID, ESP_OTA_IMG_ABORTED, ESP_OTA_IMG_UNDEFINED = -1 } esp_ota_img_states_t;
const esp_partition_t *esp_ota_get_running_partition(void);
esp_err_t esp_ota_get_state_partition(const esp_partition_t *, esp_ota_img_states_t *);
esp_err_t esp_ota_mark_app_valid_cancel_rollback(void); esp_err_t esp_ota_mark_app_invalid_rollback_and_reboot(void);
esp_err_t esp_crt_bundle_attach(void *conf);
typedef struct { const char *url; int timeout_ms; esp_err_t (*crt_bundle_attach)(void *conf); const char *cert_pem; } esp_http_client_config_t;
typedef struct { const esp_http_client_config_t *http_config; } esp_https_ota_config_t;
esp_err_t esp_https_ota(const esp_https_ota_config_t *);
/* camera (esp32-camera component) */
typedef enum { PIXFORMAT_RGB565, PIXFORMAT_YUV422, PIXFORMAT_GRAYSCALE, PIXFORMAT_JPEG } pixformat_t;
typedef enum { FRAMESIZE_96X96, FRAMESIZE_QQVGA, FRAMESIZE_QVGA = 5, FRAMESIZE_VGA = 8 } framesize_t;
typedef enum { CAMERA_GRAB_WHEN_EMPTY, CAMERA_GRAB_LATEST } camera_grab_mode_t;
typedef enum { CAMERA_FB_IN_PSRAM, CAMERA_FB_IN_DRAM } camera_fb_location_t;
typedef struct { int pin_pwdn, pin_reset, pin_xclk, pin_sccb_sda, pin_sccb_scl, pin_d7, pin_d6, pin_d5, pin_d4, pin_d3, pin_d2, pin_d1, pin_d0, pin_vsync, pin_href, pin_pclk;
    int xclk_freq_hz; ledc_timer_t ledc_timer; ledc_channel_t ledc_channel; pixformat_t pixel_format; framesize_t frame_size; int jpeg_quality; size_t fb_count;
    camera_fb_location_t fb_location; camera_grab_mode_t grab_mode; } camera_config_t;
typedef struct { uint8_t *buf; size_t len; size_t width; size_t height; pixformat_t format; } camera_fb_t;
esp_err_t esp_camera_init(const camera_config_t *); camera_fb_t *esp_camera_fb_get(void); void esp_camera_fb_return(camera_fb_t *);
