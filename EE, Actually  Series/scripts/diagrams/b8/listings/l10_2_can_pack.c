// Packing reader-lab values into an 8-byte classic CAN payload, and back.
// Layout (little-endian): temp int16 0.01 degC | hum uint16 0.01 % | press uint32 Pa.
#include <stdint.h>
#include <stdio.h>

static void put_u16(uint8_t *p, uint16_t v) { p[0] = (uint8_t)v; p[1] = (uint8_t)(v >> 8); }
static void put_u32(uint8_t *p, uint32_t v) { put_u16(p, (uint16_t)v); put_u16(p + 2, (uint16_t)(v >> 16)); }
static uint16_t get_u16(const uint8_t *p) { return (uint16_t)(p[0] | (p[1] << 8)); }
static uint32_t get_u32(const uint8_t *p) { return get_u16(p) | ((uint32_t)get_u16(p + 2) << 16); }

static void env_pack(uint8_t out[8], int16_t t_x100, uint16_t h_x100, uint32_t p_pa)
{
    put_u16(out, (uint16_t)t_x100);
    put_u16(out + 2, h_x100);
    put_u32(out + 4, p_pa);
}

int main(void)
{
    uint8_t frame[8];
    env_pack(frame, -523, 4520, 101325);      // -5.23 degC, 45.20 %, 1013.25 hPa
    for (int i = 0; i < 8; i++) printf("%02X ", frame[i]);
    printf("\n");
    int16_t t = (int16_t)get_u16(frame);
    printf("T %.2f C, H %.2f %%, P %.2f hPa\n", t / 100.0, get_u16(frame + 2) / 100.0,
           get_u32(frame + 4) / 100.0);
    return 0;
}
