w = int(input('Weight: '))
h = int(input('Height: '))
h /= 100

bmi = w/(h*h)
bmi_str = format(bmi, '.1f')
print(f'Your BMI is {bmi_str}', end=' ')

if(30<=bmi):
    print("You're in the obese range.")
elif(25<=bmi):
    print("You're in the overweight range.")
elif(18.6<=bmi):
    print("You're in the healthy weight range.")
else:
    print("You're in the underweight range.")