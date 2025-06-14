def execute():
    print('\nOlá seja bem vindo ao desafio #61 - GERADOR de PA!')
    print('-=' * 20)
    primeiro_termo = int(input('Digite o primeiro termo: '))
    rz_pa = int(input('Razão da PA: '))
    counter = 1
    termo_gerado = primeiro_termo
    print(primeiro_termo, end=' => ')

    while counter < 10:
        termo_gerado = termo_gerado + rz_pa
        print(termo_gerado, end=' => ')
        counter += 1

    print('\033[31mAcabou!\033[m')


if __name__ == '__main__':
    execute()
