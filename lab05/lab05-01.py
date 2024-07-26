def isPrime(number):
    if(number==1): return False
    if(number==2): return True

    for i in range(2, number//2+1):
        if(number%i==0):
            return False
        
    return True

def printAllPrimes(limit):
    txt=""
    for i in range(1, limit+1):
        if(isPrime(i)): txt+=str(i)+" "
    print(txt)

number = int(input("Input n: "))
printAllPrimes(number)