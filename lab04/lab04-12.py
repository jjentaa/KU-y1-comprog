t = int(input("Estimated time : "))
w = t//7
pt, wt, ft = 0, 0, 0

for i in range(w):
    print(f"Week{i+1}")
    num1 = int(input("Physical therapy : "))
    num2 = int(input("Weight training : "))
    num3 = int(input("Fitness training : "))
    pt+=num1
    wt+=num2
    ft+=num3

if((pt>=2.5*t) and (wt>=2.5*t) and(ft>=2.5*t)): print("Buzzy has recovered in time.")
else: print("Buzzy has not recovered in time.")