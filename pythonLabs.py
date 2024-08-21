#basic python

"""print("hello") # it prints hello to the terminal
print('hello') # it also prints hello to the terminal
#print(hello) # it gives an error

#math
print(4 + 5)

print (8 * 3)

print (4 /3)

print(4.0 / 3)

print(3 +5 *9)

#adding strings
print("abc" + "def")
print ("hello" + " " + "world")
print("123" + "5")

#variables
first = "hello"
second = "world"
third = first + " " + second
print(type(first))
print(first)
print (third)

#user input
name = input("what is your name?")
print(type(name))
age = input("What is your age?")
print(type(age))"""

#CONVERSIONS
#convert 32 degrees to radian
import math
degrees = 32
radian = degrees * (math.pi/180)
print(round(radian, 4))

#ASK user for the value of the radius and print out surface area and volume of a sphere
radius = float(input("Enter the value of the radius: "))
surfaceArea = 4 * math.pi * (radius**2)
volume = (4/3) * math.pi * (radius**3)
print(round(surfaceArea, 4))
print(round(volume, 4))

# what time of day it is
print(f"Its 3:38 pm, therefore its afternoon")

#split sentence into words
sentence = "Welcome to Accra"
words = sentence.split()
print(words)

#join a list of words
#way 1
print("Accra " + "is " + "a " + "big " + "city")
print(f"Accra is a big city")