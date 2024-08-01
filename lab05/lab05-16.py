def different_ls(ls1, ls2):
    ans = []
    for i in ls1:
        if(i not in ls2): ans.append(i)
    return ans

txt1 = input("Input list1: ")
txt2 = input("Input list2: ")

ls1 = eval(txt1)
ls2 = eval(txt2)

missing_in_list1 = different_ls(ls2, ls1)
additional_in_list1 = different_ls(ls1, ls2)

print("Missing values in list1 =", missing_in_list1)
print("Additional values in list1 =", additional_in_list1)
print("Missing values in list2 =", additional_in_list1)
print("Additional values in list2 =", missing_in_list1)
