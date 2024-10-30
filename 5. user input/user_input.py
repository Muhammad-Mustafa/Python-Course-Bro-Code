name = input("What is your name : ")

# here we can see we have asked the age of the user but the input only retuns a string so if we want to get the input in integer
# we need to typecast that string to integer same for float and boolen values 
age = input("What is your age : ") 
print("Hello "+ name)
print("age " + age)
print ("The data type of age : "+ str(type(age)))

print("Now we need to convert the data type of age in string to we are asking again, so this time we will save the integer value ")
age  = int(input("what is your age again : "))


print("Hello "+ name)
print("age " + str(age))
print ("The data type of age : "+ str(type(age)))

print("So you will be "+str(age + 1)+" next year !")