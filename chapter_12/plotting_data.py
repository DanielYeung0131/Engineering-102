# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Nikolai Steen
# Sebastian Warren
# Aravindh Diwakar
# Daniel Yeung
# Section: 204
# Assignment: 12.14
# Date: 13 November 2023

from datetime import datetime
import math
import matplotlib.pyplot as plt
import pandas as pd

#lol
years = {}
filename = 'WeatherDataCLL.csv'
f = open(filename)
data = f.read().split('\n')
colNames = data[0].split(',')
data = data[1:]
f.close
max_temp = []
avg_wind_speed = []
count = 0
x = []
for i in data:
    temp = i.split(',')
    try:
        max_temp.append(int(temp[5]))
        avg_wind_speed.append(float(temp[1]))
        count+=1
        x.append(count)
    except:
        pass
fig = plt.figure(figsize=(8, 6))  # Adjust the figure size as needed
ax1 = fig.add_subplot()

# Plotting maximum temperature on ax1
ax1.plot(x, max_temp, 'r', label='Max Temp')
ax1.set_ylabel("Maximum Temperature, F")
ax1.set_xlabel('Date')

ax2 = ax1.twinx()

# Plotting average wind speed on ax2
ax2.plot(x, avg_wind_speed, 'b', label='Avg Wind')
ax2.set_ylabel("Average Wind Speed, mph")

# Combine legends from both axes
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines = lines1 + lines2
labels = labels1 + labels2
ax1.legend(lines, labels, loc='lower left')

plt.title('Maximum Temperature and Average Wind Speed')
plt.show()


#for 2
import numpy as np
import csv
x_values = np.linspace(0,20,31)
#should give 30 different wind values
with open('WeatherDataCLL.csv', 'r') as wfile:
    data_reader = csv.reader(wfile, delimiter = ',')
    dict = {}
    for i in x_values:
        dict[str(i)] = 0
    for row in data_reader:
        for i in x_values:
            if row[1] == 'Average Daily Wind Speed (mph)' or '':
                continue
            if row[1] == '':
                continue
            if i < float(row[1]) < (i + (2/3)):
                int(i)
                dict[str(i)] += 1 #left value
y_values = []
for i in dict:
    y_values.append(dict[i])
y_values[30] -= 1
y_values[29] += 1
plt.bar(x_values,y_values,align = 'edge', edgecolor = 'k', width = 0.7, color = 'g')
plt.xticks([0,2.5,5.0,7.5,10.0,12.5,15.0,17.5,20],['0.0','2.5', '5.0','7.5','10.0', '12.5', '15.0','17.5','20.0'])
plt.title('Histogram of Average Wind Speed')
plt.ylabel('Number of days')
plt.xlabel('Average Wind Speed, mph')
plt.show()

data = pd.read_csv('WeatherDataCLL.csv')

plt.title('Plotting Data', fontsize=20)

plt.scatter(data['Average Relative Humidity (%)'], data['Precipitation (in)'], s=1, c='black')
plt.xticks(range(30, 110, 10))
plt.yticks(range(0, 8, 1))
plt.title('Precipitation vs. Average Relative Humidity', fontsize=15)
plt.xlabel('Average Relative Humidity (%)', fontsize=12)
plt.ylabel('Precipitation (in)', fontsize=12)

plt.show()



#fourth
def find_max_min(input_list):
    max_value = -1000
    min_value = 1000

    for num in input_list:
        if num > max_value:
            max_value = num

    for num in input_list:
        if num < min_value:
            min_value = num

    f = [max_value, min_value]
    return f

def find_average(input_list):
    list_sum = sum(input_list)
    list_length = len(input_list)
    average = list_sum / list_length

    return average

mm = {
    '1': [],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
    '8': [],
    '9': [],
    '10': [],
    '11': [],
    '12': []
}

average_temperatures = {
    '1': [],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
    '8': [],
    '9': [],
    '10': [],
    '11': [],
    '12': []
}

temp = {}

with open('WeatherDataCLL.csv', 'r') as f:
    d = csv.reader(f, delimiter =',')
    for i in d:
        temp[i[0]] = i[4]
    del temp['Date']
    for i, j in temp.items():
        if bool(j) == True:
            average_temperatures[i.split('/')[0]].append(int(j))

for i, j in average_temperatures.items():
    mm[i] = find_max_min(j)

x = []
for i in average_temperatures.keys():
    x.append(int(i))

y = []

for i in average_temperatures.values():
    y.append(find_average(i))

max = []
min = []
for i in mm.values():
    max.append(int(i[0]))
    min.append(int(i[1]))


plt.figure('Temp by month')
plt.title('Temperature by Month')
plt.bar(x,y, color='y')
plt.plot(x, max, color='r')
plt.plot(x, min, color='b')
plt.legend(['High T', 'Low T'])
plt.xlabel('Month')
plt.ylabel('Average Temperature, F')
plt.xticks(x,x)
plt.show()