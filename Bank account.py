class BankAccount:
    def __init__(self, account_number, account_name):
        self.__account_number = account_number
        self.__account_name = account_name
        self.__balance = 0.0

    def get_account_number(self):
        return self.__account_number

    def get_account_name(self):
        return self.__account_name

    def show_balance(self):
        print("*********************")
        print(f"Your balance is ₱{self.__balance:.2f}")
        print("*********************")

    def deposit(self):
        print("*********************")
        try:
            amount = float(input("Enter an amount to be deposited: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            print("*********************")
            return

        print("*********************")
        if amount <= 0:
            print("*********************")
            print("Amount must be greater than 0")
            print("*********************")
        else:
            self.__balance += amount
            print(f"₱{amount:.2f} successfully deposited.")

    def show_account_details(self):
        print("*********************")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Name: {self.__account_name}")
        print("*********************")


def main():
    print("*********************")
    print(" Create Your Bank Account ")
    print("*********************")
    
    acc_num = float(input("Enter an Account Number: "))
    acc_name = input("Enter an Account Name: ")
    
    user_account = BankAccount(acc_num, acc_name)

    is_running = True
    while is_running:
        print("\n*********************")
        print(" Banking Program ")
        print("*********************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Account Details")
        print("4.Exit")
        print("*********************")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            user_account.show_balance()
        elif choice == '2':
            user_account.deposit()
        elif choice == '3':
            user_account.show_account_details()
        elif choice == '4':
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
