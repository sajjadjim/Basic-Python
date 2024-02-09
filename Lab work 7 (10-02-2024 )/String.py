my_string = "S. M. SAJJAD HOSSAIN JIM !!"

print("Original string:", my_string)

print("First character:", my_string[0])
print("Last character:", my_string[-1])

# Slicing the string
print("Substring from index 7 to the last:", my_string[7:])
print("Substring from index 7 to 12:", my_string[7:12])

# Concatenate strings
new_string = my_string + " Welcome!"
print("Concatenated string:", new_string)

# Length of the string
print("Length of the string:", len(my_string))

# Convert the string to uppercase and lowercase
print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())

# Replace a substring
replaced_string = my_string.replace("world", "Python")
print("String after replacement:", replaced_string)

# Split the string into a list of substrings
split_string = my_string.split(",")
print("Split string:", split_string)
