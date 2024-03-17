########################################### Dictionary Function Using  #######################
person = {'name': 'Jim', 'age': 30, 'city': 'Dhaka'}


########################## Key Print the ############################################################
for value in person.keys():
    print(f"Print only value : {value}")

######### Update Value ########
person.update({'name':'XYZ'})
person['age']= 25


############## Update Value ############
person.update({'gender' :'Male'})
person['gender'] = 'Male'

############ Print Dictionary items #####################
for value in person.items():
    print(value)

############################### Specific Key & Item Print the value #################################
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for key, item in thisdict.items():
  print(key, item)
