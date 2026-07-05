# ----------------------------------------------------------
# config.py
# Configuration file for PDN Load Transient Test
# ----------------------------------------------------------
# This file stores the instrument addresses and test
# parameters used during automation.
# VISA addresses below are examples and should be replaced
# with the actual addresses available in the laboratory.
# ----------------------------------------------------------

# Example VISA Addresses

POWER_SUPPLY = "USB0::0x05E6::0x2230::PSU123456::INSTR"
ELECTRONIC_LOAD = "USB0::0x05E6::0x2380::LOAD123456::INSTR"
OSCILLOSCOPE = "USB0::0x0957::0x17A4::SCOPE123456::INSTR"
DMM = "USB0::0x05E6::0x6500::DMM123456::INSTR"


# -------------------------
# Test Parameters
# -------------------------

INPUT_VOLTAGE = 5.0
CURRENT_LIMIT = 3.5

# -------------------------
# Load Transient Settings
# -------------------------

LOW_LOAD = 0.5      # A
HIGH_LOAD = 3.0     # A
TRANSIENT_TIME = 10 # ms
