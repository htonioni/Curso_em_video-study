older_than_18 = men_count = women_younger_20 = 0
while True:
    print('-' * 37)
    print('          CROWD ANALYZER     ')
    print('-' * 37)
    

    person_age = int(input('How old is him/her?: '))
    if person_age > 18:
        older_than_18 += 1
    person_sex = ' '
    while person_sex not in 'FM':
        person_sex = str(input('What is his gender? [M/F]: ')).strip().upper()[0]
    if person_sex in ('m', 'M'):
        men_count += 1
    if person_sex in ('f', 'F'):
        if person_age < 20:
            women_younger_20 += 1

    print('-' * 37)
    should_continue = str(input('\033[31mDo you want do continue? [Y/N]\033[m: '))
    print('        ')
    if should_continue in ('N', 'n'):
        break

print(f'Total de pessoas com mais de 18 anos: {older_than_18}')
print(f'Ao todo temos {men_count} homens cadastrados')
print(f'E temos {women_younger_20} mulheres com menos de 20 anos')

