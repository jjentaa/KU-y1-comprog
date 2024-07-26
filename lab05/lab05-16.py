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
    

def different_ls(ls1, ls2):
    ans = []
    for i in ls1:
        if(i not in ls2): ans.append(i)
    return ans

ast = AST()
txt1 = input("Input list1: ")
txt2 = input("Input list2: ")

# ls1 = ast.literal_eval(txt1)
# ls2 = ast.literal_eval(txt2)

ls1 = eval(txt1)
ls2 = eval(txt2)

missing_in_list1 = different_ls(ls2, ls1)
additional_in_list1 = different_ls(ls1, ls2)

print("Missing values in list1 =", missing_in_list1)
print("Additional values in list1 =", additional_in_list1)
print("Missing values in list2 =", additional_in_list1)
print("Additional values in list2 =", missing_in_list1)