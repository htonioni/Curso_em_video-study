sommation = number = counter = 0


while True:
    number = int(input('Type a number (999 to stop): '))
    if number == 999:
        break
    sommation = number + sommation
    counter += 1
    
print(f'The sum of these {counter} numbers is {sommation}')