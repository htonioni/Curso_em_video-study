from time import sleep
from random import choice
from datetime import date

quest1 = input('Gostaria de ir para o exercício #36?: ')
if quest1.strip().lower() == 'yes' or quest1.strip().lower() == 'y':
    print('\033[1;31mOk então vamos lá\033[m')
    print('Bem vindo ao banco, você gostaria de um empréstimo, certo? .....')
    sleep(0.8)
    salario = float(input('Qual seu salário?: '))
    anos = int(input('Deseja pagar em quantos anos?: '))
    meses = anos * 12
    casa = float(input('Qual o valor da casa?: '))
    if casa >= 1000000:
        print('EITA! Que casa cara.')
    trinta = salario * 0.3
    prest = casa / meses
    if prest > trinta:
        print('Infelizmente não conseguiremos conceder um empréstimo!')
    elif prest <= trinta:
        print(f'Esta ok, a prestação fica \033[31mR${prest:.2f}\033[m'
              'por mês no período de'
              f'\033[31m{anos}\033[m anos')
        sleep(0.8)
        print('Agradecemos a preferência, volte sempre!')
else:
    quest2 = input('Gostaria de ir para o exercício #37?: ')
    if quest2.lower().strip() == 'yes' or quest2.lower().strip() == 'y':
        print('Neste exercício iremos converter um numero decimal em hexa, bin e octa decimais....')
        sleep(1.5)
        num2 = int(input('Digite um número inteiro: '))
        print('''Escolha uma base para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
        #        print('Escolha uma base para converter:\n'
        #              '[ 1 ] converter para BINÁRIO\n'
        #              '[ 2 ] converter para OCTAL\n'
        #              '[ 3 ] converter para HEXADECIMAL')
        base = int(input('Sua escolha: '))
        if base == 1:
            print(
                f'O número {num2} convertido para binário é: {bin(num2)[2:]}')
        elif base == 2:
            print(
                f'O número {num2} convertido para OCTAL é: {oct(num2)[2:]}')
        elif base == 3:
            print(
                f'Seu numero {num2} convertido para HEXADECIMAL é: {hex(num2)[:2]}')
        else:
            print('Valor incorreto!')
    else:
        quest3 = input('Gostaria de ir para o #38?: ')
        if quest3.lower().strip() == 'yes' or quest3.lower().strip() == 'y':
            print('\033[31mEntão vamos lá\033[m')
            num3_1 = int(input('Digite um número inteiro: '))
            num3_2 = int(input('Digite outro número inteiro: '))
            if num3_1 > num3_2:
                print('O\033[4m primeiro\033[m número é\033[31;1m maior\033[m')
            elif num3_1 < num3_2:
                print('O \033[4msegundo\033[m número é \033[1;31mmaior\033[m')
            elif num3_1 == num3_2:
                print('Os valores são', 'iguais'.upper())
        else:
            quest4 = input('Então vamos para o exercício #39?: ')
            if quest4.lower().strip() == 'yes' or quest4.lower().strip() == 'y':
                print('\033[31mOk então vamos la!\033[m')
                sleep(1.2)
                ano = int(input('Qual seu ano de nascimento?: '))
                idade = date.today().year - ano
                if idade > 18:
                    atrasado = (idade - 18) * 12
                    print(
                        f'Você ja passou do seu alistamento, esta {atrasado} meses \033[31;2matrasado!!!!!\033[m')
                elif idade < 18:
                    falta = (18 - idade) * 12
                    print(f'Você ainda não pode se alistar, faltam {falta}' 
                            'meses para realizar seu alistamento')
                elif idade == 18:
                    print('\033[31;1mEstá na hora de se alistar\033[m,'
                            'corra para a junta militar no Aterrado')
            else:
                quest5 = input('Então você quer ir para o ex #40?: ')
                if quest5 == 'y':
                    print('\033[31;4mOk então vamos lá!\033[m')
                    sleep(0.8)
                    nota_1 = float(input('Qual foi a sua nota na primeira prova?: '))
                    nota_2 = float(input('E qual a nota na segunda prova?: '))
                    media = (nota_1 + nota_2) / 2
                    if media >= 7:
                        print(f'Parabéns pelas notas, a media foi {media} e está \033[31;4mAPROVADO!\033[m')
                    elif media < 5:
                        print(f'Que pena, media de {media} você \033[31mREPROVOU\033[m')
                    elif 7 > media >= 5:
                        print(f'Bom, com uma média de {media} você ficou de \033[31mRECUPERAÇÃO\033[m')
                else:
                    quest6 = input('Quer ir para o ex #41 então?: ')
                    if quest6 == 'y' or quest6 == 'yes':
                        print('Ok então vamos para a natação!')
                        nasc = int(input('Qual seu ano de nascimento?: '))
                        idade = date.today().year - nasc
                        print(f'O atleta tem anos {idade}')
                        if idade <= 9:
                            print('Sua classificação é \033[36;4mMIRIM\033[m')
                        elif 9 < idade <= 14:
                            print('Sua classificação é \033[36;4mINFANTIL\033[m')
                        elif 14 < idade <= 19:
                            print('Sua classificação é \033[36;4mJUNIOR\033[m')
                        elif 19 < idade <= 25:
                            print('Sua classificação é \033[36;4mSÊNIOR\033[m')
                        else:
                            print('Sua classificação é \033[36;4mMASTER\033[m, Parabéns!')
                    else:
                        quest7 = input('Você quer ir para o #42 então?')
                        if quest7 == 'y' or quest7 == 'yes':
                            print('\033[31mOK vamos lá então\033[m')
                            s1 = float(input('Digite um segmento: '))
                            s2 = float(input('Digite o segundo seguimento: '))
                            s3 = float(input('Digite o terceiro: '))
                            if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
                                print('Forma um triângulo!')
                                # if s1 == s2 == s3:
                                if s1 == s2 and s2 == s3:
                                    print('E ele é \033[36mEQUILÁTERO\033[m')
                                elif s1 == s2 or s2 == s3 or s1 == s3:
                                    print('E ele é \033[36mISÓSCELES\033[m')
                                elif s1 != s2 and s1 != s3 and s2 != s3:
                                    print('E é um \033[36mESCALENO\033[m')
                            else:
                                print('Não forma um triângulo!')
                        else:
                            quest8 = str(input('Gostaria de ir para a aula #43 então?: '))
                            if quest8 == 'y' or quest8 == 'yes':
                                print('\033[36mOK VAMOS LÁ\033[m')
                                peso = float(input('Qual seu peso?: '))
                                altura = float(input('E qual sua altura?: '))
                                imc = peso / (altura ** 2)
                                print(f'Ok seu \033[31mIMC\033[m é de {imc:.2f}!')
                                sleep(0.8)
                                if imc < 18.5:
                                    print(f'Seu IMC de {imc:.2f} está para pessoas abaixo do peso.')
                                elif 18.5 <= imc < 25:
                                    print('Esse é seu índice ideal!')
                                elif 25 <= imc < 30:
                                    print('Você está acima do peso!')
                                elif 30 <= imc < 40:
                                    print('Você está bastante acima do peso!')
                                elif imc > 40:
                                    print('Procure um profissional da área media, agora!')
                            else:
                                quest9 = str(input('Quer ir para o EX #44 então?'))
                                if quest9 == 'y' or quest9 == 'yes':
                                    print(f'{" Mercado da esquina :) ":=^40}')
                                    preco = float(input('Qual o \033[32mpreço\033[m total das suas compras?: '))
                                    print('''Qual seria a forma de \033[31mpagamento\033[m?
                                    [ 1 ] à vista dinheiro/cheque (\033[34m10% de desconto\033[m)
                                    [ 2 ] à vista cartão (\033[36m5% de desconto\033[m)
                                    [ 3 ] 2x no cartão (\033[35mSem juros\033[m)
                                    [ 4 ] 3x ou mais no cartão (\033[33mjuros de 20%\033[m)''')
                                    esc = int(input(': '))
                                    if esc == 1:
                                        stats = f'R${preco - (preco * 0.1)} aplicando o desconto de 10%'
                                    elif esc == 2:
                                        stats = f'R${preco - (preco * 0.05)} aplicando o desconto de 5%'
                                    elif esc == 3:
                                        stats = f'duas parcelas de R${preco / 2} sem juros'
                                    elif esc == 4:
                                        parcelas = int(
                                            input('Quantas parcelas serão?: '))
                                        stats = f'em {parcelas} parcelas de {((preco * 0.2) + preco) / parcelas}'
                                    else:
                                        stats = preco
                                        print('\033[31mERRO!!!!!\033[m')
                                    print(f'O seu total de R${preco} ficara {stats}')
                                else:
                                    quest10 = str(input('Quer ir para o ex #45 \033[31mULTIMO\033[m?'))
                                    if quest10 == 'y':
                                        print('OK! VAMOS PARA O JOKEN PO\n'
                                              '\033[31mSuas opções são:\033[m\n'
                                              '[ 1 ] \033[35mPEDRA\033[m\n'
                                              '[ 2 ] \033[36mPAPEL\033[m\n'
                                              '[ 3 ] \033[33mTESOURA\033[m')
                                        esc = int(input('Qual sua escolha?: '))
                                        esc_c = choice([1, 2, 3])
                                        if esc == esc_c:
                                            print('Puts, o computador escolheu o mesmo que você!')
                                        elif esc_c == 1:
                                            print('O computador escolheu \033[35mPEDRA\033[m')
                                            if esc == 2:
                                                print('Você escolheu \033[36mPAPEL\033[m, logo você\n'
                                                      '     \033[31mGANHOU!!!!!!\033[m')
                                            elif esc == 3:
                                                print('PEDRA ganha de tesoura, logo você\n'
                                                      '   \033[31mPERDEUUUUUU!!!!!!\033[m')
                                        elif esc_c == 2:
                                            print('O computador escolheu \033[36mPAPEL\033[m')
                                            if esc == 1:
                                                print('Você escolheu \033[35mPEDRA\033[m\n'
                                                      'PEDRA perde de papel, logo você:\n'
                                                      '    \033[31mPERDEUUUUUU!!!!!!\033[m')
                                            elif esc == 3:
                                                print('Você escolheu \033[33mTESOURA\033[m\n'
                                                      'TESOURA ganha de PAPEL logo você\n'
                                                      '\033[31mGANHOU!!!!!!\033[m')
                                        elif esc_c == 3:
                                            print('O computer escolheu TESOURA...')
                                            sleep(.5)
                                            print(f'Você escolheu {esc}')
                                            if esc == 1:
                                                print('Você escolheu \033[35mPEDRA\033[m\n'
                                                      'PEDRA vence de TESOURA, logo você\n'
                                                      '\033[31mGANHOU!!!!!!\033[m')
                                            elif esc == 2:
                                                print('Você escolheu \033[36mPAPEL\033[m\n'
                                                      'TESOURA vence de PAPEL, logo você\n'
                                                      '\033[31mPERDEUUUUUU!!!!!!\033[m')
