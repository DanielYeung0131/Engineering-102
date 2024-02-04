# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Nikolai Steen
# Sebastian Warren
# Aravindh Diwakar
# Daniel Yeung
# Section: 204
# Assignment: 6.11
# Date: 18 September 2023

# pyramids

from math import *

side_length = float(input('Enter the side length in meters: '))
layers = int(input('Enter the number of layers: '))
pyramid = 0
surface_area = 0

for i in range(layers, 0, -1):
  pyramid += i**2
  surface_area += ((sqrt(3) / 4 * side_length**2 * i**2) -
                   (sqrt(3) / 4 * side_length**2 *
                    ((i - 1)**2))) + (side_length**2 * (3 * i))

print(f'You need {surface_area:.2f} m^2 of gold foil to cover the pyramid')
