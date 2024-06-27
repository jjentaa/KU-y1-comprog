num = int(input("Input Level: "))

mid = 3 + (4*num)

#tri
for i in range(num-1):
    for j in range(mid//2-(2*i)):
        print(' ', end='')
    for k in range(1+(4*i)):
        print('o', end='')
    print()
#rec
for i in range((num+1)*2):
    print(' '*3+'o'*(1+(4*(num-1))))
#middle
for i in range(num):
    print('o'*mid)
    
#dam
for i in range(num+2):
    print(' '*(num+2)+'o'*((num*2)-1))
    
#dam big
for i in range(num):
    print(' '*3+'o'*(1+(4*(num-1))))
    
#print last
print(' '*(num+2)+'o'*((num*2)-1))