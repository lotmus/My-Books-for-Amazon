// Two-point ADC calibration and averaging; pure C, tested on the PC with bench numbers.
#include <stdint.h>
#include <stdio.h>

typedef struct { float gain_v_per_code; float offset_v; } adc_cal_t;

// Measured on the bench: code c1 at v1 and code c2 at v2 from a reference source.
static adc_cal_t adc_cal_two_point(uint16_t c1, float v1, uint16_t c2, float v2)
{
    adc_cal_t cal;
    cal.gain_v_per_code = (v2 - v1) / (float)(c2 - c1);
    cal.offset_v = v1 - cal.gain_v_per_code * (float)c1;
    return cal;
}

static float adc_to_volts(const adc_cal_t *cal, uint16_t code)
{
    return cal->offset_v + cal->gain_v_per_code * (float)code;
}

// Average n samples (n <= 64) with an integer sum, then convert once.
static uint16_t adc_average(const uint16_t *s, unsigned n)
{
    uint32_t sum = 0;
    for (unsigned i = 0; i < n; i++) sum += s[i];
    return (uint16_t)((sum + n / 2) / n);             // rounded mean
}

int main(void)
{
    adc_cal_t cal = adc_cal_two_point(412, 0.500f, 3690, 3.000f);
    printf("gain %.1f uV/code, offset %.4f V\n", cal.gain_v_per_code * 1e6, cal.offset_v);
    const uint16_t s[4] = {2398, 2401, 2403, 2398};
    uint16_t code = adc_average(s, 4);
    printf("code %u -> %.4f V calibrated, %.4f V ideal (3.3 V / 4096)\n",
           (unsigned)code, adc_to_volts(&cal, code), code * 3.3f / 4096.0f);
    return 0;
}
