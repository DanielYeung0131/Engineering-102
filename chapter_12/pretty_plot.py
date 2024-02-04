# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 12.14.1: LAB: Pretty plot
# Date: 11/12/2023

import numpy as np
import matplotlib.pyplot as plt

# Initial point and matrix
point = np.array([0, 1])
matrix = np.array([[1.02, 0.095], [-0.095, 1.02]])

# Store the points for plotting
x_points = [point[0]]
y_points = [point[1]]

# Multiply the matrix by the point 250 times
for i in range(250):
    point = np.dot(matrix, point)
    x_points.append(point[0])
    y_points.append(point[1])

# Plotting the data
plt.figure('Pretty Plot', layout = 'constrained')
plt.plot(x_points, y_points, marker='o', linestyle='-')
plt.title('Matrix Multiplication Plot: The Fibonacci Spiral')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
