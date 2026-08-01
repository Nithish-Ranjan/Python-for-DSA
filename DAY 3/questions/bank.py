accno = int(input("Enter your account number: "))
bal = 60000
if accno == 123456:
    print("Account number is valid")
    pin = int(input("Enter your pin: "))
    if pin == 1234:
        print("Pin is valid")
        op = input("Enter your operation (withdraw/deposit): ")
        if op == "withdraw":    
            amt = int(input("Enter the amount to withdraw: "))
            if amt <= bal:
                bal -= amt
                print(f"Withdrawal successful. New balance: {bal}")
            else:
                print("Insufficient balance.")
        elif op == "deposit":
            amt = int(input("Enter the amount to deposit: "))
            bal += amt
            print(f"Deposit successful. New balance: {bal}")
        else:
            print("Invalid operation. Try again.")
    else:
        print("Invalid pin. Try again.")
else:
    print("Invalid account number.")