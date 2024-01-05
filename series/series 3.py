#1^2 + 2^2 + 3^2........+ n^2
num =int(input("Enter the last number of series:"))

sum =0

for x in range(1,num+1,1):
    sum = sum + x*x

print("series number :",sum)