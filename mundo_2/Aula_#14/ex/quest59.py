def execute():
    
    print('\nOlá seja bem vindo ao desafio #59 - Operações com dois valores!')
    number_1 = int(input('Digite o primeiro valor: '))
    number_2 = int(input('Digite o segundo valor: '))
    acertou = False
    print(acertou)
    print(not acertou, '<-')
    while not acertou:
        user_option = int(input('\nSuas opções:\n'
        '         [ 1 ] Somar\n'
        '         [ 2 ] Multiplicar\n'
        '         [ 3 ] Maior número\n'
        '         [ 4 ] Novos números\n'
        '         [ 5 ] Sair\n'
        '>>>>>>>> Qual gostaria de realizar?: '))
        if user_option == 1:
            print(f'\nO resultado da soma é: {number_1 + number_2}')
        elif user_option == 2:
            print(f'\nO resultado da multiplicação é: {number_1 - number_2}')
        elif user_option == 3:
            if number_1 > number_2:
                print(f'\nO maior número é {number_1}')
            elif number_2 > number_1:
                print(f'\nO maior número é {number_2}')
        elif user_option == 4:
            number_1 = int(input('Digite o primeiro valor: '))
            number_2 = int(input('Digite o segundo valor: '))
        elif user_option == 5:
            acertou = True
        else:
            print('\033[31mOpção inválida\033[m, tente novamente!\n')
    print('\nObrigado por utilizar nosso serviços!')


if __name__ == '__main__':
    execute()