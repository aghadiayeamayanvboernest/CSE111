from water_flow import pressure_gain_from_water_height, water_column_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction, kpa_to_psi
from pytest import approx 
import pytest 

def test_water_column_height():
    """Test function to verify the correctness of the water_column_height function.
    This function tests the water_column_height function by comparing its output
    against expected values for different combinations of tower heights and tank
    wall heights.

    Test cases:
    - When the tower height and tank wall height are both 0, the water column height
    should be 0.
    - When the tower height is 0 and the tank wall height is 10, the water column
    height should be 7.5.
    - When the tower height is 25 and the tank wall height is 0, the water column
    height should be equal to the tower height (25).
    - When the tower height is 48.3 and the tank wall height is 12.8, the water column
    height should be 57.9.

    The pytest.approx function is used to handle floating-point comparisons.
    """

    assert water_column_height(0.0, 0.0) == approx(0.0)
    assert water_column_height(0.0, 10.0) == approx(7.5)
    assert water_column_height(25.0, 0.0) == approx(25.0)
    assert water_column_height(48.3, 12.8) == approx(57.9)

def test_pressure_gain_from_water_height():
    """
Test function to verify the correctness of the pressure_gain_from_water_height function.

This function tests the pressure_gain_from_water_height function by comparing its output
against expected values for different heights of the water column.

Test cases:
- When the height of the water column is 0, the pressure should be approximately 0 kPa.
- When the height of the water column is 30.2 meters, the pressure should be approximately 295.628 kPa.

The pytest.approx function is used to handle floating-point comparisons.
"""

    assert pressure_gain_from_water_height(0) == approx(0.000, abs=0.01)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.01)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.01)

def test_pressure_loss_from_pipe(): 
    """
    Test function to verify the correctness of the pressure_loss_from_pipe function.

    This function tests the pressure_loss_from_pipe function by comparing its output
    against expected values for different combinations of pipe diameter, pipe length,
    friction factor, and fluid velocity.

    Test cases:
        - When the pipe diameter is 0.048692 meters, the pipe length is 0 meters,
        the friction factor is 0.018, and the fluid velocity is 1.75 meters per second,
         the pressure loss should be approximately 0 kPa with an absolute tolerance of 0.001 kPa.
        - Similarly, you can add test cases for the remaining combinations of parameters.

    The pytest.approx function is used to handle floating-point comparisons.
    """ 
    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) ==approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) ==approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) ==approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) ==approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) ==approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) ==approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) ==approx(-110.884, abs=0.001)

def test_pressure_loss_from_fittings():
    """
    Test function to verify the correctness of the pressure_loss_from_fittings function.

    This function tests the pressure_loss_from_fittings function by comparing its output
    against expected values for different combinations of fluid velocity and quantity of fittings.

    Test cases:
        - When the fluid velocity is 0.00 m/s and there are 3 fittings, the pressure loss should be approximately 0.000 kPa.
        - When the fluid velocity is 1.65 m/s and there are 0 fittings, the pressure loss should be approximately 0.000 kPa.
        - When the fluid velocity is 1.65 m/s and there are 2 fittings, the pressure loss should be approximately -0.131 kPa.
        - When the fluid velocity is 1.75 m/s and there are 2 fittings, the pressure loss should be approximately -0.139 kPa.
        - When the fluid velocity is 1.75 m/s and there are 5 fittings, the pressure loss should be approximately -0.873 kPa.

    The pytest.approx function is used to handle floating-point comparisons.
    """    
    assert pressure_loss_from_fittings(0.00, 3) ==approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) ==approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) ==approx(-0.131, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) ==approx(-0.139, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) ==approx(-0.873, abs=0.001)
def test_reynolds_number():
    """
    Test function to verify the correctness of the reynolds_number function.

    This function tests the reynolds_number function by comparing its output
    against expected values for different combinations of hydraulic diameter
    and fluid velocity.

    Test cases:
    - When the hydraulic diameter is 0.048692 meters and the fluid velocity is 0 m/s, 
      the Reynolds number should be approximately 0.
    - When the hydraulic diameter is 0.048692 meters and the fluid velocity is 1.65 m/s, 
      the Reynolds number should be approximately 80069.
    - When the hydraulic diameter is 0.048692 meters and the fluid velocity is 1.75 m/s, 
      the Reynolds number should be approximately 84922.
    - When the hydraulic diameter is 0.286870 meters and the fluid velocity is 1.65 m/s, 
      the Reynolds number should be approximately 471729.
    - When the hydraulic diameter is 0.286870 meters and the fluid velocity is 1.75 m/s, 
      the Reynolds number should be approximately 500318.
 
    The pytest.approx function is used to handle floating-point comparisons.
    """
    assert reynolds_number(0.048692, 0.00) == approx(0, abs=1)
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert reynolds_number(0.286870, 1.65) == approx(471729, abs=1)
    assert reynolds_number(0.286870, 1.75) == approx(500318, abs=1)
def test_pressure_loss_from_pipe_reduction():   
    """
    Test function to verify the correctness of the pressure_loss_from_pipe_reduction function.
    This function tests the pressure_loss_from_pipe_reduction function by comparing its output
    against expected values for different combinations of larger and smaller pipe diameters,
    fluid velocities, Reynolds numbers, and expected pressure losses.

    Test cases:
        - Call pressure_loss_from_pipe_reduction with provided parameters and verify the calculated
        pressure loss using pytest.approx for floating-point comparisons.

    The pytest.approx function is used to handle floating-point comparisons.
    """
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) ==approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) ==approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) ==approx(-184.182, abs=0.001)


def test_kpa_to_psi():
    """
    Test the conversion function from kilopascals (kPa) to pounds per square inch (psi).

    This test function verifies that the conversion function kpa_to_psi() accurately converts
    pressure values from kilopascals to pounds per square inch (psi). It asserts that when a pressure
    of 158.6 kPa is converted, the result is approximately 23.0 psi with an absolute tolerance of 0.1 psi.
    """
    assert kpa_to_psi(158.6) == approx(23.0, abs=0.1)
    assert kpa_to_psi(100) == approx(14.504, abs=0.01)
    assert kpa_to_psi(200) == approx(29.008, abs=0.01)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])