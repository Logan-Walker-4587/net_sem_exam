import socket
import threading

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def receive_messages():
    while True:
        message,client_address = client_socket.recvfrom(1024)
        if message:
            print(message.decode())

receiver_thread = threading.Thread(target = receive_messages)
receiver_thread.start()

while True:
    message = input("Client : ")
    client_socket.sendto(message.encode(),(host,port))

client_socket.close()