# server.py
import socket
import threading
from datetime import datetime

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            # Receive message from client
            message = client.recv(1024)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Format message with timestamp
            message_with_time = f"[{timestamp}] {message.decode('ascii')}"
            broadcast(message_with_time.encode('ascii'))
        except:
            # Remove client if there's an error
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"[{timestamp}] {nickname} keluar!".encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Terhubung dengan {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Username {nickname}")
        broadcast(f"{nickname} Bergabung!".encode('ascii'))
        client.send('Terkoneksi dengan Server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
