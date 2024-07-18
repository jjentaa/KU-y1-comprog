import ast

txt = input("InputList: ")
ls = ast.literal_eval(txt)

ans = []

count = 1
pivot = ls[0]

for i in range(1, len(ls)):
    if(ls[i]==ls[i-1]): count+=1
    else:
        sub_ls = []
        for j in range(count): 
            sub_ls.append(ls[i-1])
        ans.append(sub_ls)
        count=1
sub_ls = []
for j in range(count): 
    sub_ls.append(ls[-1])
ans.append(sub_ls)
count=1
print(ans)
