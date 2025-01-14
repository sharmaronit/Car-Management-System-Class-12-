
import mysql.connector as c

def create_connection():
    connection = c.connect(
        host='localhost',
        user='root', 
        password='admin',  
        database='car_management'
    )
    return connection

def Purchase_car():
    conn = create_connection()
    cur = conn.cursor()
    q='desc carlist'
    print("---------------PLEASE SELECT A CAR FOR THE GIVEN LIST BELOW---------------")
    cur.execute(q)
    cur.close()
    conn.close()

def add_car(car_id,make, model, year, price,varient):
    conn = create_connection()
    cur = conn.cursor()
    q = "INSERT INTO cars (car_id,make, model, year, price,varient) VALUES (%s,%s, %s, %s, %s,%s)"
    cur.execute(q, (car_id,make, model, year, price,varient))
    conn.commit()
    cur.close()
    conn.close()
    print("Car added successfully!")

def count():
    conn = create_connection()
    cur = conn.cursor()
    q = "SELECT COUNT(*) FROM cars"
    cur.execute(q)
    a=cur.fetchall()
    
    cur.close()
    conn.close()
    return a

def update_car(car_id, make, model, year, price, varient):
    conn = create_connection()
    cur = conn.cursor()
    q = """
    UPDATE cars 
    SET make = %s, model = %s, year = %s, price = %s, varient = %s 
    WHERE car_id = %s
    """
    cur.execute(q, (make, model, year, price, varient, car_id))
    conn.commit()
    cur.close()
    conn.close()
    print("Car updated successfully!")
def view_cars():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM cars")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    conn.close()

def delete_car(car_id):
    conn = create_connection()

    cur = conn.cursor()
    q = "DELETE FROM cars WHERE car_id = %s"
    cur.execute(q, (car_id,))
    conn.commit()
    cur.close()
    conn.close()
    print("Car deleted successfully!")

