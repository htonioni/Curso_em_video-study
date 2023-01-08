def execute():
    import random
    from time import sleep
    palpites = 0
    num_aleatorio = random.randrange(1, 11)
    print(num_aleatorio, '<- teste')

    print('Ok estarei pensando em um número entre 0 e 10.......')
    sleep(1.0)

    input_usuario = 0

    while num_aleatorio != input_usuario:
        input_usuario = int(input('\nTente adivinhar: '))
        if input_usuario <= 10:
            palpites += 1
            if input_usuario > num_aleatorio:
                print('Menos...')
            elif input_usuario < num_aleatorio:
                print('Mais....')
        elif input_usuario > 10:
            print('Número inválido!\nTente novamente')
    print(f'Você usou {palpites} tentativas e conseguiu acertar!')



if __name__=='__main__':
    execute()