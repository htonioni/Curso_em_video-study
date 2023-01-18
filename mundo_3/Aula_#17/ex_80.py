lista = []
counter = 0
for loop in range(0, 5):
    user_input = int(input('Digite um valor: '))
    if loop == 0 or user_input > lista[-1]:
        lista.append(user_input)
        print(f'O valor foi inserido na última pos ...')
    else:
        pos = 0
        while pos < len(lista):
            if user_input <= lista[pos]:
                lista.insert(pos, user_input)
                print(f'O valor foi inserido na pos {pos}...')
                break
            pos += 1
print('-=' * 30)
print(f'Os numeros foram: {lista}')