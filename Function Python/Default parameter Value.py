def my_function(country ="Bangladesh"):
    print("My country name is " +country)
 
my_function("USA")
my_function()
my_function("Australia")
my_function("India")

 

#Passing List is An Argumment

def my_functions(food):
    for i in food:
        print(i)

fruits = ["Mango" , "Banana" , "Pineapple"]

my_functions(fruits)

def count(Value):
    for x in Value:
        print(x ,end=' ')

number =[1,2,3,4,5,6,7,8]
count(number)
