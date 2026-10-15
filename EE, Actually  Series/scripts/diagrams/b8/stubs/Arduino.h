// Syntax-check stub for the Arduino core for ESP32 (arduino-esp32 3.x). Not for building firmware.
#pragma once
#include <stdint.h>
#include <stddef.h>
#include <stdio.h>
#define IRAM_ATTR
#define HIGH 1
#define LOW 0
#define INPUT 0x01
#define OUTPUT 0x03
#define INPUT_PULLUP 0x05
#define FALLING 0x02
#define RISING 0x01
#define digitalPinToInterrupt(p) (p)
void pinMode(uint8_t, uint8_t); void digitalWrite(uint8_t, uint8_t); int digitalRead(uint8_t);
unsigned long millis(void); unsigned long micros(void); void delay(uint32_t);
void attachInterrupt(uint8_t, void (*)(void), int);
class String {
public:
    String(const char * = ""); String &operator+=(char); bool operator==(const char *) const;
    void trim(); unsigned int length() const; const char *c_str() const;
};
class HardwareSerial {
public:
    void begin(unsigned long); int available(); int read();
    size_t print(const char *); size_t print(float, int = 2); size_t print(const String &);
    size_t println(const char * = ""); size_t println(float, int = 2);
    size_t printf(const char *, ...) __attribute__((format(printf, 2, 3)));
};
extern HardwareSerial Serial;
