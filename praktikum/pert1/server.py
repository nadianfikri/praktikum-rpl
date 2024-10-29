import socket

# Inisialisasi socket
myp = socket.SOCK_DGRAM
afn = socket.AF_INET
socketServer = socket.socket(afn, myp)
socketServer.bind(("0.0.0.0", 12345))  # Ganti 127.0.0.1 dengan 0.0.0.0 untuk menerima koneksi dari semua IP

print("Server mendengarkan...")

while True:
    clientData, addr = socketServer.recvfrom(1024)  # Terima data dari client
    msg = clientData.decode()  # Dekode pesan
    print(f"{addr[0]} : {msg}")  # Tampilkan alamat dan pesan
