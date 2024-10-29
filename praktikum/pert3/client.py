# client.py
import socket
import datetime

# Setup client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get and display client IP address automatically
client_ip = socket.gethostbyname(socket.gethostname())
print('Alamat IP Client:', client_ip)

# Manually enter server IP and port
server_host = input('Masukkan alamat IP Server: ')
server_port = int(input('Masukkan port Server: '))
name = input('Masukkan Username: ')

# Connect to the server
clientSocket.connect((server_host, server_port))
clientSocket.send(name.encode())

# Receive server username
server_name = clientSocket.recv(1024).decode()
print(server_name, 'Telah bergabung...')

# Communication loop
while True:
    # Send message to server
    message = input("Pesan: ")
    clientSocket.send(message.encode())

    # Receive response from server
    response = clientSocket.recv(1024).decode()
    print(response)
