lista = []
counter = 0
while True:
    user_input = int(input('Digite um valor: '))
    lista.append(user_input)
    # lista.append(int(input('Digite um valor: '))
    user_choice = str(input('Gostaria de continuar? [S/N]:'))
    if user_choice in ('Nn'):
        break
    
    
    counter += 1

lista.sort(reverse=True)
print(f'Voce digitou {counter} elementos')
print(f'A lista em ordem decrescente é: {lista}')
if 5 in lista[:]:
    print('Há 5 na lista!')