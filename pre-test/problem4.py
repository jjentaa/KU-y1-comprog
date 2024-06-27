num = int(input("จำนวนขั้นบันได : "))
def counter_step(i_start):
    if(i_start==1):
        return 1
    if(i_start==2):
        return 2
    step_1 = counter_step(i_start-1)
    step_2 = counter_step(i_start-2)
    
    return step_1+step_2

print(counter_step(num))