def execute():
    number = int(input('Digite um número : '))
    factorial = 1
    while number > 0:
        print(number, end='')
        factorial = factorial * number
        number -= 1
        if number > 0:
            print(' x ', end='')
        else:
            print(' = ', end='')
    print(factorial)


if __name__ == "__main__":
    execute()
