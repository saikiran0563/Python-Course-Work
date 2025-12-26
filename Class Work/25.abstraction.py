from abc import ABC, abstractmethod

class BankAccount(ABC):
    def checkbalance(self,username):
        self.username=username
        print(f"hi {self.username} welcome to the bank")
        print("display the balance")
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass

class CurrentAccount(BankAccount):
    def deposit(self):
        print("any time deposit")
    def withdraw(self):
        print("no limits")
class SavingsAccount(BankAccount):
    def deposit(self):
        print("no limits for deposit")
    def withdraw(self):
        print("limits per day")
class SalaryAccount(BankAccount):
    def deposit(self):
        print("deposit once in a month")
    def withdraw(self):
        print("no limit,charges may apply")
class JointAccount(BankAccount):
    def deposit(self):
        print("multiple users can deposit")
    def withdraw(self):
        print("multiple users can withdraw")
class PensionAccount(BankAccount):
    def deposit(self):
        print("monthly pension deposit")
    def withdraw(self):
        print("limited withdrawl")
class FixedDepositAccount(BankAccount):
    def deposit(self):
        print("lump sum deposit")
    def withdraw(self):
        print("withdrawal not allowed")

banti=CurrentAccount()
mohan=SavingsAccount()
karan=SalaryAccount()
ravipramod=JointAccount()
manoj=PensionAccount()
sachin=FixedDepositAccount()

banti.checkbalance("banti")
banti.deposit()
banti.withdraw()   

mohan.checkbalance("mohan")
mohan.deposit()
mohan.withdraw()

karan.checkbalance("karan")
karan.deposit()
karan.withdraw()

ravipramod.checkbalance("ravipramod")
ravipramod.deposit()
ravipramod.withdraw()

manoj.checkbalance("manoj")
manoj.deposit()
manoj.withdraw()

sachin.checkbalance("sachin")
sachin.deposit()
sachin.withdraw()