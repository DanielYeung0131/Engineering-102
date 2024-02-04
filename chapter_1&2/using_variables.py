# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 2.9
# Date: 08/23/2023

import math

#force
mass = 27
acceleration = 1.5
print("Force is", mass * acceleration, "N")
#wavelength
distance = 0.025
degree = 7*math.pi/36
print("Wavelength is", 2 * distance * math.sin(degree), "nm")
#radon-222
N0 = 27
t = 5
half_life = 3.8
print("Radon-222 left is", N0*math.pow(2, -t/half_life), "g")
#pressure
moles = 5
vol = 0.27
temp = 415
constant = 8.314
print("Pressure is", (constant*moles*temp/vol)/1000 , "kPa")





