def count_digits(number):
    count = 0
    if(number<0): number*=-1
    if(number==0): return 1
    while(number>0):
        count+=1
        number//=10
    return count

number = int(input("Enter number: "))
print(f"There are {count_digits(number)} digits in {number}")