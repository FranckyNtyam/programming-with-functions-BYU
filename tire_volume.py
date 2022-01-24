"""
File Name: tire_volume.py

Author: Ntyam Adjomo Francky Ludovic

Purpose: 
1. Gets the current date from the computer's operating system.
2. Opens a text file named volumes.txt for appending.
3. Appends to the end of the volumes.txt file one line of text that contains the following five values:
    a. current date
    b. width of the tire
    c. aspect ratio of the tire
    d. diameter of the wheel
    e. volume of the tire

"""
# import the math module so that I can use math.pi and datetime.
import math
from datetime import datetime

current_date_and_time = datetime.now()

print("")

width_of_tire = int(input("Enter the width of the tire in mm (ex 205): "))

aspect_ratio_of_tire = int(input("Enter the aspect ratio of the tire (ex 60): "))

diameter_of_wheel = int(input("Enter the diameter of the wheel in inches (ex 15): "))

list_of_tire_price = [75, 79, 45, 99]

# calculate volume of tire

volume = math.pi * width_of_tire**2 * aspect_ratio_of_tire * (width_of_tire * aspect_ratio_of_tire + 2540 * diameter_of_wheel) / 10**10

print(f"\nThe approximate volume is {round(volume, 2)} liters")

if width_of_tire == 185 and aspect_ratio_of_tire == 60 and diameter_of_wheel == 14:
    print(f"Price of tire size is ${list_of_tire_price[0]} ")
elif width_of_tire == 195 and aspect_ratio_of_tire == 60 and diameter_of_wheel == 14:
    print(f"Price of tire size is ${list_of_tire_price[1]} ")
elif width_of_tire == 175 and aspect_ratio_of_tire == 65 and diameter_of_wheel == 15:
    print(f"Price of tire size is ${list_of_tire_price[2]} ")
elif width_of_tire == 205 and aspect_ratio_of_tire == 70 and diameter_of_wheel == 15:
    print(f"Price of tire size is ${list_of_tire_price[3]}")
else:
     print("\nNo price was found for those sizes.")
     


answer = input("do you wants to buy tires with the dimensions that you entered? ")
if answer.lower() == "yes":
        name_of_user = input("Enter your Name please ")
        phone_number = int(input("Enter your phone number for reservation please "))
else:
        name_of_user = None
        phone_number = None
        print("Please accept our apologies if you do not see the price that applies to you.")

# Open a text file named volumes.txt in append mode.
with open("volumes.txt", "at") as volume_file:

   
    
    print(f"{current_date_and_time:%Y-%m-%d}, {width_of_tire}, {aspect_ratio_of_tire}, {diameter_of_wheel}, {round(volume, 2)}, {name_of_user}, {phone_number}", file=volume_file)
    