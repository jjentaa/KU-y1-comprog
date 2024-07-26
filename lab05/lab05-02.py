def list_factors(n):
    ls = []
    txt = ''
    for i in range(1, n+1):
        if(n%i==0): txt+=str(i)+" "
    
    return txt

def find_sum_and_num_factors(n):
    ls = list_factors(n).strip()
    ls = ls.split()
    nn = len(ls)
    factors = [int(i) for i in ls]

    return (sum(factors), len(factors))

num = int(input("Enter positive number: "))
print(f'Factors of {num} are ')

fact_ls = list_factors(num)
result = find_sum_and_num_factors(num)

print(fact_ls)
print(f'Sum of {fact_ls}is {result[0]}')
print(f'Number of factors is {result[1]}')
if (result[1] > 2) or (result[0]==1):
    print(f'{num} is not prime number.')
else:
    print(f'{num} is prime number.')