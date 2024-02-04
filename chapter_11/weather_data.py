# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: 11.13
# Date: 11/6/2023

#import
import csv

z = {}
c = -1000000
d = 10000000
with open('WeatherDataCLL.csv','r') as file:
    a = csv.reader(file, delimiter=',')
    x = []
    for b in a:
        z[b[0]] = b[1:]
    del z['Date']
    for a in z:
        comp = z[a][4]
        try:
            if int(comp) > c:
                c = int(comp)
        except:
            continue
    print(f'10-year maximum temperature: {c} F')
    for a in z:
        try:
            comp = z[a][5]
            if int(comp) < d:
                d = int(comp)
        except:
            continue
    print(f'10-year minimum temperature: {d} F\n')

month = input('Please enter a month: ')
year = input('Please enter a year: ')
print()

print(f'For {month} {year}:')

temp = 0

count = 0


months = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

month = months[month]

for n in range(1,32):
    try:
        d = f'{month}/{n}/{year}'
        temp += float(z[d][3])
        count+=1
    except:
        break

temp = temp/count

print(f"Mean average daily temperature: {temp:.1f} F")

humid = 0
count = 0

for n in range(1,32):
    try:
        d = f'{month}/{n}/{year}'
        humid += float(z[d][2])
        count+=1
    except:
        break

humid = humid/count

print(f"Mean relative humidity: {humid:.1f}%")

wind = 0
count = 0

for n in range(1,32):
    try:
        d = f'{month}/{n}/{year}'
        wind += float(z[d][0])
        count+=1
    except:
        break

wind = wind/count


print(f"Mean daily wind speed: {wind:.2f} mph")

prec = 0
count = 0

for n in range(1,32):
    try:
        d = f'{month}/{n}/{year}'
        if float(z[d][1]) > 0:
            prec += 1
        count+=1
    except:
        break

prec = prec/count * 100
#print
print(f"Percentage of days with precipitation: {prec:.1f}%")
