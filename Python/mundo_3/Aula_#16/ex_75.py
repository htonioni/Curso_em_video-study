numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')), 
            int(input('Digite mais um número: ')), int(input('Digite o último número: ')))

tupla = (numeros)

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
print(f'Os valores pares digitados foram ', end='')
for par in tupla:
    if par % 2 == 0:
        print(par, end=' ')