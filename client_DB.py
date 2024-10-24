import socket

# Create a socket for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

# Receive and send the username prompt
message = client.recv(1024).decode()
client.send(input(message).encode())

# Receive and send the password prompt
message = client.recv(1024).decode()
client.send(input(message).encode())

# Receive the final login status and print it
response = client.recv(1024).decode()
print(response)

client.close()
