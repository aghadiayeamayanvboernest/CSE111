"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
    
print("enter the following information")
print()
age = int(input ("what your age?: "))
max_range = 220-age
lowest = max_range * .65
heigest = max_range * .85

print("when you exercise to strength your heart, you should ")
print(f"keep your heart rate between {lowest:.0f} and {heigest:.0f} \nbeats per minute")
print()




