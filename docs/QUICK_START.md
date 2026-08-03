# ⚡ Quick Start Guide

Welcome! This quick start guide will help you quickly navigate, build, and customize the embedded firmware, Edge AI models, and vector design assets in this repository.

---

## 🚀 Quick Navigation

- 🔬 **[Portable NIR Microplastic Analyzer](#1-nir-microplastic-analyzer):** ESP32 + AS7263 NIR Spectral Sensor + Edge ML.
- 🌊 **[RP2040 Waveform Generator](#2-rp2040-waveform-generator):** RP2040 Dual-Core + PIO Assembly + R-2R DAC.
- 📊 **[Handheld Digital Oscilloscope](#3-handheld-digital-oscilloscope):** Analog Front-End (AFE) + Protocol Decoding.

---

## 1. NIR Microplastic Analyzer Setup

1. **Hardware Connection:**
   Connect the **AS7263** NIR sensor module to the **ESP32** via I²C interface:
   - `SDA` $\rightarrow$ `GPIO 21`
   - `SCL` $\rightarrow$ `GPIO 22`
   - `VCC` $\rightarrow$ `3.3V`
   - `GND` $\rightarrow$ `GND`

2. **Flash Firmware:**
   ```bash
   pio run -e esp32_nir_analyzer -t upload
   ```

3. **Run ML Pipeline:**
   ```bash
   python scripts/train_nir_classifier.py --data dataset/spectral_samples.csv
   ```

---

## 2. RP2040 Waveform Generator Quick Start

1. **Hardware Setup:**
   Connect 8-bit R-2R Resistor Ladder to RP2040 `GPIO 0` through `GPIO 7`.

2. **Compile PIO Assembly & Upload Firmware:**
   ```bash
   mkdir build && cd build
   cmake ..
   make
   picotool load waveform_gen.uf2
   ```

3. **Frequency Control:**
   Use the LCD encoder to switch between Sine, Square, Triangle, and Sawtooth lookup tables (LUTs).

---

## 3. Regenerating Vector SVG Assets

All profile SVG assets match the **Dark Neon Dashboard Design System** (`#090A12`, `#22D3EE`, `#8B5CF6`). To regenerate or update any SVG:

```bash
# Regenerate Technical Skill Matrix SVG
python scratch/gen_tech_stack.py
```
