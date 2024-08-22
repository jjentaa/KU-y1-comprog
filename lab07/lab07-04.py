class Coin:
    def __init__(self, value: int= 1):
        self.value = value

    def __str__(self) -> str:
        return f'{self.value} Baht Coin'

class BankNote:
    def __init__(self, value: int=20):
        self.value = value

    def __str__(self) -> str:
        return f'{self.value} Baht Banknote'
    
money = int(input("Input amount : "))
banks = [
    BankNote(1000),
    BankNote(500),
    BankNote(100),
    BankNote(50),
    BankNote(20)
]
coins = [
    Coin(10),
    Coin(5),
    Coin(2),
    Coin(1)
]

for i in range(len(banks)):
    if(banks[i].value <= money):
        total = money//banks[i].value
        money = money%banks[i].value
        print(f"You get {total} of", banks[i])

for i in range(len(coins)):
    if(coins[i].value <= money):
        total = money//coins[i].value
        money = money%coins[i].value
        print(f"You get {total} of", coins[i])