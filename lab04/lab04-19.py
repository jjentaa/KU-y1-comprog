def count_digits(number):
    count = 0
    if(number<0): number*=-1
    if(number==0): return 1
    while(number>0):
        count+=1
        number//=10
    return count

def get_last_digit(n):
    return n%10

def get_distribution(number):
    ans = ''
    n = count_digits(number)
    for i in range(n):
        txt = f'{get_last_digit(number)}x10^{i} + '
        ans+=txt
        number = number//10
    return ans[0:-2]

num = int(input("Input number: "))
print(f'{num} =', get_distribution(num))