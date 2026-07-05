"""
Configuration file containing instrument VISA addresses
and test parameters.
Replace the VISA addresses with actual addresses during testing.
"""

# VISA Resource Addresses (Example)
POWER_SUPPLY = "USB0::0x05E6::0x2230::PSU123456::INSTR"
ELECTRONIC_LOAD = "USB0::0x05E6::0x2380::LOAD123456::INSTR"
OSCILLOSCOPE = "USB0::0x0957::0x17A4::SCOPE123456::INSTR"
DMM = "USB0::0x05E6::0x6500::DMM123456::INSTR"

# Test Parameters
INPUT_VOLTAGE = 5.0
CURRENT_LIMIT = 3.5

# Load Transient Parameters
LOAD_LOW = 0.5
LOAD_HIGH = 3.0
TRANSIENT_DURATION_MS = 10
