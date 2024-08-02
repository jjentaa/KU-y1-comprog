def merge(a, b):
    def strCompare(l1, l2):
        l = min(len(l1), len(l2))
        if(ord(l1[0])<ord(l2[0])): return False
        for k in range(l):
            if(ord(l1[k])>ord(l2[k])): return True
        return False
    res = a+b
    isString = (97<=ord(str(res[0])[0])<=122 or 65<=ord(str(res[0])[0])<=90)

    for i in range(len(res)-1):
        for j in range(i+1, len(res)):
            #int type
            if(isString):
                if(strCompare(res[i], res[j])):
                    res[i], res[j] = res[j], res[i]
            else:
                if(res[i]>res[j]):
                    res[i], res[j] = res[j], res[i]
    return res

def getInput():
    a = eval(input('Enter list a: '))
    b = eval(input('Enter list b: '))
    return a,b

### main begins here
a,b = getInput()
res = merge(a,b)
print(res)