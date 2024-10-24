# Authentication-System-Python
Login System with SQLite


# User Authentication System

This project is a simple user authentication system using Python. It demonstrates how to create a client-server architecture where a client can log in with a username and password. The credentials are stored securely in a SQLite database with password hashing for added security.

## Purpose

The purpose of this project is to showcase a basic implementation of user authentication using socket programming, threading, and a database in Python. It allows users to log in, verifying their credentials against stored data in a SQLite database.

## Components

The project consists of three main scripts:

1. **login_db.py**: Sets up the SQLite database, creates a user table, and populates it with sample user credentials.
2. **server_db.py**: Implements the server that listens for client connections, handles login requests, and validates user credentials against the database.
3. **client_db.py**: Represents the client that connects to the server, sends username and password, and receives the login status.

## Requirements

- Python 3.x
- SQLite3

## How to Run

1. **Run the Database Setup**: First, execute `login_db.py` to create the SQLite database and populate it with sample users.
   ```bash
   python login_db.py
   ```

2. **Start the Server**: Run `server_db.py` to start the server that will handle client connections.
   ```bash
   python server_db.py
   ```

3. **Run the Client**: In a new terminal, execute `client_db.py` to start the client application.
   ```bash
   python client_db.py
   ```

4. **Interact with the Client**: Follow the prompts to enter the username and password. The client will send the credentials to the server, which will respond with either "Login Successful!" or "Login Failed!".

## Code Explanation

### login_db.py

- Connects to the SQLite database and creates a `userdata` table if it doesn’t exist.
- Hashes the passwords using SHA-256 and inserts sample users into the database.

### server_db.py

- Creates a socket server that listens for incoming connections.
- Handles each connection in a separate thread using the `handle_connection` function.
- Requests the username and password from the client, hashes the password, and checks the credentials against the database.

### client_db.py

- Connects to the server and prompts the user for their username and password.
- Sends the credentials to the server and prints the server's response regarding the login status.

## Example

1. Enter `mike123` as the username and `mikepassword` as the password to log in successfully.
2. Enter `wronguser` or an incorrect password to see the "Login Failed!" message.

## Conclusion

This project serves as an educational example of how to implement user authentication in Python using socket programming and SQLite. It can be extended with additional features such as password recovery, user registration, or more robust error handling.
