
# Author: Aghadiaye Amayanvbo Ernest
# Purpose: This program is designed to track fitness activities and manage calorie intake. It allows users to log their activities and food consumption, calculates their Basal Metabolic Rate (BMR) and Total Daily Energy Expenditure (TDEE), and generates progress reports to help users monitor their fitness goals and make informed decisions about their diet and exercise routines.

from datetime import datetime

def calculate_bmr(weight, height, age, gender):
    """
    Calculates Basal Metabolic Rate (BMR) using the Mifflin-St Jeor Equation.

    Parameters
    ----------
    weight : float
        Weight of the individual in kilograms.
    height : float
        Height of the individual in centimeters.
    age : int
        Age of the individual in years.
    gender : str
        Gender of the individual. Can be 'male' or 'female'.

    Returns
    -------
    float
        Basal Metabolic Rate (BMR) based on the Mifflin-St Jeor Equation.

    Notes
    -----
    The Mifflin-St Jeor Equation is a widely used formula for estimating BMR:
    
    For men:
    BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5

    For women:
    BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161
    
    References
    ----------
    Mifflin MD, St Jeor ST, Hill LA, Scott BJ, Daugherty SA, Koh YO. A new predictive equation for resting energy expenditure in healthy individuals. Am J Clin Nutr. 1990 Feb;51(2):241-7. doi: 10.1093/ajcn/51.2.241. PMID: 2305711.
    """
    try:
        if gender.lower() == 'male':
            return (10 * weight) + (6.25 * height) - (5 * age) + 5
        elif gender.lower() == 'female':
            return (10 * weight) + (6.25 * height) - (5 * age) - 161
        else:
            raise ValueError("Gender must be 'male' or 'female'")
    except ValueError as e:
        print(f"Error: {e}")
        return None


def calculate_tdee(bmr, activity_level):
    """
    Calculates Total Daily Energy Expenditure (TDEE) based on Basal Metabolic Rate (BMR) and activity level.

    Parameters
    ----------
    bmr : float
        Basal Metabolic Rate (BMR) of the individual.
    activity_level : str
        Activity level of the individual. Can be one of the following:
        - 'sedentary': Little to no exercise
        - 'light': Light exercise/sports 1-3 days a week
        - 'moderate': Moderate exercise/sports 3-5 days a week
        - 'active': Hard exercise/sports 6-7 days a week
        - 'very active': Very hard exercise/sports & physical job or training twice a day

    Returns
    -------
    float
        Total Daily Energy Expenditure (TDEE) based on BMR and activity level.

    Raises
    ------
    ValueError
        If the provided activity level is not one of the predefined levels.

    Notes
    -----
    The activity level determines the multiplier applied to BMR to estimate TDEE.
    The following multipliers are used:
    - Sedentary: 1.2
    - Light: 1.375
    - Moderate: 1.55
    - Active: 1.725
    - Very active: 1.9
    The calculated TDEE represents the total number of calories burned per day, including activity.
    """
    try:
        activity_multipliers = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725,
            'very active': 1.9
        }
        if activity_level.lower() not in activity_multipliers:
            raise ValueError("Invalid activity level")
        return bmr * activity_multipliers[activity_level.lower()]
    except ValueError as e:
        print(f"Error: {e}")
        return None
def log_activity(activity, duration, weight):
    """
    Calculates the calories burned during a specific activity.

    Parameters
    ----------
    activity : str
        The type of activity performed. Can be one of the following:
        - 'running'
        - 'cycling'
        - 'weightlifting'
    duration : float
        The duration of the activity performed, in minutes.
    weight : float
        The weight of the individual performing the activity, in kilograms.

    Returns
    -------
    float
        The total calories burned during the activity.

    Raises
    ------
    ValueError
        If the provided activity type is not one of the predefined types.

    Notes
    -----
    This function calculates the calories burned during a specific activity based on the Metabolic Equivalent of Task (MET) values.
    MET values represent the energy cost of various physical activities relative to resting metabolism.
    The activity types and their corresponding MET values used in the calculation are as follows:
    - Running: MET = 9.8
    - Cycling: MET = 7.5
    - Weightlifting: MET = 3.0
    The total calories burned during the activity are calculated using the formula:
    Calories burned = MET * weight * duration / 60
    where duration is measured in minutes.
    This function can be used to track and monitor calorie expenditure during different physical activities.

    Example
    -------
    >>> log_activity('running', 30, 70)
    686.0
    """
    try:
        activity_met = {
            'running': 9.8,
            'cycling': 7.5,
            'weightlifting': 3.0
        }
        if activity.lower() not in activity_met:
            raise ValueError("Invalid activity type")
        return activity_met[activity.lower()] * weight * duration / 60
    except ValueError as e:
        print(f"Error: {e}")
        return None
