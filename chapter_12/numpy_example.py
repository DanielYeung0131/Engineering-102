# By submitting this assignment, I agree to the following:
  # "Aggies do not lie, cheat, or steal, or tolerate those who do"
  # "I have not given or received any unauthorized aid on this assignment."
  #
  # Names: Nikolai Steen
  # Sebastian Warren
  # Aravindh Diwakar
  # Daniel Yeung
  # Section: 204
  # Assignment: 12.12.1: LAB: Numpy example
  # Date: 13 November 2023

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import numpy as np

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

# Create matrices A, B, and C
A = np.arange(12).reshape(3, 4)
B = np.arange(8).reshape(4, 2)
C = np.arange(6).reshape(2, 3)

# Print matrices A, B, and C
print("A =")
print(A)
print("\nB =")
print(B)
print("\nC =")
print(C)

# Compute the product D = ABC
D = np.dot(np.dot(A, B), C)
print("\nD =")
print(D)

# Print the transpose of D
print("\nD^T =")
print(np.transpose(D))

# Calculate and print E = sqrt(D) / 2
E = np.sqrt(D) / 2
print("\nE =")
print(E)