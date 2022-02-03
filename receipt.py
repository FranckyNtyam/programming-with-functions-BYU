"""
File Name: receipt.py

Author : Ntaym Adjomo Francky Ludovic

Purpose:
 write a program that reads the CSV file and prints to the terminal window 
 a receipt that lists the purchased items and shows the subtotal, the sales 
 tax amount, and the total.
"""
import csv

PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

def main():

     # Index of the phone number column
    # in the products.csv file.
    PRODUCT_INDEX = 0
    
    # Read the contents of the dentists.csv into a
    # compound dictionary named dentists_dict. Use
    # the phone numbers as the keys in the dictionary.
    products_dict = read_dict("products.csv", PRODUCT_INDEX)

    # Print the dentists compound dictionary.
    print(products_dict)

    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)

        next(reader)


        
        for row_list in reader:

            key_dict = row_list[0]
            request_quantity = row_list[1]
            value_dict = products_dict[key_dict]
            product_name = value_dict[PRODUCT_NAME_INDEX]
            product_price = value_dict[PRODUCT_PRICE_INDEX]

            print(product_name, request_quantity, product_price) 
              
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
    # to the opened file in a variable named text_file.
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