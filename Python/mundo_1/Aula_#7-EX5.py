# n1 = int(input('Digite um numero: '))
# n2 = int(input('Digite outro numero: '))
# s = n1 + n2
# m = n1 * n2
# print(f'A soma é {s} \nA divisão é {n1/n2:.4f} \nA multiplicação é {m}')
# print('Obrigado Humano')

print('<<<<<<<<<<Exercicio 4>>>>>>>>>>')
na = int(input('Digite um numero inteiro: '))
suc = na + 1
ant = na - 1

print('<<<<<<<<<<Exercicio 5>>>>>>>>>>')
print(f'O sucessor do seu número é {suc}\nO antessedor do seu número é {ant}')

print('<<<<<<<<<<Exercicio 6>>>>>>>>>>')
print(f'Seu dobro é: {na * 2}\nO seu triplo é: {na * 3}\nE sua raiz qudrada é {na ** 1/2:.0f}')

print('<<<<<<<<<<Exercicio 7>>>>>>>>>>')
aluno1 = float(input('Qual sua nota?: '))
aluno_2 = float(input('Qual sua outra nota?: '))
med = (aluno1 + aluno_2)/2
print(f'As notas {aluno1} e {aluno_2} resultam em uma média de <{med}>')

print('<<<<<<<Exercicio 8><<<>>>>>>')
metros = float(input('Digite um valor em metros: '))
cm = metros * 100
mm = metros * 1000
print(f'A medida em centrímetros é {cm:.0f} cm\nA medida em milímetros é {mm:.0f} mm')

print('<<<<<<<<<<<<Exercicio 11>>>>>>>>>>>>')
largura = float(input('Qual a largura da parede?: '))
altura = float(input('Qual a altura da sua parede?: '))
area = largura * altura
print(f'A sua área é de {area}m²')
print(f'Para pintar essa parede será necessário {area/2}l de tinta')

print('<<<<<<<<<<<Exercicio 013>>>>>>>>>>>')
sal = float(input('Qual o seu sálario?: '))
desc = sal * 1.15
print(f'Seu novo salário será de: {desc:.2f}')

print('<<<<<<<<<<<<Exercicio 015>>>>>>>>>>>>')
km = int(input('Bem vindo a Localiza, quantos KM voce percorreu?: '))
days = int(input('Quantos dias você utilizou o carro?: '))
k2 = km * 0.15
d2 = days * 60
print(f'Você andou {days} dias com o carro, o que resulta em R${d2} e pela gasolina R${k2}.'
      f'Logo seu total é de R${k2+d2}')