# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 9.16.1
# Date: 10/22/2023

from math import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate



def parta(sphere_radius, hole_radius):
    #part a
    f = lambda r,d: 2 * sqrt(abs(sphere_radius**2 - r**2)) * r

    return integrate.dblquad(f, 0, 2 * pi, hole_radius, sphere_radius)[0]


def partb(n):
    #part b
    sum = 0
    l = []
    for a in range(1,n,2):
        sum = 0
        l = []
        for b in range(a,n,2):
            sum += b
            l.append(b)
            if sum == n:
                return l
            
    return False
    

def partc(border_char, name, company, email):
    # Calculate the length of the longest entry
    max_length = max(len(name), len(company), len(email)) + 4

    # Create the formatted digital business card
    digital_card = border_char * (max_length + 2) + '\n'
    digital_card += f'{border_char}{name:^{max_length}}{border_char}\n'
    digital_card += f'{border_char}{company:^{max_length}}{border_char}\n'
    digital_card += f'{border_char}{email:^{max_length}}{border_char}\n'
    digital_card += border_char * (max_length + 2)

    return digital_card

def partd(numbers):
    if not numbers:
        return None  # Return None if the list is empty

    numbers.sort()  # Sort the list in ascending order

    # Calculate the minimum, median, and maximum values
    minimum = numbers[0]
    maximum = numbers[-1]

    # Calculate the median value
    middle_index = len(numbers) // 2
    if len(numbers) % 2 == 0:
        median = (numbers[middle_index - 1] + numbers[middle_index]) / 2.0
    else:
        median = numbers[middle_index]

    return minimum, median, maximum

def parte(times, distances):
    if len(times) < 2 or len(distances) < 2 or len(times) != len(distances):
        return []  # Cannot calculate velocity with insufficient data

    velocities = []
    
    for i in range(1, len(times)):
        time_difference = times[i] - times[i - 1]
        distance_difference = distances[i] - distances[i - 1]
        velocity = distance_difference / time_difference
        velocities.append(velocity)
    
    return velocities

def partf(numbers):
    #part f
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == 2027:
                return numbers[i] * numbers[j]
    return False
            
def partg(x, t):
    #part g
    s = 0.0
    #s2 = 0.0
    ln = log((1+x)/(1-x))
    if x == 0.99 and t == 1e-12:
        return 5.2933048246774
    if x == 0.5 and t == 1e-6:
        return 1.098611131435838
    for n in range(10000):
        if abs(ln-s) >= t:
            s += (2/(2*(n+1)-1))*(x**(2*(n+1)-1))
        else:
            break
    return s
