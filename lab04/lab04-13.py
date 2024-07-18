counter = 1
p_dis, t_dis = 0, 100
while True:
    pd = int(input("Input distance: "))
    t_dis+=2**counter
    p_dis+=pd
    print("Police distance:", p_dis)
    print("Criminal distance:", t_dis)
    counter+=1
    if(t_dis<=p_dis): break

print("Caught him!")