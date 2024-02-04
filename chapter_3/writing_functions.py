from math import *

# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 3.18
# Date: 08/29/2023
# simple functions definitions, one for each shape
# these stay at the top of your program, only the imports and your header go earlier


def triangle(a):    # btw, "a" up here = "side" from down in the main program
    area = a * a * sin(pi*1/3) / 2 # what goes here?
    print(f'A triangle with side {a:.2f} has area {area:.3f}') # what goes in here?

def square(a):
    area = a * a
    print(f'A square with side {a:.2f} has area {area:.3f}')

def pentagon(a):
    area = 5 * (a * ((a/2) / tan(pi*36/180)) / 2)
    print(f'A pentagon with side {a:.2f} has area {area:.3f}')

def dodecagon(a):
    area = 3 * (2 + sqrt(3)) * a**2
    print(f'A dodecagon with side {a:.2f} has area {area:.3f}')


# this is the main program area down here
side = float(input("Please enter the side length: "))      # <-- get input from user here 
triangle(side)         # <-- then we start 'calling' the functions, one at a time
square(side)
pentagon(side)
dodecagon(side)