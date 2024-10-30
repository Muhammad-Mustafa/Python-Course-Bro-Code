# list = used to store multiple values in a variable

colors = ["red", "blue", "green", "pink"]
print(colors[:2])

colors[2] = "black"
print(colors)

for x in colors:
    print(x)

colors.append("white")
print(colors)

colors.remove("blue")
print(colors)

colors.pop()
print(colors)

colors.insert(0, "brown")
print(colors)

colors.sort()
print(colors)

colors.clear()
print