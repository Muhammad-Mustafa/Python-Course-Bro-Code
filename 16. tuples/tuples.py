#tuples are collections that are unchangeable

student = ("Mustafa", 22, "Male")

print(student.count("Male"))
print(student[1])
print(student.index(22))

for val in student:
  print(val)

if "Male" in student:
  print("The student gender is male")