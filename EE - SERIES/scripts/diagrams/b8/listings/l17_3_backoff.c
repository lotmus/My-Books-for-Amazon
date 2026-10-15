// Reconnect back-off: 1, 2, 4, ... s capped at 60 s, with up to 25 % random jitter.
// Pure C, runs on the PC; on the ESP32-S3 replace rand() with esp_random().
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static uint32_t backoff_ms(unsigned attempt)
{
    uint32_t base = 1000u << (attempt < 6 ? attempt : 6);   // 1 s .. 64 s
    if (base > 60000u) base = 60000u;                       // cap at 60 s
    uint32_t jitter = (uint32_t)rand() % (base / 4 + 1);    // 0 .. 25 %
    return base - jitter;                                   // never more than the cap
}

int main(void)
{
    srand(1);
    uint32_t total = 0;
    for (unsigned a = 0; a < 10; a++) {
        uint32_t d = backoff_ms(a);
        total += d;
        printf("attempt %u: wait %5.1f s (total %6.1f s)\n", a + 1, d / 1000.0, total / 1000.0);
    }
    return 0;
}
