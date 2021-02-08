import sqlite3

# Creating an `Account` object to store the data associated with an account
class Account:
    def __init__(self, service, username password, email = None, url = None)
        self.service = service
        self.usr = username
        self.pwd = password
        self.email = email
        self.url = url


# Create/ Connect to a database, and create a cursor to execute commands
conn = sqlite3.connect("memory")
cur = con.cusor()

cur.execute("""
    CREATE TABLE pwds(
    service text,
    username text,
    password text,
    email text,
    url text
    )
""")

Acc1 = Account("sevice1", "samuelmbwinter", "A very strong password")

