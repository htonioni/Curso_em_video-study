palavras = ('aprender', 'programar', 'linguagem', 
            'python', 'curso', 'gratis', 'trabalhar',
            'mercado', 'programador', 'futuro')

for vogais in palavras:
    print(f'\nNa palavra {vogais.upper()} temos ', end='')
    
    for letra in vogais:
        
        if letra in ('aeiouAEIOU'):
            print(letra, end=' ')
    # Para evitar a quebra no começo:
    # print(end='\n')