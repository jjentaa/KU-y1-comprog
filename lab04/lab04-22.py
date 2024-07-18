def convert_tuple(target):
    ls = []
    for t in target:
        sub_ls = [int(ele) for ele in t]
        ls.append(tuple(sub_ls))
    return ls

txt = input("Enter list of tuple: ")
ls_str = list(txt.split(" "))
#print(ls_str)
print("Input list:", convert_tuple(ls_str))
ls_num = [int(i) for i in ls_str]
for i in range(len(ls_num)):
    for j in range(i, len(ls_num)):
        last1 = ls_num[i]%10
        last2 = ls_num[j]%10
        if(last1>last2):
            ls_num[i], ls_num[j] = ls_num[j], ls_num[i]


ls_sorted_str = [str(j) for j in ls_num]

print("Output list:", convert_tuple(ls_sorted_str))