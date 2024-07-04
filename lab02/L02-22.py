days = int(input('How many day : '))
start = 0.95

add_all = 0.0
for i in range(days):
    txt = f'Input price in day {i+1} : '
    price = float(input(txt))
    add_all+=price*(start)
    start-=0.01
    
print('Summary price =', format(add_all, '.2f'))