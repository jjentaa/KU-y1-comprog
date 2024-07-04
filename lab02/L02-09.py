num = int(input('Input number: '))

for i in range(num):
    for j in range(i+1):
        print(j+1, end=' ')
    print()