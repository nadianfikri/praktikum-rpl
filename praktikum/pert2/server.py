# server.py
import socket
import threading
import time

socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketClient.bind(("127.0.0.1", 12345))
print("Server is waiting for messages...")

def handle_client(number):
    while True:
        try:
            data, addr = socketClient.recvfrom(1024)
            message = data.decode()
            print(f"User-{number} ({addr[0]}): {message}")
            time.sleep(1)
            print(f"User-{number} ({addr[0]}): {message}")
        except:
            break

client_number = 0
while True:
    client_number += 1
    client_thread = threading.Thread(target=handle_client, args=(client_number,))
    client_thread.start()
