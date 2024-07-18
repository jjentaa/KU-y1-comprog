txt = input("Enter list of number: ")
ls = txt.split(" ")
ls_num = [int(i) for i in ls]

ans = []
for i in range(len(ls_num)):
    for j in range(i+1, len(ls_num)):
        if((ls_num[i]-ls_num[j]==3) or (ls_num[i]-ls_num[j]==-3)): ans.append([ls_num[i], ls_num[j]])

print("Output list:", ans)