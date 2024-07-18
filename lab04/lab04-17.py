def is_Valid(a, b, c):
    if(a==0 and b==0): return False
    if(c==0 and b==0): return False
    if(c==0 and a==0): return False
    return True

def ans(a, b, c):
    if(a==0 and b==0): return "C"
    if(c==0 and b==0): return "A"
    if(c==0 and a==0): return "B"

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

while(is_Valid(a, b, c)):
    if(a>=c and b>=c): 
        a-=1
        b-=1
        c+=1
    elif(a>=b and c>=b): 
        a-=1
        c-=1
        b+=1
    elif(b>=a and c>=a): 
        b-=1
        c-=1
        a+=1

print(ans(a, b, c))
