num1 = input("Enter a number (to stop, just [Enter]): ")
if(num1==''): print("Nothing to do.")
else:
    ls = []
    ls.append(float(num1))
    while True:
        txt = input("Enter a number (to stop, just [Enter]): ")
        if(txt==''): break
        ls.append(float(txt))
    print("The maximum is", format(max(ls), '.2f'))
    print("The minimum is", format(min(ls), '.2f'))
    print("The average is", format(sum(ls)/len(ls), '.2f'))