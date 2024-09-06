import random, time
import turtle

class Card():
    """ Card(): create a card object. To create a deck, try \Card.test_Card()\! """
    symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
    def get_name(self):
        return self.name
    def get_suit(self):
        return self.suit
    def __repr__(self):
        return f"{self.name}{Card.symbols[self.suit]}"
    def test_Card():
        Names = ["A",2,3,4,5,6,7,8,9,"T","J","Q","K"]
        Suits = ["D","C","H","S"]
        deck = [Card(str(n), s) for s in Suits for n in Names]
        random.shuffle(deck)
        res = [str(card) for card in deck]
        return " ".join(res)
    
class Deck:
    """ Deck(): สร้างสำรับไพ่ """
    Names = ["A",2,3,4,5,6,7,8,9,"T","J","Q","K"]
    Suits = ["D","C","H","S"]
    def __init__(self):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
    def shuffle(self):
        random.shuffle(self.cards)
    def get_card(self):
        return self.cards.pop()
    def set_cards(self, cards):
        self.cards = cards
    def reset(self, n=1):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
        for i in range(n):
            self.shuffle()
    def __repr__(self):
        res = [str(x) for x in self.cards]
        return " ".join(res)
    
def preamble(RENDER=False):
    """ จัดการ environment ในการวาดเต่า """
    if not RENDER:
        return None
    #--------------------------------------------------------------------------------------
    global wn, pen
    wn, pen = turtle.Screen(), turtle.Turtle()
    wn.bgcolor("black")
    wn.setup(800, 600)
    wn.title("Deck of Cards Simulator by @TokyoEdtech, rebrewed by KunTotoNaMikeLabDotNet")
    pen.speed(0)
    pen.hideturtle()
    #--------------------------------------------------------------------------------------

def test_turtle_deck(RENDER=False):
    """ ไว้ตรวจสอบเต่าวาดไพ่ ฟังชัน Card.render() """
    preamble(RENDER)
    # create a deck f card
    deck = Deck()
    # shuffle deck
    deck.reset()
    print(deck)
    # render n cards (back) in a row
    nbOfCards = 5
    start_x = -250
    for x in range(nbOfCards):
        card = Card("", "")
        card.render(start_x + x*125, 175, "orange", RENDER=True)
    time.sleep(1)
    # re-render n cards in a row
    start_x = -250
    for x in range(nbOfCards):
        card = deck.get_card()
        card.render(start_x + x*125, 175, RENDER=True)
    print("Done..")

def createVirtualDeck(s="K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠"):
    dd = s.split()
    res = []
    suit = {"♦":"D","♣":"C","♥":"H","♠":"S"}
    for d in dd:
        card = Card(d[0], suit[d[1]])
        res.append(card)
    deck = Deck()
    deck.set_cards(res)
    return deck

class CardInHand:
    def __init__(self, name, hidden_status):
        self.name = name
        self.cards = []
        self.hidden_status = hidden_status
        self.score = 0
        self.nAce = 0

        self.n2val = {"O":0, "A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":10, "Q":10, "K":10}
        
    def checkBust(self) -> bool:
        if(self.score>21): return True
        return False
    
    def checkBlackjack(self) -> bool:
        if(self.score == 21 and len(self.cards)==2): return True
        if(self.score<=21 and len(self.cards)==5): return True

    def drawCard(self, card):
        self.cards.append(card)
        self.score += self.n2val[card.get_name()]
        if(card.get_name()=="A"):
            self.nAce+=1

        if(self.score>21 and self.nAce>0):
            self.score-=10
            self.nAce-=1

    def decision(self, op_score, isbj) -> bool:
        if(self.score<21 and not self.checkBlackjack() and len(self.cards)<5):
            if(self.score<=16): return True
            if(self.score<op_score and op_score<=21): return True
            if(self.score<21 and isbj): return True
        return False

    
    def __str__(self) -> str:
        txt = " "*(9-len(self.name))+self.name+": "

        for c in self.cards:
            txt+=str(c)+" "

        space = 16-3*len(self.cards)
        txt+=" "*space
        txt+=f"-> {self.score}"

        return txt
    
    def hidden(self) -> str:
        score = 0
        txt = " "*(9-len(self.name))+self.name+": "

        for c in range(len(self.cards)):
            if(c==0):
                txt += "O"+Card.symbols[self.cards[c].get_suit()]+" "
                score+=0
            else:
                # if(self.cards[c].get_name()=="A"): 
                #     score+=10
                score += self.n2val[self.cards[c].get_name()]
                txt+=str(self.cards[c])+" "

        space = 16-3*len(self.cards)
        txt+=" "*space
        txt+=f"-> {score}"

        return txt
    
