from random import randint
print('-=' * 36)
print("Let's play even or odd")

while True:
    print('-=' * 36)
    user_number = int(input('Type a value: '))
    user_choice = ' '
    while user_choice not in 'OE':
        user_choice = str(input('Even or odd? [E/O]: ')).strip().upper()[0]
    aleatory = randint(1, 10)

    if (user_number + aleatory)%2 == 0:
        print('-'*36)
        print(f"You have select {user_number} and the MACHINE selected {aleatory}. Total of {user_number+aleatory} so it's a even number! ")
        print('-'*36)
        if user_choice in ('e', 'E'):
            print("You've won!")
            print("Let's play again ....")
        else:
            print("You've LOST!")
            break
    else:
        print('-'*36)
        print(f"You have select {user_number} and the MACHINE selected {aleatory}. Total of {user_number+aleatory} so it's a odd number! ")
        print('-'*36)
        if user_choice in ('o','O'):
            print("You've won!")
            print("Let's play again ....")
        else:
            print("You've LOST!")
            break


