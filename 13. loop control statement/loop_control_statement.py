# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

# while True:
#  name = input("What is your name ")
#  if name != "":
#    break


phone_number = "0315-9658-552"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
