#!/usr/bin/python
# encoding: utf-8

import socket

address = ("localhost", 7777)

# Create sockets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)

# COMMAND:VALUE1;VALUE2...

# Echo
while True:
    text = input("Digite o comando seguido dos valores ou 'exit' para desconectar-se: ")
    
    if(text.lower() =="exit"):
        client_socket.close()
        break

    client_socket.send(text.encode())

    print(client_socket.recv(1024).decode())
    
