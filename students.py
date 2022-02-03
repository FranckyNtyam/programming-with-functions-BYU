"""
File Name: students.py

Author: Ntyam Adjomo Francky Ludovic

Purpose: 
Write a Python program named students.py that does the following:

1. Opens the students.csv file for reading, skips the first line of text in the file because it contains only headings, and reads the other lines of the file into a compound dictionary. The program must store each student I-Number as a key and each I-Number and name in a list as a value in the compound dictionary.
2. Gets an I-Number from the user, uses the I-Number to find the corresponding student name in the dictionary, and prints the name.
3. If a user enters an I-Number that doesn't exist in the dictionary, your program must print the message, "No such student" (without the quotes).
"""
import csv

def main():

     # Index of the phone number column
    # in the dentists.csv file.
    PHONE_INDEX = 0
    
    # Read the contents of the dentists.csv into a
    # compound dictionary named dentists_dict. Use
    # the phone numbers as the keys in the dictionary.
    students_dict = read_student_file("students.csv", PHONE_INDEX)

    # Print the dentists compound dictionary.
    print(students_dict)

    # Gets an I-Number from the user
    i_number = input("Please enter an I-Number (xxxxxxxxx): ")

    
    NAME_INDEX = 1
    # list contain student information.

    if i_number in students_dict:
         values_of_student = students_dict[i_number]
        # Get the name of student
         student_name = values_of_student[NAME_INDEX]
         print(student_name)
    else:
        print("No such student")
    


    


def read_student_file(filename, key_column_index):
    """Read the contents of a text file into a dictionary
    and return the dictionary that contains each student 
    I-Number as a key and each I-Number and name in a list
    as a value in the compound dictionary.

    Parameter filename: the name of the text file to read
    Return: a dictionary
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
