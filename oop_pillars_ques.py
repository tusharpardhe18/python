# create Account class w 2 attr - balance & acc no.
# create methods of debit, credit and printing the balance

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"{amount}$ is debited from you account {self.account_no}")

    def credit(self, amount):
        self.balance +=  amount
        print(f"{amount}$ is credited to your account {self.account_no}")

    def show_balance(self):
        print(f"{self.balance}$ is in your account {self.account_no}")

myAcc = Account(300, 123456789)
myAcc.debit(400) # Insufficient Balance
myAcc.show_balance() # 300$

    
        