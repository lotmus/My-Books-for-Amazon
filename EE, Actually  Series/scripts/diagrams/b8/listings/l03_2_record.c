// Field order changes a struct's size: padding made visible; runs on the PC.
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>

struct rec_a { uint8_t id; uint32_t time; uint16_t hum; uint8_t flags; };
struct rec_b { uint32_t time; uint16_t hum; uint8_t id; uint8_t flags; };

int main(void)
{
    printf("rec_a: %zu bytes (time at %zu, hum at %zu, flags at %zu)\n",
           sizeof(struct rec_a), offsetof(struct rec_a, time),
           offsetof(struct rec_a, hum), offsetof(struct rec_a, flags));
    printf("rec_b: %zu bytes\n", sizeof(struct rec_b));
    return 0;
}
