user_inputs = []
for i in range(5):

    user_input = input("Enter value {}: ".format(i + 1))
    user_inputs.append(user_input)

print("You entered:")
for input_value in user_inputs:
    print(input_value)

