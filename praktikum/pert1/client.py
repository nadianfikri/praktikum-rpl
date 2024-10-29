import socket

# Meminta IP Address dan Port Server secara dinamis
ip_address = input("Masukkan IP Address Server: ")
port = int(input("Masukkan Port Server: "))

# Membuat socket
socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Mengatur variabel untuk pengiriman pesan
counter = 1

while True:
    # Mengambil input pesan dari pengguna
    message = input("Masukkan pesan (atau ketik 'exit' untuk berhenti): ")
    
    # Menghentikan pengiriman jika pengguna mengetik 'exit'
    if message.lower() == 'exit':
        print("Pengiriman pesan dihentikan.")
        break
    
    # Mengirim pesan dengan penambahan angka
    full_message = f"{message} {counter}"
    socketClient.sendto(full_message.encode(), (ip_address, port))
    
    # Meningkatkan counter untuk pesan selanjutnya
    counter += 1
