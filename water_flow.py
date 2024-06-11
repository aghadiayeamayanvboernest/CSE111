
# Constants for water properties.
# These constants represent the density, gravity, and viscosity of water, which are used in various calculations.
density = 998.2  # Density of water in kilograms per cubic meter (kg/m^3).
gravity = 9.80665  # Acceleration due to gravity on Earth's surface in meters per second squared (m/s^2).
viscosity = 0.0010016  # Dynamic viscosity of water in Pascal seconds (Pa*s).

def water_column_height(tower_height, tank_height):
    """
    Calculate the height of a water column given a tower height and tank wall height.

    Parameters
    ----------
    tower_height : float
        Height of the tower.
    tank_height : float
        Height of tank walls on top of the tower.

    Returns
    -------
    float
        Height of the water column.
    """
    height = tower_height + (3 * tank_height) / 4
    return height


def pressure_gain_from_water_height(height):
    """
    Calculate the pressure caused by Earth’s gravity pulling on the water stored in an elevated tank.

    Parameters
    ----------
    height : float
        Height of the water column in meters.

    Returns
    -------
    float
        Pressure exerted by the water column in kilopascals (kPa).
    """
   

    pressure = (density * gravity * height) / 1000
    return pressure


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculate and return the water pressure lost due to friction within a pipe.

    This function calculates the pressure loss experienced by water flowing through a pipe
    due to friction between the water and the walls of the pipe. The pressure loss is
    expressed in units of kilopascals (kPa).

    Parameters
    ----------
    pipe_diameter : float
        The diameter of the pipe through which water is flowing, in meters (m).
    pipe_length : float
        The length of the pipe through which water is flowing, in meters (m).
    friction_factor : float
        The friction factor of the pipe, which affects the friction between the water
        and the pipe walls.
    fluid_velocity : float
        The velocity of water flow through the pipe in meters per second (m/s).

    Returns
    -------
    float
        The water pressure lost due to friction within the pipe, expressed in kilopascals (kPa).
    """ 

    

    loss_pressure = -(friction_factor * pipe_length * density * fluid_velocity ** 2) / (2000 * pipe_diameter)
    return loss_pressure
def pressure_loss_from_fittings(quantity_fittings, fluid_velocity):
    """
    Calculate and return the water pressure lost due to fittings such as 45° and 90° bends in a pipeline.

    This function calculates the pressure loss experienced by water flowing through a pipeline
    due to fittings such as bends. The pressure loss is expressed in units of kilopascals (kPa).

    Parameters
    ----------
    fluid_velocity : float
        The velocity of water flow through the pipeline in meters per second (m/s).
    quantity_fittings : int
        The total quantity of fittings, such as 45° and 90° bends, in the pipeline.

    Returns
    -------
    float
        The water pressure lost due to fittings within the pipeline, expressed in kilopascals (kPa).
    """
   
    loss_pressure_fittings = (-0.04 * density * fluid_velocity**2 * quantity_fittings) /2000
    return loss_pressure_fittings
def reynolds_number(hydraulic_diameter, fluid_velocity): 
    """Calculate and return the Reynolds number for a pipe with water flowing through it.

    The Reynolds number is a unitless ratio of the inertial and viscous forces in a fluid
    that is useful for predicting fluid flow in different situations.

    Parameters
 
        hydraulic_diameter : float
            The hydraulic diameter of the pipe, which is a measure of the effective diameter for flow calculations, in meters (m).
        fluid_velocity : float
            The velocity of water flow through the pipe in meters per second (m/s).

    Returns
    float
        The Reynolds number, a unitless ratio of inertial and viscous forces in the fluid.
    """
   
    reynolds = (density * hydraulic_diameter * fluid_velocity) /viscosity
    return reynolds
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculate and return the water pressure lost due to water moving from a pipe with a large diameter
    into a pipe with a smaller diameter.

    This function calculates the pressure loss experienced by water flowing from a pipe with a large diameter
    into a pipe with a smaller diameter, taking into account the fluid velocity, Reynolds number, and diameters
    of both pipes.

    Parameters

    larger_diameter : float
        The diameter of the larger pipe, from which water moves, in meters (m).
    fluid_velocity : float
        The velocity of water flow through the pipe in meters per second (m/s).
    reynolds_number : float
        The Reynolds number, a unitless ratio of inertial and viscous forces in the fluid.
    smaller_diameter : float
        The diameter of the smaller pipe, into which water moves, in meters (m).

    Returns
  
    float
        The water pressure lost due to water moving from a pipe with a large diameter into a pipe with a smaller diameter,
        expressed in kilopascals (kPa).
    """
   
    k = (0.1 + 50/reynolds_number) * ((larger_diameter/smaller_diameter)**4 - 1)
    loss_pressure_from_pipe_reducton = -(k * density * fluid_velocity**2) / 2000
    return loss_pressure_from_pipe_reducton


def kpa_to_psi(pressure):
    """
    Convert pressure from kilopascals (kPa) to pounds per square inch (psi).

    Parameters
    ----------
    pressure : float
        Pressure value in kilopascals (kPa).

    Returns
    -------
    float
        Pressure value converted to pounds per square inch (psi).
    """
    # 1 kPa = 0.145038 psi
    pressure_psi = pressure * 0.145038
    return pressure_psi



PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss


   # Convert the pressure from kilopascals (kPa) to pounds per square inch (psi)
    pressure_psi = kpa_to_psi(pressure)


    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house in psi: {pressure_psi:.1f} pounds per square inch")
main() 
print()