minute = float(input('Minutes before due: '))
temp = float(input('Temperature: '))
is_rain = input('Is it raining (y/n)? ')

day = minute/(24*60)
if(1>day>=0.5):
    day=1
else :
    day = round(day)
print(f'>>> {round(day)} days before due.')



if(day<2):
    print('>>> I will do the assignment.')
elif(5<day):
    print('>>> I will not do the assignment.')
else:
    if(temp>40):
        print('>>> I will not do the assignment.')
    elif(temp>25 and is_rain in ['y', 'Y']):
        print('>>> I will not do the assignment.')
    else:
        print('>>> I will do the assignment.')
