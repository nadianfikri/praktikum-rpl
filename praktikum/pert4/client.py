# client.py
import socket
import threading
from datetime import datetime

userName = input("Masukkan username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(userName.encode('ascii'))
            else:
                print(message)  # Display received message with timestamp
        except:
            print("Terjadi kesalahan!")
            client.close()
            break

def write():
    while True:
        # Capture the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Format the message with timestamp before sending
        message = f"[{timestamp}] {userName}: {input('>> ')}"
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
