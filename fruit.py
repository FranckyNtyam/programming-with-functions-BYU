"""
File Name: boxes.py

Author: Ntyam Adjomo Francky Ludovic

Purpose: Improve your ability to write object-oriented code.
"""

def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    # reverse and print fruit_list.
    fruit_list.reverse()
    print(f" Reverse list: { fruit_list} ")
    # append "orange" in the list
    fruit_list.append("orange")
    print(f"append orange: {fruit_list} ")

    #find where "apple is located in fruit_list"
    fruit_list.index("apple")
    fruit_list.insert(fruit_list.index("apple") - 1, "cherry")
    print(f"Insert cherry: {fruit_list}")

    # Remove "banana" in the list
    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list} ")

    # pop the element in the list

    popped_element =  fruit_list.pop()
    print(f"popped element: {popped_element} ")
    print(f"pop orange list: {fruit_list} ")

    # sort the list
    fruit_list.sort()
    print(f"Sorted list: {fruit_list} ")

    # clear the list 
    fruit_list.clear()
    print(f"Cleared list: {fruit_list} ")

# Call main to start this program.
if __name__ == "__main__":
    main()
