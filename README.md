# PDN Load Transient Test Automation

## Overview

This repository contains a Python-based automation framework developed for load transient testing of a Power Distribution Network (PDN). The automation communicates with laboratory instruments using "PyVISA" and "SCPI" commands to execute standardized load transient tests.

The objective is to reduce manual intervention, improve repeatability, and automatically generate test reports for production testing.

---

## Test Equipment

- Keithley 2230-30-1 Programmable DC Power Supply
- Keithley 2380 Electronic Load
- Keysight DSOX6004A Oscilloscope
- Keithley DMM6500 Digital Multimeter

---

## Features

- Automatic instrument initialization
- SCPI-based instrument control
- Load transient execution
- Oscilloscope waveform capture
- CSV result logging
- Pass/Fail evaluation
- Automated report generation

---

## Repository Structure

```
PDN-Load-Transient-Test-Automation
│
├── README.md
├── requirements.txt
├── config.py
├── main.py
├── power_supply.py
├── electronic_load.py
├── oscilloscope.py
├── dmm.py
├── report_generator.py
└── results/
```

---

## Workflow

1. Initialize all instruments.
2. Configure the programmable power supply.
3. Configure the electronic load.
4. Execute the load transient test.
5. Capture oscilloscope waveform.
6. Measure output voltage.
7. Save waveform with timestamp.
8. Store measurements in CSV format.
9. Generate final report.

---

## Python Libraries

- PyVISA
- Pandas
- NumPy
- Matplotlib

---

## Author

Dona Mariya Thomas
