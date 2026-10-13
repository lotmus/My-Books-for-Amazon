// Wraparound-safe timeouts with a 32-bit millisecond counter; runs on the PC.
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

static bool timed_out(uint32_t now, uint32_t start, uint32_t timeout_ms)
{
    return (uint32_t)(now - start) >= timeout_ms;   // correct across the wrap
}

static bool timed_out_naive(uint32_t now, uint32_t start, uint32_t timeout_ms)
{
    return now >= start + timeout_ms;               // wrong near the wrap
}

int main(void)
{
    uint32_t start = 0xFFFFFF00u;    // 256 ms before the counter wraps to 0
    uint32_t now   = 0xFFFFFF80u;    // 128 ms later, before the wrap
    printf("elapsed %u ms, safe %d, naive %d\n",
           (unsigned)(now - start), timed_out(now, start, 1000),
           timed_out_naive(now, start, 1000));      // 128, 0, 1 (naive is wrong)
    now = 0x00000064u;               // 356 ms after start, after the wrap
    printf("elapsed %u ms, safe %d\n",
           (unsigned)(now - start), timed_out(now, start, 1000));   // 356, 0
    return 0;
}
