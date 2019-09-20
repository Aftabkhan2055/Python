class bank():
    amount=0
    def __init__(self,cname,cacc,balance):
        self.cname=cname                         #input("enter your name")
        self.cacc=cacc                          #int(input("enter your account no"))
        self.balance=balance                    # int(input("enter your balance"))
    def deposit(self,amt):
        self.balance=self.balance+amt
    def withdraw(self,amt):
        if amt<self.balance:
            self.balance=self.balance-amt
        else:
            print("low balance")
    def display(self):
        print(self.cname)
        print(self.cacc)
        print(self.balance)
x=bank("aftab",1001,1200)
x.deposit(1000)
x.withdraw(800)
x.display()