def log_food(food_item, quantity, calories):
    """
    Logs a food item along with its quantity and calorie count.

    Parameters
    ----------
    food_item : str
        The name or description of the food item.
    quantity : float
        The quantity or serving size of the food item.
    calories : int
        The calorie count of the food item per serving.

    Returns
    -------
    dict
        A dictionary representing the logged food item, including its name, quantity, and calorie count.

    Notes
    -----
    This function is used to record the consumption of a specific food item.
    It stores information such as the name of the food item, the quantity consumed, and the corresponding calorie count per serving.
    The logged information can be used for tracking daily calorie intake, nutritional analysis, or dietary monitoring.

    Example
    -------
    >>> log_food('Apple', 1, 95)
    {'food_item': 'Apple', 'quantity': 1, 'calories': 95}
    """
    return {'food_item': food_item, 'quantity': quantity, 'calories': calories}
def generate_report(user_profile, activities, foods):
    """
    Generates a daily report including calories burned, calories consumed, discounted calories consumed, and a survey invitation.

    Parameters
    ----------
    user_profile : dict
        The user's profile containing relevant information such as age, weight, height, etc.
    activities : list of dict
        A list of activities performed by the user, each containing information about the activity such as type and calories burned.
    foods : list of dict
        A list of foods consumed by the user, each containing information about the food such as name and calories.

    Returns
    -------
    dict
        A dictionary representing the daily report, including the following key-value pairs:
        - 'calories_burned': Total calories burned from activities
        - 'calories_consumed': Total calories consumed from foods
        - 'discounted_calories': Total calories consumed after applying a discount based on the current date and time
        - 'survey_invitation': A message prompting the user to complete an online survey for feedback.

    Notes
    -----
    This function generates a daily report for the user, summarizing their calorie intake and expenditure for the day.
    It calculates the total calories burned from performed activities and the total calories consumed from consumed foods.
    Additionally, it applies a discount to the total calories consumed based on the current date and time.
    The discounted calories represent the adjusted calorie intake after applying the discount.
    The function also includes a survey invitation encouraging the user to provide feedback through an online survey.

    Example
    -------
    >>> user_profile = {'age': 30, 'weight': 70, 'height': 175}
    >>> activities = [{'activity': 'running', 'calories': 300}, {'activity': 'cycling', 'calories': 200}]
    >>> foods = [{'food_item': 'Apple', 'calories': 95}, {'food_item': 'Chicken', 'calories': 250}]
    >>> generate_report(user_profile, activities, foods)
    {'calories_burned': 500, 'calories_consumed': 345, 'discounted_calories': 345, 'survey_invitation': 'Please complete our online survey for feedback!'}
    """
    report = {}
    total_calories_burned = sum(activity['calories'] for activity in activities)
    total_calories_consumed = sum(food['calories'] for food in foods)
    
    discount = 0.10 if datetime.now().weekday() in [1, 2] or datetime.now().hour < 11 else 0
    discounted_calories = total_calories_consumed * (1 - discount)
    
    report['calories_burned'] = total_calories_burned
    report['calories_consumed'] = total_calories_consumed
    report['discounted_calories'] = discounted_calories
    report['survey_invitation'] = "Please complete our online survey for feedback!"
    
    return report
def get_user_profile():
    """
    Collects and returns user profile information from input prompts.

    Prompts the user to enter their age, weight, height, gender, and activity level, 
    and returns this data as a dictionary.

    Returns
    -------
    dict
        A dictionary containing the user's age, weight, height, gender, and activity level.
    """
    try:
        age = int(input("Enter your age: "))
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in cm): "))
        gender = input("Enter your gender (male/female): ")
        activity_level = input("Enter your activity level (sedentary, light, moderate, active, very active): ")
        return {'age': age, 'weight': weight, 'height': height, 'gender': gender, 'activity_level': activity_level}
    except ValueError as e:
        print(f"Error: {e}")
        return None

def update_user_profile(user_profile):
    """
    Updates user profile information with new input values.

    Prompts the user to update their age, weight, height, gender, and activity level. 
    If the user provides new values, the corresponding fields in the user profile are updated. 
    If the user leaves a prompt blank, the current value is retained.

    Parameters
    ----------
    user_profile : dict
        A dictionary containing the user's current profile information, 
        including 'age', 'weight', 'height', 'gender', and 'activity_level'.

    Returns
    -------
    None
        The function updates the `user_profile` dictionary in place.
    """
    try:
        print("Update your profile information (leave blank to keep current value):")
        age = input(f"Enter your age [{user_profile['age']}]: ")
        weight = input(f"Enter your weight (in kg) [{user_profile['weight']}]: ")
        height = input(f"Enter your height (in cm) [{user_profile['height']}]: ")
        gender = input(f"Enter your gender (male/female) [{user_profile['gender']}]: ")
        activity_level = input(f"Enter your activity level (sedentary, light, moderate, active, very active) [{user_profile['activity_level']}]: ")
        
        if age: user_profile['age'] = int(age)
        if weight: user_profile['weight'] = float(weight)
        if height: user_profile['height'] = float(height)
        if gender: user_profile['gender'] = gender
        if activity_level: user_profile['activity_level'] = activity_level
    except ValueError as e:
        print(f"Error: {e}")

