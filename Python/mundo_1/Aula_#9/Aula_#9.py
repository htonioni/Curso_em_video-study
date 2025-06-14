frase = 'Hugo toni'
#        012345678
''' print(frase[3:9:2])
 print(frase[:5])
 print(frase[5:])
 print(frase[1::2])'''
# TODO: comprimento da frase(quantidade de caracteres)'
print(len(frase))
# TODO: aonde começa a string entre parenteses, Caso não existe a string terá o retorno -1, logo não existe'
print(frase.find('hugo'))
# TODO: Existe hugo na variavel frase?'
print('hugo' in frase)
#  TODO: Subistituir a frase por outra frase
print(frase.replace('Hugo', 'Monica'))
# TODO: Tudo em maísculo, min
print(frase.upper())
print(frase.lower())
# TODO : Apenas a primeira letra em maiúsculo (Hugo toni)
print(frase.capitalize())
# TODO: todos começo de palavra em maisculo
print(frase.title())
# TODO: Remoção de espaços no início e espaços no final
# frase.strip()
# frase.rstrip() <<<<< remoção apenas do final (lado direito)
# frase.lstrip() <<<<< remoção apenas do final (lado esquerdo)
# TODO: Dividir a frase pelos espaços (cada palavra é colocada em nova string)
print(frase.split())
# TODO: Juntar as STR que estavam por espaços por um 'x'
print('-'.join(frase))

print('''Conta para depósito bancário:
CAIXA ECONOMICA FEDERAL
AG 4079
OP 003
C/C 1045-2
Jose Maciel de Santana 
11.017.907/0001-80''')
# TODO: Contar quantos O idependente de ser maiscula
frase.upper().count('o')
# TODO: contar quantos carecters, mas removendo os espaços
len(frase.strip())
# TODO: imprimir uma palvra da lista criado por um .split
frase2 = 'Hugo Tonioni de Santana'
fdivi = frase2.split()
print(fdivi[0][1:4])
