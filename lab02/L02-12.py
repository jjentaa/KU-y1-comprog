minute = int(input('How long have Buzz played ?: '))
hr = minute//60
leftover = minute%60

if(leftover>20):
    hr+=1

price = hr*900

if(hr>=5):
    print(f'Total price is {round(price*0.7)} baht.')
elif(hr>=4):
    print(f'Total price is {round(price*0.8)} baht.')
elif(hr>=2):
    print(f'Total price is {round(price*0.9)} baht.')
else:
    print(f'Total price is {round(price)} baht.')