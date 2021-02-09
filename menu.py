import pwmanager as pwm

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
: <service> <username> <email> <url>
------------------------------
        """)
    elif option == "r":
                print("""
------------------------------
Retrieve a password
- Use the service name to retrieve a password
: <service>
------------------------------
        """)
    else:
        print("""
------------------------------
Something has gone missing!
------------------------------
        """)
        display_prompt("h")

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
            acc_str = input("> ")
            acc = pwm.Account(
                    *acc_str.split()
            )
            pwds.add_acc(acc)
        
        elif user == "r":
            service_str = input("> ")
            acc_ls = pwds.retrieve_acc(service=service_str)
            for acc in acc_ls:
                print(acc.attrs())
                
            

            

            
