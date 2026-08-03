# 🔌 Hardware Setup & Technical Specifications

This document outlines the hardware schematics, pinout mapping, power delivery, and sensor interfaces for the three primary open-source hardware projects.

---

## 🔬 1. NIR Microplastic Analyzer

### Hardware Specifications
- **Main Microcontroller:** ESP32-WROOM-32D (Dual-core 240MHz, 520KB SRAM)
- **Spectral Sensor:** AMS AS7263 NIR Spectral Sensor (6-channel optical sensing: 610nm, 680nm, 730nm, 760nm, 810nm, 860nm)
- **Display:** 0.96" SSD1306 OLED (128x64 resolution, I²C interface)
- **Power Supply:** 3.7V 18650 Li-ion cell with TP4056 USB-C charging and LDO 3.3V regulation

### Pinout Mapping

| Component | Pin Name | ESP32 GPIO | Notes |
| --- | --- | --- | --- |
| **AS7263 Sensor** | SDA | GPIO 21 | Pull-up 4.7kΩ to 3.3V |
| **AS7263 Sensor** | SCL | GPIO 22 | Pull-up 4.7kΩ to 3.3V |
| **SSD1306 OLED** | SDA | GPIO 21 | Shared I²C bus (Address 0x3C) |
| **SSD1306 OLED** | SCL | GPIO 22 | Shared I²C bus |
| **NIR LED Indicator** | EN | GPIO 16 | Optical illumination trigger |

---

## 🌊 2. RP2040 Waveform Generator

### Hardware Specifications
- **MCU:** Raspberry Pi RP2040 (Dual ARM Cortex-M0+ @ 133MHz, 264KB SRAM)
- **DAC Topology:** 8-Bit Precision R-2R Resistor Ladder (10kΩ / 20kΩ 1% metal film)
- **Op-Amp Buffer:** TL072 / LM358 in non-inverting unity gain configuration for impedance matching
- **Output Voltage Range:** 0.0V – 3.3V Peak-to-Peak

### Pinout Mapping

| DAC Bit | RP2040 GPIO | Resistor Network |
| --- | --- | --- |
| Bit 0 (LSB) | GPIO 0 | 20kΩ to Bit 0 |
| Bit 1 | GPIO 1 | 20kΩ to Bit 1 |
| Bit 2 | GPIO 2 | 20kΩ to Bit 2 |
| Bit 3 | GPIO 3 | 20kΩ to Bit 3 |
| Bit 4 | GPIO 4 | 20kΩ to Bit 4 |
| Bit 5 | GPIO 5 | 20kΩ to Bit 5 |
| Bit 6 | GPIO 6 | 20kΩ to Bit 6 |
| Bit 7 (MSB) | GPIO 7 | 20kΩ to Bit 7 |

---

## 📊 3. Portable Digital Oscilloscope

### Analog Front-End (AFE) Specifications
- **Input Channels:** Single / Dual Channel
- **Bandwidth:** DC to 150kHz
- **Input Attenuation:** 1x / 10x selectable switch
- **Protection:** BAV99 clamping diodes + 1MΩ input impedance buffer stage
