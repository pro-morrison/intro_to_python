#print ("Hello world")
#print ('hello')

#data types
"""
a = 3.56788
b = 23
c = True
d = "happy day"

print(type(a))
print(type(b))
print(type(c))
print(type(d))

#type conversion
print (int (a))
print (float(b))
print (str(a))
print(type(a))

#concatenation. you can only concatenate strings in python
print('my ' + 'name ' + 'is ' + 'Yasmin')
"""

#user input. it aslways comes as astring when you use input function as a
#method of getting input.
name = input('please enter your name: ')
age = input("please enter your age: ")
newAge = int(age) + 5

#print ("my " + "name " + "is " + name + " and " + 
 #      "i " + "am " + str(newAge))

# use f string instead of concatenation top print out strings.
print(f"Your name is {name} and you are {newAge}")

#indexing : accessing an element by the index
#slicing : accessing multiple elements by the index

word = "helicopter"
print(word[2])
print(word[0:4])