
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
        print('1: ')
        print(data[0],data[1])
        if data[1] and (data[0] == rSeqNum):
            
            print('2: ')
            #make packet to send ACK
            ACK = packet.make(rSeqNum)

            #send ACK package
            udt.send(ACK, client, (ip_address,port))
        
            #increment received seq. number
            rSeqNum = rSeqNum + 1

            #if the received sequence number is 1 put it back to 0

            print('3: ')
            if rSeqNum >0:
                print('4: ')
                rSeqNum = rSeqNum - 1

            print('5: ')
            file = open('Test.txt', 'wb')

            file.write(data[1])

            print('6: ')
        else:

            print('7: ')
            print('Data is empty')
            break

print('8: ')
#close file
file.close()

print('9: ')
#close server
client.close()

print("Goodbye")

