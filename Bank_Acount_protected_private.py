
class BankAccount:
    """
    # Using protected and private properties:
    # Create a class called "BankAccount" that has protected properties for account balance and private properties for account number.
    # Then define methods named "deposit" and "withdraw" that will deposit and withdraw money from the account respectively.
    """
    def __init__(self, account_number, account_balance):
        self.__account_number = account_number
        self._account_balance = account_balance
        account_balance = 0

    def deposit(self, amount):
        self._account_balance += amount
        print(f"Deposited ${amount}.")

    def withdraw(self, amount):
        self._account_balance -= amount
        print(f"Withdrew ${amount}.")


account = BankAccount("123456789", 1500)
print(f"Your initial account balance is: ${account._account_balance}")
