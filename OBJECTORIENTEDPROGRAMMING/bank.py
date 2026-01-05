class Bank:
    acc_num=int
    name=str
    acc_type=str
    balance=int

    def set_bank(self,acc_num,name,acc_type,balance):
        self.acc_num=acc_num
        self.name=name
        self.acc_type=acc_type
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"your account{self.acc_num} credited with {amount} your avl bal is {self.balance}")

    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print(f"your account{self.acc_num} credited with {amount}your avl is {self.balance}")
        else:
            print("transaction failed insufficient balance")

    def balance_enq(self):
        print(f"hai {self.name} your acc bal is{self.balance}")
    def display(self):
        print(self.acc_num,self.name,self.acc_type)
        
bank_instance1=Bank()
bank_instance1.set_bank(345,283993938,"personal",100)
bank_instance1.withdraw(10000)
bank_instance1.deposit(1000000)