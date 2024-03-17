child1 = {
  "name" : "sajjad Jim",
  "year" : 1999
}
child2 = {
  "name" : "XYZ",
  "year" : 2001
}
child3 = {
  "name" : "ABCD",
  "year" : 2011
}

myfamily = {
  "myself1" : child1,
  "myself2" : child2,
  "myself3" : child3
}
print(f"Nested Dictionary print -> {myfamily}")

##############################################################
myfamily = {
  "child1" : {
    "name" : "Sajjad",
    "year" : 2004
  },
  "child2" : {
    "name" : "Hossain",
    "year" : 2007
  },
  "child3" : {
    "name" : "Jim",
    "year" : 2011
  }
}
print(F"Print my name ->{myfamily["child2"]["name"]}")
