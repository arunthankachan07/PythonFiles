class Bank:
    # def create_account(self,acc_no,name,min_bal):
    #     self.acc_no=acc_no
    #     self.person_name=name
    #     self.balance=min_bal
    def __init__(self,acc_no,name,min_bal):
        self.acc_no=acc_no
        self.person_name=name
        self.balance=min_bal
    def deposit(self,amount):
        self.balance+=amount
        print("Account credited with amount",amount,"Available balance",self.balance)
    def withdrawn(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print("Account debited with amount", amount, "Available balance", self.balance)

ob=Bank(100,"Arun","10000")
#ob.create_account(1000,"Arun",12000)
# ob.deposit(5000)
# ob.withdrawn(3000)