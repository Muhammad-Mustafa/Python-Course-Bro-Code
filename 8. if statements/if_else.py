# if statement =  a block of code only runs when its TURE
# elif = if we have more conditions other then if statements we use elif
# else statement = when the IF statement is false then else stetement will run

age = int(input("What is your age : "))
if age == 100:
    print("you are a century old !!")
elif age > 18:
    print("You are an adult now!!")
elif age <= 18 and age > 0:
    print("You are still a kid buddy !")
else:
    print("you are not even born yet ;(")
