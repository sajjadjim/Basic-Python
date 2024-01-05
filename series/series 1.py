#1 + 2 + 3........+ n
num =int(input("Enter the last number of series:"))

sum =0

for x in range(1,num+1,1):
    sum = sum +x

print("series number :",sum)