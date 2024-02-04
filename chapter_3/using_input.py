import math
# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 3.17
# Date: 08/28/2023

#force
print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg): "))
acceleration = float(input("Please enter the acceleration (m/s^2): "))
force = mass*acceleration
print(f'Force is {force:.1f} N')

print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm): "))
degree = float(input("Please enter the angle (degrees):"))
wavelength = 2 * distance * math.sin(math.pi * (degree / 180))
print(f'Wavelength is {wavelength: .4f} nm')

print("This program calculates how much Radon-222 is left given time and initial amount")
time = float(input("Please enter the time (days): "))
amount = float(input("Please enter the initial amount (g): "))
radon = amount*math.pow(2, -time/3.8)
print(f'Radon-222 left is {radon: .2f} g')

print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
vol = float(input("Please enter the volume (m^3): "))
temp = float(input("Please enter the temperature (K): "))
pressure = int(round((8.314 * temp * moles / vol)/1000))
print(f'Pressure is {pressure: d} kPa')