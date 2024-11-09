class Account:
    def __init__(self, account_no,balance):
        self.account_no = account_no
        self.__balance = balance

    def debit(self,amount):
        if amount > self.__balance:
            print("Insufficient Balance..!")
        else:
            self.__balance -= amount
            print(amount , " Debited Successfully..")
            print("Current Balance : ", self.__balance)
    
    def credit(self,amount):
        self.__balance += amount
        print(amount, " Credit Successfully..")
        print("Current Balance : ", self.__balance)

    def print_balance(self):
        print("Account Number : ", self.account_no , "Total Balance : "  , self.__balance)

acc1=Account("SBI55066",5000)
acc1.print_balance()
acc1.debit(1000)
acc1.print_balance()
acc1.debit(10000)
acc1.credit(500)
acc1.print_balance()