from numpy import number


def execute():
    print('Seja bem vindo ao exercício #65 - Maior e Menor valores!')
    keep_playing = 'S'
    number_total = 0 
    counter = 0
    soma = 0
    maior_num = menor_num = 0
    
    while keep_playing == 'S':
        user_input_number = int(input('Digite um número: '))
        keep_playing = str(input('Gostaria de continuar? [S/N] ')).upper().strip()[0]
        if counter == 0:
            number_total = 0
        counter += 1
        if counter == 1:
            maior_num = menor_num = user_input_number
        else:
            if user_input_number > maior_num:
                maior_num = user_input_number
            elif user_input_number < menor_num:
                menor_num = user_input_number
        number_total = soma 
        soma = user_input_number + number_total
        
    media = soma / counter
    
    print(f'Você digitou {counter} numeros e a média foi {media}')
    print(f'O maior numero foi {maior_num} e o menor numero foi {menor_num}')



if __name__ == '__main__':
    execute()