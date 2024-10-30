# we use nested loops when we have to iterate loop within a loop

rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
symbol = input("tell me the symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print("")
