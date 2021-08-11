import admin
import home
from customer import book_car

def showcar_rent(option):
    fp_car = open('car_details.txt','r')
    if option == 'b':
        print("\n-----------------Available Cars for Rent with Payment Details------------------\n")
        print("Car Model\t\tCost per Day\t\tAdditional Charge Per Hour")
        print()
        for cars in fp_car:
            cars = cars.strip('\n')
            cars = cars.split(',')
            if (cars[7] == '1'):
                print(cars[1]+'\t\t\t'+cars[5]+' RM\t\t\t'+cars[6]+' RM')
        fp_car.close()
            
    elif option == 'a':
            print("\n-----------------Available Cars for Rent------------------\n")
            print("Car Model:")
            print()
            for cars in fp_car:
                cars = cars.strip('\n')
                cars = cars.split(',')
                if (cars[7] == '1'):
                    print(cars[1])
            fp_car.close()   
    else:
        print("Wrong Input!!!")
        home.home()

    home.home()


#function for details
def detail_show(user_name):
    file = open('car_details.txt', 'r')
    car_records = file.readlines()
    count = 0
    skip = 0
    for record in car_records:
        items = record.strip()
        items = items.split(',')
        if items[7] == '1':
            print('[', (items[0]), ']\t' +items[1])
            count += 1
        
    choice = int(input("\nWhich Car's Details You Want to See [Car Code]: "))

    chosen_record = car_records[choice-1000-1]

    chosen_record = chosen_record.strip()
    items = chosen_record.split(',')

    car_code = items[0] #for booking purpose

    print("\nCar Model: ",items[1])
    print("Seat Num : ",items[2])
    print("Condition: ",items[3])
    print("Color    : ",items[4])
    print("Cost (RM): ",items[5])
    print("Addt Cost: ",items[6])

    file.close()
    
    print("\n[1] Book This Car.")
    print("[2] Go Back")
    print("[3] Go Home")

    choice_3 = input("\nEnter Your Choice: ")

    if choice_3 == '1':
        book_car(car_code, user_name)
    elif choice_3 == '2':
        detail_show(user_name)
    else:
        home.home()
    
