def check_prime(n):
    if(n==1):
        return False
    for i in range(2, int(n**0.5)+1):
        if(n%i==0):
            return False
    return True

def factor_count(n):
    if(check_prime(n)):
        return 2
    else:
        counter = 0
        for i in range(1, n+1):
            if(n%i==0): counter+=1
        return counter

num = int(input("Enter n: "))
c = factor_count(num)
print(c)