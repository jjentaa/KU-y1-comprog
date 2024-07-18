import ast
ans = []

def isList(target):
    if('[' in str(target)): return True
    return False

def all_ele(lss):
    global ans
    if(isList(lss)):
        #print(lss)
        for i in lss:
            #print(i)
            all_ele(i)
    else:
        ans.append(lss)

txt = input("Original list: ")
ls = ast.literal_eval(txt)
for j in ls:
    all_ele(j)

print("Flatten list:", ans)