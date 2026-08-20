class BankAccount:
    def __init__(self, account_number, account_name, account_Type, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_name = account_name
        self.__account_Type = account_Type
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_account_name(self):
        return self.__account_name
    
    def get_account_Type(self):
        return self.__account_Type
    
    def show_balance(self):
        print("*********************")
        print(f"Your balance is ₱{self.__balance:.2f}")
        print("*********************")
    
    def show_account_details(self):
        print("*********************")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Name: {self.__account_name}")
        print(f"Account Type: {self.__account_Type}")
        self.show_balance()
        print("*********************")

    def deposit(self):
        try:
            print("*********************")
            amount = float(input("Enter an amount to be deposited: "))
        except ValueError:
            print("*********************")
            print("Invalid input. Please enter a number.")
            print("*********************")
            return

        if amount <= 0:
            print("Amount must be greater than 0")
        else:
            self.__balance += amount
            print(f"₱{amount:.2f} successfully deposited.")
        print("*********************")

    def withdraw(self):
        try:
            print("*********************")
            amount = float(input("Enter an amount to be withdrawn: "))
        except ValueError:
            print("*********************")
            print("Invalid input. Please enter a number.")
            print("*********************")
            return

        if amount <= 0:
            print("Amount must be greater than 0")
        elif amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"₱{amount:.2f} successfully withdrawn.")
        print("*********************")