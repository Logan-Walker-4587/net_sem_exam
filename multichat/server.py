import socket 
import threading

host = '127.0.0.1' 
port = 12345

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((host,port))

clients = set()

def handle_client():
    while True:
         message,client_address = server_socket.recvfrom(1024)
         clients.add(client_address)
         print(f"client : {message.decode()}")
         broadcast_message(client_address,message)

def broadcast_message(sender_address,message):
    for client in clients:
            if client!=sender_address:
                 server_socket.sendto(message,client)

def broadcast():
    while True:
          message = input("server : ")
          message = "server : " + message
          broadcast_message(None,message.encode())

def accept_clients():
    while True:
        handle_client()
        thread = threading.Thread(target = handle_client)
        thread.start()

accept_thread = threading.Thread(target = accept_clients)
accept_thread.start()

broadcast()