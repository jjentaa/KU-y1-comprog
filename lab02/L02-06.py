b_amount = float(input('Enter buying amount: '))
if(b_amount<1000):
    print('Amount due after discount is', format(b_amount, '.2f'), 'baht.')
if(1000<=b_amount<3000):
    print('Amount due after discount is', format(b_amount*0.9, '.2f'), 'baht.')
elif(b_amount>=3000):
    print('Amount due after discount is', format(b_amount*0.85, '.2f'), 'baht.')
