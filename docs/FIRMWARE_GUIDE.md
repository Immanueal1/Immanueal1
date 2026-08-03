# ⚡ Embedded Firmware Guide

This document details the software architecture, peripheral driver implementations, and FreeRTOS concurrency strategies used across ESP32, RP2040, and STM32 target platforms.

---

## 💻 Firmware Stack Overview

```
+-------------------------------------------------------+
|             Application & Edge ML Layer               |
|  (Spectral Classifier / Signal Gen / Waveform LUTs)   |
+-------------------------------------------------------+
|            FreeRTOS / Multitasking Kernel             |
|   (Task Queues, Mutexes, Semaphore Synchronization)   |
+-------------------------------------------------------+
|          Hardware Abstraction Layer (HAL)             |
|    (ESP-IDF Drivers / RP2040 SDK / STM32 CubeHAL)     |
+-------------------------------------------------------+
|             Microcontroller Hardware                  |
|     (ESP32 / RP2040 / STM32 ARM Cortex-M Peripherals)  |
+-------------------------------------------------------+
```

---

## 🛠️ Key Drivers & Implementations

### 1. AS7263 I²C Spectral Driver (`driver_as7263.cpp`)
- **Protocol:** Standard I²C @ 100kHz / 400kHz.
- **Register Interface:** Virtualized register read/write over I²C.
- **Integration Setup:**
  ```cpp
  #include <Wire.h>

  #define AS7263_ADDR 0x49

  void init_as7263() {
      Wire.begin(21, 22, 400000); // SDA=21, SCL=22
      // Virtual register setup
  }
  ```

### 2. RP2040 PIO Waveform State Machine (`waveform.pio`)
- **Engine:** Direct memory access (DMA) feeding 8-bit GPIO output via Programmable I/O (PIO) state machines.
- **Zero CPU Overhead:** The RP2040 CPU sets up the DMA ping-pong buffer and sleeps while PIO streams sine wave lookup tables at 100 kSPS.

---

## ⏱️ FreeRTOS Multitasking Strategy

For ESP32 systems, execution is divided between Core 0 and Core 1:
- **Core 0 (Protocol & Sensor Acquisition Task):** Higher priority task dedicated to real-time ADC sampling and I²C communication.
- **Core 1 (UI & Telemetry Task):** Handles OLED rendering, button debouncing, and serial data transmission.