def main():
        print("----------------------------------------------------------------------------------------------------------------------------")
        print("+-----------------------------------------------------CAR MANAGEMENT SYSTEM------------------------------------------------+") 
        print()
        print()
        print()
        print()
        print('                                        ⢀⣀⣀⣀⣀⡀⠀⣀⠄⡀⢀⣀⣀⣀⣀⡀⠀⠀')
        print('                                    ⣷⡮⠥⠍⠒⠚⠻⡟⣉⠍⠉⢙⠛⠉⠉⠉⣀⢈⣀⣁⣈⣀⣤⣥⣤⣤⡬⠴⢦⣤⡀')
        print('                                       ⢠⣤⠀⠂⠀⣽⣷⣾⣥⡆⠉⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⣦⡅⠈⢻⡗⣤')
        print('                                    ⠠⠀⠀⠀⠐⠲⣦⡙⢿⣿⣿⣿⣷⣿⣿⣧⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣶⣄⠈⠻⣕⡦⣨⠀')
        print('                                    ⢀⣮⣀⠀⢀⡘⡀⠠⠆⠉⠉⠻⣿⣿⣿⣿⣧⠘⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣟⣻⣻⢿⡶⢿⢿⢾⣖⣖⡀⠐⠂⠤⠤⡄⠀⠀⡀')
        print('                                    ⢸⣿⣿⣆⠆⡇⠈⠀⠋⠉⡉⠐⣎⡭⠉⡟⠛⠛⠟⠻⠿⠟⣻⠛⠉⠀⠀⠀⠀⠈⠉⠉⠛⠛⠮⣷⣎⣶⣹⣏⣶⣦⣤⡀⠁⠐⠀⢁⠀⠢⠄⠀')
        print('                                    ⢸⣿⣿⣿⡚⢭⢂⣄⠀⠀⠀⠈⠀⠱⢋⠙⠤⢄⣀⠀⠀⠀⠀⠀⠀⠁⠂⠀⠄⡀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⢷⡄⠀⠀⠀⠢⡈⢪⢢⡀⠀⠀')
        print('                                    ⠘⣿⣿⣿⣧⢿⣇⡐⢊⡒⢄⣀⠀⠀⢸⠈⢠⣾⣿⠗⠀⠀⠀⠀⠀⠠⣴⣶⣤⣤⣈⠀⠂⠄⡀⠀⠀⠀⠀⠀⠁⠲⢆⠉⠀⠈⠑⢆⣀⠀⠈⠀⠹⡟⠆⠀⠀⠀')
        print('                                    ⠀⣿⣿⣿⣿⢈⣿⣿⡉⠶⢁⢆⡉⢆⡈⢰⣿⣿⢁⣾⣿⣿⣷⡀⠀⠀⠈⢿⣿⣿⣿⣿⣶⣀⡀⠁⢆⢀⡀⢀⠀⠀⡀⠀⡀⠀⠶⠀⠉⠆⠀⠀⠀⠸⠆⢱⠀⠀⠀')
        print('                                    ⠀⠘⢿⣿⣿⣷⣾⣭⣿⣳⢶⣥⡊⠆⡜⣿⡿⡁⣾⣿⣿⣿⣿⣿⣶⡀⠀⠀⣙⡿⣦⡙⢿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⡇⠀⠀')
        print('                                    ⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣾⣿⡷⣼⣁⢣⠡⣿⣿⣿⣟⣿⣿⣿⣷⠌⠁⠀⠀⠈⠉⠓⠒⠋⠉⠍⠹⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣞⢰⡄⠀⠀')
        print('                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣝⡶⣿⣿⣿⣹⣿⣿⣿⣿⣎⠃⡤⣀⠀⠤⠀⠄⠀⠀⠀⡀⢀⢀⡀⣀⠀⣀⣠⣠⣄⣤⣤⣴⣶⣿⣿⡟⡤⠏⣷⣄⠀ ')
        print('                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣔⢡⠂⣵⣾⣿⣿⣾⣶⣷⣶⣶⣶⣤⡤⠜⢿⣿⣿⣿⣿⣿⣿⠿⡛⢅⣾⣡⣴⣿⣟⠀  ')
        print('                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠩⣸⢏⣩⣉⣩⣭⣤⣥⣾⣿⣿⣿⣿⣿⣿⠿   ')
        print('                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⢛⡠⢛⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠀⠀  ')
        print('                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⠿⢿⣿⣿⣿⣷⣴⣦⣴⣤⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠁⠀⠀⠀⠀⠀')
        print('                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
        print()
        print()
        print()
        print()
        print("+-----------------------------------------------------CAR MANAGEMENT SYSTEM------------------------------------------------+")
        print("----------------------------------------------------------------------------------------------------------------------------")
        print()
        print()
        print()
        print()
        print()
def RONTI():
             
            login=int(input("+-----------LOGIN AS---------------+\n           1.STAFF               \n           2.CUSTOMER                \n           3.EXIT                \n+----------------------------------+\nENTER CHOICE-"))
            if login==3:
                 print('EXITING THE SYSTEM......')
                 exit()
                 
            while login==2:
                print("+----------------------SARGAM MOTORS----------------------+")
                print("|                   *1.PURCHASE VEHICLE                   |")                
                print("|                   *2.SERVICE VEHICLE                    |")
                print("|                   *3.SELL VEHICLE                       |")  
                print("|                   *4.MODIFY VEHICLE                     |")
                print("|                   *5.Close Programme                    |")
                print("+---------------------------------------------------------+")
                choice=int(input("\t..::Select option::.."""))
                if choice==1:
                    print('Available car models in our showroom---------- ')
                    view_cars()
            
                    model = input("ENTER CAR MODEL YOU WANT TO BUY: ")
                    varient = input("ENTER CAR VARIENT TOP MODEL=T, BASE MODEL=B: ")
                    if varient.upper()=='T':
                        print("YOU HAVE SELECTED TOP MODEL CAR:")
                    elif varient.upper()=='B':
                        print("YOU HAVE SELECTED BASE MODEL CAR:")
                    else:
                        print("Invalid choice")
                        am=input('DO YOU WANT AUTOMATIC/MANUAL------------------')
                        if am.upper()=='AUTOMATIC':
                            print("YOU HAVE SELECTED AUTOMATIC CAR")
                        elif am.upper()=='MANUAL':
                            print('YOU HAVE SELECTED MANUAL CAR')
                        else:
                            print('PLEASE SELECT EITHER AUTOMATIC OR MANUAL')
                    print('CAR PURCHASED SUCCESSFULLY')
                elif choice==2:
                    print('-------------------------SERVICE VEHICLE-------------------------')
                    print()
                    print()
                    print('                       ⢀⠀⠀⠀⢠⣶⣶⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
                    print('             ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣷⣄⢀⣸⣿⣿⣿⣿⣄⠀⣴⣿⣿⣶⣄⠀⠀⠀⠀⠀')
                    print('             ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀')
                    print('             ⠀⠀⠀⢀⣴⣦⣤⣠⣾⣿⣿⣿⠟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣤⣤⡄⠀')
                    print('             ⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⢙⣿⣿⣿⣿⣿⡿⠋⢹⣿⣿⣿⣿⣿⣿⣿⡆')
                    print('             ⠀⠀⠀⠉⠻⣿⣿⣿⡿⠁⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⠃⠀⠻⠿⠃⣿⣿⣿⣿⠋⠀')
                    print('             ⠀⣡⣀⣀⣼⣿⣿⣿⡇⠀⠀⣠⡟⠉⠙⢿⣿⣿⡿⠉⠀⢀⣨⣤⣴⣿⣿⣿⣿⣀⣀')
                    print('             ⠀⢸⣿⣿⣿⣿⣿⣿⣷⣠⣾⣿⣿⣦⡄⣠⡿⠃⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
                    print('             ⠀⠼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⣠⡾⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
                    print('             ⠀⠀⠀⠀⢙⣿⣿⣿⣿⣿⠿⠿⠟⠁⠀⣠⣾⣧⡀⠀⠈⠻⣿⣿⣿⣿⣿⣿⡏⠀⠀')
                    print('             ⠀⠀⠀⣵⣿⣿⣿⣿⣿⠁⣾⡀⠀⢠⣾⣿⣿⣿⣿⣦⡀⠀⠈⢻⣿⣿⣿⣿⣿⣶⡀')
                    print('             ⠀⠀⠀⢻⣿⣿⣿⣿⣿⣼⣿⡟⠀⣼⣿⣿⣿⣿⣿⣿⣿⣦⣤⣾⣿⣿⣿⣿⣿⣿⠃')
                    print('             ⠀⠀⠀⠀⠙⠉⠁⠈⣻⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠉⠙⠁⠀')
                    print('             ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀')
                    print('             ⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⠏⠀⠀⢸⣿⣿⣿⣿⠀⠀⠘⠿⠿⠛⠁⠀⠀⠀⠀⠀')
                    print()
                    print()
                    print('+------------------- SERVICE TYPE---------------------+')
                    print('|                    1.OIL CHANGE                     |')
                    print('|                    2.BATTERY CHANGE                 |')
                    print('|                    3.TYRE CHANGE                    |')
                    print('|                    4.BRAKE PAD REPLACEMENT          |')
                    print('|                    5.ENGINE OIL CHANGE              |')
                    print('|                    6.FULL SERVICE                   |')
                    print('|                    7.CANCEL                         |')
                    print('+-----------------------------------------------------+')
                    service=int(input('ENTER SERVICE TYPE:'))
                    if service==1:
                        print('OIL CHANGE SERVICE')
                        print('SERVICE COST: 5000')
                        print('SERVICE CHARGES: 1000')
                        print('TOTAL AMOUNT: 6000')
                    elif service==2:
                        print('BATTERY REPLACEMENT SERVICE')
                        print('SERVICE COST: 8000')
                        print('SERVICE CHARGES: 2000')
                        print('TOTAL AMOUNT: 10000')
                    elif service==3:
                        print('TIRE REPLACEMENT SERVICE')
                        print('SERVICE COST: 7000')
                        print('SERVICE CHARGES: 1500')
                        print('TOTAL AMOUNT: 8500')
                    elif service==4:
                        print('BRAKE PAD REPLACEMENT SERVICE')
                        print('SERVICE COST: 6000')
                        print('SERVICE CHARGES: 1200')
                        print('TOTAL AMOUNT: 7200')
                    elif service==5:
                        print('ENGINE OIL REPLACEMENT SERVICE')
                        print('SERVICE COST: 4000')
                        print('SERVICE CHARGES: 800')
                        print('TOTAL AMOUNT: 4800')
                    elif service==6:
                        print('FULL SERVICE')
                        print('SERVICE COST: 12000')
                        print('SERVICE CHARGES: 3000')
                        print('TOTAL AMOUNT: 15000')
                    elif service==7:
                        print('SERVICE CANCELLED')
                    else:
                        print('PLEASE SELECT A VALID SERVICE TYPE')
                        print('SERVICE VEHICLE')
                elif choice==3:
                    print('SELL VEHICLE')
                    print('+------------------VEHICLE DETAILS-------------------+')
                    print('|                    1.MARUTI SUZUKI                 |')
                    print('|                    2.HYUNDAI                       |')
                    print('|                    3.TATA                          |')
                    print('|                    4.FORD                          |')
                    print('|                    5.TOYOTA                        |')
                    print('|                    6.CANCEL                        |')
                    print('+---------------------------------------------------+|')

                    vehicle=int(input('ENTER VEHICLE TYPE:'))
                    if vehicle==1:
                        print('MARUTI SUZUKI')
                        print('VEHICLE PRICE: 800000')
                        print('VEHICLE DISCOUNT: 20000')
                        print('VEHICLE TOTAL PRICE: 780000')
                        print("DO YOU WANT TO SELL THE VEHICLE?")
                        sell=input("YES/NO:")
                        if sell.upper()=="YES":
                            x=count()
                            car_id=x[0][0]+1
                            make = input("ENTER CAR MAKER: ")
                            model = input("ENTER CAR MODEL NAME: ")
                            year = int(input("ENTER YEAR OF MAUFACTURING: "))
                            price = 780000
                            varient=input('ENTER VARIENT MANUAL/AUTOMATIC:')
                            add_car(car_id,make, model, year, price,varient)
                            print("VEHICLE SOLD!!")
                        elif sell.upper=="NO":
                                print("VEHICLE NOT SOLD")
                    elif vehicle==2:
                            print('HYUNDAI')
                            print('VEHICLE PRICE: 900000')
                            print('VEHICLE DISCOUNT: 25000')
                            print('VEHICLE TOTAL PRICE: 875000')
                            print("DO YOU WANT TO SELL THE VEHICLE?")
                            sell=input("YES/NO:")
                            if sell.upper()=="YES":
                                x=count()
                                car_id=x[0][0]+1
                                make = input("ENTER CAR MAKER: ")
                                model = input("ENTER CAR MODEL NAME: ")
                                year = int(input("ENTER YEAR OF MAUFACTURING: "))
                                price = 875000
                                varient=input('ENTER VARIENT MANUAL/AUTOMATIC:')
                                add_car(car_id,make, model, year, price,varient)

                                print("VEHICLE SOLD!!")
                            elif sell.upper=="NO":
                                print("VEHICLE NOT SOLD")
                    elif vehicle==3:
                            print('TATA')
                            print('VEHICLE PRICE: 700000')
                            print('VEHICLE DISCOUNT: 15000')
                            print("DO YOU WANT TO SELL THE VEHICLE?")
                            sell=input("YES/NO:")
                            if sell.upper()=="YES":
                                x=count()
                                car_id=x[0][0]+1
                                make = input("ENTER CAR MAKER: ")
                                model = input("ENTER CAR MODEL NAME: ")
                                year = int(input("ENTER YEAR OF MAUFACTURING: "))
                                price = 700000
                                varient=input('ENTER VARIENT MANUAL/AUTOMATIC:')
                                add_car(car_id,make, model, year, price,varient)
                                print("VEHICLE SOLD!!")
                            elif sell.upper=="NO":
                                print("VEHICLE NOT SOLD")
                    elif vehicle==4:
                            print('FORD')
                            print('VEHICLE PRICE: 1000000')
                            print("DO YOU WANT TO SELL THE VEHICLE?")
                            sell=input("YES/NO:")
                            if sell.upper()=="YES":
                                x=count()
                                car_id=x[0][0]+1
                                make = input("ENTER CAR MAKER: ")
                                model = input("ENTER CAR MODEL NAME: ")
                                year = int(input("ENTER YEAR OF MAUFACTURING: "))
                                price = 1000000
                                varient=input('ENTER VARIENT MANUAL/AUTOMATIC:')
                                add_car(car_id,make, model, year, price,varient)
                                print("VEHICLE SOLD!!")
                            elif sell.upper=="NO":
                                print("VEHICLE NOT SOLD")
                    elif vehicle==5:
                            print('TOYOTA')
                            print('VEHICLE PRICE: 1100000')
                            print("DO YOU WANT TO SELL THE VEHICLE?")
                            sell=input("YES/NO:")
                            if sell.upper()=="YES":
                                x=count()
                                car_id=x[0][0]+1
                                make = input("ENTER CAR MAKER: ")
                                model = input("ENTER CAR MODEL NAME: ")
                                year = int(input("ENTER YEAR OF MAUFACTURING: "))
                                price = 11000000
                                varient=input('ENTER VARIENT MANUAL/AUTOMATIC:')
                                add_car(car_id,make, model, year, price,varient)
                                print("VEHICLE SOLD!!")
                            elif sell.upper=="NO":
                                print("VEHICLE NOT SOLD")
                    elif vehicle==6:
                            print('VEHICLE SALE CANCELLED')
                    else:
                        print('PLEASE SELECT A VALID VEHICLE TYPE')

                elif choice==4:
                    print('-------------------------MODIFY VEHICLE-------------------------')
                    print()
                    print()
                    print('             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀')
                    print('                    ⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀')
                    print('             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
                    print('             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
                    print('             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡇⠀')
                    print('             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡇⠀')
                    print('             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣦⣤⣀⣀⠀⢀⣴⣿⣿⣿⣿⠃⠀')
                    print('             ⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀')
                    print('             ⠀⠀⠀⠀⠀⠀⣠⡾⠋⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀')
                    print('             ⠀⠀⠀⠀⣠⡾⠋⣠⣾⣿⣿⣿⣿⠟⣩⣿⠟⠿⠿⠿⠿⠟⠛⠉⠁⠀⠀⠀⠀⠀')
                    print('             ⠀⠀⣠⡾⠋⣠⣾⣿⣿⣿⣿⠟⣡⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
                    print('             ⠀⡾⠋⣠⣾⣿⣿⣿⣿⠟⢁⣼⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
                    print('             ⠀⣠⣾⣿⣿⣿⣿⠟⢁⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
                    print('             ⠀⣿⣿⣿⣿⠟⣡⣶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
                    print('             ⠀⠛⠛⠋⠁⠘⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
                    print()
                    print()
                    print('+------------------MODIFICATION DETAILS-------------------+')
                    print('|                  1.HEADLIGHTS                           |')
                    print('|                  2.PAINT                                |')
                    print('|                  3.WHEELS                               |')
                    print('|                  4.INTERIOR                             |')
                    print('|                  5.MUSIC SYSTEM                         |')
                    print('|                  6.CANCEL                               |')
                    print('+---------------------------------------------------------+')


                    modi=int(input('ENTER MODIFICATION  TYPE:'))
                    if modi==1:

                        print('+------------------------HEADLIGHTS-------------------------+')
                        print('|                        1.WHITE-Rs10000                    |')
                        print('|                        2.HALOGEN-Rs9000                   |')
                        print('|                        3.FOGLAMP-Rs8000                   |')
                        print('|                        4.BULB CHANGE-Rs1000               |')
                        print('|                        5.CANCEL                           |')
                        print('+-----------------------------------------------------------+')
                        head=int(input('ENTER HEADLIGHT TYPE:'))
                        if head==1:
                                print('WHITE HEADLIGHTS')
                                print('PRICE: 10000')
                        elif head==2:
                                print('HALOGEN HEADLIGHTS')
                                print('PRICE: 9000')
                        elif head==3:
                                print('FOGLAMP HEADLIGHTS')
                                print('PRICE: 8000')
                        elif head==4:
                                print('BULB CHANGE')
                                print('PRICE: 1000')
                        elif head==5:
                                print('MODIFICATION CANCELLED')
                        elif head>5:
                                print('PLEASE SELECT A VALID HEADLIGHT TYPE')
                    elif modi==2:
                        print('PAINT')
                        print('1.PINK-Rs10000')
                        print('2.GREEN-Rs9000')
                        print('3.RED-Rs8000')
                        print('4.BLUE-Rs7000')
                        print('5.CANCEL')
                        paint=int(input('ENTER PAINT TYPE:'))
                        if paint==1:    
                            print('----->PINK PAINT')
                            print()
                            print()
                            print()
                            print()
                            print("\033[95m                                        ⢀⣀⣀⣀⣀⡀⠀⣀⠄⡀⢀⣀⣀⣀⣀⡀⠀⠀\033[0m")
                            print("\033[95m                                    ⣷⡮⠥⠍⠒⠚⠻⡟⣉⠍⠉⢙⠛⠉⠉⠉⣀⢈⣀⣁⣈⣀⣤⣥⣤⣤⡬⠴⢦⣤⡀\033[0m")
                            print("\033[95m                                       ⢠⣤⠀⠂⠀⣽⣷⣾⣥⡆⠉⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⣦⡅⠈⢻⡗⣤\033[0m")
                            print("\033[95m                                    ⠠⠀⠀⠀⠐⠲⣦⡙⢿⣿⣿⣿⣷⣿⣿⣧⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣶⣄⠈⠻⣕⡦⣨⠀\033[0m")
                            print("\033[95m                                    ⢀⣮⣀⠀⢀⡘⡀⠠⠆⠉⠉⠻⣿⣿⣿⣿⣧⠘⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣟⣻⣻⢿⡶⢿⢿⢾⣖⣖⡀⠐⠂⠤⠤⡄⠀⠀⡀\033[0m")
                            print("\033[95m                                    ⢸⣿⣿⣆⠆⡇⠈⠀⠋⠉⡉⠐⣎⡭⠉⡟⠛⠛⠟⠻⠿⠟⣻⠛⠉⠀⠀⠀⠀⠈⠉⠉⠛⠛⠮⣷⣎⣶⣹⣏⣶⣦⣤⡀⠁⠐⠀⢁⠀⠢⠄⠀\033[0m")
                            print("\033[95m                                    ⢸⣿⣿⣿⡚⢭⢂⣄⠀⠀⠀⠈⠀⠱⢋⠙⠤⢄⣀⠀⠀⠀⠀⠀⠀⠁⠂⠀⠄⡀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⢷⡄⠀⠀⠀⠢⡈⢪⢢⡀⠀⠀\033[0m")
                            print("\033[95m                                    ⠘⣿⣿⣿⣧⢿⣇⡐⢊⡒⢄⣀⠀⠀⢸⠈⢠⣾⣿⠗⠀⠀⠀⠀⠀⠠⣴⣶⣤⣤⣈⠀⠂⠄⡀⠀⠀⠀⠀⠀⠁⠲⢆⠉⠀⠈⠑⢆⣀⠀⠈⠀⠹⡟⠆⠀⠀⠀\033[0m")
                            print("\033[95m                                    ⠀⣿⣿⣿⣿⢈⣿⣿⡉⠶⢁⢆⡉⢆⡈⢰⣿⣿⢁⣾⣿⣿⣷⡀⠀⠀⠈⢿⣿⣿⣿⣿⣶⣀⡀⠁⢆⢀⡀⢀⠀⠀⡀⠀⡀⠀⠶⠀⠉⠆⠀⠀⠀⠸⠆⢱⠀⠀⠀\033[0m")
                            print("\033[95m                                    ⠀⠘⢿⣿⣿⣷⣾⣭⣿⣳⢶⣥⡊⠆⡜⣿⡿⡁⣾⣿⣿⣿⣿⣿⣶⡀⠀⠀⣙⡿⣦⡙⢿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⡇⠀⠀\033[0m")
                            print("\033[95m                                    ⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣾⣿⡷⣼⣁⢣⠡⣿⣿⣿⣟⣿⣿⣿⣷⠌⠁⠀⠀⠈⠉⠓⠒⠋⠉⠍⠹⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣞⢰⡄⠀⠀\033[0m")
                            print("\033[95m                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣝⡶⣿⣿⣿⣹⣿⣿⣿⣿⣎⠃⡤⣀⠀⠤⠀⠄⠀⠀⠀⡀⢀⢀⡀⣀⠀⣀⣠⣠⣄⣤⣤⣴⣶⣿⣿⡟⡤⠏⣷⣄⠀ \033[0m")
                            print("\033[95m                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣔⢡⠂⣵⣾⣿⣿⣾⣶⣷⣶⣶⣶⣤⡤⠜⢿⣿⣿⣿⣿⣿⣿⠿⡛⢅⣾⣡⣴⣿⣟⠀  \033[0m")
                            print("\033[95m                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠩⣸⢏⣩⣉⣩⣭⣤⣥⣾⣿⣿⣿⣿⣿⣿⠿   \033[0m")
                            print("\033[95m                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⢛⡠⢛⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠀⠀  \033[0m")
                            print("\033[95m                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m")
                            print()
                            print()
                            print()
                            print()
                            print('PRICE: 10000')
                        elif paint==2:
                            print('----->GREEN PAINT')
                            print()
                            print()
                            print()
                            print()
                            print("\033[92m                                        ⢀⣀⣀⣀⣀⡀⠀⣀⠄⡀⢀⣀⣀⣀⣀⡀⠀⠀\033[0m")
                            print("\033[92m                                    ⣷⡮⠥⠍⠒⠚⠻⡟⣉⠍⠉⢙⠛⠉⠉⠉⣀⢈⣀⣁⣈⣀⣤⣥⣤⣤⡬⠴⢦⣤⡀\033[0m")
                            print("\033[92m                                       ⢠⣤⠀⠂⠀⣽⣷⣾⣥⡆⠉⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⣦⡅⠈⢻⡗⣤\033[0m")
                            print("\033[92m                                    ⠠⠀⠀⠀⠐⠲⣦⡙⢿⣿⣿⣿⣷⣿⣿⣧⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣶⣄⠈⠻⣕⡦⣨⠀\033[0m")
                            print("\033[92m                                    ⢀⣮⣀⠀⢀⡘⡀⠠⠆⠉⠉⠻⣿⣿⣿⣿⣧⠘⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣟⣻⣻⢿⡶⢿⢿⢾⣖⣖⡀⠐⠂⠤⠤⡄⠀⠀⡀\033[0m")
                            print("\033[92m                                    ⢸⣿⣿⣆⠆⡇⠈⠀⠋⠉⡉⠐⣎⡭⠉⡟⠛⠛⠟⠻⠿⠟⣻⠛⠉⠀⠀⠀⠀⠈⠉⠉⠛⠛⠮⣷⣎⣶⣹⣏⣶⣦⣤⡀⠁⠐⠀⢁⠀⠢⠄⠀\033[0m")
                            print("\033[92m                                    ⢸⣿⣿⣿⡚⢭⢂⣄⠀⠀⠀⠈⠀⠱⢋⠙⠤⢄⣀⠀⠀⠀⠀⠀⠀⠁⠂⠀⠄⡀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⢷⡄⠀⠀⠀⠢⡈⢪⢢⡀⠀⠀\033[0m")
                            print("\033[92m                                    ⠘⣿⣿⣿⣧⢿⣇⡐⢊⡒⢄⣀⠀⠀⢸⠈⢠⣾⣿⠗⠀⠀⠀⠀⠀⠠⣴⣶⣤⣤⣈⠀⠂⠄⡀⠀⠀⠀⠀⠀⠁⠲⢆⠉⠀⠈⠑⢆⣀⠀⠈⠀⠹⡟⠆⠀⠀⠀\033[0m")
                            print("\033[92m                                    ⠀⣿⣿⣿⣿⢈⣿⣿⡉⠶⢁⢆⡉⢆⡈⢰⣿⣿⢁⣾⣿⣿⣷⡀⠀⠀⠈⢿⣿⣿⣿⣿⣶⣀⡀⠁⢆⢀⡀⢀⠀⠀⡀⠀⡀⠀⠶⠀⠉⠆⠀⠀⠀⠸⠆⢱⠀⠀⠀\033[0m")
                            print("\033[92m                                    ⠀⠘⢿⣿⣿⣷⣾⣭⣿⣳⢶⣥⡊⠆⡜⣿⡿⡁⣾⣿⣿⣿⣿⣿⣶⡀⠀⠀⣙⡿⣦⡙⢿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⡇⠀⠀\033[0m")
                            print("\033[92m                                    ⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣾⣿⡷⣼⣁⢣⠡⣿⣿⣿⣟⣿⣿⣿⣷⠌⠁⠀⠀⠈⠉⠓⠒⠋⠉⠍⠹⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣞⢰⡄⠀⠀\033[0m")
                            print("\033[92m                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣝⡶⣿⣿⣿⣹⣿⣿⣿⣿⣎⠃⡤⣀⠀⠤⠀⠄⠀⠀⠀⡀⢀⢀⡀⣀⠀⣀⣠⣠⣄⣤⣤⣴⣶⣿⣿⡟⡤⠏⣷⣄⠀ \033[0m")
                            print("\033[92m                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣔⢡⠂⣵⣾⣿⣿⣾⣶⣷⣶⣶⣶⣤⡤⠜⢿⣿⣿⣿⣿⣿⣿⠿⡛⢅⣾⣡⣴⣿⣟⠀  \033[0m")
                            print("\033[92m                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠩⣸⢏⣩⣉⣩⣭⣤⣥⣾⣿⣿⣿⣿⣿⣿⠿   \033[0m")
                            print("\033[92m                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⢛⡠⢛⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠀⠀  \033[0m")
                            print("\033[92m                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m")
                            print()
                            print()
                            print()
                            print()
                            print('PRICE: 9000')
                        elif paint==3:
                            print('----->RED PAINT')
                            print()
                            print()
                            print()
                            print()
                            print("\033[91m                                        ⢀⣀⣀⣀⣀⡀⠀⣀⠄⡀⢀⣀⣀⣀⣀⡀⠀⠀\033[0m")
                            print("\033[91m                                    ⣷⡮⠥⠍⠒⠚⠻⡟⣉⠍⠉⢙⠛⠉⠉⠉⣀⢈⣀⣁⣈⣀⣤⣥⣤⣤⡬⠴⢦⣤⡀\033[0m")
                            print("\033[91m                                       ⢠⣤⠀⠂⠀⣽⣷⣾⣥⡆⠉⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⣦⡅⠈⢻⡗⣤\033[0m")
                            print("\033[91m                                    ⠠⠀⠀⠀⠐⠲⣦⡙⢿⣿⣿⣿⣷⣿⣿⣧⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣶⣄⠈⠻⣕⡦⣨⠀\033[0m")
                            print("\033[91m                                    ⢀⣮⣀⠀⢀⡘⡀⠠⠆⠉⠉⠻⣿⣿⣿⣿⣧⠘⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣟⣻⣻⢿⡶⢿⢿⢾⣖⣖⡀⠐⠂⠤⠤⡄⠀⠀⡀\033[0m")
                            print("\033[91m                                    ⢸⣿⣿⣆⠆⡇⠈⠀⠋⠉⡉⠐⣎⡭⠉⡟⠛⠛⠟⠻⠿⠟⣻⠛⠉⠀⠀⠀⠀⠈⠉⠉⠛⠛⠮⣷⣎⣶⣹⣏⣶⣦⣤⡀⠁⠐⠀⢁⠀⠢⠄⠀\033[0m")
                            print("\033[91m                                    ⢸⣿⣿⣿⡚⢭⢂⣄⠀⠀⠀⠈⠀⠱⢋⠙⠤⢄⣀⠀⠀⠀⠀⠀⠀⠁⠂⠀⠄⡀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⢷⡄⠀⠀⠀⠢⡈⢪⢢⡀⠀⠀\033[0m")
                            print("\033[91m                                    ⠘⣿⣿⣿⣧⢿⣇⡐⢊⡒⢄⣀⠀⠀⢸⠈⢠⣾⣿⠗⠀⠀⠀⠀⠀⠠⣴⣶⣤⣤⣈⠀⠂⠄⡀⠀⠀⠀⠀⠀⠁⠲⢆⠉⠀⠈⠑⢆⣀⠀⠈⠀⠹⡟⠆⠀⠀⠀\033[0m")
                            print("\033[91m                                    ⠀⣿⣿⣿⣿⢈⣿⣿⡉⠶⢁⢆⡉⢆⡈⢰⣿⣿⢁⣾⣿⣿⣷⡀⠀⠀⠈⢿⣿⣿⣿⣿⣶⣀⡀⠁⢆⢀⡀⢀⠀⠀⡀⠀⡀⠀⠶⠀⠉⠆⠀⠀⠀⠸⠆⢱⠀⠀⠀\033[0m")
                            print("\033[91m                                    ⠀⠘⢿⣿⣿⣷⣾⣭⣿⣳⢶⣥⡊⠆⡜⣿⡿⡁⣾⣿⣿⣿⣿⣿⣶⡀⠀⠀⣙⡿⣦⡙⢿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⡇⠀⠀\033[0m")
                            print("\033[91m                                    ⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣾⣿⡷⣼⣁⢣⠡⣿⣿⣿⣟⣿⣿⣿⣷⠌⠁⠀⠀⠈⠉⠓⠒⠋⠉⠍⠹⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣞⢰⡄⠀⠀\033[0m")
                            print("\033[91m                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣝⡶⣿⣿⣿⣹⣿⣿⣿⣿⣎⠃⡤⣀⠀⠤⠀⠄⠀⠀⠀⡀⢀⢀⡀⣀⠀⣀⣠⣠⣄⣤⣤⣴⣶⣿⣿⡟⡤⠏⣷⣄⠀ \033[0m")
                            print("\033[91m                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣔⢡⠂⣵⣾⣿⣿⣾⣶⣷⣶⣶⣶⣤⡤⠜⢿⣿⣿⣿⣿⣿⣿⠿⡛⢅⣾⣡⣴⣿⣟⠀  \033[0m")
                            print("\033[91m                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠩⣸⢏⣩⣉⣩⣭⣤⣥⣾⣿⣿⣿⣿⣿⣿⠿   \033[0m")
                            print("\033[91m                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⢛⡠⢛⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠀⠀  \033[0m")
                            print("\033[91m                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m")
                            print()
                            print()
                            print()
                            print()
                            print('PRICE: 8000')
                        elif paint==4:
                            print('----->BLUE PAINT')
                            print()
                            print()
                            print()
                            print()
                            print("\033[94m                                        ⢀⣀⣀⣀⣀⡀⠀⣀⠄⡀⢀⣀⣀⣀⣀⡀⠀⠀\033[0m")
                            print("\033[94m                                    ⣷⡮⠥⠍⠒⠚⠻⡟⣉⠍⠉⢙⠛⠉⠉⠉⣀⢈⣀⣁⣈⣀⣤⣥⣤⣤⡬⠴⢦⣤⡀\033[0m")
                            print("\033[94m                                       ⢠⣤⠀⠂⠀⣽⣷⣾⣥⡆⠉⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⣦⡅⠈⢻⡗⣤\033[0m")
                            print("\033[94m                                    ⠠⠀⠀⠀⠐⠲⣦⡙⢿⣿⣿⣿⣷⣿⣿⣧⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣶⣄⠈⠻⣕⡦⣨⠀\033[0m")
                            print("\033[94m                                    ⢀⣮⣀⠀⢀⡘⡀⠠⠆⠉⠉⠻⣿⣿⣿⣿⣧⠘⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣟⣻⣻⢿⡶⢿⢿⢾⣖⣖⡀⠐⠂⠤⠤⡄⠀⠀⡀\033[0m")
                            print("\033[94m                                    ⢸⣿⣿⣆⠆⡇⠈⠀⠋⠉⡉⠐⣎⡭⠉⡟⠛⠛⠟⠻⠿⠟⣻⠛⠉⠀⠀⠀⠀⠈⠉⠉⠛⠛⠮⣷⣎⣶⣹⣏⣶⣦⣤⡀⠁⠐⠀⢁⠀⠢⠄⠀\033[0m")
                            print("\033[94m                                    ⢸⣿⣿⣿⡚⢭⢂⣄⠀⠀⠀⠈⠀⠱⢋⠙⠤⢄⣀⠀⠀⠀⠀⠀⠀⠁⠂⠀⠄⡀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⢷⡄⠀⠀⠀⠢⡈⢪⢢⡀⠀⠀\033[0m")
                            print("\033[94m                                    ⠘⣿⣿⣿⣧⢿⣇⡐⢊⡒⢄⣀⠀⠀⢸⠈⢠⣾⣿⠗⠀⠀⠀⠀⠀⠠⣴⣶⣤⣤⣈⠀⠂⠄⡀⠀⠀⠀⠀⠀⠁⠲⢆⠉⠀⠈⠑⢆⣀⠀⠈⠀⠹⡟⠆⠀⠀⠀\033[0m")
                            print("\033[94m                                    ⠀⣿⣿⣿⣿⢈⣿⣿⡉⠶⢁⢆⡉⢆⡈⢰⣿⣿⢁⣾⣿⣿⣷⡀⠀⠀⠈⢿⣿⣿⣿⣿⣶⣀⡀⠁⢆⢀⡀⢀⠀⠀⡀⠀⡀⠀⠶⠀⠉⠆⠀⠀⠀⠸⠆⢱⠀⠀⠀\033[0m")
                            print("\033[94m                                    ⠀⠘⢿⣿⣿⣷⣾⣭⣿⣳⢶⣥⡊⠆⡜⣿⡿⡁⣾⣿⣿⣿⣿⣿⣶⡀⠀⠀⣙⡿⣦⡙⢿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⡇⠀⠀\033[0m")
                            print("\033[94m                                    ⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣾⣿⡷⣼⣁⢣⠡⣿⣿⣿⣟⣿⣿⣿⣷⠌⠁⠀⠀⠈⠉⠓⠒⠋⠉⠍⠹⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣞⢰⡄⠀⠀\033[0m")
                            print("\033[94m                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣝⡶⣿⣿⣿⣹⣿⣿⣿⣿⣎⠃⡤⣀⠀⠤⠀⠄⠀⠀⠀⡀⢀⢀⡀⣀⠀⣀⣠⣠⣄⣤⣤⣴⣶⣿⣿⡟⡤⠏⣷⣄⠀ \033[0m")
                            print("\033[94m                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣔⢡⠂⣵⣾⣿⣿⣾⣶⣷⣶⣶⣶⣤⡤⠜⢿⣿⣿⣿⣿⣿⣿⠿⡛⢅⣾⣡⣴⣿⣟⠀  \033[0m")
                            print("\033[94m                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠩⣸⢏⣩⣉⣩⣭⣤⣥⣾⣿⣿⣿⣿⣿⣿⠿   \033[0m")
                            print("\033[94m                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⢛⡠⢛⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠀⠀  \033[0m")
                            print("\033[94m                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m")
                            print()
                            print()
                            print()
                            print()
                            print('PRICE: 7000')
                        elif paint==5:
                            print('MODIFICATION CANCELLED')
                        elif paint>5:
                            print('PLEASE SELECT A VALID PAINT TYPE')
                    elif modi==3:
                        print('+------------------------WHEELS-------------------------+')
                        print('|                    1.STANDARD-Rs10000                 |')
                        print('|                    2.ALMERGA-Rs9000                   |')
                        print('|                    3.BRABUS-Rs8000                    |')
                        print('|                    4.CANCEL                           |')
                        print('+-------------------------------------------------------+')
                        wheels=int(input('ENTER WHEEL TYPE:'))
                        w=0
                        if wheels == 1:
                            w = 10000
                            print('----->STANDARD WHEELS')
                            print('PRICE: 10000')
                        elif wheels == 2:
                            w = 9000
                            print('----->ALMGERA WHEELS')
                            print('PRICE: 9000')
                        elif wheels == 3:
                            w = 8000
                            print('----->BRABUS WHEELS')
                            print('PRICE: 8000')
                        elif wheels == 4:
                            print('MODIFICATION CANCELLED')
                    elif modi==4:
                        print('+----------------------INTERIOR----------------------------+')
                        print('|                    1.BLACK-Rs10000                       |')
                        print('|                    2.WHITE-Rs9000                        |')
                        print('|                    3.RED-Rs8000                          |')
                        print('|                    4.CANCEL                              |')
                        print('+----------------------------------------------------------+')
                        interior=int(input('ENTER INTERIOR TYPE:'))
                        if interior == 1:
                            interior = 10000
                            print('----->BLACK INTERIOR')
                            print('PRICE: 10000')
                        elif interior == 2:
                            interior = 9000
                            print('----->WHITE INTERIOR')
                            print('PRICE: 9000')
                        elif interior == 3:
                            interior = 8000
                            print('----->RED INTERIOR')
                            print('PRICE: 8000')
                        elif interior == 4:
                            print('MODIFICATION CANCELLED')
                    elif modi==5:
                        print('+----------------------MUSIC SYSTEM-------------------------+')
                        print('|                    1. STANDARD - Rs10000                  |')
                        print('|                    2. JBL - Rs23000                       |')
                        print('|                    3. BOSE - Rs25000                      |')
                        print('|                    4. CANCEL                              |')
                        print('+-----------------------------------------------------------+')
                        music = int(input('ENTER MUSIC SYSTEM TYPE: '))
                        if music == 1:
                            music_price = 10000
                            print('----->STANDARD MUSIC SYSTEM')
                            print('PRICE: 10000')
                        elif music == 2:
                            music_price = 23000
                            print('----->JBL MUSIC SYSTEM')
                            print('PRICE: 23000')
                        elif music == 3:
                            music_price = 25000
                            print('----->BOSE MUSIC SYSTEM')
                            print('PRICE: 25000')
                        elif music == 4:
                            print('MODIFICATION CANCELLED')
                    elif modi==6:
                        print('CANCEl')
                        print('MODIFICATION CANCELLED')

                elif choice==5:
                    print("PROGRAMME CLOSED")
                    RONTI()
                    

                    
            while login==1:
                print("+---------------------ADD VEHICHLE-----------------------+")
                print("|                     1.Add Vehicle                      |")
                print("|                     2.Remove Vehicle                   |")
                print("|                     3.View Vehicle                     |")
                print("|                     4.Update Details                   |")
                print("|                     5.EXIT                             |")
                print("+--------------------------------------------------------+")
                choice=int(input("ENTER CHOICE:"))
                if choice==1:
                    x=count()
                    car_id=x[0][0]+1
                    make = input("ENTER CAR MAKER: ")
                    model = input("ENTER CAR MODEL NAME: ")
                    year = int(input("ENTER YEAR OF MAUFACTURING: "))
                    price = float(input("ENTER SELLING PRICE OF THE CAR: "))
                    varient=input('ENTER VARIENT MANUAL/AUTOMATIC:')
                    add_car(car_id,make, model, year, price,varient)

                elif choice==5:
                        print("LOGGING OFF.........")
                        RONTI()
                        
                            
                elif choice==3:
                        view_cars()
                elif choice==2:
                        view_cars()
                        car_id = int(input("Enter car ID to discard: "))

                        delete_car(car_id)
                elif choice==4:
                    view_cars()
                    
                    car_id = int(input("Enter car ID to update: "))
                    make = input("ENTER CAR MAKER: ")
                    model = input("ENTER CAR MODEL NAME: ")
                    year = int(input("ENTER YEAR OF MANUFACTURING: "))
                    price = float(input("ENTER SELLING PRICE OF THE CAR: "))
                    varient = input("ENTER VARIENT MANUAL/AUTOMATIC: ")

                    update_car(car_id, make, model, year, price, varient)
                     
                     
                else:
                    print("Invalid choice! Please try again.")


main()
RONTI()