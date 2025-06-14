# Um programa que leia 5 valores e guarde em uma lista
# No final mostre o max e min 
# e suas posições na lista :wow:
def min_value():
    return min(lista)

def max_value():
    return max(lista)


lista = []
for c_lista in range(0, 5):
    user_input = int(input(f'Digite um valor para a posição {c_lista}: '))
    lista.append(user_input)

print(f'Você digitou os valores {lista}')

print(f'O menor valor foi: {min_value()} nas posições:', end= ' ')
for counter, valor_lista in enumerate(lista):
    if valor_lista == min_value():
        print(counter, end=' ')

print(f'\nO maior valor foi: {max_value()} nas posições: ', end=' ')
for counter, valor in enumerate(lista):
    if valor == max_value():
        print(counter, end=' ')
