// ESP-IDF + esp32-camera: OV2640 on an ESP32-S3-EYE-style board, QVGA JPEG, frame buffers in PSRAM.
#include "esp_camera.h"
#include "esp_log.h"
#include "esp_timer.h"

static const char *TAG = "cam";

esp_err_t camera_start(void)
{
    camera_config_t c = {
        .pin_pwdn = -1, .pin_reset = -1, .pin_xclk = 15,
        .pin_sccb_sda = 4, .pin_sccb_scl = 5,
        .pin_d7 = 16, .pin_d6 = 17, .pin_d5 = 18, .pin_d4 = 12,
        .pin_d3 = 10, .pin_d2 = 8, .pin_d1 = 9, .pin_d0 = 11,
        .pin_vsync = 6, .pin_href = 7, .pin_pclk = 13,
        .xclk_freq_hz = 20000000,
        .ledc_timer = LEDC_TIMER_0, .ledc_channel = LEDC_CHANNEL_0,
        .pixel_format = PIXFORMAT_JPEG,          // the sensor compresses; RGB565 would be 153 600 bytes
        .frame_size = FRAMESIZE_QVGA,            // 320 x 240
        .jpeg_quality = 12,                      // 0..63, lower is better quality
        .fb_count = 2,                           // capture the next frame while this one is used
        .fb_location = CAMERA_FB_IN_PSRAM,
        .grab_mode = CAMERA_GRAB_LATEST,
    };
    return esp_camera_init(&c);
}

void camera_measure(int frames)
{
    int64_t t0 = esp_timer_get_time();
    size_t bytes = 0;
    for (int i = 0; i < frames; i++) {
        camera_fb_t *fb = esp_camera_fb_get();
        if (!fb) { ESP_LOGE(TAG, "capture failed"); continue; }
        bytes += fb->len;                        // use fb->buf here: send, save, or analyze
        esp_camera_fb_return(fb);                // always give the buffer back
    }
    int64_t us = esp_timer_get_time() - t0;
    ESP_LOGI(TAG, "%d frames, %.1f fps, %u bytes per frame",
             frames, frames * 1e6 / (double)us, (unsigned)(bytes / (frames ? frames : 1)));
}
