// Host unit tests: gcc -std=c11 -Wall -Wextra -Werror -o test_ringbuf l24_2_test_ringbuf.c l24_1_ringbuf.c && ./test_ringbuf
// A minimal CHECK macro keeps this self-contained; Unity or GoogleTest add reporting.
#include <stdio.h>
#include "l24_1_ringbuf.h"

static int failures, checks;
#define CHECK(cond) do { checks++; if (!(cond)) { failures++; \
    printf("FAIL %s:%d: %s\n", __FILE__, __LINE__, #cond); } } while (0)

static int init_buffer(ringbuf_t *rb)
{
    if (!rb_init(rb)) { CHECK(false); return 0; }
    return 1;
}

static void test_empty(void)
{
    ringbuf_t rb; uint8_t b;
    if (!init_buffer(&rb)) return;
    CHECK(rb_count(&rb) == 0);
    CHECK(!rb_get(&rb, &b));
}

static void test_fifo_order(void)
{
    ringbuf_t rb; uint8_t b;
    if (!init_buffer(&rb)) return;
    for (int i = 0; i < 10; i++) CHECK(rb_put(&rb, (uint8_t)i));
    for (int i = 0; i < 10; i++) { CHECK(rb_get(&rb, &b)); CHECK(b == i); }
}

static void test_full_drops_and_counts(void)
{
    ringbuf_t rb;
    if (!init_buffer(&rb)) return;
    for (unsigned i = 0; i < RB_SIZE; i++) CHECK(rb_put(&rb, 0xAA));
    CHECK(!rb_put(&rb, 0x55));
    CHECK(rb_dropped(&rb) == 1u);
    CHECK(rb_count(&rb) == RB_SIZE);
}

static void test_index_wraparound(void) /* unsigned counters wrap modulo 2^32 */
{
    ringbuf_t rb; uint8_t b;
    if (!init_buffer(&rb)) return;
    atomic_store_explicit(&rb.head, 0xFFFFFFF0u, memory_order_relaxed);
    atomic_store_explicit(&rb.tail, 0xFFFFFFF0u, memory_order_relaxed);
    for (int i = 0; i < 40; i++) CHECK(rb_put(&rb, (uint8_t)i));
    CHECK(rb_count(&rb) == 40u);
    for (int i = 0; i < 40; i++) { CHECK(rb_get(&rb, &b)); CHECK(b == i); }
    CHECK(rb_count(&rb) == 0u);
}

int main(void)
{
    test_empty();
    test_fifo_order();
    test_full_drops_and_counts();
    test_index_wraparound();
    printf("%d checks, %d failures\n", checks, failures);
    return failures != 0;
}
