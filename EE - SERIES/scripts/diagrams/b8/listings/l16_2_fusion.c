// Complementary filter and 1-D Kalman filter for one tilt axis, on simulated data.
// Pure C, runs on the PC. Same code runs on the ESP32-S3 at 100 Hz.
#include <math.h>
#include <stdint.h>
#include <stdio.h>

#define DT 0.01f                         // 100 Hz
static uint32_t seed = 12345;
static float noise(void)                 // approximately Gaussian, sigma 1 (sum of 12 uniforms)
{
    float s = 0.0f;
    for (int i = 0; i < 12; i++) { seed = seed * 1664525u + 1013904223u; s += (seed >> 8) / 16777216.0f; }
    return s - 6.0f;
}

typedef struct { float angle, bias, P[2][2]; } kalman_t;   // state: angle and gyro bias

static float complementary(float *angle, float gyro_dps, float acc_deg, float alpha)
{
    *angle = alpha * (*angle + gyro_dps * DT) + (1.0f - alpha) * acc_deg;
    return *angle;
}

static float kalman_step(kalman_t *k, float gyro_dps, float acc_deg)
{
    const float Q_angle = 0.001f, Q_bias = 0.003f, R = 4.0f;   // R = (2 deg)^2
    k->angle += (gyro_dps - k->bias) * DT;                      // predict
    k->P[0][0] += DT * (DT * k->P[1][1] - k->P[0][1] - k->P[1][0] + Q_angle);
    k->P[0][1] -= DT * k->P[1][1];
    k->P[1][0] -= DT * k->P[1][1];
    k->P[1][1] += Q_bias * DT;
    float S = k->P[0][0] + R;                                    // update
    float K0 = k->P[0][0] / S, K1 = k->P[1][0] / S;
    float y = acc_deg - k->angle;
    k->angle += K0 * y;
    k->bias  += K1 * y;
    float P00 = k->P[0][0], P01 = k->P[0][1];
    k->P[0][0] -= K0 * P00; k->P[0][1] -= K0 * P01;
    k->P[1][0] -= K1 * P00; k->P[1][1] -= K1 * P01;
    return k->angle;
}

int main(void)
{
    const float truth = 10.0f, bias = 0.5f;      // true tilt (deg), gyro bias (deg/s)
    float gyro_only = 0.0f, comp = 0.0f, e_acc = 0.0f, e_comp = 0.0f, e_kal = 0.0f;
    kalman_t k = { 0 };
    int n = 0;
    for (int i = 1; i <= 2000; i++) {            // 20 s
        float gyro = bias + 0.1f * noise();      // the board is still
        float acc  = truth + 2.0f * noise();     // accelerometer tilt, sigma 2 deg
        if (i == 1) { gyro_only = truth; comp = acc; k.angle = acc; }   // gyro starts from the true angle
        gyro_only += gyro * DT;
        complementary(&comp, gyro, acc, 0.98f);
        kalman_step(&k, gyro, acc);
        if (i > 1000) {                          // statistics over the last 10 s
            e_acc  += (acc - truth) * (acc - truth);
            e_comp += (comp - truth) * (comp - truth);
            e_kal  += (k.angle - truth) * (k.angle - truth);
            n++;
        }
    }
    printf("gyro only after 20 s: %.2f deg (drift %.2f)\n", gyro_only, gyro_only - truth);
    printf("rms error: accel %.2f, complementary %.2f, kalman %.2f deg\n",
           sqrtf(e_acc / n), sqrtf(e_comp / n), sqrtf(e_kal / n));
    printf("kalman bias estimate %.3f deg/s\n", k.bias);
    return 0;
}
