class BankAccount:
    def __init__(self, balance=0, interest=0):
        self.balance = balance
        self.interest = interest

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            else
            print("Insufficient funds: Charging a $5 fee")
            return self

    def display_account_info(self):
        print(
            f"Current account balance is: ${self.balance}.")

    def yield_interest(self)
    if self.balance > 0:
        self.balance += round(self.balance*self.interest)
        else:
            print("No positive balance to calculate interest toward ")
            return self

            usaa = BankAccount(0.005, 1400)
            navyfed = BankAccount(0.00067, 500)


usaa.deposit(1200).deposit(100).deposit(50).withdraw(
    500).yield_interest().display_account_info()

navyfed.deposit(1200).deposit(300).withdraw(100).withdraw(600).withdraw(
    50).withdraw(130).yield_interest().display_account_info()
