# Aula de Listas em Python
num = [2, 5, 9, 1]

num[0] = 1 # O indice 0 é transformado em 1

num.append(15) # Insere um valor na ultima posição
num.insert(2, 9) # Insere um valor no index 2 insert(index, valor)
print(num, '<- 1º\n')

num.sort()
num.sort(reverse=False)
print(num, '<- 2º Sorted values\n')

num.pop(4) # Remove um item: .pop(index) -> sem um valor ele remove o ultimo item
num.remove(9) # Remove X item da lista, removendo sua primeira ocorrencia

print('Tamanho da lista:', len(num))
print(num)

# Imprimir os valores "Formatados"
for valores in num:
    print('Achei o valor: ', valores )

# Imprimir os valores, mas com uma contagem  
print(num)
for contador, valores in enumerate(num):
    print(f'Na posição {contador} encontrei o numero {valores}')


# Python iguala listas umas com as outras
a = [0, 1, 2, 3]
b = a
b[2] = 9
print(a) 
# Alterando B tambem alteramos A
# Para realizar apenas a copia -> b = a[:]
