# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Nikolai Steen
# Sebastian Warren
# Aravindh Diwakar
# Daniel Yeung
# Section: 204
# Assignment: Week 9 Team Programs (Canvas Lab—Deep Plots by Jack Handy) 
# Date: 18 October 2023
import matplotlib.pyplot as plt
import math

list_t = [0, 0.45, 1.1, 1.75, 2.25, 2.7]
list_y = [0, 0.23, 0.4, 0.18, 0.07, 0.01]
plt.figure('Frodo likes this.', layout = 'constrained')

plt.subplot(2,1,1)
plt.plot(list_t,list_y,marker = 'o', linestyle = ' ', color = 'k')
plt.title("Data and two curves vs. time")
plt.xlabel("time")
plt.ylabel("y")
plt.ylim(-0.1,max(list_y)+0.6)
plt.xlim(0,max(list_t)+0.3)


func_vals_t = []
func_vals_y = []
func_vals_y2 = []
for i in range(51):
    t = 0 + i/16.67
    y = t**4*math.exp(-t**2)
    y2 = t**2*math.exp(-t**2)
    func_vals_t.append(t)
    func_vals_y.append(y)
    func_vals_y2.append(y2)
plt.plot(func_vals_t,func_vals_y2,color = 'red')
plt.plot(func_vals_t,func_vals_y,color = 'blue') 

plt.legend(['data', 't^2 exp(-t^2)', 't^4 exp(-t^2)'])


plt.subplot(2,1,2)
plt.plot(list_t,list_y, marker = '^', color = 'y')
plt.xlim(1.0,2.0)
plt.ylim(0,0.5)
plt.title("Data interpolation and Curve 1")
plt.xlabel("time")
plt.ylabel("y")
plt.plot(func_vals_t,func_vals_y2, color = 'blue')
plt.annotate("It's closest here!", xy = (1.4,0.27),xycoords = 'data', xytext=(-10, -40), textcoords = "offset points", arrowprops=dict(arrowstyle = '->'), horizontalalignment='center', verticalalignment='bottom')
plt.legend(['data','t^2 exp(-t^2)' ])


plt.show()