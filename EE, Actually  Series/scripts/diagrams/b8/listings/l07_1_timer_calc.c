// Prescaler and auto-reload for an STM32 timer: f_pwm = f_clk / ((PSC+1)(ARR+1)).
// Runs on the PC; paste the results into CubeMX or the init code.
#include <stdint.h>
#include <stdio.h>

typedef struct { uint32_t psc, arr; double f_actual; } timer_cfg_t;

// Choose the smallest prescaler that lets ARR fit in 16 bits (best duty resolution).
static int timer_solve(uint32_t f_clk, double f_pwm, timer_cfg_t *out)
{
    for (uint32_t psc = 0; psc <= 0xFFFFu; psc++) {
        double arr = f_clk / ((psc + 1.0) * f_pwm) - 1.0;
        if (arr <= 65535.0) {
            out->psc = psc;
            out->arr = (uint32_t)(arr + 0.5);
            out->f_actual = f_clk / ((psc + 1.0) * (out->arr + 1.0));
            return 0;
        }
    }
    return -1;   // frequency too low for this timer clock
}

int main(void)
{
    const double targets[] = { 50.0, 1000.0, 20000.0 };
    for (int i = 0; i < 3; i++) {
        timer_cfg_t c;
        if (timer_solve(84000000u, targets[i], &c) == 0)
            printf("%8.0f Hz: PSC=%5u ARR=%5u -> %.3f Hz, %u steps\n",
                   targets[i], (unsigned)c.psc, (unsigned)c.arr, c.f_actual, (unsigned)c.arr + 1u);
    }
    return 0;
}
