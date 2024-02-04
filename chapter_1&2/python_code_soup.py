# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 2.11
# Date: 08/23/2023

x = 1
y = 10
z = 0

z += x #z = 1
print(z) 

x += 1 # x = 2
y *= x # y = 20
z += y
x += 1 # x = 3
z += x
z += x
print(z) #z = 27

y *= x
z += y
x += 1
x += 1
z += x
z += x
z += x
print(z)

y = 10
x = y
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
z = 0
z += y
print(z)

z = 0
y = 10
y *= x
y *= x
x = 1
x += 1
y *= x
y *= x
y *= x
z += y
y = 10
x = y
y *= x
x = y
y += x
y += x
y += x
y += x
y += x
z += y
x = 1
y = 10
x += 1
x += 1
x += 1
x += 1
y += x
y *= x
z += y
print(z)