# server.py
import socket
import datetime

# Setup server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("127.0.0.1", 12345))
print("Alamat IP: 127.0.0.1")

# Server enters username
name = input('Masukkan Username: ')
serverSocket.listen()
msg, addrs = serverSocket.accept()
print("Menerima koneksi dari ", addrs[0])

# Display date once upon connection
current_date = datetime.datetime.now().strftime("%Y-%m-%d")
print('Tanggal:', current_date)
print('Connection Established. Terkoneksi dari:', addrs[0])

# Receive client username
client = (msg.recv(1024)).decode()
print(client + ' sudah terhubung.')
msg.send(name.encode())

# Communication loop
while True:
    # Receive message from client and display with timestamp
    message = msg.recv(1024).decode()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{client} ({current_time}): {message}")
    
    # Send a message to the client
    response = input("Balasan: ")
    response_with_time = f"{current_date} {current_time} - {response}"
    msg.send(response_with_time.encode())
