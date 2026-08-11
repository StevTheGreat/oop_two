class BankAccount:
    def __init__(self, account_number, account_name):
        self.__account_number = account_number
        self.__account_name = account_name
        self.__balance = 0.0

    def get_account_number(self):
        return self.__account_number

    def get_account_name(self):
        return self.__account_name

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

    def show_balance(self):
        print("*********************")
        print(f"Your balance is ₱{self.__balance:.2f}")
        print("*********************")

    def show_account_details(self):
        print("*********************")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Name: {self.__account_name}")
        print("*********************")


def main():
    print("*********************")
    print(" Create Your Bank Account ")
    print("*********************")
    

    while True:
        acc_num = input("Enter an Account Number: ").strip()
        if acc_num == "":
            print("Input cannot be empty. Please try again")
            continue
        try:

            float(acc_num)
            break
        except ValueError:
            print("Invalid Account Number. Please enter numbers only")


    while True:
        acc_name = input("Enter an Account Name: ").strip()
        if acc_name == "":
            print("Input cannot be empty. Please try again")
            continue

        if not all(c.isalpha() or c.isspace() for c in acc_name):
            print("Invalid Account name. Please enter name only")
            continue
        break

    user_account = BankAccount(acc_num, acc_name)
    is_running = True
    
    while is_running:
        print("\n*********************")
        print(" Banking Program ")
        print("*********************")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Account Details")
        print("5. Exit")
        print("*********************")
        
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            user_account.deposit()
        elif choice == '2':
            user_account.withdraw()
        elif choice == '3':
            user_account.show_balance()
        elif choice == '4':
            user_account.show_account_details()
        elif choice == '5':
            is_running = False
        else:
            print("*********************")
            print("That is not a valid choice")
            print("*********************")
            
    print("*********************")
    print("Thank you! Have a nice day!")
    print("*********************")


if __name__ == "__main__":
    main()
