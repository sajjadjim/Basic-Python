class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("Sajjad Hossain Jim" , 25)
print(p1)


#ANother Code
class Person:
  def __init__(self, name, address):
    self.name = name
    self.address = address

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("I am a student of " + self.address)

P1=Person("Sajjad Hossain Jim" , "Daffodil International University" )
P1.myfunc()