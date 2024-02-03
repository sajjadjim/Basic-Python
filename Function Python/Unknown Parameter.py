def my_function(*kids):  #Multiple Types of kist Given * using
    print("The oldest Person is " + kids[0])   # Define the number of serial which i want ot print

my_function("JIM", "Sajjad" , "Hossain")


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Kubra", child2 = "Siam", child3 = "Jim")


def my_functions(**fruits):
    print("\n\nThe most tested fruites is " +fruits["num1"])
    print("The most expensive fruits is " +fruits["num2"])

my_functions(num1 ="Mango" , num2="BlackBerry" , num3 ="Jackfruits")