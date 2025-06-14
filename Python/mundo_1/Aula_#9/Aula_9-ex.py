quest1 = input('Você gostaria de realizar o exercício #22, nome completo?: ').lower()
if quest1 == 'y':
    print('Ok... vamos lá')
    nomec = input(str('Qual seu nome completo?\n'))
# nomespl = nomec.split() ou assim
    print(f'O seu nome com todas maiúsculas será:\n{nomec.upper()}\n'
          f'O seu nome com todas minúsculas será:\n{nomec.lower()}\n'
          f'O seu nome possui {len(nomec.strip()) - nomec.count(" ")} caracteres\n'
          f'E o primeiro nome possui {len(nomec.split()[0])} caracteres')
else:
    quest2 = input('So do you wanna do the exercice #23 about 9999?: ')
    if quest2 == 'y':
        num = int(input('Digita um número interiro ai de 0 até 9999: '))
        und = num // 1 % 10
        dez = num // 10 % 10
        cent = num // 100 % 10
        mil = num // 1000 % 10
        print(f'Anlise do numero: {num}\n'
              f'A unidade deste número é: {und}\n'
              f'A dezena deste número é: {dez}\n'
              f'A centena deste número é: {cent}\n'
              f'A milhar deste número é: {mil}\n')
    else:
        quest3 = input('Vamos para o #24 então???: ')
        if quest3 == 'y':
            cid = str(input('Qual o nome da sua cidade?: ')).strip()
#           Sempre colocar o .strip no input, para ele ja cortar os espaços
#           Aqui embaixo nos pegamos a cidade e colocamos em maisculas, logo após checamos se há 'SANTO' maiusculo nela
            if cid[0:5].upper() == 'SANTO':
                print(f'Há Santo no começo de {cid}')
            else:
                print('Não há Santo no começo da sua cidade')
        else:
            quest4 = input('Você quer ir para o exercício #25?: ')
            if quest4 == 'y':
                pessoa = str(input('Será q seu nome tem? Digita ai: ')).strip()
                if 'SILVA' in pessoa.upper():
                    print('Há Silva')
                else:
                    print('Não há Silva :((((((')
            else:
                quest5 = input('Quer ir para o #26? ')
                if quest5 == 'y':
                    l_a = str(input('Digita uma frase ai, pode ser grande: ')).strip()
                    print(f'A quantidade de A na sua frase é de: {l_a.lower().count("a")}\n'
                          f'Ela aparece a primeira vez em {l_a.lower().find("a"[0:]) + 1}\n'
                          f'E ela aparece a ultima vez em {l_a.lower().rfind("a")}')
                else:
                    quest6 = input('Vamos para o ultimo então, #27?: ')
                    if quest6 == 'y':
                        nm1 = str(input('Qual seu nome completo?: '))
                        nm2 = nm1.split()
                        print(f'Seu nome em modo lista é: {nm2}\n'
                              f'Logo seu primeiro nome é: \n{nm2[0]}\n'
                              f'O seu ultimo nome é \n{nm2[-1]}')
                    else:
                        quit('Ok!')
