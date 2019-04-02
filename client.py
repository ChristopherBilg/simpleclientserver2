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

sent_message = raw_input("Message to send: ")
socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_.connect((HOST, PORT))
socket_.send(shift_text(str(sent_message), 3))

print("Message sent was: " + shift_text(str(sent_message), 3))

received_message = socket_.recv(BUFFER_SIZE)
if not received_message:
    exit

print("Message received was: " + received_message)

socket_.close()
