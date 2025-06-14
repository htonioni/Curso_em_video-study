# Podemos criar tuplas sem parênteses
lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
print(lanche)
print(lanche[-3:])

# Para CADA comida EM lanche
for comida in lanche:
    print(comida)


# Realizado com RANGE

for index in range(0, len(lanche)):
    print('->', lanche[index])

# Iteração comum realizada com contador

for posição, comida in enumerate(lanche):
    print(f'Comida {comida} esta na posição: {posição}')


# para colocar em ordem crescente sorted(lanche)
# Podemos somar tuplas, desde que guardamos seu resultado em uma variável
# Podemos contar certa STR em uma tupla = x.count()


# Mostra a posição (index) de determinado objeto (STR, INT, FLOAT)
print(lanche.index('Suco'))