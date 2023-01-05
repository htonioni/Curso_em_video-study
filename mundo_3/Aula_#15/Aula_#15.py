# from time import sleep
# a = 0
# while True:
#     print (a, end=' ')
#     sleep(.8)
#     a += (a + 3)
#     if a > 150:
#         break

soma = 0
while True:
    user_input = int(input('Digite um numero: '))
    if user_input == 999:
        break
    soma = soma + user_input
print(f'A soma vale {soma}')
