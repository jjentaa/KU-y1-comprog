def fibo(num):
    if(num==1 or num==2):
        return 1
    arr = [1, 1]
    for i in range(num-2):
        arr.append(arr[-1]+arr[-2])
    return arr[num-1]

n = int(input("Enter n: "))
print(f"fibo({n}) =", fibo(n))