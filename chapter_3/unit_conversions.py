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

#input
quantity = float(input('Please enter the quantity to be converted: '))


def pounds_to_newtons(quantity):
  return f'{quantity:.2f} pounds force is equivalent to {quantity*4.44822:.2f} Newtons'


def meters_to_feet(quantity):
  return f'{quantity:.2f} meters is equivalent to {quantity*3.2808399:.2f} feet'


def atmospheres_to_kilopascals(quantity):
  return f'{quantity:.2f} atmospheres is equivalent to {quantity*101.325:.2f} kilopascals'


def lps_to_gpm(quantity):
  return f'{quantity:.2f} liters per second is equivalent to {quantity*15.8503231:.2f} US gallons per minute'


def degrees_celsius_to_degrees_fahrenheit(quantity):
  return f'{quantity:.2f} degrees Celsius is equivalent to {(quantity*9/5)+32:.2f} degrees Fahrenheit'


def watt_to_btu(quantity):
  return f'{quantity:.2f} watts is equivalent to {3.4121416331*quantity:.2f} BTU per hour'


print(pounds_to_newtons(quantity))
print(meters_to_feet(quantity))
print(atmospheres_to_kilopascals(quantity))
print(watt_to_btu(quantity))
print(lps_to_gpm(quantity))
print(degrees_celsius_to_degrees_fahrenheit(quantity))
