from bank import BankAccount

def main():
    print("*********************")
    print(" Create Your Bank Account ")
    print("*********************")
    
    while True:
        account_number = input("Enter an Account Number: ").strip()
        if account_number == "":
            print("Input cannot be empty. Please try again")
            continue
        try:
            float(account_number)
            break
        except ValueError:
            print("Invalid Account Number. Please enter numbers only")

    while True:
        account_name = input("Enter an Account Name: ").strip()
        if account_name == "":
            print("Input cannot be empty. Please try again")
            continue
        if not all(c.isalpha() or c.isspace() for c in account_name):
            print("Invalid Account name. Please enter name only")
            continue
        break
        
    while True:
        account_Type = input("Enter an Account Type: ").strip()
        if account_Type == "":
            print("Input cannot be empty. Please try again")
            continue
        if not all(c.isalpha() or c.isspace() for c in account_Type):
            print("Invalid Account type. Please enter letters only")
            continue
        break    


    while True:
        try:
            initial_balance = float(input("Enter Initial Balance (₱): "))
            if initial_balance < 0:
                print("Initial balance cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            
            

 
    user_account = BankAccount(account_number, account_name, account_Type, initial_balance)
    is_running = True
        
    while is_running:
        print("\n*********************")
        print(" Banking Program ")
        print("*********************")
        print("1. Account Details")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Show Balance")
        print("5. Exit")
        print("*********************")
        
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            user_account.show_account_details()
        elif choice == '2':
            user_account.deposit()
        elif choice == '3':
            user_account.withdraw()
        elif choice == '4':
            user_account.show_balance()
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

