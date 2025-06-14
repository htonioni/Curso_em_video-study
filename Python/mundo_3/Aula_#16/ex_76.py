listagem = ('Lápis', 1.75, 
            'Borracha', 2.00, 
            'Caderno', 15.9,
            'Compasso', 10,
            'Livro', 50)

print('-' * 55)
print('listagem de preços'.upper().center(55,' '))
print('-' * 55)

for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<43}', end='')
    else:
        print(f'R${listagem[posicao]:>10.2f}')
print('-' * 55)


# print(listagem[0].ljust(44, '.'), end='R$')
# print(listagem[1].rjust(9))
# print(listagem[4].ljust(44, '.'), end='R$')
# print(listagem[5].rjust(9))