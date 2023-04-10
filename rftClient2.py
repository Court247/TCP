
# client - reciever

# Import socket module
from socket import *
from HelperModule import udt
from HelperModule import packet
from HelperModule import timer

# Create a socket object
client = socket(AF_INET, SOCK_STREAM)

#create timer for transmission
t = timer.Timer(30)

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

#expected sequence number
exSeq = 0

try:

    while(True):

        #set the received information
        rPack,addr = udt.recv(client)

        #set the packet extraction information
        rSeqNum, data = packet.extract(rPack)

        print('1: ')
        print(rSeqNum, data)

        #if the data is not empty and the  sequence numbers match
        if data!= b' ' and (rSeqNum == exSeq):

            print('2: ')

            #make packet to send ACK
            msg = "ACK " + str(rSeqNum)

            ACK = packet.make(rSeqNum,bytes(msg, FORMAT))

            #send ACK package
            udt.send(ACK, client, (ip_address,port))

            #increment received seq. number
            exSeq = exSeq + 1

            #if the received sequence number is 1 put it back to 0
            print('3: ')
            if exSeq >0:
                print('4: ')
                exSeq = exSeq - 1

            print('5: ')

            #create the file
            file = open('Test.txt', 'wb')

            #write to the file 
            file.write(data)

            print('6: ')
        else:
            print("File empty")

finally:

    print('Transfer Done')

    print('8: ')
    #close file
    file.close()

    print('9: ')
    #close server
    client.close()

    print("Goodbye")

