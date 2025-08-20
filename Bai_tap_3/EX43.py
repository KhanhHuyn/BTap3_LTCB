# 43. Write a Python program to print the square and cube symbols in the area of a rectangle and
# the volume of a cylinder.
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3
from math import pi


def rectangle_area(length, width):
    return length * width


def cylinder_volume(radius, height):
    return pi * radius**2 * height


rectangle_length = float(input("Enter the length of the rectangle: "))
rectangle_width = float(input("Enter the width of the rectange: "))
print(f" The area of the rectangle is {rectangle_area(rectangle_length, rectangle_width):.2f}cm\u00b2")


cylinder_radius = float(input("Enter the radius of the cylinder: "))
cylinder_height= float(input("Enter the height of the cylinder: "))
print(f" The volume of the cylinder is {cylinder_volume(cylinder_radius, cylinder_height):.2f}cm\u00b3")