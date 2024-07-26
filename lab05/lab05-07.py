lucky = input("Enter lucky number : ")
n = int(input("Enter amount of candidates : "))
pivot = ""
counter = 0
for i in range(n):
    txt = f"Enter ID card number {i+1}: "
    ids = input(txt)
    now = ids.count(lucky)
    if(now>counter):
        counter=now
        pivot=ids
    elif(now==counter and int(pivot)<int(ids)):
        counter=now
        pivot=ids

print("Winner:", pivot)