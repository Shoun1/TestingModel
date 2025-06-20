#define a server using socket
import socket
import threading 

header=64 #bytes of data
FORMAT='utf-8'
#ip_address = socket.gethostbyname(socket.gethostname())
server = socket.gethostbyname(socket.gethostname())
#print(ip_address)
#ip_address = '172.25.240.1'
port = 5432
addr = (server, port)
#define a socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(addr)
DISCONNECT_MESSAGE = "DISCONNECT"

def handle_client(conn,addr):
    client_info = find_client_ip(conn,addr)
    print(f"[NEW CONNECTION] {addr} connected.")

    connected =True
    while connected:
        #message received from socket
        message_length = conn.recv(header).decode(FORMAT)
        print(message_length)
        if message_length:
            message_length = int(message_length)
            msg = conn.recv(message_length).decode(FORMAT)
            print(f"[{addr}] {msg}")
            if msg == DISCONNECTED_MESSAGE:
                connected = False
    print(f"Client is on {server}")
    conn.close()

def find_client_ip(conn, addr):
    client_ip, client_port = addr
    try:
        # Attempt reverse DNS lookup to get hostname
        client_hostname = socket.gethostbyaddr(client_ip)[0]
        print(client_hostname)
    except socket.herror:
        client_hostname = "Unknown"

    print(f"[CLIENT INFO] IP: {client_ip}, Port: {client_port}, Hostname: {client_hostname}")
    return {
        "ip": client_ip,
        "port": client_port,
        "hostname": client_hostname
    }

def start():
    conn, addr = server.accept()
    find_client_ip(conn, addr)  # call it here or inside handle_client

    server.listen()
    #server.bind(('0.0.0.0', 5432))
    print(f"Server is on {server}")

    while True:
        conn,addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")

print("[server] is starting...")
if __name__ == "__main__":
    start()
    handle_client(conn,addr)
    dict = find_client_ip(conn,addr)
    print(dict)