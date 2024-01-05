#2 + 4 + 6........+ n
num =int(input("Enter the last number of series:"))

sum =0

for x in range(2,num+1,2):
    sum = sum +x

print("series number :",sum)