def main():
    print()
    # Print a welcome message to the user
    print("Welcome to the Fitness Tracking and Calorie Management Tool (FitTrack)")

    try:
        # Get user profile information by calling the get_user_profile function
        user_profile = get_user_profile()
        if not user_profile:
            # If user profile retrieval fails, print an error message and exit the function
            print("Failed to get user profile. Exiting.")
            return

        # Calculate BMR using user profile details
        bmr = calculate_bmr(user_profile['weight'], user_profile['height'], user_profile['age'], user_profile['gender'])
        if bmr is None:
            # If BMR calculation fails, print an error message and exit the function
            print("Failed to calculate BMR. Exiting.")
            return

        # Calculate TDEE using BMR and activity level from user profile
        tdee = calculate_tdee(bmr, user_profile['activity_level'])
        if tdee is None:
            # If TDEE calculation fails, print an error message and exit the function
            print("Failed to calculate TDEE. Exiting.")
            return

        # Print calculated BMR and TDEE values
        print()
        print(f"Basal Metabolic Rate (BMR): {bmr} calories/day")
        print(f"Total Daily Energy Expenditure (TDEE): {tdee} calories/day")
        print()

        #Initializes empty lists to store logged activities and food intake, then enters an infinite loop
        # where it continuously prompts the user to choose an action: log activity, log food, update profile, 
        # generate report, or quit.
        # 1. Initializes `activities` and `foods` lists to store logged data.
        # 2. Prompts the user to input an action:
            #  'a': Logs a fitness activity, appends it to the `activities` list, and prints a confirmation message
            # - 'f': Logs a food item, appends it to the `foods` list, and prints a confirmation message.
            # - 'u': Updates the user profile by calling `update_user_profile`, recalculates BMR and TDEE, and prints the updated values.
            #  - 'r': Generates a progress report by calling `generate_report` and prints the report.
            # - 'q': Exits the loop and prints a farewell message.
            # - Any other input results in an error message prompting the user to choose again.
        # 3. Includes exception handling to catch any unexpected errors and print an error message with the exception details.


        # Initialize empty lists to store logged activities and food intake
        activities = []
        foods = []

        while True:
            # Prompt user to choose an action: log activity, log food, update profile, generate report, or quit
            action = input("Would you like to log an activity (a), log food (f), update profile (u), generate report (r), or quit (q)? ").lower()
            
            if action == 'a' or action == 'log an activity' or action == 'activity':
                # Log a fitness activity
                activity = input("Enter activity (running, cycling, weightlifting): ")
                duration = float(input("Enter duration in minutes: "))
                calories_burned = log_activity(activity, duration, user_profile['weight'])
                if calories_burned is not None:
                    # Append logged activity to the activities list
                    activities.append({'activity': activity, 'duration': duration, 'calories': calories_burned})
                    # Print confirmation of the logged activity
                    print(f"Logged {activity} for {duration} minutes, burning {calories_burned} calories.")
            
            elif action == 'f' or action == 'log food' or action == 'food':
                # Log a food item
                food_item = input("Enter food item: ")
                quantity = int(input("Enter quantity: "))
                calories = float(input("Enter calories: "))
                food_log = log_food(food_item, quantity, calories)
                # Append logged food item to the foods list
                foods.append(food_log)
                # Print confirmation of the logged food item
                print(f"Logged food: {food_item}, quantity: {quantity}, calories: {calories}.")
            
            elif action == 'u' or action == 'user profile' or action == 'profile':
                # Update user profile information
                update_user_profile(user_profile)
                # Recalculate BMR and TDEE with updated profile information
                bmr = calculate_bmr(user_profile['weight'], user_profile['height'], user_profile['age'], user_profile['gender'])
                if bmr is None:
                    print("Failed to calculate BMR. Exiting.")
                    return

                tdee = calculate_tdee(bmr, user_profile['activity_level'])
                if tdee is None:
                    print("Failed to calculate TDEE. Exiting.")
                    return

                # Print updated BMR and TDEE values
                print(f"Updated Profile. New BMR: {bmr}, New TDEE: {tdee}.")
            
            elif action == 'r' or action == 'generate report' or action == 'report' :
                # Generate and print a progress report
                report = generate_report(user_profile, activities, foods)
                print(f"Report: {report}")
            
            elif action == 'q' or action == 'quit':
                # Exit the program with a farewell message
                print("Exiting the program. Stay healthy!")
                break

            else:
                # Print an error message for invalid actions
                print("Invalid action. Please choose again.")

    except Exception as e:
        # Catch any unexpected exceptions and print an error message
        print("An error occurred:", e)

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()