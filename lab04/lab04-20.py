def factorial(x):
    if(x==1): return 1
    return x*factorial(x-1)

num = int(input("Input k: "))
total = 0
for i in range(num):
    print(f'{i+1}! = {factorial(i+1)}')
    total+=factorial(i+1)

print(f"Summation of factorial 1!-{num}! = {total}")