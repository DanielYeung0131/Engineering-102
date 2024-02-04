# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 5.4
# Date: 09/11/2023

from math import *

#input
temp = float(input('Enter the excess temperature: '))

#if-else
#if temp is less than 1.3
if temp < 1.3:
    print("Surface heat flux is not available")
#if temp is less than 5 and greater or equal 1.3
elif temp >=1.3 and temp < 5:
    print(f'The surface heat flux is approximately {round(1000 * pow((temp/1.3),(log(7000/1000)/log(5/1.3))))} W/m^2')
#if temp is less than 30 and greater or equal 5
elif temp >=5 and temp < 30:
    print(f'The surface heat flux is approximately {round(7000 * pow((temp/5),(log(1.5*10**6/7000)/log(30/5))))} W/m^2')
#if temp is less than 120 and greater or equal 30
elif temp >=30 and temp < 120:
    print(f'The surface heat flux is approximately {round(1.5*10**6 * pow((temp/30),(log(2.5*10**4/(1.5*10**6))/log(120/30))))} W/m^2')
#if temp is less than 1200 and greater or equal 120
elif temp >=120 and temp < 1200:
    print(f'The surface heat flux is approximately {round(2.5*10**4 * pow((temp/120),(log(1.5*10**6/(2.5*10**4))/log(1200/120))))} W/m^2')
#if temp is greater or equal 1200
else:
    print(f'Surface heat flux is not available')
