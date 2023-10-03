class BankAccount:
    """
    # Using protected properties:
    # Create a class called "BankAccount" that has protected properties for the account balance.
    # Then define methods for depositing and withdrawing funds.
    """
    def __init__(self, account_balance):
        self._account_balance = account_balance
        print(f"initial account balance: {account_balance}$.")

    def deposit(self, amount):
        self._account_balance += amount
        print(f"Deposited {amount}$.")

    def withdraw(self, amount):
        self._account_balance -= amount
        print(f"Withdrew {amount}$.")


account = BankAccount(6000)
account.deposit(1000)
account.withdraw(2000)
print(f"final account balance is: {account._account_balance}$")
