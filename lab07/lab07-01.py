class BankAccount:
    def __init__(self, accountID: str="1001", balance: float=0.00):
        self.accountID = accountID
        self.balance = balance

    def __str__(self) -> str:
        return f"ID: {self.accountID}, Balance: {self.balance:.2f}"

    def set_accout_ID(self, newID: str):
        self.accountID = newID

    def set_balance(self, new_balance: float):
        self.balance = new_balance

    def get_account_ID(self) -> str:
        return self.accountID
    
    def get_balance(self) -> int:
        return self.balance
    
    def deposit(self, amount: float):
        self.balance += amount

    def withdrawal(self, amount: float):
        self.balance -= amount
    
# test
account = BankAccount("1001",500)

print(account.get_account_ID())
print(account.get_balance())
account.set_balance(5000)
print(account.get_balance())

amount = float(input("Enter your deposit amount: "))
account.deposit(amount)
print(amount)

amount = float(input("Enter your withdrawal amount: "))
account.withdrawal(amount)
print(account)

