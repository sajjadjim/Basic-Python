# Prime Number or Not prime Number


def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

user_input = int(input("Enter an integer number: "))

if check_prime(user_input):
    print(f"{user_input} is a prime number")
else:
    print(user_input, "is not a prime number.")

