txt = input("Enter a string: ")
txt = txt.lower()

v = []
c = []

for i in txt:
    if(97<=ord(i)<=122):
        if(i in ['a', 'e', 'i', 'o', 'u']):
            if(i not in v): v.append(i)
        else:
            if(i not in c): c.append(i)

print("Unique vowels: ", v)
print("Unique consonants: ", c)