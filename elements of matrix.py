n = 3 
m = 3  
arr = [[3, 2, 7], [2, 6, 8], [5, 1, 9]]
sum = 0

# Iterating over all 1-D arrays in 2-D array
for i in range(n):
	# Printing all elements in ith 1-D array
	for j in range(m):
		# Printing jth element of ith row
		sum += arr[i][j]

print(sum)

# This code id contributed by shivhack999
