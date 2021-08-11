import display
from datetime import datetime
import home

#customer login pag
def cus_login():
    fp_cus = open('customer_details.txt', 'r')
    cus_details = fp_cus.readlines()
    
    
    user_name = input("Enter Your Email: ")

    for item in cus_details:
        
        item = item.strip()
        item = item.split(',')
        
        if item[1] == user_name:
            password = input("Password: ")
            
            if password == item[2]:
                print("\nWelcome " +item[0])
                print("\n")
                fp_cus.close()
                cus_page(user_name)
                break
            else:
                print("Wrong Password!!")
                cus_login()

    else:
        print("\nEmail not found! Try again!")
        cus_login()







#function for new customer to register
def cus_reg():
    fp_cus = open('customer_details.txt', 'a')
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    password = input("Enter a Password: ")

    fp_cus.write('\n' +name+',' +email+ ',' +password)

    fp_cus.close()
    print("\nYour name has been registered!\n")
    cus_page(email)









#Interface after logging in

def cus_page(user_name):
    print("[1] View Rental History")
    print("[2] View Details of Cars for Renting")
    print("[3] Home Menu")
    print("[4] Exit\n")

    choice = input("Enter Your Choice: ")
    if choice == '1':
        view_history(user_name)
    elif choice == '2':
        display.detail_show(user_name)
    elif choice == '4':
        exit()
    else:
        home.home()













#page for new customer
def customer_notreg():
    print("[1] View All Cars Available for Rent")
    print("[2] Register to Access Other Details")
    print("[3] Exit")

    choice = input("Enter Your Choice (1,2,3): ")

    if choice == '1':
        display.showcar_rent('a')

    elif choice == '2':
        cus_reg()

    elif choice == '3':
        exit()

    else:
        print("Wrong Input!!")
        customer_notreg()








#function for viewing rental history
        
def view_history(email):
    file = open('rental_history.txt', 'r')

    rental_records = file.readlines()

    print("Email: " +email)
    print()
    count = 1
    for records in rental_records:
        records = records.strip()
        records = records.split(',')
        if records[1] == email:
            car_code = records[0]
            fp_car = open('car_details.txt', 'r')
            car_records = fp_car.readlines()

            for items in car_records:
                items = items.strip()
                items = items.split(',')
                if car_code == items[0]:
                    car_name = items[1]
                    fp_car.close()

            #printing history
            
            print("Rental History: ",count)
            print("Car  : " +car_name)
            print("Rented for: "+records[2]+ " Days")
            print("Rented on : " +records[3])
            print("Paid      : " +records[4]+ " RM")
            print()
            count += 1
    if count == 1:
        print("No History Found!")
    
    file.close()
    cus_page(email)














#function for booking a car
        
def book_car(car_code, user_name):

    file_r = open('car_details.txt', 'r')
    car_records = file_r.readlines()

    count = 0
    for record in car_records:
        record = record.strip()
        item = record.split(',')
        if item[0] == car_code:
            car_records[count] = car_records[count].strip()
            temp_record = car_records[count].split(',')
            temp_record[7] = '0'
            cost_day = int(item[5])
            car_records[count] = ','.join(temp_record)
            car_records[count] = car_records[count] + '\n'
    
        count += 1
        
    file_r.close()

    time = int(input("\nFor How Many Days You Want to Rent: "))

    print("\nFor ",time, "days, Cost Will Be: ", time * cost_day) #Cost Calculating
    choice = input("\nType 'y' to Confirm Payment: ")

    if choice == 'y':
        #update rental history

        fp_rental = open('rental_history.txt', 'a')

        date = datetime.now()
                
        fp_rental.write('\n' +car_code+ ',' +user_name+ ',' +str(time)+ ',' +str(date)+ ',' +str(time*cost_day))
        fp_rental.close()
        
        #Rental History Updated
        
        print("\nPayment Done!")
        print("Renting Car Successful!!!!!")
        print()
        
        file_w = open('car_details.txt', 'w')
        file_w.writelines(car_records) #availablity changed '1' to '0'
        file_w.close()
        cus_page(user_name)
        
    else:
        print("Payment Unsuccessful\n")
        cus_page(user_name) 
    
    
    
