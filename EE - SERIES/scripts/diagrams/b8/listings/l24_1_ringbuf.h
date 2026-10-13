/* Single-producer, single-consumer UART ring buffer.
 * Initialize before enabling either context. Verify target ISR support. */
#ifndef RINGBUF_H
#define RINGBUF_H
#include <stdbool.h>
#include <stdint.h>
#include <stdatomic.h>

#define RB_SIZE 256u                          /* power of two */

typedef struct {
    uint8_t data[RB_SIZE];
    _Atomic uint32_t head;                    /* written only by producer */
    _Atomic uint32_t tail;                    /* written only by consumer */
    _Atomic uint32_t dropped;                 /* producer writes; either side may read */
} ringbuf_t;

/* false means these atomics are not lock-free on this build. */
bool     rb_init(ringbuf_t *rb);
bool     rb_put(ringbuf_t *rb, uint8_t b);   /* false if full */
bool     rb_get(ringbuf_t *rb, uint8_t *b);  /* false if empty */
uint32_t rb_count(const ringbuf_t *rb);       /* approximate concurrent snapshot */
uint32_t rb_dropped(const ringbuf_t *rb);     /* atomic diagnostic snapshot */
#endif
