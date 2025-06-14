from time import sleep

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        user_input = int(input('Digite um número entre 0 e 20: '))
        if user_input > 20 or user_input < 0:
            print('\033[31mInválido!\033[m')
            sleep(1)
        else:
            break
    print(f'Voce digitou o número: {tupla[user_input].title()}')
    continuar = str(input('Gostaria de continuar?: '))
    if continuar in 'Nn':
        break
