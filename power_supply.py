# ----------------------------------------------------------
# power_supply.py
# Controls the Keithley 2230-30-1 Power Supply
# ----------------------------------------------------------

import pyvisa
class PowerSupply:
    def __init__(self, address):
        """
        Connect to the programmable power supply
        using its VISA address.
        """
        resource_manager = pyvisa.ResourceManager()
        self.instrument = resource_manager.open_resource(address)

    def configure(self, voltage, current):
        """
        Configure the output voltage
        and current limit.
        """
        self.instrument.write(f"VOLT {voltage}")
        self.instrument.write(f"CURR {current}")
        print(f"Power Supply Configured : {voltage} V , {current} A")

    def output_on(self):
        """
        Turn ON the output.
        """
        self.instrument.write("OUTP ON")
        print("Power Supply Output : ON")

    def output_off(self):
        """
        Turn OFF the output.
        """
        self.instrument.write("OUTP OFF")
        print("Power Supply Output : OFF")
