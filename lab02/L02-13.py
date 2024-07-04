inj =input('Is Bulotelli injured?(y/n) ')
if(inj=='y'):
    print('Not available')
else:
    lt = input('Is Bulotelli late for the training?(y/n) ')
    if(lt=='n'):
        print('Starter')
    else:
        pw = input('Did Bulotelli perform well in training?(y/n) ')
        if(pw=='n'):
            print('Not selected')
        else:
            print('Substitute')