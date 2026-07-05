"""
Digital Multimeter Module
Keithley DMM6500
"""

import pyvisa

class DigitalMultimeter:

    def __init__(self, address):
        rm = pyvisa.ResourceManager()
        self.instrument = rm.open_resource(address)

    def measure_voltage(self):
        return self.instrument.query("MEAS:VOLT?")
