import socket 

host = '127.0.0.1' 
port = 12345

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))

print(f"connected to server {host}:{port}")

message = "hello server im client"
client_socket.send(message.encode())

reply = client_socket.recv(1024)
print(f"server : {reply.decode()}")

client_socket.close()