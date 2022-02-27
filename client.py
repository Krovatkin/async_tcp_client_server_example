

import socket  
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.connect(('127.0.0.1', 5000))  
#sock.send('Test\n')  
sock.send("rara".encode("utf-8"))  
print(sock.recv(1024).decode("utf-8"))
sock.close()