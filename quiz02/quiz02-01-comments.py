# define list of some chracters for print
rat = '__QQ\n()">'.split("\n")
hunter = ' O \n/|\\\n/ \\'.split("\n")
lion = ' /\_/\ \n( o.o )\n > ^ < '.split("\n")

patterns = [rat, hunter, lion]

# get names
name1 = input("Player1 name: ")
name2 = input("Player2 name: ")

# define initial scores
s1 = 0
s2 = 0

# main loop
for i in range(5):
    # if score of someone = 3 just break the loop
    if(s1==3 or s2==3): break
    
    # print some lines
    print()
    print(f"Round {i+1}!")
    print(f"{name1} {s1} / {name2} {s2}")

    # format the text for using in the input
    txt1 = f"{name1}'s choice (1/rat, 2/hunter and 3/lion): "
    txt2 = f"{name2}'s choice (1/rat, 2/hunter and 3/lion): "
    
    # user input choice
    c1 = int(input(txt1))
    c2 = int(input(txt2))

    # conditions for checking and updating score
    if(c1==3 and c2==1): s1+=1
    if(c1==3 and c2==2): s2+=1

    if(c1==2 and c2==1): s2+=1
    if(c1==2 and c2==3): s1+=1

    if(c1==1 and c2==2): s1+=1
    if(c1==1 and c2==3): s2+=1

    # display the pattern
    '''
    the rat is the one pattern that use only 2 lines for display 
    but the others use 3 lines
    so we have to use some condition to check it
    '''
    for j in range(3):
        # if c1 = rat and c2 also = rat and it is the last round of print so don't print the last line
        if(c1==1 and c2==1 and j==2):
            pass
        else:
            # if c1 = rat and it's the last line so we will print the space
            if(c1==1 and j==2):
                print("    ", end="  ")
            else:
                print(patterns[c1-1][j], end="  ")
            
            # if the loop run to the middle or second line just print "VS"
            if(j==1):
                print("VS", end="  ")
            else:
                print("  ", end="  ")

            # if c2 = rat and it's the last line so we will print the space
            if(c2==1 and j==2):
                print("    ", end="  ")
            else:
                print(patterns[c2-1][j], end="")
            print()


# display the final result
print()
print(f"{name1} {s1} / {name2} {s2}")

# find the winner
if(s1>s2): print(f"{name1} win!")
elif(s1<s2): print(f"{name2} win!")
else: print("Draw!")

print()

#10.17.124.152