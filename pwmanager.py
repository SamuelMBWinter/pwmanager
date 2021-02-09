# Database, Cryptographically secure random number generation, and hashing functions
import sqlite3
import secrets
import base64

# Creating an `Account` class to store the data associated with an account
class Account:
    def __init__(self, service, username, password, email = None, url = None):
        self.service = service
        self.usr = username
        self.pwd = password
        self.email = email
        self.url = url
    def attrs(self):
        return [
        self.service,
        self.usr,
        self.pwd,
        self.email,
        self.url,
        ]
# SQLite3 `Safe` class to manage the data base - this helps remove biolerplate code
# This class will have the safe storage of the pass words built in.
class Safe:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE pwds(
            service text,
            username text,
            password text,
            email text,
            url text
            )
        """)
        
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()

    def add_acc(self, account):
        self.cursor.execute("""
            INSERT INTO pwds VALUES (:ser, :usr, :pwd, :email, :url)
            """,
            {
                'ser': account.service,
                'usr': account.usr,
                'pwd': account.pwd,
                'email': account.email,
                'url': account.url,
            }
        )
    
    def retrieve_acc(self, service=None, username=None):
        self.cursor.execute("""
            SELECT * FROM pwds WHERE service=:service OR username=:username
            """,
            {
                'service': service,
                'username': username,
            }
        )
        db_ls = self.cursor.fetchall()
        acc_ls = []
        for entry in db_ls:
            acc_ls.append(
                Account(
                    entry[0],
                    entry[1],
                    entry[2],
                    entry[3],
                    entry[4],
                )
            )
        return acc_ls

if __name__ == "__main__":
        
    Acc1 = Account("service1", "samuelmbwinter", "A very strong password")

    db_path = ":memory:"

    with Safe(db_path) as pwds:
        pwds.add_acc(Acc1) 
        pwds.cursor.execute("SELECT * FROM pwds WHERE service='service1'")
        print(pwds.retrieve_acc(service="service1")[0].attrs())
        
