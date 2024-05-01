import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 65438
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))

while True:
    MESSEGE = input('Ketikkan : ')
    s.send(MESSEGE.encode())
    data = s.recv(BUFFER_SIZE)
    print(MESSEGE)
    
conn.close()
print(data)