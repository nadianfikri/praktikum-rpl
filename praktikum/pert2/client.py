# client.py
import socket
import threading
import time

def send_messages(socketClient, username):
    while True:
        message = input('Enter your message: ')
        full_message = f"{username}: {message}"
        socketClient.send(full_message.encode())
        time.sleep(1)  # Send messages every second

# Connect to the server
socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketClient.connect(("127.0.0.1", 12345))

# Prompt the user to enter their username
username = input("Enter your username: ")

# Start a thread to send messages continuously
send_thread = threading.Thread(target=send_messages, args=(socketClient, username))
send_thread.start()
