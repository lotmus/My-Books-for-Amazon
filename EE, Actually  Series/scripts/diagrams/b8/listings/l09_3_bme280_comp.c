// BME280/BMP280 temperature compensation (integer formula from the Bosch data sheet),
// with the data sheet's own test vector as a PC unit test.
#include <stdint.h>
#include <stdio.h>

typedef struct { uint16_t T1; int16_t T2, T3; } bme280_tcal_t;   // read from 0x88..0x8D

// Returns temperature in 0.01 degC; *t_fine is needed later by the pressure
// and humidity formulas.
static int32_t bme280_temp_x100(const bme280_tcal_t *c, int32_t adc_T, int32_t *t_fine)
{
    int32_t var1 = ((((adc_T >> 3) - ((int32_t)c->T1 << 1))) * ((int32_t)c->T2)) >> 11;
    int32_t var2 = (((((adc_T >> 4) - ((int32_t)c->T1)) *
                      ((adc_T >> 4) - ((int32_t)c->T1))) >> 12) * ((int32_t)c->T3)) >> 14;
    *t_fine = var1 + var2;
    return (*t_fine * 5 + 128) >> 8;
}

int main(void)
{
    const bme280_tcal_t cal = { 27504, 26435, -1000 };   // data sheet example
    int32_t t_fine;
    int32_t t = bme280_temp_x100(&cal, 519888, &t_fine);
    printf("T = %ld.%02ld degC (t_fine %ld)\n", (long)(t / 100), (long)(t % 100), (long)t_fine);
    return t == 2508 ? 0 : 1;                             // expected 25.08 degC
}
