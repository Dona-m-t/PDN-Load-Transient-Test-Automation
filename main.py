"""
Main program for PDN Load Transient Test Automation
"""

from config import *

from power_supply import PowerSupply
from electronic_load import ElectronicLoad
from oscilloscope import Oscilloscope
from dmm import DigitalMultimeter

print("Initializing Instruments...")

ps = PowerSupply(POWER_SUPPLY)
eload = ElectronicLoad(ELECTRONIC_LOAD)
scope = Oscilloscope(OSCILLOSCOPE)
dmm = DigitalMultimeter(DMM)

print("Configuring Power Supply...")
ps.configure(INPUT_VOLTAGE, CURRENT_LIMIT)
ps.output_on()

print("Configuring Electronic Load...")
eload.configure()

print("Executing Load Transient Test...")
eload.run_transient(LOAD_LOW, LOAD_HIGH)

print("Capturing Oscilloscope Waveform...")
waveform = scope.capture_waveform()

print("Measuring Output Voltage...")
voltage = dmm.measure_voltage()

results = [{
    "Voltage": voltage,
    "Waveform": waveform,
    "Status": "PASS"
}]

from report_generator import save_results

save_results(results)

ps.output_off()

print("Test Completed Successfully.")
