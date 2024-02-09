def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        while n > 0:
            result *= n
            n = n - 1
        return result

num = int(input("Enter a number to find its factorial: "))
print("Factorial of", num, "is", factorial(num))
