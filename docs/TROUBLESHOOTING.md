# 🔍 Troubleshooting Guide

This guide covers common issues and solutions related to GitHub profile statistics, SVG asset rendering, GitHub Actions workflow failures, and embedded hardware flashing.

---

## 📊 1. GitHub Stats & Top Languages Card Issues

### Issue: GitHub Stats Card returns `503 Service Unavailable` or times out.
- **Root Cause:** The default Vercel instance for `github-readme-stats` occasionally experiences rate limits or server downtime.
- **Solution:** Use the high-availability Vercel mirror endpoint:
  ```html
  <img src="https://github-readme-stats-eight-theta.vercel.app/api?username=Immanueal1&..." />
  ```

### Issue: Only Python is shown in the Top Languages card (missing C, C++, MATLAB).
- **Root Cause:** By default, GitHub API only scans public repositories unless private contribution indexing is enabled.
- **Solution:**
  1. Go to [github.com/settings/profile](https://github.com/settings/profile) $\rightarrow$ Scroll to **Contributions & Activity**.
  2. Check **`[x] Include private contributions on my profile`**.
  3. Ensure `count_private=true&include_all_commits=true` is present in the `top-langs` URL parameters.

---

## 🧊 2. 3D Contribution Calendar Workflow Failures

### Issue: Workflow fails with `Process completed with exit code 1`.
- **Root Cause:** `yoshi389111/github-profile-3d-contrib` requires valid `"type"` and `"fileName"` attributes in `profile-3d-settings.json`.
- **Solution:** Ensure `.github/workflows/profile-3d-settings.json` contains:
  ```json
  {
    "type": "night-green",
    "fileName": "profile-customize.svg"
  }
  ```

---

## 🔌 3. Hardware & Firmware Upload Issues

### Issue: ESP32 fails to connect (`A fatal error occurred: Failed to connect to ESP32: Timed out waiting for packet header`).
- **Solution:**
  1. Hold down the **BOOT** button on the ESP32 development board while PlatformIO begins uploading.
  2. Ensure the USB-to-UART CP2102 / CH340 drivers are installed.
  3. Check COM port permissions on Windows/Linux.
