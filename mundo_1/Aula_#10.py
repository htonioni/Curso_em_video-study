# tempo = int(input('Quantos anos tem seu carro?: '))
# print('carro novo' if tempo <= 3 else 'carro velho')
# print('FIM')
from random import choice
from time import sleep

print('\033[7;40mExercicios do Guanabara\033[m')
quest1 = str(input('Quer fazer o exercício \033[4;31m#28\033[m dos desafios?: '))
if quest1.lower() == 'y':
    print('\033[1;32mOk vamos lá então\033[m')
    #   alea = radint(0, 5)
    alea = choice([0, 1, 2, 3, 4, 5])
    print('Estarei pensando aqui em um numero ..........')
    sleep(2.0)
    numale = int(input('Ok, digita um número de \033[31m0\033[m à \033[31m5\033[m ai: '))
    if numale == alea:
        print('True')
    else:
        print(f'Eu ganhei! Pensei no número {alea} e não em {numale}')
        quit(f'Mais sorte na proxima otário')
else:
    quest2 = str(input('Quer ir para o exerício \033[31m#29\033[m então?: '))
    if quest2.lower() == 'y':
        print('-_-' * 20)
        print('\033[4mVoce foi pego na blitz.......... ')
        print('-_-' * 20)
        sleep(1.5)
        vel = float(input('Agora fala ai qual \033[31mkm/h\033[m vc estava?: '))
        if vel > 80:
            print(f'Voce sera multado em \033[4;31mR${(vel - 80) * 7:.2f}')
        else:
            print('Esta liberado ')
    else:
        quest3 = str(input('Quer ir para o exercício \033[31m#30\033[m então?: '))
        if quest3 == 'y':
            print('Vamos la entao')
            inteiro = int(input('Digita um numero \033[4minteiro\033[m ai: '))
            if inteiro % 2 == 0:
                print(f'Seu número {inteiro} é um número \033[4;34mPAR')
            else:
                print(f'O número {inteiro} é um número \033[4;34IMPAR')
        else:
            quest4 = str(input('Você quer ir para o \033[31m#31\033[m então?: '))
            if quest4 == 'y':
                print('Vamos apara o exercicio viagem')
                sleep(0.5)
                km = float(input('Qual a distancia \033[31mem km\033[m da sua viajem?: '))
                if km <= 200:
                    # print(f'A sua viagem de {km}km terá o preço de R${km*0.5:.2f}')
                    preco = km * 0.5
                else:
                    # print(f'O preço da sua passagem é R${km*0.45:.2f}')
                    preco = km * 0.45
                print(f'A sua viagem de {km}km terá o valor de \033[31;4mR${preco:.2f}')
            else:
                print('Partiu proxima então')
                quest5 = str(input('Pronto para o exercicio #32?: '))
                if quest5 == 'y':
                    ano = int(input('Quer verificar se um ano é bissexto? Digita ele ai: '))
                    div = ano % 4
                    print(div)
                    if div == 0 and div % 100 != 0 or div % 400 == 0:
                        print(f'{ano} é um ano BISSEXTO')
                    else:
                        print(f'{ano} não é um ano BISSEXTO')
                else:
                    print('Vamos para o exericio #33')
                    quest6 = input('Você quer começar?')
                    if quest6 == 'y':
                        print('Ok vamos la!')
                        sleep(0.6)
                        num1 = int(input('Digite o primeiro número: '))
                        num2 = int(input('Digite o segundo número: '))
                        num3 = int(input('Digite o terceiro número: '))
                        lista = [num1, num2, num3]
                        print(f'O maior da sua lista é {max(lista)}')
                        print(f'O menor da sua lista é {min(lista)}')
                    else:
                        quest7 = str(input('Partiu para o #34 então??: '))
                        if quest7 == 'y':
                            print('Vamos lá ta na hora de calcular seu aumento')
                            sleep(0.6)
                            salario = float(input('Qual seu salário? '))
                            if salario > 1250:
                                aumento = salario * 1.1
                            else:
                                aumento = salario * 1.5
                            print(f'Seu novo salario será de {aumento}')
