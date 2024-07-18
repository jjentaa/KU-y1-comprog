import ast

txt = input("InputList: ")
ls = ast.literal_eval(txt)

ans = [ls[0]]
for i in range(1, len(ls)):
    if(ls[i]!=ans[-1]): ans.append(ls[i])
    
print(ans)