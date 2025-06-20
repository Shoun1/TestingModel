#define a client using socket
import socket

HEADER=64
PORT = 5432
FORMAT='utf-8'
#DISCONNECT MESSAGE="DISCONNECT"
#SERVER = '192.168.56.1'
#HOST='192.168.56.1' 
HOST = socket.gethostbyname(socket.gethostname())
#HOST='172.25.240.1'
#ADDR = (SERVER,PORT)
DISCONNECT_MESSAGE = "DISCONNECT"

#client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket = socket.socket()
client_socket.connect((HOST,PORT))
#172.25.240.1
#192.168.56.1
#client.connect(ADDR)

def send_data(msg):
    #encode the received message 
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER-len(send_length))
    client_socket.send(send_length)
    client_socket.send(message)

send_data('Hello Client!')
ip_address = socket.gethostbyname(socket.gethostname())
print(f"Client is on {HOST}")
send_data(DISCONNECT_MESSAGE)