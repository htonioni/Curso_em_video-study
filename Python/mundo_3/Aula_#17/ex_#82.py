
lista = []
lista_par = []
lista_impar = []
while True:
    number_input = int(input('Digite um número: '))
    lista.append(number_input)
    if number_input % 2 == 0:
        lista_par.append(number_input)
    else:
        lista_impar.append(number_input)
    
    user_input = str(input('Quer continuar? [S/N]:')) 
    if user_input in ('Nn'):
        break
    
print(f'A lista completa é: {lista}')
print(f'A lista dos pares é: {lista_par}')
print(f'A lista dos impares é: {lista_impar}')
