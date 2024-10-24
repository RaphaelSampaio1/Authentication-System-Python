import hashlib
import sqlite3
import socket
import threading

# Create a socket for communication
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

def handle_connection(c):
    try:
        # Request and receive the username
        c.send("Username: ".encode())
        username = c.recv(1024).decode().strip()

        # Request and receive the password
        c.send("Password: ".encode())
        password = c.recv(1024).decode().strip()
        password = hashlib.sha256(password.encode()).hexdigest()

        # Connect to the database
        conn = sqlite3.connect("userdatabase.db")
        cur = conn.cursor()

        # SQL command to check user credentials
        cur.execute("SELECT * FROM userdata WHERE Username = ? AND Password = ?", (username, password))

        if cur.fetchone():  # Using `fetchone` instead of `fetchall` for better performance
            c.send("Login Successful!".encode())
        else:
            c.send("Login Failed!".encode())

        conn.close()  # Close the database connection
    except Exception as e:
        print(f"An error occurred: {e}")
        c.send("An error occurred on the server.".encode())
    finally:
        c.close() 

# Loop to accept new connections and start threads to handle them
while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()
