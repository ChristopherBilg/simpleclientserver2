#!/usr/bin/env python2

import socket

HOST = "127.0.0.1"
PORT = 8001
BUFFER_SIZE = 1024

sent_message = raw_input("Message to send: ")
socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_.connect((HOST, PORT))
socket_.send(str(sent_message))
received_message = socket_.recv(BUFFER_SIZE)
print("Message received was: " + received_message)

socket_.close()
