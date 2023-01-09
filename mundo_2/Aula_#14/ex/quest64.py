def execute():
    continuar = False
    contador = 0
    soma = 0
    while not continuar:
        numero = int(input('Digite um número [999 para parar]: '))
        if numero == 999:
            continuar = True
        else:
            contador += 1
            soma = numero + soma
    print(f'A soma desses {contador} números é {soma}')


if __name__ == '__main__':
    execute()
