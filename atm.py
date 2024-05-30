def account(account_pin, account_choice, account_balance, log_count, flag):
    if account_choice == 5:
        print("Successfully logged out.")
        next_login_choice = int(input("Do you want to login again?\n1. yes\n2. no"))
        if next_login_choice == 2:
            log_count -= 1
            flag = False
        return account_balance, log_count, flag, account_pin
    elif account_choice == 1:
        print(f"Available Account Balance: {account_balance}")
        flag = False
        return account_balance, log_count, flag, account_pin
    elif account_choice == 2:
        withdrawl_amount = float(input(f"Enter the amount to withdrawl: "))
        if withdrawl_amount > account_balance:
            print("Insufficient Account Balance.")
        else:
            account_balance -= withdrawl_amount
            print("Cash withdrawl is successful.")
        flag = False
        return account_balance, log_count, flag, account_pin
    elif account_choice == 3:
        deposit_amount = float(input(f"Enter the amount to deposit(from 1 to 100000): "))
        if deposit_amount <= 0 or deposit_amount > 100000:
            print(f"the amount is not in the range(1 to 100000)")
        else:
            account_balance += deposit_amount
            print("Cash deposit is successful")
        flag = False
        return account_balance, log_count, flag, account_pin
    elif account_choice == 4:
        old_pin = int(input("Enter your old pin: "))
        if account_pin != old_pin:
            print("Pin is incorrect.")
            flag = False
        else:
            new_pin = int(input("Please Enter you new pin: "))
            account_pin = new_pin
            print(f"Account Pin changed successfully, Please login again.")
            flag = True
        return account_balance, log_count, flag, account_pin
    else:
        print("Please Enter the correct choice.")
        flag = False
        return account_balance, log_count, flag, account_pin


pin = 1234
balance = 5000
print(f"Do you want to login ?\n1. yes\n2.no")
input1 = int(input("Please enter your choice: "))
count = 1
login_flag = True

while count >= 1:
    if input1 == 1:
        if login_flag:
            input_pin = int(input("Enter your 4 digit pin: "))
            if input_pin != pin:
                print("Pin is incorrect.\nPlease Enter again.")
        if pin == input_pin:
            print("Welcome to ABC Bank!!!\n1. View Balance\n2. Cash Withdrawl\n3. Cash Deposit\n4. Change PIN\n5. log out")
            choice_input = int(input("Enter your choice: "))
            balance, count, login_flag, pin = account(pin, choice_input, balance, count, login_flag)
    else:
        count -= 1
        print('Exited.')
print('Exited.')