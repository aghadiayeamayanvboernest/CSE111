def main():
    # Prompt the user to input the first odometer reading in miles
    startng = float(input("Enter the first odometer reading (miles): "))
    # Prompt the user to input the second odometer reading in miles
    ending = float(input("Enter the second odometer reading (miles): "))
    # Prompt the user to input the amount of fuel used in gallons
    gallaon = float(input("Enter the amount of fuel used (gallons): "))

    # Calculate miles per gallon using the provided function
    mpg = miles_per_gallon(startng, ending, gallaon)
    # Convert miles per gallon to liters per 100 kilometers using the provided function
    lp100k = lp100k_from_mpg(mpg)
    # Print the result of miles per gallon calculation with two decimal points
    print(f"{mpg:.2f} miles per gallon")
    # Print the result of liters per 100 kilometers conversion with two decimal points
    print(f"{lp100k:.2f} liters per 100 kilometers")

def miles_per_gallon(starting, ending, gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    
    Parameters
        starting: An odometer value in miles.
        ending: Another odometer value in miles.
        gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    # Calculate miles per gallon by dividing the difference in miles by the amount of fuel used
    mpg = (ending - starting) / gallons

    return mpg

def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    
    Parameter 
        mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    # Convert miles per gallon to liters per 100 kilometers using the conversion factor 235.215
    lp100k = 235.215 / mpg
    return lp100k

main()