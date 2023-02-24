expressao = str(input('Digite uma expressao: '))
count1 = expressao.count('(')
count2 = expressao.count(')')
if count1 == count2:
    print(f'A expressao é valida e possui {count2+count2} parenteses')
else:
    print('Expressao inválida')