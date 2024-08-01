def countConsec(target):
    if not target:
        return []

    result = []
    current_element = target[0]
    current_count = 1

    for i in range(1, len(target)):
        if target[i] == current_element:
            current_count += 1
        else:
            result.append((current_element, current_count))
            current_element = target[i]
            current_count = 1

    # Add the last group
    result.append((current_element, current_count))

    return result

txt = input("Enter a list of objects: ")
ls = eval(txt)

if(len(ls)==0): print("Nothing to do.")
else:
    #ls = ast.literal_eval(txt)
    counters = countConsec(ls)
    pivot = counters[0][1]
    idx = 0
    for i in range(1, len(counters)):
        if(counters[i][1]>pivot):
            pivot = counters[i][1]
            idx = i
    
    print(counters[idx][0])
    print(counters[idx][1])
