def execute():
    print('Ok, vamos lá')
    gen = str(input('Digite seu sexo: ')).strip().upper()[0]

    while gen not in 'FM':
        gen = str(input('Dados inválidos. Por favor informe novamente: ')).strip().upper()[0]
    print(f'Sexo {gen} registrado com sucesso!')

if __name__=='__main__':
    execute()