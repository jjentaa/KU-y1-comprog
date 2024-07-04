target = 72
while True:
    guess = int(input('Enter your guess (0 - 100): '))

    if(0<=guess<=100):
        if(guess==target):
            print('Congratulations, your guess is correct.')
            break
        elif(guess>target):
            print('Sorry, your guess is too high, try again later.')
        else:
            print('Sorry, your guess is too low, try again later.')
    else:
        print('Sorry, out of range, try again later.')