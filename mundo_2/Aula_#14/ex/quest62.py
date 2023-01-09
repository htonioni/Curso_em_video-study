def execute():
    print('Ok, bem vindo ao exercício #62 - Progressão Aritmética v3.0!')
    primeiro_termo = int(input('Primeiro termo: '))
    rz_pa = int(input('Razão da PA: '))
    counter = 1
    termo_gerado = primeiro_termo
    total = 0
    continuar = 10
    while continuar != 0:
        total = total + continuar
        while counter <= total:
            print(termo_gerado, end=' => ')
            termo_gerado = termo_gerado + rz_pa
            counter += 1
        print('PAUSA!')
        continuar = int(input('Quantos termos você quer mostrar a mais?: '))


if __name__ == '__main__':
    execute()
