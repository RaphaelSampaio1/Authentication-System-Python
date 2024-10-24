import sqlite3
import hashlib

# Create the conexion with SQLite DB
conn = sqlite3.connect("userdatabase.db")
cur = conn.cursor()

# Create table 
cur.execute(""" 
CREATE TABLE IF NOT EXISTS userdata(
    Id INTEGER PRIMARY KEY,
    Username VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL      
            )
""")

# Create user and hash password
username1, password1 = "mike123", hashlib.sha256("mikepassword".encode()).hexdigest()
username2, password2 = "Catarinaabk", hashlib.sha256("teste1111".encode()).hexdigest()
username3, password3 = "felipemiliduke", hashlib.sha256("123teste".encode()).hexdigest()
username4, password4 = "raphaelsampaio", hashlib.sha256("agoravai".encode()).hexdigest()

print(username4, password4) # Confirm if it's ok

# Create users in DB
cur.execute("INSERT INTO userdata(Username, Password) VALUES (?, ?) ", (username1, password1))
cur.execute("INSERT INTO userdata(Username, Password) VALUES (?, ?) ", (username2, password2))
cur.execute("INSERT INTO userdata(Username, Password) VALUES (?, ?) ", (username3, password3))
cur.execute("INSERT INTO userdata(Username, Password) VALUES (?, ?) ", (username4, password4))

conn.commit()
