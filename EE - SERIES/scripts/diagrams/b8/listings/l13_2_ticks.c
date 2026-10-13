// Why vTaskDelay(pdMS_TO_TICKS(5)) does not wait 5 ms at a 100 Hz tick: run on the PC.
#include <stdint.h>
#include <stdio.h>

typedef uint32_t TickType_t;
#define configTICK_RATE_HZ 100u                               // the ESP-IDF default
#define pdMS_TO_TICKS(ms) ((TickType_t)(((TickType_t)(ms) * (TickType_t)configTICK_RATE_HZ) / (TickType_t)1000u))

int main(void)
{
    const unsigned ms[] = { 5, 10, 15, 25, 100 };
    for (int i = 0; i < 5; i++) {
        TickType_t t = pdMS_TO_TICKS(ms[i]);
        unsigned lo = t ? (t - 1) * 1000u / configTICK_RATE_HZ : 0;   // delay starts mid-tick
        unsigned hi = t * 1000u / configTICK_RATE_HZ;
        printf("%3u ms -> %u ticks -> real delay %u to %u ms\n", ms[i], (unsigned)t, lo, hi);
    }
    return 0;
}
