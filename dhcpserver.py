from http import client
import socket,random

DHCPserverSocket=socket.create_server(('localhost',8000),backlog=5)
Unassignedip=list(range(2,255))
random.shuffle(Unassignedip)
while True:
    ( clientSocket, clientAddress ) = DHCPserverSocket.accept()
    clientSocket.send(Unassignedip[0].to_bytes(3,"big"))
    print("127.0.0."+str(Unassignedip[0]))
    del Unassignedip[0]
    clientSocket.close()
