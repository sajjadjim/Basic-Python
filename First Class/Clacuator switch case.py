oparator = input('Enter The oparator  here :')
numbers = list(map(int, input().split()))

match oparator:
    case '+':
        print(sum(numbers))
   case '-':
        temp = numbers[0]

        for x in range(1, len(numbers)):
        temp = temp - numbers[x]
        print(temp)

    case '*':
      temp = numbers[0]

       for x in range(1, len(numbers)):
       temp = temp * numbers[x]
     print(temp)
   case '/':
       temp = numbers[0]

     for x in range(1, len(numbers)):
        temp = temp / numbers[x]
       print(temp)