# Type casting is when you convert the data type of a variable to another data type

x, y, z = 5, 65.8, "5"
print("The Type of X is " + str(type(x)))
print("The Type of Y is " + str(type(y)))
print("The Type of Z is " + str(type(z)))

x, y, z = str(5), str(65.8), int("5")

print("The value of X is " + str(x))
print("The value of Y is " + str(y))
print("The value of Z is " + str(z))

print("The Type of X is " + str(type(x)))
print("The Type of Y is " + str(type(y)))
print("The Type of Z is " + str(type(z)))
