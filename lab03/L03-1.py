x = int(input())
y = int(input())

def func1(y):
    global x
    return y+x+1


print(func1(y)==y+x+1)