// A RAM trace avoids serial output in the timing-critical path; measure its target overhead.
// Events are stored in RAM with a timestamp and printed later, outside the timing-critical code.
// Pure C, runs on the PC; on the target, now_us() reads a hardware timer.
#include <stdatomic.h>
#include <stdint.h>
#include <stdio.h>

#define TRACE_LEN 64                       // power of two, so the index wraps with a mask
typedef struct { uint32_t t_us; uint16_t id; uint16_t arg; } trace_t;
static trace_t trace_buf[TRACE_LEN];
static atomic_uint trace_head;             // total events ever written

static uint32_t fake_clock;
static uint32_t now_us(void) { return fake_clock; }      // target: esp_timer_get_time() etc.

static inline void trace(uint16_t id, uint16_t arg)      // Atomic ticket; verify lock-free ISR support on the target
{
    uint32_t i = atomic_fetch_add(&trace_head, 1) & (TRACE_LEN - 1);
    trace_buf[i] = (trace_t){ now_us(), id, arg };
}

enum { EV_ISR = 1, EV_TASK_START, EV_TASK_END, EV_I2C_NACK };
static const char *names[] = { "?", "isr", "task start", "task end", "i2c nack" };

static void trace_dump(void)               // call from a low-priority task or on a fault
{
    uint32_t head = atomic_load(&trace_head);
    uint32_t n = head < TRACE_LEN ? head : TRACE_LEN;
    for (uint32_t k = head - n; k != head; k++) {
        const trace_t *e = &trace_buf[k & (TRACE_LEN - 1)];
        printf("%8lu us  %-10s %u\n", (unsigned long)e->t_us, names[e->id], e->arg);
    }
}

int main(void)
{
    for (int cycle = 0; cycle < 25; cycle++) {        // 25 x 3 + 1 = 76 events; the buffer keeps 64
        fake_clock = 1000u * cycle;      trace(EV_ISR, cycle);
        fake_clock += 12;                trace(EV_TASK_START, cycle);
        if (cycle == 22) { fake_clock += 250; trace(EV_I2C_NACK, 0x76); }
        fake_clock += 180;               trace(EV_TASK_END, cycle);
    }
    printf("%u events written, the last %d kept\n", atomic_load(&trace_head), TRACE_LEN);
    trace_dump();
    return 0;
}
