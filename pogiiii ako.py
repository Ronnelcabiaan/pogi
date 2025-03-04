class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # Public attribute
        self._balance = balance               # Protected attribute
        self.__account_number = self._generate_account_number()  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self._balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: ${self._balance}")

    def _generate_account_number(self):
        # This is a protected method used to generate a fake account number.
        return "123-456-789"

    def get_account_number(self):
        # Public method to access private attribute
        return self.__account_number


# Example usage:
account = BankAccount("John Doe", 1000)
print(f"Account Holder: {account.account_holder}")  # Public access
account.deposit(500)  # Accessing through public method
account.withdraw(200)  # Accessing through public method
account.check_balance()

# Accessing private attribute via public method
print(f"Account Number: {account.get_account_number()}")

# Trying to access private attribute directly will raise an error:
# print(account.__account_number)  # This will cause an AttributeError

# Accessing protected attribute (it's still allowed, but conventionally avoided)
print(f"Protected Balance: {account._balance}")