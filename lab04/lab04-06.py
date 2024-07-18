password = "Programming is fun"

counter = 1
while counter<4:
    txt = input('Enter the password: ')
    if(txt==password): 
        print("Correct password")
        print("Access allowed")
        break
    else:
        print(f"Password is wrong, attempt #{counter}")
        print("Access not allowed")
    counter+=1

if(counter==4):
    print("Maximum attempts exceeded")