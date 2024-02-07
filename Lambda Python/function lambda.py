#1
def my_function(n):
    return lambda a : a *n

myDoubler = my_function(3)
print(myDoubler(11))

#2
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))


#3
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


