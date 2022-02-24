'''
Input value of radius and print Area
~Akanksha
'''

#from the library math get value of pi
from math import pi

#first take radius as input from user
radius = input ("Enter radius of circle : ")

#convert radius to float
r = float(radius)

#calculate area
ar = pi * (r**2)

#display output
print ("The area of circle with radius " + radius + " is :")
#using the string value of radius (string concatenation)
print (ar)
