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

    'REGISTRATION': "DECLARO, SOB PENA DE LEI, QUE O INDIVÍDUO DE NOME: _NAME E IDENTIFICAÇÃO _ID ESTÁ MATRICULADO NA ESCOLA _SCHOOL DE ACORDO COM OS REQUERIMENTOS CONSTADOS NA MATRÍCULA DO MESMO.",
    'INCOME': "O INDIVÍDUO _NAME, QUE MORA NO ENDEREÇO _ADDRESS, POSSUI UMA QUANTIA DECLARADA DE R$ _VALUE PARA MAIS INFORMAÇÕES CONSULTE O SITE DO GOVERNO: WWW.GOVERNO.COM.GOV."
}

def extract_info(data):

    cmd = []
    p = []
    text = ''

    cmd = data.split(':')[0].upper()

    if cmd in commands:

        p = data.split(':')[1].split(';')

        if len(p) != 3:
            return "301 - Parâmetros inválidos, digite o comando novamente com os seguintes parâmetros respectivamente" + str(commands[cmd])

        parameters = {}
        i = 0

        for key in commands[cmd]:
            parameters[key] = p[i]
            i+=1

        text = texts[cmd]

        for key in commands[cmd]:
            text = text.replace(key, parameters[key])

        return "200 - " + text

    else:
        return "300 - Comando inválido, digite um dos comandos novamente (INCOME, REGISTRATION)" 
  
def thread(c, addr): 

    while True: 
        
        # data received from client 
        data = c.recv(1024).decode()

        if not data: 
            print('400 - Bye ' + addr[0])
            break

        text = extract_info(data)

        c.send(text.encode())
  
    # connection closed 
    c.close() 

host = "localhost" 
  
# reverse a port on your computer
port = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host, port)) 
print("socket binded to port", port) 

# Put the socket into listening mode 

s.listen(5) 
print("socket is listening") 

# A forever loop until client wants to exit 
while True: 

    # Establish connection with client 
    c, addr = s.accept() 
 
    print('Connected to :', addr[0], ':', addr[1]) 

    # Inicializing the thread
    start_new_thread(thread, (c, addr)) 

s.close() 

