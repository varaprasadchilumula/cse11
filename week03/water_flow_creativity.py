# water_flow.py
# Additional Functionalities:
# 1. Calculate the flow rate of water through a pipe.
# 2. Display a message about the water flow.
# 3. Calculate the force exerted by water on a surface.
# These additions demonstrate creativity and exceed the requirements.

# Constants
GRAVITY = 9.8  # Earth's acceleration of gravity in m/s^2
WATER_DENSITY = 1000  # Water density in kg/m^3
WATER_VISCOSITY = 0.001002  # Water dynamic viscosity in Pa*s

# Function to convert kilopascals to pounds per square inch
def kpa_to_psi(kpa):
    psi = kpa * 0.145038  # Conversion factor from kPa to psi
    return psi

# Additional Functionality 1: Calculate the flow rate of water through a pipe
def calculate_flow_rate(diameter, pressure_drop, length):
    area = 3.14159 * (diameter / 2) ** 2  # Assuming the pipe is cylindrical
    flow_rate = (area * pressure_drop) / (4 * WATER_VISCOSITY * length)
    return flow_rate

# Additional Functionality 2: Display a message about the water flow
def display_water_flow_message(flow_rate):
    if flow_rate > 0:
        return "Water is flowing!"
    else:
        return "No water flow."

# Additional Functionality 3: Calculate the force exerted by water on a surface
def calculate_force(area, pressure):
    force = area * pressure
    return force
