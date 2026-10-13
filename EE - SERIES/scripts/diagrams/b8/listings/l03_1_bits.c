// Building the BME280 ctrl_meas register value with bit fields; runs on the PC.
#include <stdint.h>
#include <stdio.h>

#define BIT(n)            (1u << (n))
#define SET_BITS(r, m)    ((r) |= (m))
#define CLEAR_BITS(r, m)  ((r) &= ~(m))

// ctrl_meas (register 0xF4): osrs_t in bits 7..5, osrs_p in bits 4..2, mode in bits 1..0
#define OSRS_T_SHIFT  5u
#define OSRS_P_SHIFT  2u
#define MODE_MASK     0x03u
#define MODE_NORMAL   0x03u

static uint8_t field_write(uint8_t reg, uint8_t mask, unsigned shift, uint8_t value)
{
    return (uint8_t)((reg & ~(mask << shift)) | ((value & mask) << shift));
}

int main(void)
{
    uint32_t reg = 0xA4u;                 // 1010 0100
    SET_BITS(reg, BIT(3));                // 1010 1100 = 0xAC
    CLEAR_BITS(reg, BIT(5));              // 1000 1100 = 0x8C
    printf("reg = 0x%02X\n", (unsigned)reg);

    uint8_t ctrl_meas = 0;
    ctrl_meas = field_write(ctrl_meas, 0x07u, OSRS_T_SHIFT, 1);   // temperature x1
    ctrl_meas = field_write(ctrl_meas, 0x07u, OSRS_P_SHIFT, 1);   // pressure x1
    ctrl_meas = field_write(ctrl_meas, MODE_MASK, 0, MODE_NORMAL);
    printf("ctrl_meas = 0x%02X\n", (unsigned)ctrl_meas);          // 0x27
    return 0;
}
