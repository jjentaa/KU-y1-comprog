n =  int(input("Enter a positive integer n: "))

def factt(num):
    ans = 1
    for i in  range(2, num+1): ans*=i
    return ans

print(f'>call fac({n})')

if(n==0):print(" 1", end="")
else:
    for i in range(n+1):
        print(" ", end="")
        for j in range(i+1):
            if(n-j==0):
                print(1, end='')
            else:
                print(n-j, end=' * ')
        
        if(i==n):
            pass
        else:
            print(f'fac({n-i-1})')
        
print()
    
print(f'>fac({n})={factt(n)}')