def find_sum(n):
    total = 1
    for i in range(2, n+1):
        if(i%2): total+=i
        else : total-=i
    return total

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n, find_sum(n)))
