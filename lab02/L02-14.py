is_man = input("What's the result of Manchester city's match? ")
is_liver = input("What's the result of Liverpool's match? ")

if(is_man=='won' and is_liver=='lost'):
    print('Manchester city is the champion of Premier League.')
elif(is_man=='lost' and is_liver=='won'):
    print('Liverpool is the champion of Premier League.')
else:
    m_goal = int(input('What is the margin that Manchester city won by? '))
    l_goal = int(input('What is the margin that Liverpool won by? '))
    if(m_goal>l_goal):
        print('Manchester city is the champion of Premier League.')
    elif(l_goal>m_goal):
        print('Liverpool is the champion of Premier League.')
    else:
        play_off = input('Which team won the play-off match?(Manchester city/Liverpool) ')
        if(play_off=='Liverpool'):
            print('Liverpool is the champion of Premier League.')
        else:
            print('Manchester city is the champion of Premier League.')