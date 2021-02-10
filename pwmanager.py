# Database, Cryptographically secure random number generation, and hashing functions
import sqlite3
import base64
import os
import getpass
import secrets

from hashlib import sha256

# Secret key so no master password is actually saved on the machine
secret_key = os.environ.get("SECRET_KEY").encode('utf-8')
master_pwd = os.environ.get("DB_PWD")

# Creating an `Account` class to store the data associated with an account
class Account:
    def __init__(self, service, username, email = None, url = None, password=None):
        self.service = service
        self.usr = username
        self.email = email
        self.url = url
        self.pwd = password
    
    def attrs(self):
        return [
        self.service,
        self.usr,
        self.email,
        self.url,
        self.pwd
        ]

# SQLite3 `Safe` class to manage the data base - this helps remove biolerplate code
# This class will have the safe storage of the pass words built in.
enter_prompt = "Please enter the master password to enter the Safe"
class Safe:
    
    def __init__(self, path):
        self.path = path

    # check user knows the master password
    def __enter__(self):
        print(enter_prompt)
        self.master_pass = getpass.getpass(": ")
        if sha256(self.master_pass.encode('utf-8') + secret_key).hexdigest() == master_pwd:
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
        else:
            raise NotImplementedError("Incorrect Password")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()
    
    def add_acc(self, account, length):
        word = self.make_pwd_seed(length)
        self.cursor.execute("""
            INSERT INTO pwds VALUES (:ser, :usr, :email, :url, :pwd)
            """,
            {
                'ser': account.service,
                'usr': account.usr,
                'email': account.email,
                'url': account.url,
                'pwd': word,
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
        entry = self.cursor.fetchone()
        acc = Account(
            entry[0],
            entry[1],
            entry[2],
            entry[3],
        )
        pwd = self.make_pwd_out(entry[4]) 
        return acc, pwd

    def make_pwd_seed(self, length):
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTYVWXYZ0123456789(,._-*~"<>|!@#$%^&)'
        word = ""
        while len(word) < length:
            word += secrets.choice(chars)
        return word   
    
    def make_pwd_out(self, seed):
        hsh = sha256(seed.encode('utf8') + self.master_pass.encode('utf8') + secret_key[:20]).hexdigest()
        ints = [(int(hsh[i : i+2], 16)) for i in range(0, len(hsh), 2)]
        print(*ints)
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTYVWXYZ0123456789(,._-*~"<>|!@#$%^&)'
        word = ""
        for i in range(len(seed)):
            word += chars[ints[i] % (len(chars))] 
        return  word
