# server - sender

# Import socket module
from socket import *
from HelperModule import packet
from HelperModule import timer
from HelperModule import udt


# Create a socket object
server = socket(AF_INET, SOCK_STREAM)

#set up the timer for the whole transmission
t = timer.Timer(300)

#max size of bytes
size = 1000

#encode type
FORMAT = "utf-8"

#set host address
host = '0.0.0.0'

#give port number
port = int(input("Provide Port number: "))

# Bind to the port
server.bind((host , port))

# Now wait for client connection.
server.listen(100)

#initialize sequence number
seqNum = 0

#initialize transmitted packet counts
transCount = 0

#initialize retransmitted packet counts
reTranCount = 0

#allow for the first data packet to send
toSend = True

#set file name
fileName = "Test.txt"

print("Listening for connection at ", port)

# Establish connection with client.
client, addr = server.accept()

print("Connection accepted from ", addr)


while(True):

    if toSend:

        #check if file exists
        file = open(fileName, 'rb')

        #get the file size bytes
        data = file.read(size)

        #make the data packet
        cPack = packet.make(seqNum, data)

        #send the data packet
        udt.send(cPack, client, addr)

        #start the timer
        t.start()

        #increment sequence number
        seqNum = seqNum + 1

        #set to send to false
        toSend = False

        #add transmission count
        transCount = transCount + 1

    elif client.recv(size):
        data2 = client.recv(size)

        if(data2 == "Ack " + seqNum):

            t.stop()
            toSend = True

    elif t.timeout:

        #send the data packet again
        udt.send(cPack, client, host)

        #add retransmission count
        reTranCount = reTranCount +1

        #start the timer again
        t.start()

    #close the file
    file.close()

    print("Transfer Complete!")

    #close the server
    server.close()

    print("Connection closed, See you later!")
