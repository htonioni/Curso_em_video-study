import ex.quest57 as q57
import ex.quest58 as q58
import ex.quest59 as q59
import ex.quest60 as q60
import ex.quest61 as q61
import ex.quest62 as q62
import ex.quest63 as q63
import ex.quest64 as q64
import ex.quest65 as q65


menu = str(input('Escolha uma opção:\n'
                '[ A ] Escolher número do exercício\n'
                '[ B ] Passar por todos\n'
                'Sua escolha: '))
if menu not in ('AaBb'):
    print('Inválido!')
else:
    if menu in ('Bb'):
        quest57 = input('Gostaria de fazer o exercício #57 - M ou F?: ')
        if quest57.lower() in ('y', 'yes'): q57.execute()
        else:
            quest58 = str(input('Gostaria de fazer o exercício #58 - Jogo de adivinha?: '))
        if quest58 in ('y', 'yes'): q58.execute()
        else:
            quest_59 = str(input('Gostaria de fazer o exercício #59 - Operações com dois valores?: '))
        if quest_59 in ('y', 'yes'):q59.execute()
        else:
            quest_60 = str(input('Gostaria de fazer o exercício #60 - Cálculo de fatorial?: '))
            if quest_60 in ('y', 'yes'):
                q60.execute()
            else:
                quest_61 = str(input('Gostaria de fazer o exercício #61 - Progressão aritmética?: '))
                if quest_61 in ('y', 'yes'):
                    q61.execute()
                else:
                    quest_62 = str(input('Gostaria de fazer o exercício #62 - Super progressão Aritmética?: '))
                    if quest_62 in ('y', 'yes'):
                        q62.execute()
                    else:
                        quest_63 = str(input('Gostaria de fazer o exercício #63 - Sequência de Fibonacci?: '))
                        if quest_63 in ('y', 'yes'):
                            q63.execute()
                        else:
                            quest_64 = str(input('Gostaria de fazer o exercício #64 - Tratando valores?: '))
                            if quest_64 in ('yes', 'y'):
                                q64.execute()
                            else:
                                quest_65 = str(input('Gostaria de fazer o exercício #65 - Media, Maior e Menor valores?: '))
                                if quest_65 in ('yes', 'y'):
                                    q65.execute()
                                else:
                                    print('Acabaram os exercícios da aula #14!!')
    else:
        user_choice = int(input('Qual número do exercício?: '))
        if user_choice == 57:
            q57.execute()
        elif user_choice == 58:
            q58.execute()
        elif user_choice == 59:
            q59.execute()
        elif user_choice == 60:
            q60.execute()
        elif user_choice == 61:
            q60.execute()
        elif user_choice == 62:
            q62.execute()
        elif user_choice == 63:
            q63.execute()
        elif user_choice == 64:
            q64.execute()
        elif user_choice == 65:
            q65.execute()