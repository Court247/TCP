
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
        data = packet.extract(rData[0])
        print(data[0],data[1])
        if data[1] and (data[0] == rSeqNum):
            
            #make packet to send ACK
            ACK = packet.make(rSeqNum)
            
            #send ACK package
            udt.send(ACK, client, (ip_address,port))
            #increment received seq. number
            rSeqNum = rSeqNum + 1

            #if the received sequence number is 1 put it back to 0
            if rSeqNum >0:
                rSeqNum = rSeqNum - 1
        else:
            print('Data is empty')
            break

#close server
client.close()

print("Goodbye")

