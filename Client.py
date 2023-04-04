import socket
from time import sleep
import random
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8080  # The port used by the server
timeInterval = 20 # sleep interval default 20. it should updated by server

def echo_client():
    global timeInterval
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            # Generate a random byte representing temperature sensor data
            temp_data = random.randint(0, 255)
            # Convert the int to bytes
            temp_bytes = bytes([temp_data])
            s.sendall(temp_bytes)
            print(f"data is: {temp_data!r}")
            print(f"Current Interval: {timeInterval}")
            # update current interval from server
            data = s.recv(1024)
            timeInterval = data.decode('utf8')
            sleep(int(timeInterval))


if __name__ == '__main__':
    echo_client()
