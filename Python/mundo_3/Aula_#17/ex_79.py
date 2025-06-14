lista = []
while True:

    user_value = int(input('Digite um valor: '))
    if user_value not in lista:
        lista.append(user_value)
        print('Valor adicionado com sucesso ....')
    else:
        print('Valor duplicado! Não vou adicionar ....')

    user_choice = str(input('Quer continuar? [S/N]: '))
    if user_choice.upper() == 'N':
        break
    

print(sorted(lista))
    

