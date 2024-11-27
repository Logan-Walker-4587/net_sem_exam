import socket 

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))

data = input("Enter the data : ")
d = []
for i in range(len(data)):
    d.append(int(data[i]))

p0 = d[3]^d[2]^d[0]
p1 = d[3]^d[1]^d[0]
p2 = d[2]^d[1]^d[0]

c = [d[0],d[1],d[2],p2,d[3],p1,p0]

codeword = "".join(str(bit) for bit in c)

client_socket.send(codeword.encode())

client_socket.close()