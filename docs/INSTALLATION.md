# 🛠️ Installation & Environment Setup Guide

This guide details the prerequisites, toolchains, and environment setup required to compile firmware, run Edge AI pipelines, and inspect PCB hardware schematics across this open-source repository.

---

## 📌 Prerequisites & Software Dependencies

### 1. Embedded Firmware Development
- **VS Code** with [PlatformIO IDE Extension](https://platformio.org/)
- **ESP-IDF v5.1+** (for ESP32 bare-metal and FreeRTOS development)
- **Raspberry Pi Pico C/C++ SDK v1.5+** (for RP2040 PIO & DMA driver development)
- **STM32CubeIDE / STM32CubeCLT** (for ARM Cortex-M bare-metal development)
- **Git** version 2.40+

### 2. Edge AI & Machine Learning Tools
- **Python 3.10+** (Virtual environment recommended)
- Key Python packages:
  ```bash
  pip install numpy pandas scikit-learn torch torchvision opencv-python matplotlib
  ```

### 3. Electronics & PCB Design
- **KiCad EDA v7.0+** or **v8.0+**
- **Proteus Design Suite 8.15+**

---

## ⚙️ Environment Setup Steps

### Step 1: Clone the Repository
```bash
git clone https://github.com/Immanueal1/Immanueal1.git
cd Immanueal1
```

### Step 2: Configure Python Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activate on Linux / macOS
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### Step 3: PlatformIO Project Initialization
To build firmware for ESP32 or RP2040 target boards:
```bash
# Verify PlatformIO CLI
pio --version

# Build firmware binary
pio run -e esp32dev
```

---

## 🔍 Verification
Run the python helper scripts under `scratch/` to verify SVG generation tools locally:
```bash
python scratch/gen_tech_stack.py
```
If `assets/tech-stack.svg` generates without error, your local environment is fully configured!
