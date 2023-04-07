
# client - reciever

# Import socket module
from socket import *
from HelperModule import udt
from HelperModule import packet
from HelperModule import timer

# Create a socket object
client = socket(AF_INET, SOCK_STREAM)

#create timer for transmission
t = timer.Timer(300)

#max size allowed
size = 1000

#encode format
FORMAT = "utf-8"

# user input for ip
ip_address = input("Provide Server IP: ")

# user input for port number
port = int(input("Provide Port number: "))

#connect to server
client.connect((ip_address, port))

#recieved sequence number
rSeqNum = 0

while(True):
    rData = udt.recv(client)
    if rData:
        data = packet.extract(rData)
        if (data[0] == rSeqNum):
            rSeqNum = rSeqNum + 1

        ackMsg = 'ACK' + rSeqNum
        client.send(ackMsg.encode())
