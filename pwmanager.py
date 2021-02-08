import sqlite3

# Creating an `Account` class to store the data associated with an account
class Account:
    def __init__(self, service, username, password, email = None, url = None):
        self.service = service
        self.usr = username
        self.pwd = password
        self.email = email
        self.url = url

# SQLite3 `Safe` class to manage the data base - this helps remove biolerplate code
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
                'ser': Acc1.service,
                'usr': Acc1.usr,
                'pwd': Acc1.pwd,
                'email': Acc1.email,
                'url': Acc1.url,
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
        return self.cursor.fetchall()

if __name__ == "__main__":
        
    Acc1 = Account("service1", "samuelmbwinter", "A very strong password")

    db_path = ":memory:"

    with Safe(db_path) as pwds:
        pwds.add_acc(Acc1) 
        pwds.cursor.execute("SELECT * FROM pwds WHERE service='service1'")
        print(pwds.retrieve_acc(service="service1"))
        
