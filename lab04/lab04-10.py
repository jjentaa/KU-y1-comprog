d = int(input("Distance from starting point(m.): "))
counter = 0
dis = 0
while(dis!=d):
    if(dis<d):
        dis+=5
        print(dis, end=' ')
        dis-=2
        print(dis, end=' ')
    else:
        dis-=4
        print(dis, end=' ')
        dis+=3
        print(dis, end=' ')
    counter+=1
#print(dis)
if(d==0): print("0\nBuzz moved 0 set(s)")
else: print(f"\nBuzz moved {counter} set(s)")