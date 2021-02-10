import pwmanager as pwm
import pyperclip

# Defining the menu functions, and what they do:
def menu_home():
    title = "Home"
    print('')
    print("--<" + title + ">" + "-" * (31- len(title)))
    print("h - Home Menu")
    print("a - Add account")
    print("r - Retrieve account data and password")
    print("q - Quit")
    print("':' is the menu prompt - use the options above")
    print("'>' is the entry prompt - enter as instructed")
    print("-" * 35)
    option = input(": ")
    print("")
    return option

def menu_add():
    title = "Add"
    print('')
    print("--<" + title + ">" + "-" * (31- len(title)))
    print("To add an account the service and username are required")
    print("<service> <username> [<email>] [<url>]")
    print("-" * 35)
    acc = pwm.Account(*input("> ").split())
    print("Length of password (in chars)")
    length = int(input("> "))
    word = pwds.add_acc(acc, length)
    pyperclip.copy(word)
    print("Account added sucessfully - Password has been copied to clipboard")
    print("\nGo to")
    option = input(": ")
    return option
         
def menu_ret():
    title = "Retrieve"
    print('')
    print("--<" + title + ">" + "-" * (31- len(title)))
    print("To retrieve account data, enter the name of ther service")
    print("<service>")
    print("-" * 35)
    ser = input("> ")
    acc, pwd = pwds.retrieve_acc(service=ser)
    print(*acc.attrs())
    pyperclip.copy(pwd)
    print("Password has been copied to the clipboard\n")
    print("Go to")
    option = input(": ")
    return option

def menu_list():
    title = "List"
    print('')
    print("--<" + title + ">" + "-" * (31- len(title)))
    print("Here is a list of the accounts")
    print("-" * 35)
    for entry in pwds.list_acc():
        print(*entry)
    print("Go to")
    option = input(": ")
    return option

def menu_error():
    title = "Error"
    print('')
    print("--<" + title + ">" + "-" * (31- len(title)))
    print("Something has gone wrong here!")
    print("Let's go home now...")
    print("-" * 35)
    menu_home()


db_path = "/home/samwinter/.config/pypwdman/pwds.db"

option = 'h'

with pwm.Safe(db_path) as pwds:
    while True: 
        if option in ["h", "home", ""]:
            option = menu_home()
            
        elif option in ["a", "add"]:
            option = menu_add()

        elif option in ["r", "retrieve"]:
            option = menu_ret()

        elif option in ["l", "list"]:
            option = menu_list()

        elif option in ["q", "quit"]:
            break

        else:
            option = menu_error()
