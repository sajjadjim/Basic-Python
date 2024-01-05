# 1 x 2 x 3 ........x n
num =int(input("Enter the last number of series:"))

sum =1

for x in range(1,num+1,1):
    sum = sum * x

print("series number :",sum)