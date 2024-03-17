my_dictionary =  {
    "name" : "JIM",
    "age" : 24,
    "District" : "Manikjong"
}
######### Both Value nad key print Dictionary
for x , y in my_dictionary.items():
    print(f"Key ->{x}, value ->{y}")

##### Value Print Only
for y in my_dictionary.values():
    print(y)
########### Key Print Only
for x in my_dictionary.keys():
    print(x)


############## Copy the Dictionary Values
copy_dict = my_dictionary.copy()
print(copy_dict)
