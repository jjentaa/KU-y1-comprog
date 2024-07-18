h = int(input("How deep is the well? "))
u = int(input("Enter the height the frog can jump up: "))
d = int(input("Enter the height the frog slips down: "))

if(u==d and h!=u): print("The frog will never escape from the well.")
else:
    dis = h
    counter = 1
    while(dis-u>0):
        dis-=u
        print(f"On day {counter} the frog leaps to the depth of {dis} meters.")
        dis+=d
        print(f"At night he slips down to the depth of {dis} meters.")
        counter+=1

    print(f"The frog is free on day {counter}.")