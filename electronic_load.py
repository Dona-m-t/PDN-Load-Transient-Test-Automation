"""
Electronic Load Control Module
Keithley 2380
"""

import pyvisa

class ElectronicLoad:

    def __init__(self, address):
        rm = pyvisa.ResourceManager()
        self.instrument = rm.open_resource(address)

    def configure(self):
        self.instrument.write("MODE CC")

    def run_transient(self, low_current, high_current):
        self.instrument.write(f"CURR {low_current}")
        self.instrument.write(f"CURR {high_current}")

    def disable(self):
        self.instrument.write("INPUT OFF")
