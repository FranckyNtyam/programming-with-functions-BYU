"""
File Name: boxes.py

Author: Ntyam Adjomo Francky Ludovic

Purpose: Check your understanding of calling built-in Python functions and functions that are in a standard Python module.
"""
import math

number_Of_manufactured = int(input("Enter the number of items: "))

item_per_box = int(input("Enter the number of items per box: "))

print(f"For {number_Of_manufactured} items, packing {item_per_box} items in each box, you will need {math.ceil(number_Of_manufactured/item_per_box)} boxes.")