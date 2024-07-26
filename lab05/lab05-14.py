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

class AST:
    def literal_nested_list(self, ls_txt):
        current = ""
        final_ls = []

        nowQuote = ""
        isString = False
        for s in ls_txt:
            #start string
            if(s in "\"'" and not isString):
                nowQuote = s
                isString = True
            #end string
            elif(s == nowQuote and isString):
                isString = False
            
            if(s=="," and not isString):
                final_ls.append(self.literal_eval(current))
                current=""
            else:
                current+=s

        if(current):
            final_ls.append(self.literal_eval(current))
        
        return final_ls
    
    def literal_nested_tuple(self, ls_txt):
        current = ""
        final_ls = []

        nowQuote = ""
        isString = False
        for s in ls_txt:
            #start string
            if(s in "\"'" and not isString):
                nowQuote = s
                isString = True
            #end string
            elif(s == nowQuote and isString):
                isString = False
            
            if(s=="," and not isString):
                final_ls.append(self.literal_eval(current))
                current=""
            else:
                current+=s

        if(current):
            final_ls.append(self.literal_eval(current))
        
        return tuple(final_ls)
    
    def literal_nested_set(self, ls_txt):
        current = ""
        final_ls = ()

        nowQuote = ""
        isString = False
        for s in ls_txt:
            #start string
            if(s in "\"'" and not isString):
                nowQuote = s
                isString = True
            #end string
            elif(s == nowQuote and isString):
                isString = False
            
            if(s=="," and not isString):
                final_ls.append(self.literal_eval(current))
                current=""
            else:
                current+=s

        if(current):
            final_ls.append(self.literal_eval(current))
        
        return set(final_ls)
    
    def literal_eval(self, text):
        s = text.strip()

        # detect list , set, tuple
        if(s[0]=="[" and s[-1]=="]"):
            return self.literal_nested_list(s[1:-1])
        if(s[0]=="{" and s[-1]=="}"):
            return self.literal_nested_set(s[1:-1])
        if(s[0]=="(" and s[-1]==")"):
            return self.literal_nested_tuple(s[1:-1])

        #single specific word
        if(s=="True"): return True
        if(s=="False"): return False
        if(s=="None"): return None
        if(s.isdigit()): return int(s)
        if(s[0]=='"'and s[-1]=='"'): return s[1:-1]
        if(s[0]=="'" and s[-1]=="'"): return s[1:-1]

        return s
    
ast = AST()

    #check element and type

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