def findResult(p1, p2) -> str:
    if(p1.checkBust() and p2.checkBust()): return "Draw!"
    elif(p1.checkBlackjack() and p2.checkBlackjack()): return "Draw!"
    elif(p1.checkBust() and not p2.checkBust()): return f"{p2.name} wins."
    elif(not p1.checkBust() and p2.checkBust()): return f"{p1.name} wins."
    elif(not p1.checkBlackjack() and p2.checkBlackjack()): return f"{p2.name} wins."
    elif(p1.checkBlackjack() and not p2.checkBlackjack()): return f"{p1.name} wins."
    else:
        if(p1.score>p2.score): return f"{p1.name} wins."
        elif(p1.score<p2.score): return f"{p2.name} wins."
        else: return "Draw!"

def play(player1='Computer', player2='Player', d=None, RENDER=False):
    print('Welcome to MikeLab BlackJack Casino.')
    preamble(RENDER)
    # create a deck of cards
    if d==None:
        deck = Deck()
        deck.reset()
    else:
        #----------------------------- virtual deck
        #d = 'A♦ A♥ 3♥ 4♣ 4♥ 7♣ 5♣ 6♦ A♠'
        deck = createVirtualDeck(d)

    p1 = CardInHand(name=player1, hidden_status=False)
    p2 = CardInHand(name=player2, hidden_status=False)

    p1.drawCard(deck.get_card())
    p2.drawCard(deck.get_card())
    p1.drawCard(deck.get_card())
    p2.drawCard(deck.get_card())

    print(p1.hidden())
    print(p2)

    while(p2.score<21 and len(p2.cards)<5):
        c = input("Draw another card (y/n): ")
        if(c in ["y", "Y"]):
            p2.drawCard(deck.get_card())
            print(p2)
        else: break

    while(p1.decision(p2.score, p2.checkBlackjack())):
        p1.drawCard(deck.get_card())

    print("+++++++++++++++++++++++++++++++++")
    print(p1)
    print(p2)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(findResult(p1, p2))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")

  ###--------------- student code ends here ---------------###
## main begins here
def testcase01():
    random.seed(2)
    play()
def testcase02():
    random.seed(16)
    play()
def testcase03():
    random.seed(30)
    play()
def testcase04():
    s = 'K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠'
    play('Toto', 'Tutu', d=s)

def testcase05():
    s = 'A♣ 3♥ 2♠ T♥ 8♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase06():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase07():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ T♠'
    play(d=s)
def testcase08():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ Q♥ 3♠'
    play(d=s)
def testcase09():
    s = '5♠ A♥ A♣ 8♥ J♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase10():
    s = 'A♣ 3♦ A♦ A♥ 3♥ 4♣ 4♥ 7♣ 3♣ 2♦ A♠'
    play(d=s)
#------------------------------------------
q = int(input())
if q==1:
    testcase01()
elif q==2:
    testcase02()
elif q==3:
    testcase03()
elif q==4:
    testcase04()
elif q==5:
    testcase05()
elif q==6:
    testcase06()
elif q==7:
    testcase07()
elif q==8:
    testcase08()
elif q==9:
    testcase09()
elif q==10:
    testcase10()

