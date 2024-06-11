from fit_track import calculate_bmr, calculate_tdee, log_activity, log_food, generate_report
from pytest import approx
import pytest

# Sample user profiles for testing
user_profiles = [
    {'weight': 70, 'height': 175, 'age': 25, 'gender': 'male', 'activity_level': 'sedentary'},
    {'weight': 70, 'height': 175, 'age': 25, 'gender': 'male', 'activity_level': 'light'},
    {'weight': 70, 'height': 175, 'age': 25, 'gender': 'male', 'activity_level': 'moderate'},
    {'weight': 70, 'height': 175, 'age': 25, 'gender': 'male', 'activity_level': 'active'},
    {'weight': 70, 'height': 175, 'age': 25, 'gender': 'male', 'activity_level': 'very active'},
    {'weight': 70, 'height': 175, 'age': 25, 'gender': 'female', 'activity_level': 'sedentary'},
    {'weight': 70, 'height': 175, 'age': 25, 'gender': 'female', 'activity_level': 'light'},
    {'weight': 70, 'height': 175, 'age': 25, 'gender': 'female', 'activity_level': 'moderate'},
    {'weight': 70, 'height': 175, 'age': 25, 'gender': 'female', 'activity_level': 'active'},
    {'weight': 70, 'height': 175, 'age': 25, 'gender': 'female', 'activity_level': 'very active'},
]

# Test functions
def test_calculate_bmr():
    """
    Test function to verify the correctness of the calculate_bmr function.

    This function tests the calculate_bmr function by comparing its output
    against expected values for different combinations of weight, height, age, and gender.

    Test cases:
        - When the weight is 70 kg, height is 175 cm, age is 25 years, and gender is male,
          the BMR should be approximately 1673.75 calories/day with an absolute tolerance of 0.1 calories/day.
        - When the weight is 70 kg, height is 175 cm, age is 25 years, and gender is female,
          the BMR should be approximately 1509.75 calories/day with an absolute tolerance of 0.1 calories/day.

    The pytest.approx function is used to handle floating-point comparisons.
    """
    # Assert for male BMR calculation
    assert calculate_bmr(70, 175, 25, 'male') == pytest.approx(1673.75, 0.1)

    # Assert for female BMR calculation
    assert calculate_bmr(70, 175, 25, 'female') == pytest.approx(1509.75, 0.1)

def test_calculate_tdee():
    """
    Test function to verify the correctness of the calculate_tdee function.

    This function tests the calculate_tdee function by comparing its output
    against expected values for different combinations of user profile data.

    Test cases:
        - For each user profile, the BMR is calculated first.
        - Depending on the gender and activity level, the TDEE is calculated and compared with expected values.
        
    The pytest.approx function is used to handle floating-point comparisons.
    """
    for profile in user_profiles:
        # Calculate BMR based on profile data
        bmr = calculate_bmr(profile['weight'], profile['height'], profile['age'], profile['gender'])
        
        if profile['gender'] == 'male':
            # Test TDEE calculation for male profiles
            if profile['activity_level'] == 'sedentary':
                assert calculate_tdee(bmr, 'sedentary') == pytest.approx(2008.5, 0.1)
            elif profile['activity_level'] == 'light':
                assert calculate_tdee(bmr, 'light') == pytest.approx(2301.75, 0.1)
            elif profile['activity_level'] == 'moderate':
                assert calculate_tdee(bmr, 'moderate') == pytest.approx(2595.0, 0.1)
            elif profile['activity_level'] == 'active':
                assert calculate_tdee(bmr, 'active') == pytest.approx(2888.25, 0.1)
            elif profile['activity_level'] == 'very active':
                assert calculate_tdee(bmr, 'very active') == pytest.approx(3181.5, 0.1)
        
        elif profile['gender'] == 'female':
            # Test TDEE calculation for female profiles
            if profile['activity_level'] == 'sedentary':
                assert calculate_tdee(bmr, 'sedentary') == pytest.approx(1811.7, 0.1)
            elif profile['activity_level'] == 'light':
                assert calculate_tdee(bmr, 'light') == pytest.approx(2074.125, 0.1)
            elif profile['activity_level'] == 'moderate':
                assert calculate_tdee(bmr, 'moderate') == pytest.approx(2336.55, 0.1)
            elif profile['activity_level'] == 'active':
                assert calculate_tdee(bmr, 'active') == pytest.approx(2598.975, 0.1)
            elif profile['activity_level'] == 'very active':
                assert calculate_tdee(bmr, 'very active') == pytest.approx(2861.4, 0.1)

def test_log_activity():
    """
    Test function to verify the correctness of the log_activity function.

    This function tests the log_activity function by comparing its output
    against expected values for different fitness activities and durations.

    Test cases:
        - Asserts for calories burned during running and cycling activities.

    The pytest.approx function is used to handle floating-point comparisons.
    """
    # Assert for calories burned during running activity
    assert log_activity('running', 30, 70) == pytest.approx(343.5, 0.1)
    # Assert for calories burned during cycling activity
    assert log_activity('cycling', 45, 70) == pytest.approx(393.75, 0.1)


def test_log_food():
    """
    Test function to verify the correctness of the log_food function.

    This function tests the log_food function by comparing its output
    against an expected dictionary representing a logged food item.

    Test case:
        - Asserts that logging an apple with a quantity of 2 and 95 calories
          returns a dictionary with the expected food item, quantity, and calories.

    """
    # Assert for logging an apple with quantity 2 and 95 calories
    assert log_food('apple', 2, 95) == {'food_item': 'apple', 'quantity': 2, 'calories': 95}


def test_generate_report():
    """
    Test function to verify the correctness of the generate_report function.

    This function tests the generate_report function by comparing its output
    against expected values for a specific user profile, logged activities, and logged foods.

    Test case:
        - Asserts that generating a report for a specific user profile, with logged activities
          and foods, returns a report with the expected calories burned, calories consumed,
          and discounted calories.

    """
    # Define sample activities and foods
    activities = [
        {'activity': 'running', 'duration': 30, 'calories': 343.5}
    ]
    foods = [
        {'food_item': 'apple', 'quantity': 2, 'calories': 190}
    ]
    
    # Generate a report for the first user profile with the sample activities and foods
    report = generate_report(user_profiles[0], activities, foods)
    
    # Asserts for the generated report
    assert report['calories_burned'] == 343.5
    assert report['calories_consumed'] == 190
    assert report['discounted_calories'] == pytest.approx(171, 0.1)  # Assuming a discount on a discount day or before 11 AM


pytest.main(["-v", "--tb=line", "-rN", __file__])