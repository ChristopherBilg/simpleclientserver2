#!/usr/bin/env python2

import socket

HOST = "127.0.0.1"
PORT = 8001
BUFFER_SIZE = 1024


def shift_text(text, shift_amount):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    data = []
    for letter in text:
        if letter.strip() and letter in lower:
            data.append(
                lower[(lower.index(letter) + shift_amount) % len(lower)]
            )
        elif letter.strip() and letter in upper:
            data.append(
                upper[(upper.index(letter) + shift_amount) % len(upper)]
            )
        else:
            data.append(letter)
    return "".join(data)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

connection, address = s.accept()
print("Connection: " + str(connection))
print("Address: " + str(address))

data = connection.recv(BUFFER_SIZE)
if not data:
    exit
print("Data received: " + str(data.decode()))
connection.send(shift_text(data, 3).encode())

connection.close()
