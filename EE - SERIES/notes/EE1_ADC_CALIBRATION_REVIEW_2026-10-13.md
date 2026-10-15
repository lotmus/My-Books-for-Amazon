# Book 1 ADC Accuracy and Calibration Audit

**Date:** 13 October 2026  
**Scope:** The ESP32-S3 ADC error claim in Chapter 27.5, alignment with Chapter 15, Further Reading citations, and selected render pages.

## Finding and correction

Chapter 15 correctly described Espressif's ±50 mV as a total-error limit after hardware and software calibration, but Chapter 27 said the same error persisted only "until calibrated." The current Espressif datasheet identifies the ±50 mV ATTEN3 error as a calibrated result over an effective 0–2.9 V range. Its stated test setup uses a DC input, 100 nF at the ADC, 25 °C, and Wi-Fi disabled. At the Chapter 27 thermistor slope of 36.7 mV/°C, 50 mV corresponds to 1.36 °C. The datasheet figure is a chip-level result under those conditions; the board, divider, thermistor, and reference introduce additional error.

Rewrote Chapter 27.5 to name the calibrated error limit and conditions, distinguish resolution from accuracy, and recommend checking the assembled channel against a reference thermometer. Added the [ESP32-S3 datasheet](https://documentation.espressif.com/esp32-s3_datasheet_en.pdf) and [ESP-IDF ADC Calibration Driver guide](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/peripherals/adc/adc_calibration.html) to Appendix F. The current datasheet's Section 5.5 and Table 5-6 specify the calibrated error; the guide describes curve-fitting calibration and its purpose.

## Verification and limits

The authoritative DOCX passes ZIP integrity and `python-docx` parsing; the tagged mirror was regenerated. A fresh 199-page render was inspected on page 114 (thermistor example) and page 194 (new Further Reading citation). Both remain legible. This clarifies the stated performance bound; it does not claim that the reader's dev board will achieve that limit or that a single-point thermometer check removes all error. No score increase is claimed. Full-book/Kindle visual review and a bench check remain open.
