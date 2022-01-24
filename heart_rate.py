"""
File name: heart_rate.py

Author: Ntyam Adjomo Francky Ludovic

Purpose: Write a Python program named heart_rate.py that asks for a person's age and computes and outputs the slowest and fastest rates necessary to strengthen his heart.

When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

age = int(input("Please enter your age: "))

heart_rate_min = (220 - age) * 0.65

heart_rate_max = (220 - age) * 0.85
print(f"When you exercise to strengthen your heart, you should keep your heart rate between {int(heart_rate_min)} and {int(heart_rate_max)} beats per minute.")