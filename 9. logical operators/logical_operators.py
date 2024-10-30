# logical operators in python  ==> [and, not, or] they are use to check if two or more conditions

# wite a program in with we are checking the temprature, if the temp is 0-30 then temprature is good 
# if temp less than zero or greater than 30 return temprature is bad 

temp = int(input("Hey whats the temprature is today? "))

if temp>= 0 and temp <= 30:
  print("the temprature is good today you can go outside!!!")


elif temp <0 or temp> 30:
  print("temprate today is not good, please stay at home") 