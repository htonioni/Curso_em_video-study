# cinco numeros aleatórios e adicionar a uma tupla e mostrar ela print, depois ira mostrar o menor e maior valor
from random import randint

tuplas = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))



print(f'Os valores sorteados foram:', end=' ')
for n in tuplas:
    print(f'{n}', end=' ')

print('\nO mair valor sorteado foi:', max(tuplas))
print('O menor valor sorteado foi:', min(tuplas))
    

