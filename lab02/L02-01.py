f_amount = float(input('Enter initial amount in Baht: '))
ir = float(input('Enter interest rate in percent: '))

ls = [1, 5, 10, 20]

for yr in ls:
    if(yr==1):
        print(f'Total amount after {yr} year is', format(((1+(ir/100))**(yr))*f_amount, '.2f'), 'Baht.')
    else:
        print(f'Total amount after {yr} years is', format(((1+(ir/100))**(yr))*f_amount, '.2f'), 'Baht.')