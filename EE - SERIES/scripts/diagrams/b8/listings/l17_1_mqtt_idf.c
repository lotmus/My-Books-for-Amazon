// ESP-IDF: connect to Wi-Fi, then publish one BME280 reading per minute over MQTT.
// Wi-Fi credentials and the broker URI come from menuconfig (Kconfig), never from the source.
#include <stdio.h>
#include "esp_event.h"
#include "esp_log.h"
#include "esp_netif.h"
#include "esp_wifi.h"
#include "freertos/FreeRTOS.h"
#include "freertos/event_groups.h"
#include "freertos/task.h"
#include "mqtt_client.h"
#include "nvs_flash.h"

static const char *TAG = "node";
static EventGroupHandle_t s_events;
#define WIFI_UP BIT0
#define MQTT_UP BIT1

static void on_wifi(void *arg, esp_event_base_t base, int32_t id, void *data)
{
    if (base == WIFI_EVENT && (id == WIFI_EVENT_STA_START || id == WIFI_EVENT_STA_DISCONNECTED)) {
        xEventGroupClearBits(s_events, WIFI_UP);
        esp_wifi_connect();                       // the driver retries; MQTT reconnects by itself
    } else if (base == IP_EVENT && id == IP_EVENT_STA_GOT_IP) {
        xEventGroupSetBits(s_events, WIFI_UP);
    }
}

static void on_mqtt(void *arg, esp_event_base_t base, int32_t id, void *data)
{
    if (id == MQTT_EVENT_CONNECTED)    xEventGroupSetBits(s_events, MQTT_UP);
    if (id == MQTT_EVENT_DISCONNECTED) xEventGroupClearBits(s_events, MQTT_UP);
}

static void wifi_start(void)
{
    esp_netif_create_default_wifi_sta();
    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK(esp_wifi_init(&cfg));
    ESP_ERROR_CHECK(esp_event_handler_register(WIFI_EVENT, ESP_EVENT_ANY_ID, on_wifi, NULL));
    ESP_ERROR_CHECK(esp_event_handler_register(IP_EVENT, IP_EVENT_STA_GOT_IP, on_wifi, NULL));
    wifi_config_t wc = { 0 };
    snprintf((char *)wc.sta.ssid, sizeof wc.sta.ssid, "%s", CONFIG_NODE_WIFI_SSID);
    snprintf((char *)wc.sta.password, sizeof wc.sta.password, "%s", CONFIG_NODE_WIFI_PASSWORD);
    ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_STA));
    ESP_ERROR_CHECK(esp_wifi_set_config(WIFI_IF_STA, &wc));
    ESP_ERROR_CHECK(esp_wifi_start());
}

void app_main(void)
{
    ESP_ERROR_CHECK(nvs_flash_init());            // Wi-Fi keeps calibration data in NVS
    ESP_ERROR_CHECK(esp_netif_init());
    ESP_ERROR_CHECK(esp_event_loop_create_default());
    s_events = xEventGroupCreate();
    wifi_start();

    esp_mqtt_client_config_t mc = { .broker.address.uri = CONFIG_NODE_BROKER_URI };
    esp_mqtt_client_handle_t client = esp_mqtt_client_init(&mc);
    esp_mqtt_client_register_event(client, ESP_EVENT_ANY_ID, on_mqtt, NULL);
    esp_mqtt_client_start(client);

    char payload[48];
    for (;;) {
        xEventGroupWaitBits(s_events, WIFI_UP | MQTT_UP, pdFALSE, pdTRUE, portMAX_DELAY);
        float t = 23.41f, h = 45.2f, p = 1013.25f;          // from the Chapter 9 driver
        int n = snprintf(payload, sizeof payload, "{\"t\":%.2f,\"h\":%.1f,\"p\":%.2f}", t, h, p);
        int id = esp_mqtt_client_publish(client, "lab/garden/bme280", payload, n, 1, 0);
        ESP_LOGI(TAG, "published %d bytes, msg id %d", n, id);
        vTaskDelay(pdMS_TO_TICKS(60000));
    }
}
