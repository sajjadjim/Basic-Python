def my_function(num):
  return 5 * num

print(my_function(3))
print(my_function(5))
print(my_function(9))

 
def my_function(x, /):
  print(x)

my_function(3)

#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(x):
  print(x)
my_function(x = 3)

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
