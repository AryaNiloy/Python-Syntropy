bal = 100000
p = 1234
def pin():
    z = int(input("Enter pin "))
    if z == p:
        print("Transaction Successful!")
        print("Transaction ID: TRX12340987")
        print("Date and Time: 10/01/24")
        print("Fee Charge: 0")
        print(f"Remaining Balance: {bal - int(y)}")
    else:
        print("Incorrect pin ")
        pin()
def send():
    x = input("Enter receiver's number ")
    y = input("Amount ")
    z =int(input("Enter pin "))
    if z == p:
        print("Send Money Successful!")
        print("Transaction ID: TRX12340987")
        print("Date and Time: 10/01/24")
        print("Fee Charge: 0")
        print(f"Remaining Balance: {bal - int(y)}")
    else:
        print("Incorrect pin ")
        pin()
def pay():
    x = input("Enter your number ")
    y = input("Amount to be recharged ")
    z =int(input("Enter pin "))
    if z == p:
        print("Airtime buying Successful!")
        print("Transaction ID: TRX12340987")
        print("Date and Time: 10/01/24")
        print("Fee Charge: 0")
        print(f"Remaining Balance: {bal - int(y)}")
    else:
        print("Incorrect pin ")
        pin()
def air():
    x = input("Enter your number ")
    y = input("Amount to be recharged ")
    z =int(input("Enter pin "))
    if z == p:
        print("Airtime buying Successful!")
        print("Transaction ID: TRX12340987")
        print("Date and Time: 10/01/24")
        print("Fee Charge: 0")
        print(f"Remaining Balance: {bal - int(y)}")
    else:
        print("Incorrect pin ")
        pin()
def cash():
    x = input("Enter agent number ")
    y = input("Amount to cashout ")
    z =int(input("Enter pin "))
    if z == p:
        print("Cashout Successful!")
        print("Transaction ID: TRX12340987")
        print("Date and Time: 10/01/24")
        print("Fee Charge: 0")
        print(f"Remaining Balance: {bal - int(y)}")
    else:
        print("Incorrect pin ")
        pin()
def bill():
    x = input("Enter biller's account ")
    y = input("Bill to be paid ")
    z =int(input("Enter pin "))
    if z == p:
        print("Bill payment Successful!")
        print("Transaction ID: TRX12340987")
        print("Date and Time: 10/01/24")
        print("Fee Charge: 0")
        print(f"Remaining Balance: {bal - int(y)}")
    else:
        print("Incorrect pin ")
        pin()
def rem():
    x = input("Enter country/organization name ")
    h = input("Reference ")
    y = input("Amount to be received ")
    z =int(input("Enter pin "))
    if z == p:
        print("Airtime buying Successful!")
        print("Transaction ID: TRX12340987")
        print("Date and Time: 10/01/24")
        print("Fee Charge: 0")
        print(f"Total Balance: {bal + int(y)}")
    else:
        print("Incorrect pin ")
        pin()
def help():
    print("Write us your problems faced using bKash or dial 16247\n1.Report problem\n2.Call")
    w=int(input())
    if w==1:
        re=input("Report here\n")
        print("Thanks for letting us know the issue. Our team would try to solve the problem as soon as possible.\nThanks for using bKash ")
    if w == 2:
        telephone_emoji = "\U0001F4DE"
        print(f"{telephone_emoji}")
        print("Calling bKash Helpline")
def bka():
    print("1. Check balance\n2. Reset pin\n3. Helpline")
    w = int(input())
    if w == 1:
        print("Your balance is", bal)
    elif w == 2:
        q = int(input("Enter old pin"))
        if q == p:
            n1 = int(input("New pin"))
            n2 = int(input("Confirm new pin"))
            if n1 == n2:
                p = n1
            else:
                print("Confirm pin doesn't match")
                bka()
        else:
            print("Incorrect old pin")
    elif w == 3:
        help()  
print("Welcome to bkash")
print("1.Send Money \n2.Buy Airtime \n3.Payment \n4.Cash Out \n5.Pay Bill \n6.Remittance \n7.MY bKash \n8.Helpline")
o = input("Select option ")
if o == '1':
    send()
elif o == '2':
    air()
elif o == '3':
    pay()
elif o == '4':
    cash()
elif o == '5':
    bill()
elif o == '6':
    rem()
elif o == '7':
    bka()
elif o == '8':
    help()
else:
    print("Invalid option")