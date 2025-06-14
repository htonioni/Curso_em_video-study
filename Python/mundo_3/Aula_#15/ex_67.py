'''Using while'''

# while True:
#     num1 = int(input('Quer ver a tabuáda de qual valor?: '))
#     if num1 < 0:
#         break
#     print('-'*37)
#     tabuada = 1
#     while tabuada != 11:
#         print(num1, ' X ', tabuada, ' = ', (num1*tabuada))
#         tabuada += 1
#     print('-'*37)

'''Using for'''

while True:
    user_input = int(input('Quer ver a tabuáda de qual valor?: '))
    if user_input < 0:
        break
    print('-'*37)
    counter = 1
    for tabuada in range(0,10):
        print(user_input, ' X ', counter, ' = ',(user_input * counter))
        counter += 1
    print('-'*37)
print('Programa, encerreado!')