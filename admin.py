from display import *
import home






#functionalities of admin

def admin_page():
    print("\n")
    print("What do you want?\n")
    print("1. Add New Car With Details")
    print("2. Modify Car Details")
    print("3. Display Car Details")
    print("4. Return a Rented Car")
    print("5. Search Specific Car Booking")
    print("6. Search Customer Payment")
    print("7. Go to Home Page")
    print("8. Exit\n")

    choice = int(input("Choose Your Option: "))

    if choice == 1:
        add_details()

    elif choice == 2:
        mod_details()
        
    elif choice == 3:
        print("\na) Cars Available for Rent")
        print("b) Customer Payment for a Specific Time Duration\n")
        choice_2 = input("Choose 'a' or 'b' : ")
        showcar_rent(choice_2)
        
    elif choice == 4:
        return_car()

    elif choice == 5:
        search_booking()

    elif choice == 6:
        search_user()
    
    elif choice == 7:
            home.home()
    elif choice == 8:
        exit()
















#function for loggin in the admin
    
def admin_login():
    user_name = input("\nUser Name: ")
    if user_name == 'adminhere':
        password = input("Password: ")
        if password == 'adminonly':
            print("\nWelcome to Admin Page")

        else:
            print("Wrong Password!!!!!\n")
            admin_login()

    else:
        print("No such user name found!!!!\n Try again!")
        admin_login()

    admin_page()











#add new car details
    
def add_details():
    fp_r = open('car_details.txt', 'r')
    for item in fp_r:
        item = item.strip('\n')
        item = item.split(',')
        number = int(item[0])

    fp_r.close()
    
    fp_car = open('car_details.txt', 'a')
    
    model = input("Car Model: ")
    seat = input("Seat Number: ")
    color = input("Color: ")
    condition = input ("Condition (Excellent, Very Good, Good, Fair) : ")
    cost = input("Cost Per Day: ")
    add_cost = input("Additional Cost for Extra hour: ")
    number = number + 1

    
    fp_car.write('\n'+str(number)+','+model+','+seat+','+condition+','+color+','+cost+','+add_cost+','+'1')
    fp_car.close()

    print("\n1. Add more cars")
    print("2. Go to Admin Page")
    print("3. Exit")
    choice = input("\nEnter Your Choice: ")

    if choice == '1':
        add_details()
    elif choice == '3':
        exit()
    else:
        admin_page()











#search result

def search_booking():
    fp = open('car_details.txt', 'r')

    print()
    car_records = fp.readlines()
    for records in car_records:
        records = records.strip()
        records = records.split(',')
        print('[' +records[0]+ ']\t' +records[1])
        
    fp.close()
    search_key = input("\nSearch by Car Code: ")

    fp = open('car_details.txt', 'r')
    car_records = fp.readlines()
    
    for records in car_records:
        records = records.strip()
        records = records.split(',')
        if records[0] == search_key:
            availablity = records[7]
            fp.close()
            break
    else:
        print("Car Code Not Found!")
        search_booking()

    print()
    if availablity == '1':
        print("Availablity: Available for Rent\n")
    else:
        print("Not Available for Rent\n")
    
    fp = open('rental_history.txt', 'r')
    rental_history = fp.readlines()

    for records in rental_history:
        records = records.strip()
        records = records.split(',')
        if search_key == records[0]:
            print("Rented on: " +records[3])
            print("Rented for: " +records[2]+ " days")
            print("Rented by: " +records[1])
            print()
    
    admin_page()






def search_user():
    user = input("\nEnter User Name of Customer You Want to Search: ")
    fp = open('rental_history.txt', 'r')

    rental_records = fp.readlines()

    print()
    count = 0
    for records in rental_records:
        records = records.strip()
        records = records.split(',')
        if user == records[1]:
            print("Car Rented: " +records[0])
            print("Date      : " +records[3])
            print("Paid      : " +records[4]+ " RM")
            print()
            count += 1

    if count == 0:
        print("Not Fount!")
        search_user()
        
    fp.close()
    admin_page()













    










#function for rentruning a car

def return_car():
    fp = open('car_details.txt', 'r')
    
    print("Rented Cars\n")
    for cars in fp:
        cars = cars.strip('\n')
        cars = cars.split(',')
        if (cars[7] == '0'):
            print('['+cars[0]+']\t' +cars[1])
    fp.close()   

    choice = input('Which Car Would be Returned [Car Code]: ')

    fp = open('car_details.txt', 'r')

    car_records = fp.readlines()

    for records in car_records:
        records = records.strip()
        records = records.split(',')
        if choice == records[0]:
            records[7] = '1'
            car_records[int(choice)-1000-1] = ','.join(records)
            car_records[int(choice)-1000-1] = car_records[int(choice)-1000-1] + '\n'
            fp.close()
            break
        else:
            records = ','.join(records)
    else:
        print("Car Code Not Matched")
        return_car()

    fp = open('car_details.txt', 'w')
    fp.writelines(car_records)
    fp.close()

    print("\nCar Returned!\n")
    admin_page()


































#function to modify details
def mod_details():
    file = open('car_details.txt', 'r')
    car_records = file.readlines()

    print()
    for record in car_records:
        items = record.strip()
        items = record.split(',')
        print('[', (items[0]), ']\t' +items[1])
        last_code = int(items[0])
        record = ','.join(items)

    
    choice = input("\nWhich Car's Details Do You Want to Update [Car Code]: ")

    if int(choice) < 1001 & int(choice) > last_code:
        print("Wrong Code")
        admin_page()
        return
    
    chosen_record = car_records[int(choice) - 1000 - 1]
    choice = int(choice)
    
    count = 1
    chosen_record = chosen_record.strip()
    items = chosen_record.split(',')

    print("[1] Car Model: ",items[1])
    print("[2] Seat Num : ",items[2])
    print("[3] Condition: ",items[3])
    print("[4] Color    : ",items[4])
    print("[5] Cost (RM): ",items[5])
    print("[6] Addt Cost: ",items[6])
    
    choice_item = int(input("Which Item Do You Want to Change: "))

    print("Current Value: " +items[choice_item])
    items[choice_item] = input("Add New Value: ")

    choice = choice - 1000
    car_records[choice-1] = ','.join(items)
    car_records[choice-1] = car_records[choice-1] + '\n'
    
    file.close()

    file = open('car_details.txt', 'w')

    file.writelines(car_records)  #putting back the updated file

    file.close()

    print("\nRecord Updated!")

    print("\n1. Modify more")
    print("2. Go to Admin Page")
    print("3. Exit")
    choice = input("\nEnter Your Choice: ")

    if choice == '1':
        mod_details()
    elif choice == '3':
        exit()
    else:
        admin_page()
