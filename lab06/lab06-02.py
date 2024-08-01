txt = input("Input sentence: ")
n = int(input("Input row: "))

new_arr = ['']*n
idx = 0
runner = 1
for i in range(len(txt)):
    #running top to bottom
    new_arr[idx]+=txt[i]
    if(idx<n-1 and runner==1):
        idx+=1
    #running bottom to top
    elif(idx>0 and runner==-1):
        idx-=1
    else:
        runner *= -1
        idx+=runner

print(''.join(new_arr))