d = int(input("Insert amount of bottle of dragon's milk: "))
p = int(input("Insert amount of penguin's egg: "))
g = int(input("Insert amount of grimoire: "))
tc = (d*100)+(p*140)+(g*600)
ts = (d*120)+(p*150)+(g*700)
print(f'The total cost price is {tc}.')
print(f'The total selling price is {ts}.')
profit = (ts-tc)/tc*100
print('The total profit is {0:.2f}%'.format(profit))
if(profit<15):
    print("You can't make enough profit. You are fired!!")