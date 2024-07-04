txt = input('Enter a string: ')

num = int(input("Enter arrow's size (greater than 0): "))
if(num>0): 

    half = num//2

    for i in range(half):
        print(' '*i, end='')
        print(txt)

    if(num%2==1):
        print(' '*half+txt)

    for i in range(half):
        print(' '*(half-i-1), end='')
        print(txt)

else:
    print('Size must be greater than 0.')
