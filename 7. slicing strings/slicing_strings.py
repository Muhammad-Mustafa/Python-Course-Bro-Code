# slicing = create a substring by extracting elemetns from another string 
#     indexing [] or slice()
#   indexing [start:stop:step]  
# start is inclusive means whatever index value you provide it will take it as is "n"
# stop in exclusive means whatever index value you provide it will take it as "n-1"


name = "Muhammad Mustafa"

first_name = name[:8] # we can also write [0: 8] but if we dont provide the index python will assume the index is zero 
last_name = name[9:] # we can also write [9:16] but if we dont specify the index python will assume its the last index
funky_name = name[::2]
reversed_name = name[::-1]


print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)


website1 = "https://google.com"
website2 = "https://youtube.com"
print(website1[slice(8,-4)]) 

custom_slicer = slice(8,-4)

print(website2[custom_slicer])