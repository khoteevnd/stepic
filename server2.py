# -*- coding: UTF-8 -*-

import socket, threading, string

debug = True

_connector = None
_running = True

_host = '0.0.0.0'
_port = 2222
_maxClient = 99
_recvBuffer = 1024

def printd(aString):
    if debug:
        print aString

class talkToClient(threading.Thread):
    def __init__(self, clientSock, addr):
        self.clientSock = clientSock
        self.addr = addr
        threading.Thread.__init__(self)
    def run(self):
        while True:
            recvData = self.clientSock.recv(_recvBuffer)
            if not recvData:
                self.clientSock.send('bye')
                break
            printd('Client ' + str(self.addr) + ' say "' + str(recvData) + '"')
            self.clientSock.send(recvData)
            if recvData == "close":
                break
        self.clientSock.close()

_connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_connector.bind((str(_host), int(_port)))
_connector.listen(int(_maxClient))

while _running:
    printd('Running on ' + _host + ':' + str(_port) + '.')
    clientSock, addr = _connector.accept()
    printd('Conect on : ' + str (addr))
    #talkToClient (channel, details).start ()
    while True:
        recvData = clientSock.recv(_recvBuffer)
        if not recvData:
                clientSock.send('bye')
                break
        printd('Client ' + str(addr) + ' say "' + str(recvData) + '"')
        clientSock.send(recvData)
        if recvData == "data":
                break
    clientSock.close()

_connector.close()
