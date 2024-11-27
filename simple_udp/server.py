import socket 

host = '127.0.0.1' 
port = 12345

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((host,port))

message,client_address = server_socket.recvfrom(1024)
print(f"client = {message.decode()} from {client_address}")

reply = "message received"
server_socket.sendto(reply.encode(),client_address)

server_socket.close()

