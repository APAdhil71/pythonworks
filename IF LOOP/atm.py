db_pin=1234
db_balance=1000
pin = int(input("enter the pin"))
if db_pin==pin:
    amount = int(input("enter the amount")) # q6.atm withdrawal
    if amount <db_balance:
        print ("withdrawal")
    else:
        print("insufficient balance")
else:
    print("incorrect pin")