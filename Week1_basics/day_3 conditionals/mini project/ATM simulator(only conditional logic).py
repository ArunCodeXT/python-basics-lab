username='luffy@123'
pin='1234'
balance=5000
withdraw_1='1'
check_balance='2'
user_name=input("Enter username:")
pin_1=input("Enter pin:")
if user_name==username and pin_1==pin :
    print("show menu:")
    print(" 1.) withdraw")
    print(" 2.) check balance\n")
    withdraw=input()
    if withdraw==withdraw_1 :
        amount=float(input("Enter Amount:₹"))
        if amount>balance :
            print("insufficient")
        else:
            newbalance=balance-amount
            print("new balance:₹",newbalance)
    elif withdraw==check_balance:
        print("Balance:₹{:.1f}".format(balance))
    else:
        print("invalid input")
elif user_name!=username and pin_1==pin :
    print("incorrect username")
elif user_name==username and pin_1!=pin :
    print("incorrect pin")
else:
    print("incorrect username and pin")
    

