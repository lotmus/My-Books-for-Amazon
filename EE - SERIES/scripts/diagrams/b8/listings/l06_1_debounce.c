// Sampled debouncer: call every 5 ms; the output changes after 4 equal samples.
// Pure logic, so it is unit-tested on the PC before it ever sees a button.
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

#define DEBOUNCE_SAMPLES 4u

typedef struct {
    bool    stable;     // debounced level
    uint8_t count;      // consecutive samples that disagree with 'stable'
} debounce_t;

// Returns true exactly once per accepted change of level.
static bool debounce_update(debounce_t *d, bool raw)
{
    if (raw == d->stable) {
        d->count = 0;
        return false;
    }
    if (++d->count >= DEBOUNCE_SAMPLES) {
        d->stable = raw;
        d->count = 0;
        return true;
    }
    return false;
}

int main(void)
{
    // Raw samples every 5 ms: released (1), a bouncing press, held, then released.
    const bool raw[] = {1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1};
    debounce_t d = { .stable = true, .count = 0 };
    for (unsigned i = 0; i < sizeof raw / sizeof raw[0]; i++) {
        if (debounce_update(&d, raw[i]))
            printf("t = %3u ms: level -> %d\n", i * 5u, d.stable);
    }
    return 0;   // prints: t = 35 ms: level -> 0, t = 75 ms: level -> 1
}
