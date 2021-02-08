#import pwmanager as pwm

def display_prompt(option="home"):
    if option == "h":
        print("""
------------------------------
Welcome to the PWManager
h - Home      | a - Add
l - Look up   | q - Quit
------------------------------
        """)

    elif option == "a":
        print("""
------------------------------
Add a new account
- A service name and username, 
are required
- Email and URL are optional
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

while True:
    user = input(": ")
    display_prompt(user)
    if user == "q":
        print("Thanks!")
        break



