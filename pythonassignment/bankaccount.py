class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening):
        self.account_number = account_number
        self.balance = 0  # Initial balance is set to 0
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            return amount
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return "Insufficient balance."

    def check_balance(self):
        """Print the current balance."""
        print(f"Current balance: Ksh {self.balance}")

    def customer_details(self):
        """Print the customer's details."""
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Current Balance: Ksh {self.balance}")

if __name__ == "__main__":

    account = BankAccount("59938457", "Jeff Githiomi", "2023-01-01")

    deposited_amount = account.deposit(60000)
    print(f"Deposited: Ksh {deposited_amount}")

    account.check_balance()
    withdrawn_amount = account.withdraw(35000)
    print(f"Withdrawn: Ksh {withdrawn_amount}")
    account.check_balance()
    account.customer_details()
