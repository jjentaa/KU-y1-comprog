choice = input('Enter your buffet choice: ')
if(choice not in ['Japanese', 'Korean']):
    print(f'Sorry, there is no {choice} buffet.')
else:
    is_w = input('Is today Wednesday (yes/no)? ')
    if(is_w=='yes' and choice=='Japanese'):
        print('Your payment is 850.00 Baht.')
    if(is_w=='yes' and choice=='Korean'):
        print('Your payment is 1275.00 Baht.')
    if(is_w=='no' and choice=='Japanese'):
        print('Your payment is 1000.00 Baht.')
    if(is_w=='no' and choice=='Korean'):
        print('Your payment is 1500.00 Baht.')