// Pack one garden reading into 8 bytes for LoRa, and unpack it again.
// Pure C, runs on the PC; the same functions run on the node and on the gateway.
#include <stdint.h>
#include <stdio.h>
#include <math.h>

typedef struct {
    uint8_t version, seq;
    float t_c, rh, p_hpa, vbat;
} reading_t;

static void put16(uint8_t *b, uint16_t v) { b[0] = (uint8_t)(v >> 8); b[1] = (uint8_t)v; }  // big-endian
static uint16_t get16(const uint8_t *b) { return (uint16_t)((b[0] << 8) | b[1]); }

static int clampi(long v, long lo, long hi) { return (int)(v < lo ? lo : v > hi ? hi : v); }

void pack(const reading_t *r, uint8_t out[8])
{
    out[0] = r->version;
    out[1] = r->seq;
    put16(&out[2], (uint16_t)(int16_t)clampi(lround(r->t_c * 100.0f), -32768, 32767)); // 0.01 degC
    out[4] = (uint8_t)clampi(lround(r->rh * 2.0f), 0, 200);                          // 0.5 %
    put16(&out[5], (uint16_t)clampi(lround(r->p_hpa * 10.0f), 0, 65535));            // 0.1 hPa
    out[7] = (uint8_t)clampi(lround((r->vbat - 2.5f) * 50.0f), 0, 255);             // 20 mV from 2.5 V
}

void unpack(const uint8_t in[8], reading_t *r)
{
    r->version = in[0];
    r->seq = in[1];
    r->t_c = (int16_t)get16(&in[2]) / 100.0f;
    r->rh = in[4] / 2.0f;
    r->p_hpa = get16(&in[5]) / 10.0f;
    r->vbat = 2.5f + in[7] / 50.0f;
}

int main(void)
{
    reading_t r = { 1, 42, 23.41f, 45.2f, 1013.25f, 3.86f }, back;
    uint8_t buf[8];
    pack(&r, buf);
    for (int i = 0; i < 8; i++) printf("%02X ", buf[i]);
    unpack(buf, &back);
    printf("\n-> v%u #%u  %.2f C  %.1f %%  %.1f hPa  %.2f V\n",
           back.version, back.seq, back.t_c, back.rh, back.p_hpa, back.vbat);
    r.t_c = -12.5f; pack(&r, buf); unpack(buf, &back);
    printf("negative check: %.2f C\n", back.t_c);
    return 0;
}
