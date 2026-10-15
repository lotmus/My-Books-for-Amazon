// Fixed-point helpers and a first-order IIR low-pass for chips without an FPU (RP2040).
// Pure C, tested on the PC.
#include <stdint.h>
#include <stdio.h>

typedef int16_t q15_t;                      // value = raw / 32768, range [-1, 1)

static q15_t q15_mul(q15_t a, q15_t b)
{
    int32_t p = ((int32_t)a * b + (1 << 14)) >> 15;   // round to nearest
    if (p > INT16_MAX) p = INT16_MAX;                  // only -1 * -1 overflows
    return (q15_t)p;
}

// y += (x - y) / 16, naive: the state has no fractional bits.
static int32_t iir_naive(int32_t *y, int32_t x) { *y += (x - *y) >> 4; return *y; }

// Same filter with 8 extra fractional bits kept in the state.
static int32_t iir_scaled(int32_t *acc, int32_t x)
{
    *acc += ((x << 8) - *acc) >> 4;
    return (*acc + 128) >> 8;                          // rounded output
}

int main(void)
{
    printf("0.5 * 0.25 = %d/32768\n", q15_mul(16384, 8192));      // 4096 = 0.125
    printf("-1 * -1 saturates to %d\n", q15_mul(INT16_MIN, INT16_MIN));
    int32_t yn = 0, acc = 0, n16 = 0;
    for (int n = 1; n <= 200; n++) {                   // step from 0 to 1000 counts
        iir_naive(&yn, 1000);
        int32_t ys = iir_scaled(&acc, 1000);
        if (n == 16) n16 = ys;
    }
    printf("after 16 samples: %ld (64.4 %% of 1000 expected)\n", (long)n16);
    printf("after 200 samples: naive %ld, scaled %ld\n", (long)yn, (long)((acc + 128) >> 8));
    return 0;
}
