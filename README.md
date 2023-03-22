# [DRAFT] CENG3556 - ASSIGNMENT 1 - TEMPNET
## Aim Of Porject
The aim of this project is to create a server that can serve multiple clients acting as temperature sensors.
## Expectations 
The communication between the server and clients will be done through sockets. The server will be able to define rules for the clients, which include: 
* The server will decide on the interval for the sensors' data collection (for example, 1-minute interval). 
* The server can change the data collection threshold either in bulk or individually for each sensor. 
* Each sensor should have sleep intervals to ensure power efficiency.
## To do Implement 
We need to implement load balancing to prevent overloading. We can approach this problem by using a pool of worker threads or processes.
