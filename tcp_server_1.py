# Разработать простейший TCP echo сервер.
#
#Требования
#
#    Запускается на порту 2222
#    Получает сообщения длинной не более 1024 байт и отправляет обратно клиенту
#    Закрывает соединение при получении сообщения с текстом close﻿

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 2222))
s.listen(10) # очередь - 10 клиентов
while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
    if data == 'close': break
conn.close()

