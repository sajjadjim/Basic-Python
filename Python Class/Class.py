#Create a Class
class MyClass :
    x = 5

p1 = MyClass()  #MyClass class initial the new name
print(p1.x)

#New Code
class Person:
    #Note: The __init__()function is called automatically every time the  class is being used to create a new object.
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Sajjad Hossain Jim", 36)
print(p1.name , p1.age)
print(p1)
