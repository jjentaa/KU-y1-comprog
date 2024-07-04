tv = int(input('How many TVs? '))
dvd = int(input('How many DVD players? '))
aus = int(input('How many Audio Systems? '))

price = (tv*6000)+(dvd*1500)+(aus*3000)
print('Total price is', format(price, '.2f'), 'baht.')

if(price>=24000):
    print("You've got a discount of", format(price*0.2, '.2f'), 'baht.')
    print('Your payment is', format(price*0.8, '.2f'), 'baht. Thank you!')
else:
    print('Your payment is', format(price, '.2f'), 'baht. Thank you!')