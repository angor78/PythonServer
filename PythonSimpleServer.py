import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 2000))

server.listen(4)
print('Working....')
client_socket, addres = server.accept()
data = client_socket.recv(1024).decode('utf-8')
print(data)