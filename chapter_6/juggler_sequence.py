# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 6.15 LAB: Juggler sequence
# Date: 09/18/2023

from math import *

num = int(input("Enter a positive integer: "))
count = 0
numlist = [num]
n = num

#while loop
while num > 1:
    if num % 2 == 0:
        num = int(sqrt(num))
        count += 1
        numlist.append(num)
    else:
        num = int(floor(num ** 1.5))
        count += 1
        numlist.append(num)


print(f'The Juggler sequence starting at {n} is: ')
print(*numlist, sep=", ")
print(f'It took {count} iterations to reach 1')