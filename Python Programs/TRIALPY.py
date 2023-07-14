class bankacc:
    def __init__(self):
        self.balance=10000
    def deposit(self):
        amount=int(input('Enter amount to be deposited'))
        self.balance=self.balance+amount
        print('\n amount deposited-',self.balance+amount)
    def withdraw(self):
        amount=int(input('enter amount to be withdrawn'))
        if self.balance>=amount:
            self.balance=self.balance-amount
            print('\n amount withdrawn',self.balance-amount)
        else:
            print('\n Insufficient balance')
    def display (self):
        print('\n Net available balance',self.balance)
s=bankacc()
print("1-Amount Deposit")
print("2-Amount withdraw")
print("3-Available balance")
print("0-EXIT")
choice=int(input("enter choice-"))
if choice==1:
    print(s.deposit())
elif choice==2:
    print(s.withdraw())
elif choice==3:
    print(s.display())
elif choice==0:
    print("EXIT")
else:
    print("Invalid")
print()
            
