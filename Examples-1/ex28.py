class SavingsAccount:
    def __init__(self,name="",account_balance=0.0):
        self.name=name
        self.account_balance=account_balance
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setBalance(self,account_balance):
        self.account_balance=account_balance
    def getBalance(self):
        return self.account_balance
    def makeDeposit(self,amount):
        self.account_balance+=amount
    def makeWithdrawal(self,amount):
        if amount<=self.account_balance:
            self.account_balance-=amount
        else:
            print("Insufficient funds, transaction denied.")

def main():
    account=SavingsAccount()
    name1=input("Enter the person's name:")
    account.setName(name1)
    print("D=Deposit W=Withdrawal Q=Quit")
    request=input("Enter D , W or Q:").upper()
    while True:
        if request=='D':
            amountofDeposit=float(input("Enter the amount of deposit:"))
            account.makeDeposit(amountofDeposit)
            print(f"Balance:{account.getBalance()}")
            request=input("Enter D , W or Q:").upper()
        elif request=='W':
            amountofWithdrawal=float(input("Enter the amount of withdrawal:"))
            account.makeWithdrawal(amountofWithdrawal)
            print(f"Balance {account.getBalance()}")
            request=input("Enter D , W or Q:").upper()
        elif request=='Q':
            print(f"End of transactions, Have a good day {account.getName()}.")
            break
        else:
            request=input("Enter D, W or Q:").upper()

main()