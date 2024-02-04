# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 4.14 LAB: Pretty equation
# Date: 09/06/2023

from math import *

a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

d = a
e = b
f = c

if a == 0:
    a = ""
elif a ==1:
    a = "x^2"
elif a == -1:
    a = "- x^2"
elif a > 1:
    a = f'{a}x^2'
elif a < -1:
    a = f'- {abs(a)}x^2'

if b == 0:
    b = ""
elif b == 1:
    if d == 0:
        b = "x"
    else:
        b = " + x"
elif b == -1:
    b = " - x"
elif b > 1 and d == 0:
    b = f'{b}x'
elif b > 1 and d != 0:
    b = f' + {b}x'
else:
    b = f' - {abs(b)}x'

if c == 0:
    c = ""
elif c > 0 and e != 0:
    c = f' + {c}'
elif c > 0 and e == 0:
        c = f'{c}'
else:
    c = f' - {abs(c)}'

#equation
print(f"The quadratic equation is {a}{b}{c} = 0")