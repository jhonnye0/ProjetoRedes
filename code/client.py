#!/usr/bin/python
# encoding: utf-8

import socket

address = ("localhost", 12345)

# Create sockets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)


# COMMAND:VALUE1;VALUE2...

# Echo
while True:
    text = input("Digite os dados ou 'sair' para desconectar: ")
    
    if(text == "sair"):
        client_socket.close()
        break

    client_socket.send(text.encode())

    print(client_socket.recv(1024).decode())
    
