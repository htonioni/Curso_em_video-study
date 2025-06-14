print('='*37)
print('BANCO VR'.center(37,' '))
print('='*37)

user_qnt = int(input('What quantity would you like to withdraw?: $'))
avaliable_bills = [50, 20, 10, 1]
counter_50 = counter_20 = counter_10 = counter_1 = 0
value_left = user_qnt 

while True:
  counter_50 += 1
  value_left -= avaliable_bills[0]
  
  if value_left < avaliable_bills[0]:
    print(f'Total of {counter_50} $50.00 bills')
    break

if value_left != 0 and value_left > 20:
   while True:
     counter_20 +=1
     value_left -= avaliable_bills[1]

     if value_left < avaliable_bills[1]:
      print(f'Total of {counter_20} $20,00 bills')
      break

if value_left != 0 and value_left > 10:
  while True:
    counter_10 += 1
    value_left -= avaliable_bills[2]

    if value_left < avaliable_bills[2]:
      print(f'Total of {counter_10} $10,00 bills')
      break
if value_left != 0:
  while True:
    counter_1 += 1
    value_left = value_left - avaliable_bills[3]

    if value_left < avaliable_bills[3]:
        print(f'Total of {counter_1} $1,00 bills')
        break
print('='*37)
print('BANCO VR wish you a happy Christmas! Have a nice day')