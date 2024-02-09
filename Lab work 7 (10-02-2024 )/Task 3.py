matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")  # Print the element
    print()

max_value = matrix[0][0] #Initial Set a max value
for row in matrix:
    for element in row:
        if element > max_value:
            max_value = element

print("Maximum value in the matrix:", max_value)
