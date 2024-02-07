x = lambda a : a + 10
print(x(5))


x = lambda a , b : a * b
print(x(5,5))

x = lambda c , d : c - d
print(x(10,7))
'''  A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression. '''

n = lambda a,b,c,d : (a+b) * (c+d)
print(n(5,6,2,3))