import socket

#########DHCP################
mySocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mySocket.connect(('localhost',8000))
address=int.from_bytes(mySocket.recv(3),"big")
mySocket.close()

SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(("127.0.0."+str(address),PORT))
client.connect((SERVER, PORT))
client.sendall(bytes("This is from Client",'UTF-8'))
while True:
  in_data =  client.recv(1024)
  print("From Server :" ,in_data.decode())
  out_data = input()
  client.sendall(bytes(out_data,'UTF-8'))
  if out_data=='bye':
    break
client.close()