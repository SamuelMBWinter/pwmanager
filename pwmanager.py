import sqlite3

# Creating an `Account` object to store the data associated with an account
class Account:
    def __init__(self, service, username, password, email = None, url = None):
        self.service = service
        self.usr = username
        self.pwd = password
        self.email = email
        self.url = url


# Create/ Connect to a database, and create a cursor to execute commands
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE pwds(
    service text,
    username text,
    password text,
    email text,
    url text
    )
""")

Acc1 = Account("service1", "samuelmbwinter", "A very strong password")

cur.execute(
    "INSERT INTO pwds VALUES (:ser, :usr, :pwd, :email, :url)",
    {
        'ser': Acc1.service,
        'usr': Acc1.usr,
        'pwd': Acc1.pwd,
        'email': Acc1.email,
        'url': Acc1.url,
    }
)
conn.commit()

cur.execute("SELECT * FROM pwds WHERE service='service1'")
print(cur.fetchall())

cur.close

conn.commit()

conn.close()
