# variable is a container for a value, and they behave as the value they contain 

name = "Mustafa"

#we are printing a variable, variable called name contains a string value "Mustafa"
# we can simply print the name just by print(name) but here we are concatenating a variable and a string 
print("My name is : " + name)

# here we are printing the datatype of name variable 
print(type(name))

first_name = "Muhammad"
last_name = "Mustafa"
# here we are concatinating 2 variables into one and storing the value in a new variable full_name
full_name = first_name + last_name

print(full_name)

#we can see we have no space between the Muhammad and Mustafa we need to add a space we can do it simply

full_name_with_space = first_name + " " + last_name
print(full_name_with_space)
print(type(full_name_with_space))

# now we will stor the integer in a variable 

print("****************************************************************************************")
print(" ")
print(" ")
age = 22
age = age + 1 # we can do math operation like this 
age += 1 #shorthand way of doing he same thing

print(age)
print(type(age))
# we cannot concatenate the string with integer so if we want to use an integer with a string 
# we need to convert the integer to string by type casting 
print("Hello, my name is "+ full_name_with_space+" and my age is " + str(age))


print("****************************************************************************************")
print(" ")
print(" ")
# now we are soting the a float value in a variable (value that containe the decimal)
height = 205.5
print(height)
print(type(height))

# same as integer if we want to print it with a string we just and to typecast it into string 
print("Hello my name is "+full_name_with_space+ "and my age is "+str(age)+" and my height is "+ str(height)+" cm")

print("****************************************************************************************")
print(" ")
print(" ")
#now are are storing the boolen values in the variable 
human = True
print(human)
print(type(human))

print("Are you a human? = "+str(human))


print("****************************************************************************************")
print(" ")
print(" ")
#Multiple assignment, assignment multiple value to multiple variables in one line of code

car, color, model, is_crashed = "Alto", "red", 2015, False

print(car)
print(color)
print(model)
print(is_crashed)

print("****************************************************************************************")
print(" ")
print(" ")

#assigning same values to multiple assignmnet 

ali_age = anas_age= farooq_age = 33
farooq_age +=1
anas_age = 55

print(ali_age)
print(anas_age)
print(farooq_age)
