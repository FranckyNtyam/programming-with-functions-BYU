"""
File Name: can_sizes.py

Author: Ntyam Adjomo Francky Ludovic

Purpose: 
Write a Python program named can_sizes.py that computes and prints the storage efficiency for each of the following 12 steel can sizes. Then visually examine the output and answer this question, "Which can size has the highest storage efficiency?"

Name	           Radius                              Height                Cost per Can
                (centimeters)	                     (centimeters)	         (U.S. dollars)
#1 Picnic	      6.83	                                  10.16                   $0.28
#1 Tall	7.78	11.91	$0.43
#2	8.73	11.59	$0.45
#2.5	10.32	11.91	$0.61
#3 Cylinder	10.79	17.78	$0.86
#5	13.02	14.29	$0.83
#6Z	5.40	8.89	$0.22
#8Z short	6.83	7.62	$0.26
#10	15.72	17.78	$1.53
 #211	6.83	12.38	$0.34
 #300	7.62	11.27	$0.38
 #303	8.10	11.11	$0.42

"""
import math

def main():
    """
    Call the compute_volume and compute_surface_area functions to compute.
    """
    #list of different radius and height argument
    radius_list = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    height_list = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    name_list_of_can = ["#1 Pinic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "6Z", "#8Z short", "#10", "#211", "#300", "#303"]

    length = 0
    while length != len(radius_list):
        storage_efficiency = compute_volume(radius_list[length], height_list[length]) / compute_surface_area(radius_list[length], height_list[length])
        print(f"{name_list_of_can[length]} {storage_efficiency:.1f}")
        length += 1
    


def compute_volume(radius, height):
    """

    compute and return the volume area of circle 
    """
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    """
    compute and return the surface area of circle
    """
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

# Start this program by
# calling the main function.
main()  