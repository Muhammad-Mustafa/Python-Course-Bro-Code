# changeable unordered collection of unique key value pairs 

capitals ={
  "USA": "Washington DC",
  "China": "Beijing",
  "Russia": "Moscow",
  "Pakistan": "Islamabad"
}

print(capitals.get("Germany"))
print(capitals.get("Pakistan"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({"Germany": "Berlin"})
capitals.update({"Pakistan": "Karachi"})

for key,val in capitals.items():
  print(key, val)

capitals.pop("USA")

for key,val in capitals.items():
  print(key,val)