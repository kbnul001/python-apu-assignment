import admin
import home
import customer

def home(): #Home menu
    print("\n")
    print("Who are you?")
    print("1. Admin")
    print("2. Customer (Not-Registered)")
    print("3. Customer (Registered)\n")

    choice = input("I am (1,2,3): ")

    if choice == '1':
        admin.admin_login()

    elif choice == '2':
        customer.customer_notreg()

    elif choice == '3':
        customer.cus_login()
        
    else:
        print("Wrong Input!!!!\n")
        home.home() #if wrong input, call the function again

