// ESP-IDF: download a signed image over HTTPS into the other OTA slot, and confirm or roll back
// after a self-test on first boot. Needs CONFIG_BOOTLOADER_APP_ROLLBACK_ENABLE=y.
#include <stdbool.h>
#include "esp_crt_bundle.h"
#include "esp_https_ota.h"
#include "esp_log.h"
#include "esp_ota_ops.h"
#include "esp_system.h"

static const char *TAG = "ota";

extern bool self_test(void);        // sensor answers, Wi-Fi connects, broker reachable

void ota_confirm_or_rollback(void)  // call early in app_main
{
    const esp_partition_t *running = esp_ota_get_running_partition();
    esp_ota_img_states_t state;
    if (esp_ota_get_state_partition(running, &state) == ESP_OK &&
        state == ESP_OTA_IMG_PENDING_VERIFY) {
        if (self_test()) {
            ESP_LOGI(TAG, "new image passed self-test, keeping it");
            esp_ota_mark_app_valid_cancel_rollback();
        } else {
            ESP_LOGE(TAG, "self-test failed, rolling back");
            esp_ota_mark_app_invalid_rollback_and_reboot();
        }
    }
}

esp_err_t ota_update(const char *url)
{
    esp_http_client_config_t http = {
        .url = url,
        .crt_bundle_attach = esp_crt_bundle_attach,   // verify the server's TLS certificate
        .timeout_ms = 10000,
    };
    esp_https_ota_config_t cfg = { .http_config = &http };
    ESP_LOGI(TAG, "downloading %s", url);
    esp_err_t err = esp_https_ota(&cfg);              // writes the inactive slot, sets it to boot next
    if (err == ESP_OK) {
        ESP_LOGI(TAG, "image written, restarting");
        esp_restart();
    }
    ESP_LOGE(TAG, "OTA failed: %s", esp_err_to_name(err));
    return err;                                       // the running image is untouched
}
