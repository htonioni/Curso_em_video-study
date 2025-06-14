tupla = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 
         'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')

print('-='*45)
print(f'Os 5 primeios são: {tupla[0:5]}')
print('-='*45)
print(f'Os 4 últimos são: {tupla[-4:]}')
print('-='*45)
print(f'Times em ordem alfabética: {sorted(tupla)}')
print('-='*45)
print(f'A posição do São Paulo é: {tupla.index("São Paulo")+1}ª')

