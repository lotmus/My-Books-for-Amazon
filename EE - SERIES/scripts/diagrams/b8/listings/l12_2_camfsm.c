// Wildlife-camera state machine: pure logic, driven by events, tested on the PC.
#include <stdio.h>

typedef enum { ST_SLEEP, ST_CAPTURE, ST_SAVE, ST_COOLDOWN, ST_LOWBATT } state_t;
typedef enum { EV_MOTION, EV_CAPTURE_OK, EV_CAPTURE_FAIL, EV_SAVED, EV_TICK_1S, EV_BATT_LOW } event_t;

#define COOLDOWN_S 30

typedef struct { state_t st; int cooldown_left; int photos; int errors; } cam_t;

static const char *NAMES[] = { "SLEEP", "CAPTURE", "SAVE", "COOLDOWN", "LOWBATT" };

static void cam_handle(cam_t *c, event_t ev)
{
    if (ev == EV_BATT_LOW) { c->st = ST_LOWBATT; return; }     // from any state
    switch (c->st) {
    case ST_SLEEP:
        if (ev == EV_MOTION) c->st = ST_CAPTURE;               // action: start camera
        break;
    case ST_CAPTURE:
        if (ev == EV_CAPTURE_OK) c->st = ST_SAVE;
        else if (ev == EV_CAPTURE_FAIL) { c->errors++; c->st = ST_COOLDOWN; c->cooldown_left = COOLDOWN_S; }
        break;
    case ST_SAVE:
        if (ev == EV_SAVED) { c->photos++; c->st = ST_COOLDOWN; c->cooldown_left = COOLDOWN_S; }
        break;
    case ST_COOLDOWN:                                          // motion is ignored here
        if (ev == EV_TICK_1S && --c->cooldown_left == 0) c->st = ST_SLEEP;
        break;
    case ST_LOWBATT:                                           // stays until reset
        break;
    }
}

int main(void)
{
    cam_t c = { ST_SLEEP, 0, 0, 0 };
    const event_t script[] = { EV_MOTION, EV_CAPTURE_OK, EV_SAVED, EV_MOTION };
    for (unsigned i = 0; i < sizeof script / sizeof script[0]; i++) cam_handle(&c, script[i]);
    printf("after photo + motion in cooldown: %s, photos %d\n", NAMES[c.st], c.photos);
    for (int s = 0; s < COOLDOWN_S; s++) cam_handle(&c, EV_TICK_1S);
    printf("after 30 ticks: %s\n", NAMES[c.st]);
    cam_handle(&c, EV_BATT_LOW);
    printf("after low battery: %s\n", NAMES[c.st]);
    return (c.photos == 1 && c.st == ST_LOWBATT) ? 0 : 1;
}
