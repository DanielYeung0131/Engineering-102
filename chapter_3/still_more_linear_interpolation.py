# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Nikolai Steen
# Sebastian Warren
# Aravindh Diwakar
# Daniel Yeung
# Section: 204
# Assignment: 3.15
# Date: 30 August 2023

#functions for xyz
def xFunc(x2, x1, t, t2, t1):
  return ((x2 - x1)/(t2 - t1)) * (t - t1) + x1

def yFunc(y2, y1, t, t2, t1):
  return ((y2 - y1)/(t2 - t1)) * (t - t1) + y1
  
def zFunc(z2, z1, t, t2, t1):
   return ((z2 - z1)/(t2 - t1)) * (t - t1) + z1

t1 = float(input('Enter time 1: '))
x1 = float(input('Enter the x position of the object at time 1: '))
y1 = float(input('Enter the y position of the object at time 1: '))
z1 = float(input('Enter the z position of the object at time 1: ')) 

t2 = float(input('Enter time 2: '))
x2 = float(input('Enter the x position of the object at time 2: '))
y2 = float(input('Enter the y position of the object at time 2: '))
z2 = float(input('Enter the z position of the object at time 2: ')) 
time_interval = (t2-t1)/4
times = [t1,t1+time_interval,t1+(2*time_interval),t1+(3*time_interval),t2]
print(" ")
for t in times:
    print(f'At time {t:.2f} seconds the object is at ({xFunc(x2, x1, t, t2, t1):.3f}, {yFunc(y2, y1, t, t2, t1):.3f}, {zFunc(z2, z1, t, t2, t1):.3f})')
