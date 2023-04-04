import socket
import threading
# this library use for thread pooling 
import concurrent.futures

HOST = "127.0.0.1"  # local connection
PORT = 8080  # Port to listen on (non-privileged ports are > 1023)
currentInterval = 30 # seconds sensors intervals default 60
max_connection = 4 # how many sensor going to connect at the same time

# new thread for each connection 
def handle_client(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received from client: {int.from_bytes(data, byteorder='big')} degree ") # print data which came from sensor 
        conn.sendall(str(currentInterval).encode('utf8')) # send current interval time to sensors(client)
    conn.close()

def echo_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print('started listening')
        print(f'current max sensor count {max_connection}')
        print(f'current interval is {currentInterval}')
        s.listen()
        with concurrent.futures.ThreadPoolExecutor(max_connection) as executor: #create a thread pool for clients thread
            while True:
                conn, addr = s.accept()
                print(f"Connected by {addr}")
                executor.submit(handle_client, conn)


if __name__ == '__main__':
    echo_server()
        
