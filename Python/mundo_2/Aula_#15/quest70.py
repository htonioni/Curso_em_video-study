total_purchased = more_than_1k = less_expensive_price = test = 0
print('-'*37)
print('DOLLAR TREE'.center(37))
print('-'*37)
while True:
    product_name = str(input('What is the product name?: '))

    product_price = float(input('What is the product price?: '))
    #TODO Testar se ese preço é o mais barato
    

    if total_purchased == 0:
        test = product_price 
        less_expensive_name = product_name
    elif product_price < test:
        less_expensive_price = product_price
        less_expensive_name = product_name
    
    elif product_price > 1000:
        more_than_1k += 1
    total_purchased += product_price
    
    

    should_continue = ' '
    while should_continue not in 'YN':
        should_continue = str(input('\033[31mWould you like to continue? [Y/N]:\033[m ')).strip().upper()[0]
    
    if should_continue == 'N':
        break

print(' PROGRAM CONCLUDED '.center(37, '-'))
print(f'The total purchased is R${total_purchased:.2f}')
print(f'We have {more_than_1k} products costing more than R$1000.00')
print(f'The cheaper product is {less_expensive_name}, and cost R{less_expensive_price:.2f}')