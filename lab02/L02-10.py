while True:
    num =int(input('Input number: '))
    if(num%2==0):
        print('Please input odd number')
    else:
        break

for i in range(num):
    for j in range(i+1):
        print('x', end='')
    print()

for k in range(num-1):
    for l in range(num-1-k):
        print('x', end='')
    print()