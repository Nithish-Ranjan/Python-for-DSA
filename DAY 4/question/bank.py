class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than zero.")
        if amount > self.__balance:
            raise ValueError("Insufficient balance.")
        self.__balance -= amount
        return self.__balance

    def transfer(self, amount, target_account):
        if not isinstance(target_account, Account):
            raise TypeError("Target must be an Account object.")
        self.withdraw(amount)
        target_account.deposit(amount)
        return True

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_holder_name(self):
        return self.__holder_name

    def __str__(self):
        return (
            f"Account Number: {self.__account_number}, "
            f"Holder: {self.__holder_name}, "
            f"Balance: {self.__balance:.2f}"
        )


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0.0, interest_rate=4.0):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        return self.get_balance()

    def __str__(self):
        return f"SavingsAccount -> {super().__str__()}"


class CurrentAccount(Account):
    def __init__(self, account_number, holder_name, balance=0.0, overdraft_limit=5000.0):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than zero.")
        if amount > self.get_balance() + self.overdraft_limit:
            raise ValueError("Withdrawal exceeds overdraft limit.")
        return super().withdraw(min(amount, self.get_balance()))

    def __str__(self):
        return f"CurrentAccount -> {super().__str__()}"


class Bank:
    def __init__(self, name):
        self.name = name
        self.__accounts = {}

    def create_account(self, account_type, holder_name, initial_balance=0.0):
        account_number = len(self.__accounts) + 1

        if account_type.lower() == "savings":
            account = SavingsAccount(account_number, holder_name, initial_balance)
        elif account_type.lower() == "current":
            account = CurrentAccount(account_number, holder_name, initial_balance)
        else:
            raise ValueError("Account type must be 'savings' or 'current'.")

        self.__accounts[account_number] = account
        return account

    def find_account(self, account_number):
        return self.__accounts.get(account_number)

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account is None:
            raise ValueError("Account not found.")
        return account.deposit(amount)

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account is None:
            raise ValueError("Account not found.")
        return account.withdraw(amount)

    def transfer(self, from_account_number, to_account_number, amount):
        sender = self.find_account(from_account_number)
        receiver = self.find_account(to_account_number)

        if sender is None or receiver is None:
            raise ValueError("Invalid account number.")
        if sender.get_account_number() == receiver.get_account_number():
            raise ValueError("Cannot transfer to the same account.")

        sender.transfer(amount, receiver)
        return True

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account is None:
            raise ValueError("Account not found.")
        return account.get_balance()

    def list_accounts(self):
        return list(self.__accounts.values())


def main():
    bank = Bank("SBI Bank")

    while True:
        print("\nBank Account Management System")
        print("1. Create Savings Account")
        print("2. Create Current Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Check Balance")
        print("7. View All Accounts")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                name = input("Enter holder name: ").strip()
                balance = float(input("Enter initial balance: ").strip())
                account = bank.create_account("savings", name, balance)
                print("Savings account created successfully.")
                print(account)

            elif choice == "2":
                name = input("Enter holder name: ").strip()
                balance = float(input("Enter initial balance: ").strip())
                account = bank.create_account("current", name, balance)
                print("Current account created successfully.")
                print(account)

            elif choice == "3":
                number = int(input("Enter account number: ").strip())
                amount = float(input("Enter deposit amount: ").strip())
                print(f"Updated balance: {bank.deposit(number, amount):.2f}")

            elif choice == "4":
                number = int(input("Enter account number: ").strip())
                amount = float(input("Enter withdrawal amount: ").strip())
                print(f"Updated balance: {bank.withdraw(number, amount):.2f}")

            elif choice == "5":
                sender = int(input("Enter sender account number: ").strip())
                receiver = int(input("Enter receiver account number: ").strip())
                amount = float(input("Enter transfer amount: ").strip())
                bank.transfer(sender, receiver, amount)
                print("Transfer successful.")

            elif choice == "6":
                number = int(input("Enter account number: ").strip())
                print(f"Current balance: {bank.check_balance(number):.2f}")

            elif choice == "7":
                for account in bank.list_accounts():
                    print(account)

            elif choice == "8":
                print("Thank you for using the bank system.")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
