# ----------------------------------------------------------
# dmm.py
# Controls the Keithley DMM6500 Digital Multimeter
# ----------------------------------------------------------
import pyvisa
class DigitalMultimeter:
    def __init__(self, address):
        """
        Connect to the Digital Multimeter
        using its VISA address.
        """
        resource_manager = pyvisa.ResourceManager()
        self.instrument = resource_manager.open_resource(address)
        
    def measure_voltage(self):
        """
        Measure the output voltage.
        """
        voltage = self.instrument.query("MEAS:VOLT?")
        print(f"Measured Voltage : {voltage}")
        return voltage
