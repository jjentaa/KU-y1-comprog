n = int(input())
half = n//2

for i in range(n):
    #boundary
    if(i==0 or i==n-1):
        print('.'*n, end="")

    #upper part
    elif(0<i<n//2):
        print(".", end="")

        for m in range(i-1):
            print(" ", end="")

        print(".", end="")
        #print(n-4-2*(i-1))
        for p in range(n-4-2*(i-1)):
            print(" ", end="")

        print(".", end="")

        for o in range(i-1):
            print(" ", end="")

        print(".", end="")

    #middle part
    elif(i==(n//2)):
        print(".", end="")
        for l in range((n//2)-1):
            print(" ", end="")
        print(".", end="")
        for l in range((n//2)-1):
            print(" ", end="")
        print(".", end="")

    #lower case
    else:
        #print("Hi")
        #print(n-i-2)
        print(".", end="")

        for m in range(n-i-2):
            print(" ", end="")

        print(".", end="")
        #print(n-4-2*(i-1))
        for p in range(((i-half)*2)-1):
            print(" ", end="")

        print(".", end="")

        for o in range(n-i-2):
            print(" ", end="")

        print(".", end="")

    print()