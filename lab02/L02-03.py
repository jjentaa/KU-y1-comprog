x = int(input('x: '))
opt = input('Operator: ')
y = int(input('y: '))

if(opt not in ['+', '-', '*', '/', '%']):
    print('Unknown Operator')
else:
    if(opt == '+'):
        print(x+y)
    if(opt == '-'):
        print(x-y)
    if(opt == '*'):
        print(x*y)
    if(opt == '/'):
        print(format(x/y, '.2f'))
    if(opt == '%'):
        print(x%y)