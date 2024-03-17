my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
my_dict[("year")] = 2018
print(my_dict)

######### Another Method use

my_dict.update({"year" : 2020})
print(my_dict)


print("\n \n")

#################### Python - Add Dictionary Items
my_dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
my_dict1[("color")] = "Red"
print(my_dict1)

########## Another Process
my_dict1.update({"color" : "Yeolow"})
print(my_dict1)

print("\n")
############## Pop Item any
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

######### Index Pop
thisdict.popitem()
print(thisdict)
