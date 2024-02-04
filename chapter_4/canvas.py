# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: Week 3 Canvas Lab (individual—groupwork allowed): Rockets' Red Glare 
# Date: 09/04/2023

from math import sqrt

#part 1
a = 1/7
print(a)
b = a*7
print(b)

c = 2*a
d = 5*a
e = c+d
print(e)

x = sqrt(1/3) 
print("x =", x)
y = x*x*3
print("x*x*3 =", y)
z = x*3*x
print("x*3*x =", z)

#part 2
FIRST_STOP = 0.3
SECOND_GO = 0.4
STEP_SIZE = 0.1

current_increment = int(input("Current increment: ")) 

distance_traveled = current_increment * STEP_SIZE

if distance_traveled == FIRST_STOP:
    print("Stop the first stage!")
elif distance_traveled == SECOND_GO:
    print("Start the second stage!")
else:
    print("No action required at this point")

# When we multiply 0.1 with 3 in python, it doesn't print "Stop the first stage!" because 0.1*3 gives us 0.30000000000000004 in python.
# This is due to round-off errors.
# This program is calculating the distance traveled based on the input value/current increment. The program will tell you when distance reaches 0.3 km (First stop) and 0.4 km (Second stop). 

#part 3

TOL = 1e-08

if abs(distance_traveled - 0.3) < TOL:
    print("Stop the first stage!")
elif distance_traveled == SECOND_GO:
    print("Start the second stage!")
else:
    print("No action required at this point")


TOL = 1e-16 # 1e-16 will be the least; 1e-17 will return no action required.

if abs(distance_traveled - 0.3) < TOL:
    print("Stop the first stage!")
elif distance_traveled == SECOND_GO:
    print("Start the second stage!")
else:
    print("No action required at this point")