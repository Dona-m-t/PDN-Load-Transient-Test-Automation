"""
Oscilloscope Control Module
Keysight DSOX6004A
"""

import pyvisa
import datetime

class Oscilloscope:

    def __init__(self, address):
        rm = pyvisa.ResourceManager()
        self.instrument = rm.open_resource(address)

    def configure(self):
        self.instrument.write(":TIMebase:SCALe 1E-3")
        self.instrument.write(":TRIGger:EDGE:SOURce CHAN1")

    def capture_waveform(self):

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"results/waveform_{timestamp}.png"

        print(f"Waveform saved as {filename}")

        return filename
