age = int(input('Enter your age: '))
net_in = int(input('Enter your net income: '))
if(15<=age<=60):
    if(1<=net_in<=79999):
        left = net_in-30000
        if(left>0):
            paid = 30000*0.2-0.12*left
            print('Your negative income tax is', format(paid, '.2f'), 'Baht.')
        else:
            print('Your negative income tax is', format(net_in*0.2, '.2f'), 'Baht.')
    else:
        print('Invalid income.')
else:
    print('Invalid age.')
