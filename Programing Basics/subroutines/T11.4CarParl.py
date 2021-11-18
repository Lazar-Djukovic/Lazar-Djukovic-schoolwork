car_park =[]
x = 0
y = 0
def carpark1():
    for row in range(20):
        car_park.append([])
        for col in range(6):
            car_park[row].append('empty')
        #next col
    #next row
#end procedure

def carpark2(x,y,z):
    if car_park[x-1][y-1] == 'empty':
        car_park[x-1][y-1] = z
    else:
        print('This space is already taken')

def carpark3(regnum):
    global car_park
    for row in range(20):
        for col in range(6):
            if col == regnum:
                col = 'empty'



print('+-----------------------------------------------------------------+')
print("1. Reset all spaces in the car park to 'empty'")
print("2. Park a car")
print("3. Remove a car")
print("4. Display the car park grid")
print("5. Quit\n")
print('+-----------------------------------------------------------------+')
option = input("Enter your choice: ")

while option != "5":
    if option == "1":
        car_park = []
        carpark1()
        print(car_park) 
    elif option == "2":
        carrow = int(input('Row of the car'))
        carcol = int(input('Col of the car'))
        regnum = str(input('Enter car registarion number '))
        carpark2(carrow,carcol,regnum)
        print(car_park)
    elif option == "3":
        regis = input('Enter the registration number of the car you want removed ')
        carpark3(regis)
    elif option == "4":
        print(car_park)
    else:
        option = ("Invalid choice - please re-enter: ")
    #endif
    print('+-----------------------------------------------------------------+')
    print("1. Reset all spaces in the car park to ‘empty’")
    print("2. Park a car")
    print("3. Remove a car")
    print("4. Display the car park grid")
    print("5. Quit\n")
    print('+-----------------------------------------------------------------+')
    option = input("Enter your choice: ")
#endwhile