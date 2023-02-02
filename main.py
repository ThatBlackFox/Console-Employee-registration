import json
import os
from time import sleep

with open('db.json','r') as f:
    db = json.load(f)
    if not db:
        db={"employees":{}}

# Employee registration and login

def edit(name:str):
    os.system("cls")
    print(f"Welcome to employee update form | updating {name.capitalize()}")
    age = input("Age: ")
    email = input("Email: ")
    db['employees'][name.upper()]={'name':name.upper(),'age':age,'email':email}
    print(f"Employee {name.capitalize()} has been successfully updated!")
    sleep(2)
    os.system("cls")

def new():
    os.system("cls")
    print("Welcome to new employee registration form")
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    db['employees'][name.upper()]={'name':name.upper(),'age':age,'email':email}
    print(f"Employee {name} has been successfully registered!")
    sleep(2)
    os.system("cls")
    return True

def manage():
    os.system("cls")
    options = ['a','s','e','d','b']
    print("Welcome to employee management portal")
    print(
"""
Enter one of the following keys:
[A] to view all employee records
[S] to view a single employee
[E] to edit an employee's records
[D] to delete a record
[B] to return back to the main menu
""")
    option = input(">> ").lower()
    if option in options:
        if option==options[0]:
            counter = 1
            for employee in db['employees']:
                print(f"{counter}. | {db['employees'][employee]['name'].capitalize()} | {db['employees'][employee]['age']} | {db['employees'][employee]['email']}")
                counter+=1
            input(">> Press any key to the management portal")
        elif option==options[1]:
            os.system("cls")
            name = input("Enter employee's name: ").upper()
            if name in db['employees']:
                print(f"{db['employees'][name]['name'].capitalize()} | {db['employees'][name]['age']} | {db['employees'][name]['email']}")
                input(">> Press any key to the management portal")
            else:
                print(f"No employee found with that name.")
        elif option==options[2]:
            os.system("cls")
            name = input("Enter employee's name: ").upper()
            if name in db['employees']:
                edit(name)
            else:
                print(f"No employee found with that name.")
        elif option==options[3]:
            os.system("cls")
            name = input("Enter employee's name: ").upper()
            if name in db['employees']:
                db['employees'].pop(name)
                print(f"Employee {name.capitalize()} has been successfully deleted!")
                input(">> Press any key to the management portal")
                os.system("cls")
            else:
                print(f"No employee found with that name.")
        else:
            os.system("cls")
            return True #for option [B]

        return False
    else:
        os.system("cls")
        print("\nError: Invalid option, please use only the options that are mentioned")
        sleep(1)
        os.system("cls")
        return False



def main():
    os.system("cls")
    using=True
    while using==True:
        options = ['n','m','e']
        print(
"""Welcome to Employee Information Portal:

Enter one of the following keys to
[N] to make a new registration
[M] to enter managing menu
[E] to exit the program
""")
        option = input(">> ").lower()
        
        persist = True
        if option in options:
            while persist:
                if option==options[0]:
                    done = new()
                elif option==options[1]:
                    done = manage()
                else:
                    with open('db.json','w') as f:
                        json.dump(db,f)
                    exit()
                if done:
                    persist=False 
        else:
            print("\nError: Invalid option, please use only the options that are mentioned")
            sleep(1)
            os.system("cls")

main()