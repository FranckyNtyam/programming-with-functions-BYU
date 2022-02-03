"""
File Name: provinces.py

Author: Ntyam Adjomo Francky Ludovic

Purpose: Check your understanding of text files and lists by writing a program that reads the contents of a text file into a list and then changes some of the values in the list.
"""
def main():
    #Read the contents of the file into a list
    provinces_list = read_list("provinces.txt")

    print(provinces_list)

    # Remove the first element from the list.
    provinces_list.pop(0)

    # Remove the last elemnent from the list.
    provinces_list.pop()

    # Replace all occurrences of "AB" in the list with "Alberta".
    for elem in range(len(provinces_list)):

        if provinces_list[elem] == 'AB':
            provinces_list[elem] = 'Alberta'

    print(provinces_list)

    # Number of elements that are "Alberta"

    print(f"Alberta occurs {provinces_list.count('Alberta')} times in the modified list.")


def read_list(filename):
    """Read the contents of a text file into a list
    and return the list that contains the lines of text.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

         # Read the contents of the text
         # file one line at a time.
         for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()
            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)
    # Return the list that contains the lines of text.
    return text_list 

if __name__ == "__main__":
    main()  



