# Python Banking Program

# Show Balance

def show_balance(balance):
    print(f"Your balance is ₹ {balance:.2f}") #.2f => for 2 decimal places

# Deposit

def deposit():
    value = float(input("Enter the amount to deposit: "))
    print('****************************')
    if value <= 0:
        print("That's not a valid amount. Please enter amount greater than 0.")
        return 0
    else:
        print(f"₹{value:.2f} has been deposited to your account.")
        return value
    

# Withdraw Money

def withdraw(balance):
    value = float(input("Enter the amount to withdraw: "))
    print('****************************')
    if value > balance:
        print("You do not have enough money in your account.Try Again!!")
        return 0
    elif value <= 0:
        print("Amount must be greater than 0.")
        return 0
    else:
        print(f"₹{value:.2f} has been debited from your account.")
        return value
    

def main():
    # Set the initial balance to 0

    balance = 0

    is_running = True # if set to False, we will exit the program


    while is_running:
        print('''
                Banking Program
                ***********************
                1. Show Balance
                2. Deposit Money
                3. Withdraw Money
                4. Exit
                ************************
            ''')
        
        user_choice = input("Enter Number (1-4): ")
        
        if user_choice == '1':
            show_balance(balance)
        
        elif user_choice == '2':
            balance += deposit()
        
        elif user_choice == '3':
            
            balance -= withdraw(balance)
        
        elif user_choice == '4':
            is_running = False
            
        else:
            print("That is not a valid choice.")
            
    print("Thank you for using banking service. Have a nice day.!!")

if __name__ == '__main__':
    main()