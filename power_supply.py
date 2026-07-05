"""
Power Supply Control Module
Keithley 2230-30-1
"""

import pyvisa

class PowerSupply:

    def __init__(self, address):
        rm = pyvisa.ResourceManager()
        self.instrument = rm.open_resource(address)

    def configure(self, voltage=5.0, current=3.5):
        self.instrument.write(f"VOLT {voltage}")
        self.instrument.write(f"CURR {current}")

    def output_on(self):
        self.instrument.write("OUTP ON")

    def output_off(self):
        self.instrument.write("OUTP OFF")
