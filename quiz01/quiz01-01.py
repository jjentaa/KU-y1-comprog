target = int(input("secret number = "))

counter = 0
for i in range(3):
    num = int(input("Enter your guess : "))
    counter+=1
    if(num==target):
        print("Congratulations, your guess is correct.")
        break
    if(counter==3):
        print("You've used all your attempts.")
    else:
        if(num<target):
            print("Sorry, your guess is too low, pls try again.")
        if(num>target):
            print("Sorry, your guess is too high, pls try again.")
    