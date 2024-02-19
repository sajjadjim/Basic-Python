class MyClass:
    def __init__(mysillyobject , name , age):
        mysillyobject.name = name
        mysillyobject.age = age


    def myFunction(abc):
        print("My name is " +abc.name)
        print("I am " ,abc.age ,"Years Old")

p1=MyClass("Sajjad Jim" , 25)
p1.myFunction()

p1.age=40
del p1.age