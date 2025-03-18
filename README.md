# Bowling Project

This school project simulates a mini bowling game using a Raspberry Pi and an STM microcontroller. The system:

- Activate and detects platform movements using GPIO signals.
- Captures images using the Raspberry Pi Camera.
- Processes images to determine the state of bowling skittles.
- Controls platform movements via the STM32 microcontroller.

---

## Requirements

### Hardware
- Raspberry Pi 4B (with GPIO and camera support)
- STM nucleo-L476RG microcontroller (for platform control)
- Raspberry Pi Camera Module
- Breadboard, wires, and necessary electronic components

### Software
- Python 3.x
- STM development environment (e.g., STM32CubeIDE)

### Python Packages
- RPi.GPIO
- picamera
- Pillow
- numpy

### Install Dependencies

```bash
sudo apt-get update
sudo apt-get install python3-pip python3-pil python3-numpy
pip3 install RPi.GPIO picamera
```
You may need to use the option "--break-system-packages".

---

## How It Works

### 1. GPIO Signal Management
`SignalSending.py` sends a HIGH signal from GPIO pin 17 and waits for a response on GPIO pin 27 to detect the platform's status.

### 2. Image Capture
`TakePicture.py` captures an image of the bowling pins using the Raspberry Pi Camera.

### 3. Image Analysis
`AnalyzePicture.py` analyzes specific pixel areas to determine whether the pins are standing or have fallen, based on their color values.

### 4. Shot Detection
`DidHeShot.py` analyzes platform movement and image data to determine if a shot was made thanks to a IR led.

### 5. Platform Control (STM)
The STM code controls the physical movement of the platform.

---

## Running the Project

1. Set up your hardware.
2. Upload STM code to the microcontroller using STM32CubeIDE or equivalent.
3. Enable the Raspberry Pi Camera via `raspi-config`.
4. Run the main script:

```bash
sudo python3 main.py
```

> Note: `sudo` is required for GPIO access.

---

## Notes

- Ensure GPIO voltages are properly interfaced between Raspberry Pi and STM.
- Calibrate pixel positions and color thresholds in `AnalyzePicture.py` for accurate results.
- Adjust GPIO pins and camera settings as needed.

---

## Contributors
- **Kyle Dottin** 
- **Yousra El Yaakoubi** 
- **Paul Caillaud** 
- **William Nicolussi**

---
