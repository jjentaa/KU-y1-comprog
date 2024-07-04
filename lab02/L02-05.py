target = 72
guess = int(input('Enter your guess (0 - 100): '))

if(guess==target):
    print('Congratulations, your guess is correct.')
elif(0<=guess<=100):
    print('Sorry, your guess is wrong, try again later.')
else:
    print('Sorry, out of range, try again later.')