# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Nikolai Steen
# Sebastian Warren
# Aravindh Diwakar
# Daniel Yeung
# Section: 204
# Assignment: 6.12
# Date: 18 September 2023

# pyramids

from math import *

def pyramid_area(layers, surface_area, side_length):
    if layers > 0:
        surface_area += ((sqrt(3)/4 * side_length**2 * layers**2) - (sqrt(3)/4 * side_length**2 * ((layers-1)**2))) + (side_length**2 * (3*layers))
        layers -= 1
        return pyramid_area(layers, surface_area, side_length)
    
    return surface_area

side_length = float(input('Enter the side length in meters: '))
layers = int(input('Enter the number of layers: '))
print(f'You need {pyramid_area(layers, 0, side_length):.2f} m^2 of gold foil to cover the pyramid')

