"""
File Name: discount.py

Author: Ntyam Adjomo Francky Ludovic

Purpose: Improve my understanding of calling built-in Python functions and calling functions and methods that are in a standard Python module.
"""
from datetime import datetime

current_date_and_time = datetime.now()

day_of_week = 2

discount_amont = 0

subtotal = -1

while subtotal != 0:
    subtotal = float(input("Please enter the subtotal: "))
    sales_tax = subtotal * 0.06
   
    if day_of_week == 1 or day_of_week == 2 :

         discount_amount = subtotal * 0.1

         print(f"Discount amount: {round(discount_amount, 2)}")

    print(f"Sales tax amount: {round(sales_tax, 2)} ")
    