balance = 2000

while True:
    print("\nBalance: ", balance)
    print("1. Deposit\n2. Withdraw\n3. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Deposit successful!")
    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount
            print("Withdrawal successful!")
    elif choice == '3':
        print("Thank you for using our banking system!")
        break
    else:
        print("Invalid option. Please try again.")