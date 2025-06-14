from time import sleep
from datetime import date

print('Olá, seja bem vindo aos exercícios de \033[31mPython\033[m da aula #13!')
sleep(0.5)

quest46 = input('Gostaria de fazer o ex \033[32m#46\033[m - Fogos de Artificio?: ')
if quest46.lower() in ('y', 'yes'):
    fim_d_ano = 12 - date.today().month
    print(f'Ok, faltam \033[31m{fim_d_ano} meses\033[m para o fim do ano, mas la vai....')
    sleep(.5)
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
    print('\033[31mFELIZ ANO NOVO!\033[m')

else:
    quest47 = input('Gostaria de fazer o ex \033[32m#47\033[m - Números pares?: ')
    if quest47.lower() in ('y', 'yes'):
        print('Ok vamos lá....')
        sleep(.5)
        for pares in range(2, 51, 2):
            print(pares, end='_')
            sleep(0.2)
        print('\nEsses são todos os números pares entre 1 e 50!')
    else:
        quest48 = input('Gostaria de fazer o ex \033[32m#48\033[m - ímpares multiplos de 3?: ')
        if quest48 in ('y', 'yes'):
            print('Ok, vamos lá!')
            sleep(.5)
            input('Aperte \033[31menter\033[m para descobrir a soma de todos os números \033[31mÍMPARES\033[m '
                  'multiplos de 3 entre 1 e 500!')
            soma = 0
            count = 0
            for c in range(0, 500, 3):
                if c % 2 != 0:
                    count = count + 1
                    soma = soma + c
            print(f'\033[36m{count}\033[m números foram somados, e o resultado dessa soma foi \033[36m{soma}\033[m')
        else:
            quest49 = input('Gostaria de fazer o ex \033[32m#49\033[m - Tabuada?: ')
            if quest49.lower() in ('y', 'yes'):
                print('Ok, vamos lá!')
                sleep(.5)
                num = int(input('Digite um número inteiro para saber sua tabuada: '))
                for tabuada in range(1, 10 + 1):
                    print(f'{tabuada} x {num} = \033[31m{num * tabuada}\033[m')
                    sleep(.5)
                print('\nObrigado, volte sempre!')
            else:
                quest50 = input('Gostaria de fazer o ex \033[32m#50\033[m - '
                                'Soma de números, mas apenas considerando os num inteiros?: ')
                if quest50.lower() in ('y', 'yes'):
                    print('Ok, vamos lá!')
                    sleep(.5)
                    soma = 0
                    c = 0
                    for sum_number in range(1, 6 + 1):
                        number = int(input(f'Digite o {sum_number} número: '))
                        if number % 2 == 0:
                            c += 1
                            soma += number
                    print('Ok calculando .....')
                    sleep(1)
                    print(f'Achei {c} números pares, e a soma é \033[31m{soma}\033[m')

                else:
                    quest51 = input('Gostaria de fazer o ex \033[32m#51\033[m - 10 Termos de uma PA?: ')
                    if quest51.lower() in ('y', 'yes'):
                        print('Ok, vamos lá!')
                        sleep(.5)
                        p_term = int(input('Digite o primeiro termo: '))
                        rz = int(input('Digite a razão: '))
                        u_term = p_term + (10 * rz)
                        for x in range(p_term, u_term, rz):
                            print(x, end=' => ')
                        print('ACABOU')
                    else:
                        quest52 = input('Gostaria de fazer o ex \033[32m#52\033[m - este inteiro é um primo?: ')
                        if quest52.lower() in ('y', 'yes'):
                            print('Ok, vamos lá!')

                            vezes_dividido = 0
                            continuar = True

                            while continuar:
                                num1 = int(input('\n*Digite \033[32m0\033[m para sair*\n'
                                                 'Digite um número inteiro: '))
                                if num1 == 0:
                                    break
                                for primo in range(1, num1 + 1):
                                    div = num1 % primo
                                    if div == 0:
                                        vezes_dividido += 1

                                        print(f'\033[31m{primo}\033[m', end=' ')
                                        sleep(.1)
                                        continue
                                    print(primo, end=' ')
                                    sleep(.1)
                                print(f'\nO número \033[31m{num1}\033[m foi divisível '
                                      f'\033[36m{vezes_dividido} vezes\033[m, por isso ele: ')

                                if vezes_dividido == 2:
                                    print('\033[31mÉ\033[m um número primo!')

                                elif vezes_dividido >= 3:
                                    print('\033[31mNÃO\033[m é um primo!')

                        else:
                            quest53 = input('Gostaria de fazer o ex \033[32m#53\033[m - Esta frase é um políndromo?: ')
                            if quest53.lower() in ('yes', 'y'):
                                print('Ok vamos lá!')

                                frase_cru = str(input('Digite a frase para analise: '))
                                frase_tratada = frase_cru.upper().replace(' ', '')
                                tamanho = len(frase_tratada)
                                frase_contraria = ''

                                for contrario in range(tamanho - 1, -1, -1):
                                    frase_contraria = frase_contraria + frase_tratada[contrario]
                                if frase_contraria == frase_tratada:
                                    print(f'Está frase \033[31mé um polndromo!\033[m \n'
                                          f'Frase: {frase_tratada}\n'
                                          f'Ao contrario: {frase_contraria}')
                                else:
                                    print(f'A frase {frase_tratada} não é igual a {frase_contraria}')
                            else:
                                quest54 = str(input('Gostaria de fazer o ex \033[32m#54\033[m - '
                                                    'Maioridade de 7 pessoas?: '))
                                if quest54 in ('y', 'yes'):
                                    print('Ok vamos lá!')

                                    maiorID = 0
                                    menorID = 0
                                    hoje = date.today().year

                                    for anos in range(1, 7 + 1):
                                        nasc = int(input('Qual o ano de nascimento da {}ª pessoa?: '.format(anos)))
                                        idade = hoje - nasc
                                        if idade >= 18:
                                            maiorID += 1
                                        else:
                                            menorID += 1
                                    print(f'A quantidade de menores de idade é: {menorID}\n'
                                          f'E a quantidade de maiores de idade é: {maiorID}')
                                else:
                                    quest55 = str(
                                        input('Gostaria de fazer o ex \033[32m#55\033[m - Peso de 5 pessoas?: '))
                                    if quest55.lower() in ('y', 'yes'):
                                        print('Ok, vamos lá!')

                                        peso = []

                                        for kg in range(1, 5 + 1):
                                            pessoa = float(input(f'Qual o peso da {kg}ª pessoa?: '))
                                            peso.append(pessoa)

                                        print(f"\nA pessoa de maior peso foi a pessoa com {max(peso)} KG's\n"
                                              f"A pessoa com menor peso foi a pessoa com {min(peso)} KG'S")
                                    else:
                                        quest56 = str(input('Gostaria de fazer o ex \033[32m#56\033[m '
                                                            '- Diversas var?: '))
                                        if quest56.lower() in ('yes', 'y'):
                                            print('Ok, vamos lá!')
                                            sleep(.5)

                                            c = 0
                                            age = 0
                                            mais_velho = 0
                                            nome2 = ''
                                            c_2F = 0

                                            for data in range(1, 5):
                                                print(f'   \033[31m{data}ª\033[m PESSOA')

                                                nome = str(input('Qual seu nome?: '))

                                                age_input = int(input('Qual sua idade?: '))
                                                age = age_input + age
                                                c = c + 1

                                                sex = str(input('Qual seu sexo, [M ou F]?: '))
                                                if sex.lower() == 'm':
                                                    if data == 1:
                                                        mais_velho = age_input
                                                        if nome2 == '':
                                                            nome2 = nome
                                                    elif mais_velho < age_input:
                                                        mais_velho = age_input
                                                        nome2 = nome
                                                else:
                                                    if age_input < 20:
                                                        c_2F += 1

                                            med_idade = age / c

                                            print(f'\nA média das idades é: \033[31m{med_idade:.1f} anos\033[m'
                                                  f'\nO nome homem mais velho é: \033[31m{nome2.capitalize()}\033[m'
                                                  f'\nA quantidade de mulheres com menos de 20 anos é: '
                                                  f'\033[31m{c_2F} mulheres\033[m')

