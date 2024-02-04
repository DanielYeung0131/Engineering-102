# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 2.8
# Date: 08/23/2023

import math

y = 23027 - 2027
x = 55-10
#part 1
print("Part 1:")
print("For t = 25 minutes, the position p =", (y/x) * (25-10) +2027, "kilometers")
#part 2
print("Part 2:")
print("For t = 300 minutes, the position p =", ((y/x) * (300 -10) + 2027) % (2 * math.pi *6745), "kilometers")
