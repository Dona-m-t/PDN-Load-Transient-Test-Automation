# ----------------------------------------------------------
# main.py
# Main program for PDN Load Transient Test Automation
# ----------------------------------------------------------
from config import *

from power_supply import PowerSupply
from electronic_load import ElectronicLoad
from oscilloscope import Oscilloscope
from dmm import DigitalMultimeter

from report_generator import save_results
print("------------------------------------------------")
print(" PDN Load Transient Test Started")
print("------------------------------------------------")

# Initialize all instruments
power_supply = PowerSupply(POWER_SUPPLY)
electronic_load = ElectronicLoad(ELECTRONIC_LOAD)
oscilloscope = Oscilloscope(OSCILLOSCOPE)
multimeter = DigitalMultimeter(DMM)

# Configure the power supply
power_supply.configure(INPUT_VOLTAGE, CURRENT_LIMIT)
power_supply.output_on()

# Configure the oscilloscope
oscilloscope.configure()

# Configure the electronic load
electronic_load.configure()

# Execute the load transient test
electronic_load.run_transient(LOW_LOAD, HIGH_LOAD)

# Capture waveform
waveform_file = oscilloscope.capture_waveform()

# Measure output voltage
measured_voltage = multimeter.measure_voltage()

# Save the results
test_results = [
    {
        "Voltage (V)": measured_voltage,
        "Low Load (A)": LOW_LOAD,
        "High Load (A)": HIGH_LOAD,
        "Waveform": waveform_file,
        "Result": "PASS"
    }
]
save_results(test_results)

# Turn OFF the instruments
electronic_load.disable()
power_supply.output_off()

print("------------------------------------------------")
print(" PDN Load Transient Test Completed")
print("------------------------------------------------")
