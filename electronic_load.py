# ----------------------------------------------------------
# electronic_load.py
# Controls the Keithley 2380 Electronic Load
# ----------------------------------------------------------

import pyvisa
class ElectronicLoad:
    def __init__(self, address):
        """
        Connect to the electronic load using
        the VISA address.
        """
        resource_manager = pyvisa.ResourceManager()
        self.instrument = resource_manager.open_resource(address)

    def configure(self):
        """
        Configure the electronic load in
        Constant Current (CC) mode.
        """
        self.instrument.write("MODE CC")
        print("Electronic Load : Constant Current Mode Enabled")

    def run_transient(self, low_current, high_current):
        """
        Apply a simple load transient by changing
        the current from LOW_LOAD to HIGH_LOAD.
        """
        print(f"Applying Load : {low_current} A")
        self.instrument.write(f"CURR {low_current}")
        print(f"Changing Load : {high_current} A")
        self.instrument.write(f"CURR {high_current}")

    def disable(self):
        """
        Disable the electronic load.
        """
        self.instrument.write("INPUT OFF")
        print("Electronic Load : OFF")
