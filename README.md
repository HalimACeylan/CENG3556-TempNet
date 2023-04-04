# CENG3556 - ASSIGNMENT 1 - TEMPNET
## Aim Of Project
The aim of this project is to create a server that can serve multiple clients acting as temperature sensors.
## Expectations 
The communication between the server and clients will be done through sockets. The server will be able to define rules for the clients, which include: 
* The server will decide on the interval for the sensors' data collection (for example, 1-minute interval). 
* The server can change the data collection threshold either in bulk or individually for each sensor. 
* Each sensor should have sleep intervals to ensure power efficiency.
## Code Inside ##
### Load Balancing ###
We need to implement load balancing to prevent overloading. We can approach this problem by using a pool of worker threads. I use [concurrent.futures.ThreadPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) tto handle threads, and the thread pool is created using the following code snippet: 
```python
with concurrent.futures.ThreadPoolExecutor(max_connection) as executor: #create a thread pool for clients thread
    while True:
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        executor.submit(handle_client, conn)
```
Here, the **max_connection** variable is the maximum number of worker threads that can be created..
### Set Interval ### 
To set the interval for each sensor (client), when a client connects to the server and sends the first data, the server sends the **currentInterval** time as an integer value to the client. After receiving this message, the client updates its **timeInterval** value.
#### Server Side ### 
```python
  conn.sendall(str(currentInterval).encode('utf8')) # send current interval time to sensors(client)
```
#### Client Side #### 
```python
  data = s.recv(1024)
  timeInterval = data.decode('utf8')
  sleep(int(timeInterval))
```
