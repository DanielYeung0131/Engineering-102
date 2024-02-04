# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 1.13
# Date: 08/23/2023

## guess the number

import math
import random

print("This shows the evaluation of sin(x-1)/(x-1) evaluated close to x=1")
print("My guess is 2")


#numbers
x=1.1
print(math.sin(x-1)/(x-1))
x=1.01
print(math.sin(x-1)/(x-1))
x=1.001
print(math.sin(x-1)/(x-1))
x=1.0001
print(math.sin(x-1)/(x-1))
x=1.00001
print(math.sin(x-1)/(x-1))
x=1.000001
print(math.sin(x-1)/(x-1))
x=1.0000001
print(math.sin(x-1)/(x-1))
x=1.00000001
print(math.sin(x-1)/(x-1))
print()

print("My guess was a little off")
