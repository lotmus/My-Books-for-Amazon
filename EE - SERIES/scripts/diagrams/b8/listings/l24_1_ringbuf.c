#include "l24_1_ringbuf.h"

bool rb_init(ringbuf_t *rb)
{
    atomic_init(&rb->head, 0u);
    atomic_init(&rb->tail, 0u);
    atomic_init(&rb->dropped, 0u);
    return atomic_is_lock_free(&rb->head) &&
           atomic_is_lock_free(&rb->tail) &&
           atomic_is_lock_free(&rb->dropped);
}

uint32_t rb_count(const ringbuf_t *rb)
{
    uint32_t head = atomic_load_explicit(&rb->head, memory_order_acquire);
    uint32_t tail = atomic_load_explicit(&rb->tail, memory_order_acquire);
    uint32_t count = head - tail;              /* unsigned subtraction wraps */
    return count > RB_SIZE ? RB_SIZE : count; /* diagnostic snapshot only */
}

uint32_t rb_dropped(const ringbuf_t *rb)
{
    return atomic_load_explicit(&rb->dropped, memory_order_relaxed);
}

bool rb_put(ringbuf_t *rb, uint8_t b)
{
    uint32_t head = atomic_load_explicit(&rb->head, memory_order_relaxed);
    uint32_t tail = atomic_load_explicit(&rb->tail, memory_order_acquire);

    /* Reject any observed distance at or above the buffer capacity. */
    if ((uint32_t)(head - tail) >= RB_SIZE) {
        uint32_t dropped = atomic_load_explicit(&rb->dropped, memory_order_relaxed);
        atomic_store_explicit(&rb->dropped, dropped + 1u, memory_order_relaxed);
        return false;
    }
    rb->data[head & (RB_SIZE - 1u)] = b;
    atomic_store_explicit(&rb->head, head + 1u, memory_order_release);
    return true;
}

bool rb_get(ringbuf_t *rb, uint8_t *b)
{
    uint32_t tail = atomic_load_explicit(&rb->tail, memory_order_relaxed);
    uint32_t head = atomic_load_explicit(&rb->head, memory_order_acquire);

    if (head == tail) return false;
    *b = rb->data[tail & (RB_SIZE - 1u)];
    atomic_store_explicit(&rb->tail, tail + 1u, memory_order_release);
    return true;
}

