# Database, Cryptographically secure random number generation, and hashing functions
import sqlite3
import secrets
import base64
import os

# Secret key for safe salting of passwords
secret_key = os.environ.get("SECRET_KEY")
master_pwd = os.environ.get("DB_PWD")

# Creating an `Account` class to store the data associated with an account
class Account:
    def __init__(self, service, username, email = None, url = None, password=None,):
        self.service = service
        self.usr = username
        self.email = email
        self.url = url
        self.pwd = password
    
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
            email text,
            url text,
            password text
            )
        """)
        
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()

    def add_acc(self, account):
        # This is where the magic happens
        salt = secret_key + account.service
        account.pwd = salt
        
        self.cursor.execute("""
            INSERT INTO pwds VALUES (:ser, :usr, :email, :url, :pwd)
            """,
            {
                'ser': account.service,
                'usr': account.usr,
                'email': account.email,
                'url': account.url,
                'pwd': account.pwd,
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
        
    Acc1 = Account("service1", "samuelmbwinter")

    db_path = ":memory:"

    with Safe(db_path) as pwds:
        pwds.add_acc(Acc1) 
        pwds.cursor.execute("SELECT * FROM pwds WHERE service='service1'")
        print(pwds.retrieve_acc(service="service1")[0].attrs())
        
