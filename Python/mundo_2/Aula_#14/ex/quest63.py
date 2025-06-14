def execute():
    print('=' * 52)
    print('Bem vindo ao exercício #63 - Sequencia de Fibonacci!')
    print('=' * 52)
    n = int(input('Quantos termos você quer mostrar?: '))
    fib_termo_1 = 1
    fib_termo_2 = 0
    counter = 0
    while counter < n:
        f3 = fib_termo_1 + fib_termo_2

        fib_termo_1 = fib_termo_2
        fib_termo_2 = f3
        print(fib_termo_1, end=' → ')
        counter += 1
    print('FIM')


if __name__ == '__main__':
    execute()
