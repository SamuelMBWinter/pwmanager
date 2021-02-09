import pwmanager as pwm
import pyperclip

def display_prompt(option="h"):
    if option == "h":
        title = "Menu"
        print('')
        print("--<" + title + ">" + "-" * (31- len(title)))
        print("h - Home Menu")
        print("a - Add account")
        print("r - Retrieve account data and password")
        print("q - Quit")
        print("-" * 35)
   
    elif option == "a":
        title = "Add"
        print('')
        print("--<" + title + ">" + "-" * (31- len(title)))
        print("To add an account the service and username are required")
        print("<service> <username> [<email>] [<url>]")
        print("-" * 35)
   
    elif option == "r":
        title = "Retrieve"
        print('')
        print("--<" + title + ">" + "-" * (31- len(title)))
        print("To retrieve account data, enter the name of ther service")
        print("<service>")
        print("-" * 35)
   
    else:
        title = "Error"
        print('')
        print("--<" + title + ">" + "-" * (31- len(title)))
        print("Something has gone wrong here!")
        print("-" * 35)
        display_prompt("h")

def db_add(acc_str, length):
    acc = pwm.Account(*acc_str.split())
    pwds.add_acc(acc, length)

def db_ret(ser_str):
    acc = pwds.retrieve_acc(service=ser_str)
    return acc.attrs()

db_path = ":memory:"

user = "h"

with pwm.Safe(db_path) as pwds:
    display_prompt(user)
    while True:
        user = input(": ")
        display_prompt(user)
        if user == "q":
            print("Thanks!")
            break
        
        elif user == "a":
            while user == "a":
                acc_str = input("> ")
                print("How many characters in the password?")
                length = int(input("> "))
                db_add(acc_str, length)
                print("'a' to add another, else go home")
                user = input("> ")
            display_prompt("h")
        
        elif user == "r":
            while user == "r":
                service_str = input("> ")
                acc_ls = db_ret(service_str)
                print(*acc_ls[:-1])
                pyperclip.copy(acc_ls[-1])
                print("'r' to retrieve another, else go home")
                user = input("> ")
            display_prompt("h")
        
        else:
            continue
        
            
            
                     
            


