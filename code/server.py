#!/usr/bin/python

# import socket programming library 
import socket 

# import thread module 
from _thread import *
import threading 

commands = {
    
    'INCOME': ['_NAME', '_VALUE', '_ADDRESS'],
    'REGISTRATION': ['_NAME', '_ID', '_SCHOOL']
}

texts = {

    'REGISTRATION': "DECLARO QUE O INDIVÍDUO DE NOME: _NAME E IDENTIFICAÇÃO _ID É PORTADOR DE UMA DEFICIÊNCIA MENTAL E ESTÁ IMPOSSIBILITADO DE ESTUDAR NA ESCOLHA _SCHOOL",
    'INCOME': "ESSE INDIVÍDUO DE NOME _NAME QUE MORA NO ENDEREÇO _ADDRESS POSSUI A QUANTIA DECLARADA DE R$ _VALUE"
}
  
# thread function 
def threaded(c): 

    while True: 
        # data received from client 
        data = c.recv(1024).decode()
        if not data: 
            print('Bye')
            break
        
        cmd = []
        p = []

        cmd = data.split(':')[0]
        p = data.split(':')[1].split(';')

        parameters = {}
        i = 0

        for key in commands[cmd]:
            parameters[key] = p[i]
            i+=1

        text = texts[cmd]

        for key in commands[cmd]:
            text = text.replace(key, parameters[key])

        c.send(text.encode())
  
    # connection closed 
    c.close() 

host = "localhost" 
  
# reverse a port on your computer 
# in our case it is 12345 but it 
# can be anything 

port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host, port)) 
print("socket binded to port", port) 

# put the socket into listening mode 

s.listen(5) 
print("socket is listening") 

# a forever loop until client wants to exit 
while True: 

    # establish connection with client 
    c, addr = s.accept() 
 
    print('Connected to :', addr[0], ':', addr[1]) 

    # Start a new thread and return its identifier 
    start_new_thread(threaded, (c,)) 

s.close() 

