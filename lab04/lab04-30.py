import ast

# def comapre(n1, n2):
#     try:
#         if(int(n1)>int(n2)):
#             return True
#         else: False
#     except:
#         if()

txt = input("Input: ")
ls = ast.literal_eval(txt)

unique_ele = []
for k in ls:
    if(k not in unique_ele and '[' in str(k)): unique_ele.append(k)

ans = []
for i in unique_ele:
    ans.append([i, ls.count(i)])

for i in range(len(ans)):
    for j in range(i+1, len(ans)):
        if(ans[i][1]>=ans[j][1]):
            ans[i], ans[j] = ans[j], ans[i]
        # elif(ans[i][1]==ans[j][1]):
        #     if(ans[i][0]>ans[j][0]):
        #         ans[i], ans[j] = ans[j], ans[i]
ans.reverse()
for i in ans:
    print(f'{i[0]}: {i[1]}')