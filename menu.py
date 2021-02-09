import pwmanager as pwm
import getpass

def display_prompt(option="h"):
    if option == "h":
        print("""
------------------------------
Welcome to the PWManager
h - Home      | a - Add
r - Retrieve  | q - Quit
------------------------------
        """)

    elif option == "a":
        print("""
------------------------------
Add a new account
- A service name and username, 
are required
- Email and URL are optional
> <service> <username> <email> <url>
------------------------------
        """)
    elif option == "r":
                print("""
------------------------------
Retrieve a password
- Use the service name to retrieve a password
> <service>
------------------------------
        """)
    else:
        print("""
------------------------------
Something has gone missing!
------------------------------
        """)
        display_prompt("h")

def db_add(acc_str):
    acc = pwm.Account(*acc_str.split())
    pwds.add_acc(acc)

def db_ret(ser_str):
    acc_ls = pwds.retrieve_acc(service=ser_str)
    for acc in acc_ls:
        print(*acc.attrs())

db_path = ":memory:"

user = "h"
display_prompt(user)


with pwm.Safe(db_path) as pwds:
    while True:
        user = input(": ")
        display_prompt(user)
        if user == "q":
            print("Thanks!")
            break
        
        elif user == "a":
            while user == "a":
                acc_str = input("> ")
                db_add(acc_str)
                print("'a' to add another, else go home")
                user = input("> ")
            display_prompt("h")
        elif user == "r":
            while user == "r":
                service_str = input("> ")
                db_ret(service_str)
                print("'r' to retrieve another, else go home")
                user = input("> ")
            display_promt("h")
        
        else:
            continue
        
            
            
                     
            

            
