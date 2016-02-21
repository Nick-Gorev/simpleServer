import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data: break
        if data == 'close':
            conn.close()
            sys.exit(0)
        conn.send(data)
