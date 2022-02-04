"""
File Name: receipt.py

Author : Ntaym Adjomo Francky Ludovic

Purpose:
 write a program that reads the CSV file and prints to the terminal window 
 a receipt that lists the purchased items and shows the subtotal, the sales 
 tax amount, and the total.
"""
import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

 # Index of the product number, name , and price column
 # in the products.csv file.
PRODUCT_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2  




def main():

    try:

        # Read the contents of the products.csv into a
        # compound dictionary named products_dict. Use
        # product number as the keys in the dictionary.
        products_dict = read_dict("products.csv", PRODUCT_INDEX)

        # Print the products.dict compound dictionary.
        # print(products_dict)

        # Print the store name
        print("Inkom Emporium")

        print("")

        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)

            next(reader)

            # Variable that will contain the number of items ordered by customer.
            number_of_item_order = 0

            # Variable that will contain the subtotal of items price.
            subtotal = 0
            
            for row_list in reader:
                
                # Get the key of compound dictionary products_dict
                # in the request.csv file.
                key_dict = row_list[0]

                # Get quantity of each item ordered by customer.
                quantity = int(row_list[1])

                # dictionary values as list
                value_dict = products_dict[key_dict]

                # Get the name of product
                product_name = value_dict[PRODUCT_NAME_INDEX]

                # Get the price of product
                product_price = float(value_dict[PRODUCT_PRICE_INDEX])

                # get the total number of items ordered by the customer
                number_of_item_order += int(quantity )

                # Get of the subtotal of items price.
                subtotal += quantity * product_price

                print(f"{product_name}, {quantity} @ {product_price}") 

            print(" ")

            # Calculate the sales tax price.
            sales_tax = subtotal * 0.06
            
            # Calculate the total price of Items.
            total = subtotal + sales_tax

            # print number of items, subtotal, sales tax, and total.
            print(f"Number of Items: {number_of_item_order} ")
            print(f"Subtotal: {round(subtotal, 2)} ")
            print(f"Sales Tax: {round(sales_tax, 2)} ")
            print(f"Total: {round(total, 2)} ")
            
            print("")
            print("Thank you for shopping at the Inkom Emporium.") 

            # Print the current day of the week and the current time.
            print(f"{current_date_and_time: %c}")
    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.")





              
def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
     # Create an empty list that will store
    # the lines of text from the text file.
    dictionary = {}

    # Open the text file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

         reader = csv.reader(csv_file)
         
         next(reader)

         # Read the contents of the text
         # file one line at a time.
         for row_list in reader:
            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row_list[key_column_index]

             # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row_list
     
    return dictionary      

# Call main to start this program.
if __name__ == "__main__":
    main()