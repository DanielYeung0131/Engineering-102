from math import *
# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 4.16
# Date: 09/04/2023

#input
a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))

if a != 0:
    if b**2 - 4*a*c < 0:
        print(f"The roots are x = {-b/(2*a)} + {sqrt(abs(b**2 - 4*a*c))/2}i and x = {-b/(2*a)} - {sqrt(abs(b**2 - 4*a*c))/2}i")
    elif b**2 - 4*a*c == 0:
        print(f"The root is x = {((-b + sqrt(b**2 - 4*a*c) )/(2*a)): .1f}")
    else:
        print(f"The roots are x = {(-b + sqrt(b**2 - 4*a*c) )/(2*a): .1f} and x = {(-b - sqrt(b**2 - 4*a*c) )/(2*a): .1f}")
elif b != 0:
   print(f"The root is x = {-c/b}")
else:
    print("You entered an invalid combination of coefficients!")