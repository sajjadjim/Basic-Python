oparator = input("Choice an operator (+, -, *, /): ")

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

if oparator == '+':
    result1 = first+second
    print(f"{first} + {second} = {result1}")
elif oparator == '-':
    result2 = first-second
    print(f"{first} - {second} = {result2}")
elif oparator == '*':
    result3 = first*second
    print(f"{first} * {second} = {result3}")
elif oparator == '/':
        result4 = first / second
        print(f"{first} / {second} = {result4}")
else:
    print("Error! Operator is not correct.")
