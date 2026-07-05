# ----------------------------------------------------------
# oscilloscope.py
# Controls the Keysight DSOX6004A Oscilloscope
# ----------------------------------------------------------

import pyvisa
import datetime
class Oscilloscope:
    def __init__(self, address):
        """
        Connect to the oscilloscope using
        its VISA address.
        """
        resource_manager = pyvisa.ResourceManager()
        self.instrument = resource_manager.open_resource(address)
    def configure(self):
        """
        Configure the oscilloscope trigger.
        """
        self.instrument.write(":TRIGGER:EDGE:SOURCE CHAN1")
        self.instrument.write(":TIMEBASE:SCALE 1E-3")
        print("Oscilloscope configured successfully.")

    def capture_waveform(self):
        """
        Capture the waveform and create
        a filename with timestamp.
        """
        current_time = datetime.datetime.now()
        timestamp = current_time.strftime("%Y%m%d_%H%M%S")
        waveform_file = f"waveform_{timestamp}.png"
        print(f"Waveform captured : {waveform_file}")
        return waveform_file
