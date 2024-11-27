import socket 

host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen()

client_socket,client_address = server_socket.accept()
codeword = client_socket.recv(1024).decode()

def calculate_syndrome(codeword):
    # Assuming codeword is in the form: [d0, d1, d2, p2, d3, p1, p0]
    codeword = list(map(int, codeword))
    d0, d1, d2, p2, d3, p1, p0 = codeword
    
    # Parity check calculations
    s0 = p0 ^ (d0 ^ d2 ^ d3)   # Check parity for p0
    s1 = p1 ^ (d0 ^ d1 ^ d3)   # Check parity for p1
    s2 = p2 ^ (d1 ^ d2 ^ d0)   # Check parity for p2
    
    return s0, s1, s2

def calculate_error_position(codeword):
    s0, s1, s2 = calculate_syndrome(codeword)
    
    # Convert syndrome bits to a binary number (s2, s1, s0)
    error_position = s2 * 4 + s1 * 2 + s0 * 1
    
    if error_position == 0:
        print("No error detected.")
    else:
        print(f"Error detected at position: {error_position}")
        # Correct the error (flip the bit at the error position)
        codeword[error_position - 1] = str(1 - int(codeword[error_position - 1]))
        print(f"Corrected codeword: {codeword}")

print(f"received codeword = {codeword}")
codeword_list = list(codeword)

print(f"introducing error : ")
# Example: Introduce error by flipping the 4th bit (index 3)
codeword_list[3] = '1' if codeword_list[3] == '0' else '0'
print(f"error introduced codeword {codeword_list}")
calculate_error_position(codeword_list)


server_socket.close()
