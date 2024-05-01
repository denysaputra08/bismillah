import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 65438
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s  .bind((TCP_IP,TCP_PORT))
s.listen()

conn, addr = s.accept()
print('connection address',addr)

while 1 :
    data = conn.recv(BUFFER_SIZE)
    if not data:break
    print(data)
    conn.send(data)

conn.close()